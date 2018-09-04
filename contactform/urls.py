from django.urls import path
from .views import contact

app_name = 'contactform'
urlpatterns = [
    path('', contact, name='contact')
]

