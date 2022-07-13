from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('reception-registration/', views.receptionist_registration, name='reception_registration'),
    path('doctor-registration/', views.doctor_registration, name='doctor_registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('receptionist-dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('profile-doc/', views.profile_doc, name='profile_doc'), 
    path('profile-recep/', views.profile_recep, name='profile_recep'), 
    path('appointment/', views.appointment, name='appointment'), 
    path('appointment-update/<int:pk>', views.appointment_update, name='appointment_update'), 
    path('appointment-delete/<int:pk>', views.delete_appointment, name='appointment_delete'), 









    # <a class="btn btn-primary btn-sm ml-2 mb-2" href="{% url 'profile-update' %}">Update</a>
    






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)