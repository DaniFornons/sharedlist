from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("", views.shopping_list, name="lists_list"),
    path("add/", views.add_list, name="add_list"),
    path("<int:pk>", views.detail_list, name="detail_list"),
    path("<int:pk>/delete/", views.delete_list, name="delete_list"),

    path("<int:pk>/toggle/<int:item_id>/", views.toggle_item, name="toggle_item"),
    path("<int:pk>/delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path("<int:pk>/add/", views.add_item, name="add_item")
]
