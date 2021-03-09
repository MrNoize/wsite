from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    output = 'Hello_World.'
    return render(request, template_name, {'output':output})