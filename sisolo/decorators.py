from django.http import HttpResponse
from django.shortcuts import redirect
from sisolo.models import User

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if User.objects.filter(user = request.user).exists():
				group = User.objects.get(user = request.user)

			if group == None:
				return HttpResponse('You are not authorized to view this page')
			else:
				if group.role in allowed_roles:
					return view_func(request, *args, **kwargs)
				elif group.role == 'Pengguna':
					return redirect('pendaftaran_izin_usaha:daftar_pelaku_usaha')
				else:
					return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if User.objects.filter(user = request.user).exists():
			group = User.objects.get(user = request.user)

		if group == None:
			return HttpResponse('You are not authorized to view this page')
		else:
			if group.role == 'Admin':
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')

	return wrapper_function