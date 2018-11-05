from django.shortcuts import render
from users import models as user_models


def index(request):
    campaigns = []
    if request.user.is_authenticated:
        campaigns = request.user.campaigns.all()

    return render(request, 'index.html', {'campaigns': campaigns})