from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Main')

def create(request):
    return HttpResponse("Create")

def update(request):
    return HttpResponse('update')

def delete(request):
    return HttpResponse("delete")