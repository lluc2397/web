from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import Notifs
# Create your views here.

def ShowNotifications(request):
	user = request.user
	notifications = Notifs.objects.filter(user=user).order_by('-date')
	Notifs.objects.filter(user=user, is_seen=False).update(is_seen=True)

	template = loader.get_template('includes/navigation.html')

	context = {
		'notifications': notifications,
	}

	return HttpResponse(template.render(context, request))

def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notifs.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}
