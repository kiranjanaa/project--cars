from django.urls import path
from bmw.views import *
urlpatterns=[
      path('models/',models,name='models'),
]