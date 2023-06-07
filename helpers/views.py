from django.shortcuts import render

import os

'''Rendered html files for invalid URl and when there is an error in the server.'''

def handle_not_found(request, exception):
    template = os.path.join('main', 'not-found.html')
    context = {
    }
    return render(request, template, context=context)


def handle_server_error(request):
    template = os.path.join('main', 'server-error.html')
    context = {
    }
    return render(request, template, context=context)
