from django.shortcuts import render
from users import models as user_models


def index(request):
    return render(request, 'index.html')