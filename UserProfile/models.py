from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify



class Profile(models.Model):

    '''The attributes saved when a user sign's up.'''

    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    first_name = models.CharField(max_length=120, blank=True, null=True)
    second_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)

    date_run = models.DateField(null=True,blank=True, )

    def __str__(self):

        '''Returns the first- ,second- and last name as a user'''

        first_name = str(self.first_name)
        if (self.second_name != None):
            first_name = first_name + ' ' + str(self.second_name).capitalize()

        last_name = str(self.last_name).capitalize()

        US = first_name + ' ' + last_name
        text = [
            US,
        ]
        user_title = ' - '.join(text)
        return user_title

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name


    def save(self, *args, **kwargs):

        '''Creates and returns slug(unique nickname) '''

        ex = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name !=self.__initial_last_name or self.slug == '':
            print(self.first_name)
            if (self.first_name and self.last_name):
                to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name))
                ex = Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + ' ' + str(get_random_code()))
                    ex = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)

        self.slug = to_slug
        super().save(*args, **kwargs)

    class Meta:

        '''Creates a metadata for users, and labels them as Profile in the admin page'''

        verbose_name_plural = 'Profile'




