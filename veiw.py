from django.shortcuts import render,redirect
from .forms import  LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
from . mixins import LoginMixin
from django.views import View
from .models import Author
import json
import requests

class CustomMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_data = requests.get(
            'http://apilayer.net/api/live?access_key=f28a7ad097177b13f195a20d893451dd&currencies=EUR,GBP,CAD,PLN&source=USD&format=1')
        var = json.dumps(news_data.json(),sort_keys=True,indent=4)
        var2 = json.loads(var)
        var3 = var2['quotes']
        context['newsdata'] = var3
        print(type(var3))
        return context

class NewsDataView(CustomMixin,TemplateView):
    template_name = 'task/second.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



