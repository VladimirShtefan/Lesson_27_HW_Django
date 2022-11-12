from django.urls import path

from ads import views


urlpatterns = [
   path('', views.AdsListView.as_view(), name='ads'),
   path('<int:pk>/', views.AdsDetailView.as_view(), name='detail_ads'),
]
