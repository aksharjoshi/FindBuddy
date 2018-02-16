# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Traveller
from middleware import addUser

#importing traveller form
#from .forms import TravellerForm

# Create your views here.


def signin(request):
    return render(request, 'FindBuddy/signin.html')

def signup(request):
	if request.method == 'POST':
		email = request.POST.get('email','')
		name = request.POST.get('firstname','') + ' ' +request.POST.get('lastname','')
		number = int(request.POST.get('number',''))
		sdate = request.POST.get('sdate','')
		edate = request.POST.get('edate','')
		destination = request.POST.get('icode','')

		print destination

		traveller_obj = Traveller()
		traveller_obj.name = name
		traveller_obj.number = number
		traveller_obj.travel_start_date = sdate
		traveller_obj.travel_end_date = edate
		traveller_obj.country = destination

#		traveller_obj.save()
		addUser(traveller_obj)

		return render(request, 'FindBuddy/signin.html')
