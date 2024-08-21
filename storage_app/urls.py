from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('create_folder/', views.create_folder, name='create_folder'),  # Create folder page
    path('folder/<int:folder_id>/', views.view_folder, name='view_folder'),  # View folder and upload files
    path('folder/<int:folder_id>/update/', views.update_folder, name='update_folder'),  # Update folder name
    path('file/<int:file_id>/delete/', views.delete_file, name='delete_file'),  # Delete file
    path('logout/', views.logout_view, name='logout_view'),  # Custom logout view
    path('login/', views.login_view, name='account_login'),  # Custom login view

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
