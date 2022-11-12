from django.urls import path

from categories import views

urlpatterns = [
   path("", views.CategoryListView.as_view(), name="categories"),
   path("<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
