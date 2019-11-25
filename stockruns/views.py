from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to stock runs. You can go to { /api } to access all api endpoints")
