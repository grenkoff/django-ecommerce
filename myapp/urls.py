from django.urls import path
from myapp.views import index, index_item, contacts


app_name = 'myapp'

urlpatterns = [
    path('hello/', index),
    path('hello/<int:my_id>/', index_item, name='detail'),
    path('contacts/', contacts),
]



