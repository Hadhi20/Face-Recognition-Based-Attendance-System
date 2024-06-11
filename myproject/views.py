from django.http import HttpResponse


def Mainpage(request):
    return HttpResponse(request,'runApp')