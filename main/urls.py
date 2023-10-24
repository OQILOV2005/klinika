from django.urls import path
from . import views

urlpatterns = [
    # PATIENT NUMBER API
    path('filter/patients/1-day/', views.filter_patients_created_within_1_days),# ishladi
    path('filter/patients/30-days/', views.filter_patients_created_within_30_days),# ishladi
    path('filter/patients/365-days/', views.filter_patients_created_within_365_days),# ishladi
    path('created-count/total-patients/', views.created_count_total_patients),# ishladi

    # REPORT API
    path('filter/reports/1-day/', views.filter_report_created_within_1_days),# ishladi
    path('filter/reports/30-days/', views.filter_report_created_within_30_days),# ishladi
    path('filter/reports/365-days/', views.filter_report_created_within_365_days),# ishladi
    path('created-count/total-reports/', views.created_count_total_report),# ishladi

    # EMPLOYEE API
    path('employees/', views.get_all_employees),# ishladi

    # EMPLOYEE BY_NAME FILTERS API
    path('employees/filter/name/', views.filter_employee_by_name), # ishladi

    # EMPLOYEE BY_SPECIALTY FILTERS API
    path('employees/filter/specialty/', views.filter_employee_by_specialty),# ishladi

    # EMPLOYEE BY_STATUS FILTERS API
    path('employees/filter/status/', views.filter_employee_by_status),# ishladi

    # EMPLOYEE BY_ROOMS FILTERS API
    path('employees/filter/rooms/', views.filter_employee_by_rooms),# ishladi

    # EMPLOYEE BY_TIME FILTERS API
    path('employees/filter/time/', views.filter_employee_by_time),# ishladi

    # EMPLOYEE BY_SECTION FILTERS API
    path('employees/filter/section/', views.filter_employee_by_section),# ishladi

    # SECTION API
    path('sections/', views.get_all_sections),# ishladi

    # ROOMS API
    path('rooms/', views.get_all_rooms),# ishladi

    # ROOMS FILTERS BY_CAPACITY API
    path('rooms/filter/capacity/', views.filter_rooms_by_capacity),# so'rovi ?room_capacity=5

    # ROOMS FILTERS BY_GENDER API
    path('rooms/filter/gender/', views.filter_rooms_by_gender),# ishladi

    # ROOMS FILTERS BY_FREE API
    path('rooms/filter/free/', views.filter_rooms_by_free),# ishladi  so'rovi ?is_booked=False

    # ROOMS FILTERS BY_NAME API
    path('rooms/filter/name/', views.filter_rooms_by_name),# ishladi

    # ROOMS FILTERS BY_CATEGORY API
    path('rooms/filter/category/', views.filter_rooms_by_category),# ishladi

    # ROOMS FILTERS BY_STATUS API
    path('rooms/filter/status/', views.filter_rooms_by_status),# ishladi

    # ROOMS FILTERS BY_PRICE API
    path('rooms/filter/price/', views.filter_rooms),# ishladi

    # ROOMS FILTERS BY_SECTION API
    path('filter_rooms_by_section/', views.filter_rooms_by_section),# ishladi

    # PATIENT API
    path('patients/', views.patient_get_all),# ishladi
    path('patients/is_active/', views.patient_is_activete),# ishladi

    # PATIENT FILTERS BY_NAME API
    path('patients/filter/name/', views.filter_patient_by_name),# ishladi

    # PATIENT SEARCH DIAGNOS API
    path('patients/search/diagnos/', views.search_employees_diagnos),#bo'sh 200

    # PATIENT FILTERS BY_GENDER API
    path('patients/filter/gender/', views.filter_patient_by_gender),# ishladi

    # PATIENT FILTERS BY_ROOM API
    path('patients/filter/room/', views.filter_patients_by_room),# bosh 200

    # PATIENT FILTERS BY_DOCTOR API
    path('patients/filter/doctor/', views.filter_patient_by_doctor),# ishladi

    # PATIENT FILTERS BY_CREATE_AT API
    path('patients/filter/create-at/<int:pk>/', views.filter_patients_by_create_at),# hammasni chiqarmoda 1tasi chiqish kerak

    # PATIENT SEARCH PHONE API
    path('patients/search/phone/', views.search_patient_phone),# ishladi

    # PATIENT SEARCH NAME API
    path('patient/search/name/', views.search_patient_name),# ishladi

    # API for filtering attendance by status for a specific day
    path('attendance/filter_by_status_date/', views.filter_attendance_by_status_date),# ishladi no sach calumb - Broken pipe from ('127.0.0.1', 57115)


    # API for filtering attendance by status for a specific day with "True" status
    path('attendance/filter_by_status_day_came/<int:day>/', views.filter_attendance_by_status_date_come_true),# ishladi

    # API for filtering attendance by status for a specific day with "False" status
    path('attendance/filter_by_status_day_true_come/<int:day>/', views.filter_attendance_by_status_day_false_come),# ishladi

    # API for filtering attendance by status for a specific day with "30-days" status
    path('attendance/filter_by_status_day_false_come/<int:day>/', views.filter_attendance_by_employee_last_30_days),# ishladi

     # API cassa balance view
    path('cassa/<str:password>/', views.get_cassa_balance),# ishladi

    # API informations all view
    path('informations/all/', views.informations_get_all,),# ishladi

    # API PAYMENT daily and filter and filter by code and all
    path('payments/daily/', views.daily_payments),# ishladi

    path('payments/date-filtered/', views.date_filtered_payments),# ishladi

    path('payments/code-filtered/<str:code>/', views.code_filtered_payments),# ishladi

    path('payments/all/', views.all_payments),# ishladi

    # Operaton all doctor and all API
    path('operations/doctors/', views.all_doctors_in_operations),# ishladi

    path('operations/all/', views.all_transactions),# ishladi

    # Queue all doctor  API
    path('queues/doctor/<int:pk>/', views.queues_by_doctor),# ishladi

    path('queues/all/', views.get_all_queue),# ishladi
]


