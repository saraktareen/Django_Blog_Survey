from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # login
    path('accounts/', include('accounts.urls')), # signup
    path('survey/', include('survey.urls'))
]