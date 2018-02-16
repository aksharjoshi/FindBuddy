from celery import Celery
from django.conf import settings

app = Celery('tasks')

app.config_from_object('django.conf:settings')


@app.task
def addUser(traveller_obj):
	traveller_obj.save()
	return True