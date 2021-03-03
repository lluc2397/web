from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from web.models import PostWeb
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
#from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import Libros, Order, servicios, productos
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from usuario.forms import MyUserCreationForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from perfil.tokens import account_activation_token
from django.template.loader import render_to_string
from django.views import generic
from django.urls import reverse_lazy
from perfil.models import Perfil
from django.core.paginator import Paginator
#from .filters import Filter
from perfil.forms import ProfileUpdateForm
from escuela.models import cursos, talleres, Modulo
from cartera.forms import ModCartera, AgregarActivo
from cartera.models import Activo, Cartera

MyUser = get_user_model()

def navigation(request):
    #myFilter = Filter()

   # context = {'myFilter' : myFilter}

    return render(request, 'includes/navigation.html',{})

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        registerForm = MyUserCreationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email=(registerForm.cleaned_data['email'])
            user.set_password(registerForm.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activa tu cuenta'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse("Se ha enviado un email de validación a tu correo electrónico. Para concluir con el registro sigue las instrucciones en el email.")
    else:
        registerForm = MyUserCreationForm()
    return render(request, 'registration/register.html', {'form': registerForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'registration/activation_invalid.html')

@login_required(login_url='login')
def dashboard(request):
	return render(request, 'perfil/dashboard.html', {})

class blog_posts(LoginRequiredMixin, ListView):
    model = PostWeb
    template_name = 'perfil/blog_posts.html'
    ordering = ['-post_date']

@login_required(login_url='login')
def biblioteca(request):
    libros = Libros.objects.all()
    
    return render(request, 'perfil/biblioteca.html', {'libros' : libros})

@login_required(login_url='login')
def biblio_comentador(request):
    libros = Libros.objects.all()
    
    return render(request, 'perfil/biblio_comentador.html', {'libros' : libros})

@login_required(login_url='login')
def perfil(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.perfil)

        if pform.is_valid():
            pform.save()
            messages.success(request, f'Tu información se ha actualizado.')
            return redirect('perfil')
    else:
        pform = ProfileUpdateForm(instance=request.user.perfil)
   
    return render(request, 'perfil/perfil.html', {'pform': pform})

@login_required(login_url='login')
def Modifportfolio(request):
    activos_cartera = Cartera.objects.filter(usuario=request.user)

    if request.method =="POST":
        agractform = AgregarActivo(request.POST)
        carteraform = ModCartera(request.POST)

        if carteraform.is_valid():
            obj = carteraform.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.success(request, f'Activo agregado a tu cartera')
            return redirect('modifportfolio')

        if agractform.is_valid():
            agractform.save()
            messages.success(request, f'Activo agregado')
            return redirect('modifportfolio')

    else:
        agractform = AgregarActivo()
        carteraform = ModCartera()

    return render(request, "perfil/modifportfolio.html", {'agractform': agractform, 'carteraform': carteraform, 'activos_cartera': activos_cartera})

@login_required(login_url='login')
def portfolio(request):
    activos_cartera = Cartera.objects.filter(usuario=request.user)

    if request.method =="POST":        
        tckr = request.POST['ticker']

        return render(request, "perfil/portfolio.html", {'activos_cartera': activos_cartera, 'tckr': tckr})

    else:
        return render(request, "perfil/portfolio.html", {'activos_cartera': activos_cartera})
        
@login_required(login_url='login')
def new_post(request):
	return render(request, 'perfil/new_post.html', {})
   
@login_required(login_url='login')
def historial_pedidos(request):
    pedidos = Order.objects.filter(cliente=request.user)
    
    return render(request, 'perfil/historial_pedidos.html', {'pedidos' : pedidos})

class Talleres(LoginRequiredMixin, ListView):
    model = talleres
    template_name = 'uni/talleres.html'
    ordering = ['-fecha_publicacion']

class Cursos(LoginRequiredMixin, ListView):
    model = cursos
    template_name = 'uni/cursos.html'
    ordering = ['-fecha_publicacion']

@login_required(login_url='login')
def Curso (request, titulo):
    curso_selec = cursos.objects.get(titulo = titulo.replace('-', ' '))
    modulos_curso = curso_selec.modulo_set.all()

    context = {'curso_selec': curso_selec, 'modulos_curso': modulos_curso}

    return render(request, 'uni/curso.html', context)

class Taller (LoginRequiredMixin, DetailView):
    model = talleres 
    template_name = 'uni/taller.html'
    context_object_name = "taller"

class Modulos (LoginRequiredMixin, DetailView):
    model = Modulo 
    template_name = 'uni/modulos.html'
    context_object_name = "modulo"