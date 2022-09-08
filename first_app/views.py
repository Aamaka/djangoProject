from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Ada"
    return render(request, 'index.html', context={"name": name})


# Create your views here.
def hello(request, name: str, num: int):
    return HttpResponse(f"<h1>{num}. {name.title()}, welcome to Django</h1>")
