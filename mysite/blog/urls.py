from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main),
    path('create', create),
    path('update', update),
    path('delete', delete),

]