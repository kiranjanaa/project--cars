from django.urls import path
from audi.views import *
urlpatterns=[
      path('models/',models,name='models'),
]