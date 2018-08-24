from django.urls import path
from myQuotes import views

urlpatterns = {
    path('author/', views.author_list),
    path('authordetail/<int:pk>/', views.AuthorDetail.as_view()),
}
