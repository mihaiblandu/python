from django.shortcuts import render
from django.http import HttpResponse

def social_view(request, *args, **kwargs):
    print(request)
    return  render(request, "home.html", {})
def contact_view(request, *args, **kwargs):
    print(request)
    return  render(request, "contact.html", {})
def about_view(request, *args, **kwargs):

    my_context = {
        'my_text': "This is about us.",
        'address': 'Usa, Washington DC.',
        "my_list": [1, 2, 3, "A"],
        'range': range(10)
    }

    print(my_context)
    return  render(request, "about.html",  my_context )
def service_view(request, *args, **kwargs):
    print(request)
    return  render(request, "service.html", {})
