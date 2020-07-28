from django.urls import path
from .views import add,hello,multi,sub,div
urlpatterns = [
    path('',hello,name="hello"),
    path('add',add,name="add"),
    path('multi',multi,name="multi"),
    path('sub',sub,name="subtraction"),
    path('div',div,name="Division"),

]