from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    my_context = {}
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'title': 'This is about us',
        'this is true': True,
        'my_number': 123,
        'my_list': [553, 7665, 5656],
        'my_html': '<h1>Hello, World</h1>'
    }
    return render(request, 'about.html', my_context)