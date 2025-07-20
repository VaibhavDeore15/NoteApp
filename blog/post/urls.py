
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('hello/', home),
    # path('<int:id>/',views.display),
    path('<int:roll>/',show),
    path('demo/',demo,name='demo'),
    path('',user_login,name='login'),
    path('register/',register,name='register'),
    path('save-data/',savedata,name='save_data'),
    path('delete-view/<int:id>',deleteview,name='delete-view'),
    path('update-data/<int:id>',updateview,name='update-data'),
    path('search/',search,name="search")

]
