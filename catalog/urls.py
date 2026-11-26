from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='catalog'),
    path('create-book',views.CreateBook.as_view(),name='create-book'),
    path('detail-book/<int:pk>',views.BookDetail.as_view(),name='detail-book'),
    path('accounts/register',views.Register.as_view(),name='register')
]