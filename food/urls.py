from . import views
from django.urls import path

app_name = "food"

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete_item'),
]