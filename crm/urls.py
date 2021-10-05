from django.contrib import admin
from django.urls import path, include
from app.leads.views import landing_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('leads/',  include('app.leads.urls', namespace="leads"))
]
