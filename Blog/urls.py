from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

# usrnme-admin,pswrd-1234

urlpatterns = [

    path('admin/', admin.site.urls),
    path('/home',views.Actionhome,name ='home'),
    path('logincheck',views.ActionLogincheck,name ='index'),
    path(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('signup/',views.ActionSignup),
    path('signupcheck',views.ActionSignupcheck),
    path('add_b/', views.add_b, name='add_b'),
    path('private_blogs/', views.private_b, name='private_b'),
    path('search_user/',views.ActionSearch,name='search'),
    path('public_blogs/<slug:username>/',views.public_b,name='display')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)