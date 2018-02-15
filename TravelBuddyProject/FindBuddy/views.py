# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'FindBuddy/signin.html')

def signup(request):
    return render(request, 'FindBuddy/basic.html', {'content':['If you would like to contact me, please email me','akshar.joshi91@gmail.com']})
