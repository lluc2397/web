from .views import register, blog_posts, Talleres, Cursos, Curso, Taller, Modulos
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('register/', views.register, name="register"),

    path('activate/<slug:uidb64>/<slug:token>)/', views.account_activate, name='activate'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('talleres/', Talleres.as_view(), name="talleres"),
    path('cursos/', Cursos.as_view(), name="cursos"),
    path('blog_posts/', blog_posts.as_view(), name="blog_posts"),
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('perfil/', views.perfil, name="perfil"),
    path('Modifportfolio/', views.Modifportfolio, name="modifportfolio"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('new_post/', views.new_post, name="new_post"),
    path('biblio_comentador/', views.biblio_comentador, name="biblio_comentador"),
    path('historial_pedidos/', views.historial_pedidos, name="historial_pedidos"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),

    path('Curso/<titulo>/', Curso, name="Curso"),
    path('Taller/<int:pk>/', Taller.as_view(), name="Taller"),
    path('Modulo/<int:pk>/', Modulos.as_view(), name="Modulos"),
    
]