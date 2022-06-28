from django.urls import path
from .views import HomeView, CreateBookView, UpdateBookView, BookDeteailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateBookView.as_view(), name="create"),
    path('update/<int:pk>/', UpdateBookView.as_view(), name="update"),
    path('detail/<int:pk>/', BookDeteailView.as_view(), name="detail"),
]