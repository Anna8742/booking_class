from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('book-class/', views.book_class, name='book_class'),
    path('admin/cancel-class/<int:class_id>/', views.admin_cancel_class, name='admin_cancel_class'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),  # Admin view
]
