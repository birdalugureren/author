from django.conf.urls import url
from django.urls import path
from myQuotes import views

urlpatterns = [
    path('author/', views.author_list),
    path('authordetail/<int:pk>/', views.AuthorDetail.as_view()),
    path('mcauthorlist/', views.MCAuthorList.as_view()),
    path('mcauthordetail/<int:pk>/', views.MCAuthorDetail.as_view()),
    path('gcauthorlist/', views.GCAuthotList.as_view()),
    path('gcauthordetail/<int:pk>/', views.GCAuthorDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk/>', views.UserDetail.as_view()),

]
