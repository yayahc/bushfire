from django.urls import path


from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.detail, name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete')
]
