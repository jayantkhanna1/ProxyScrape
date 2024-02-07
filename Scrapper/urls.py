from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('startScraping',views.startScraping,name='startScraping'),
]
