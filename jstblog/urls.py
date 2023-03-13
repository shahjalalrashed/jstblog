from django.contrib import admin
from django.urls import path
from django.conf import settings
from.import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.jstblogsite,name="bloghome"),    
    path('category', views.jstcategory,name="blogcategory"),    
    path('contact', views.jstcontact,name="blogcontact"),    
    path('single', views.jstsingle,name="blogsingle"),
    path('signup',views.jstsignup,name="blogsignup"),
    path('login',views.jstlogin,name="bloglogin"),    
    path('logout',views.jstlogout,name="bloglogout"),    
    path('editprof',views.jsteditprof,name="blogeditprof"),    
    path('changepass',views.jstchangepass,name="blogchangepass"),    
]
