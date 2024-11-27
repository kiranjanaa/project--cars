from django.urls import path
from ford.views import *
urlpatterns=[
      path('models/',models,name='models'),
]