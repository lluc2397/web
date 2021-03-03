from django.urls import path
from . import views
from .views import Blog, publicaciones, Home, LikeView

urlpatterns =[
    path('', Home.as_view(), name="home"),
    path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('pricing.html', views.pricing, name="pricing"),
	path('service.html', views.service, name="service"),
    path('appointment.html', views.appointment, name="appointment"),
    path('blog.html', Blog.as_view(), name="blog"),
    path('analisis.html', views.analisis, name="analisis"),
    path('asesoramiento.html', views.asesoramiento, name="asesoramiento"),
    path('noticias.html', views.noticias, name="noticias"),
    path('publicaciones/<slug:slug>/', publicaciones.as_view(), name="publicaciones"),
    path('recomendaciones.html', views.recomendaciones, name="recomendaciones"),
    path('crypto.html', views.crypto, name="crypto"),
    path('cursos.html', views.cursos, name="cursos"),
    path('base.html', views.base, name="base"),
    path('legal.html', views.legal, name="legal"),
    path('politicas.html', views.politicas, name="politicas"),
    path('faq.html', views.faq, name="faq"),
    path('error.html', views.error, name="error"),
    path('like/<int:pk>', LikeView, name='like_post'),

    
]