from django.urls import path
from . import views

urlpatterns = [
    # EMPLOYEE GENERICS API
    path('employees/', views.CreateEmployye.as_view(), name='create-employee'),
    path('employees/update/<int:pk>/', views.UpadteEmployye.as_view(), name='update-employee'),
    path('employees/delete/<int:pk>/', views.DeleteEmployye.as_view(), name='delete-employee'),

    # SECTION GENERICS API
    # path('sections/', views.GetSection.as_view(), name='get-section'),
    path('sections/create/', views.CreateSection.as_view(), name='create-section'),
    path('sections/update/<int:pk>/', views.UpadteSection.as_view(), name='update-section'),
    path('sections/delete/<int:pk>/', views.DeleteSection.as_view(), name='delete-section'),

    # ROOM GENERICS API
    # path('rooms/', views.GetRoom.as_view(), name='get-room'),
    path('rooms/create/', views.CreateRoom.as_view(), name='create-room'),
    path('rooms/update/<int:pk>/', views.UpadteRoom.as_view(), name='update-room'),
    path('rooms/delete/<int:pk>/', views.DeleteRoom.as_view(), name='delete-room'),

    # PATIENT GENERICS API
    # path('patients/', views.GetPatient.as_view(), name='get-patient'),
    path('patients/create/', views.CreatePatienent.as_view(), name='create-patient'),
    path('patients/update/<int:pk>/', views.UpdatePatient.as_view(), name='update-patient'),
    path('patients/delete/<int:pk>/', views.DeletePatient.as_view(), name='delete-patient'),

    # OPERATION GENERICS API
    # path('operations/', views.GetOperation.as_view(), name='get-operation'),
    path('operations/create/', views.CreateOperation.as_view(), name='create-operation'),
    path('operations/update/<int:pk>/', views.UpadteOperation.as_view(), name='update-operation'),
    path('operations/delete/<int:pk>/', views.DeleteOperation.as_view(), name='delete-operation'),

    # INFORMATIONS GENERICS API
    path('informations/create/', views.CreateInformations.as_view(), name='create-informations'),
    path('informations/update/<int:pk>/', views.UpadteInformations.as_view(), name='update-informations'),
    path('informations/delete/<int:pk>/', views.DeleteInformations.as_view(), name='delete-informations'),

    # CASSA GENERICS API
    # path('cassas/', views.GetCassa.as_view(), name='get-cassa'),
    path('cassa/create/', views.CreateCassa.as_view(), name='create-cassa'),
    path('cassa/<int:pk>/', views.UpdateCassa.as_view(), name='update-cassa'),
    path('cassa/<int:pk>/delete/', views.DeleteCassa.as_view(), name='delete-cassa'),

    # REPORT GENERICS API
    path('reports/create/', views.CreateReport.as_view(), name='create-report'),
    path('reports/update/<int:pk>/', views.UpdateReport.as_view(), name='update-report'),
    path('reports/delete/<int:pk>/', views.DeleteReport.as_view(), name='delete-report'),

    # QUEUE GENERICS API
    path('queues/create/', views.CreateQueue.as_view(), name='create-queue'),
    path('queues/update/<int:pk>/', views.UpdateQueue.as_view(), name='update-queue'),
    path('queues/delete/<int:pk>/', views.DeleteQueue.as_view(), name='delete-queue'),

    # ATTENDANCE GENERICS API
    path('attendance/create/', views.CreateAttdence.as_view(), name='create-attendance'),
    path('attendance/update/<int:pk>/', views.UpdateAttdence.as_view(), name='update-attendance'),
    path('attendance/delete/<int:pk>/', views.DeleteAttdence.as_view(), name='delete-attendance'),

    # PAYMENT GENERICS API
    path('payments/create/', views.CreatePayment.as_view(), name='create-payment'),
    path('payments/update/<int:pk>/', views.UpdatePayment.as_view(), name='update-payment'),
    path('payments/delete/<int:pk>/', views.DeletePayment.as_view(), name='delete-payment'),
]
