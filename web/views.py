from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import PostWeb, CommentWeb, Category
from .forms import CommentWebForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

class Home(ListView):
	model = PostWeb
	paginate_by = 3
	template_name = 'home.html'
	ordering = ['-post_date']

def home(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_country = request.POST['your-country']
		your_service = request.POST['your-service']
		your_payment = request.POST['your-payment']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name + " / " + " Phone: " + your_phone + " / " + " Email: " + your_email + " / " + " Country: " + your_country+  " / "  + " Servicio: " + your_service + " / " + " Forma de pago: " + your_payment + " / " + " Message: " + your_message

		send_mail(
			'Petición de servicio', # subject
			appointment, # message
			your_email, # from email
			['a.inversionesyfinanzas@gmail.com'], # To Email
			)

		send_mail(
			'Solicitud recibida',
			"Gracias por confiar en nosotros" + " " + your_name +","+ " " + "hemos recibido tu petición, te responderemos en la mayor brevedad",
			"a.inversionesyfinanzas@gmail.com",
			[your_email],
			)	
		
		return render(request, 'home.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_country': your_country,
			'your_service': your_service,
			'your_payment': your_payment,
			'your_message': your_message
			})
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			"Mensaje desde Contacto", # subject
			message_name + " " + "desde:" + " " + message_email + " " + "te ha enviado: " + " " + message, # message
			message_email, # from email
			['a.inversionesyfinanzas@gmail.com'], # To Email
			)

		send_mail(
			'Solicitud recibida',
			"Gracias por confiar en nosotros" + " " + message_name +","+ " " + "hemos recibido tu petición, te responderemos en la mayor brevedad",
			"a.inversionesyfinanzas@gmail.com",
			[message_email],
			)	

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def legal(request):
	return render(request, 'legal.html', {})

def faq(request):
	return render(request, 'faq.html', {})

def politicas(request):
	return render(request, 'politicas.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def cursos(request):
	return render(request, 'cursos.html', {})

def analisis(request):
	return render(request, 'analisis.html', {})

def asesoramiento(request):
	return render(request, 'asesoramiento.html', {})

def noticias(request):
	return render(request, 'noticias.html', {})

def recomendaciones(request):
	return render(request, 'recomendaciones.html', {})

def crypto(request):
	return render(request, 'crypto.html', {})

def base(request):
	if request.method == "POST":
		nlemail = request.POST.get('nl_email')

		send_mail(
			'Te has suscrito al News Letter', # subject
			"Tu solicitud para recibir las últimas novedades y promociones exclusivas ha sido registrada. A partir de ahora recibirás promociones únicas y estarás al día de todas las noticas importantes.", # message
			'a.inversionesyfinanzas@gmail.com', # from email
			[nlemail], # To Email
			)
		return render(request, 'home.html')	
		
	else:
		return render(request, 'base.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_country = request.POST['your-country']
		your_service = request.POST['your-service']
		your_payment = request.POST['your-payment']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name + " / " + " Phone: " + your_phone + " / " + " Email: " + your_email + " / " + " Country: " + your_country+  " / "  + " Servicio: " + your_service + " / " + " Forma de pago: " + your_payment + " / " + " Message: " + your_message

		send_mail(
			'Petición de servicio', # subject
			appointment, # message
			your_email, # from email
			['a.inversionesyfinanzas@gmail.com'], # To Email
			)

		send_mail(
			'Solicitud recibida',
			"Gracias por confiar en nosotros" + " " + your_name +","+ " " + "hemos recibido tu petición, te responderemos en la mayor brevedad",
			"a.inversionesyfinanzas@gmail.com",
			[your_email],
			)	
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_country': your_country,
			'your_service': your_service,
			'your_payment': your_payment,
			'your_message': your_message
			})

	else:
		return render(request, 'appointment.html', {})

class Blog(ListView):
	model = PostWeb
	template_name = 'blog.html'
	ordering = ['-post_date']

def LikeView(request, pk):
	post = get_object_or_404(PostWeb, id=request.POST.get('post_id'))
	liked = False
	if post.likewp.filter(id=request.user.id).exists():
		post.likewp.remove(request.user)
		liked = False
	else:
		post.likewp.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('publicaciones', args=[str(pk)]))

class publicaciones(DetailView):
	model = PostWeb
	template_name = 'publicaciones.html'
	context_object_name = "post"
	slug_field = 'slug'
	
	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		comments_connected = CommentWeb.objects.filter(post_connected=self.get_object()).order_by('-date_posted')

		stuff = get_object_or_404(PostWeb, slug=self.kwargs['slug'])
		total_likes = stuff.total_likes()	

		liked = False
		if stuff.likewp.filter(id=self.request.user.id).exists():
			liked = True

		data['comments'] = comments_connected
		if self.request.user.is_authenticated:
			data['form'] = CommentWebForm(instance=self.request.user)
		
		data["total_likes"] = total_likes
		data["liked"] = liked
		return data
	
	def post(self, request, *args, **kwargs):
		new_comment = CommentWeb(content=request.POST.get('content'),
								author=self.request.user,
								post_connected=self.get_object())
		new_comment.save()

		return self.get(self, request, *args, **kwargs)
		

def error(request):
	return render(request, 'error.html', {})

