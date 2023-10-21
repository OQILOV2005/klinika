from django.urls import path
from . import views

urlpatterns = [
    # PATIENT NUMBER API
    path('filter/patients/1-day/', views.filter_patients_created_within_1_days),
    path('filter/patients/30-days/', views.filter_patients_created_within_30_days),
    path('filter/patients/365-days/', views.filter_patients_created_within_365_days),
    path('created-count/total-patients/', views.created_count_total_patients),

    # REPORT API
    path('filter/reports/1-day/', views.filter_report_created_within_1_days),
    path('filter/reports/30-days/', views.filter_report_created_within_30_days),
    path('filter/reports/365-days/', views.filter_report_created_within_365_days),
    path('created-count/total-reports/', views.created_count_total_report),

    # EMPLOYEE API
    path('employees/', views.get_all_employees),# ishladi

    # EMPLOYEE BY_NAME FILTERS API
    path('employees/filter/name/', views.filter_employee_by_name), # ishladi

    # EMPLOYEE BY_SPECIALTY FILTERS API
    path('employees/filter/specialty/', views.filter_employee_by_specialty),#ishlamadi

    # EMPLOYEE BY_STATUS FILTERS API
    path('employees/filter/status/', views.filter_employee_by_status),#ishlamadi

    # EMPLOYEE BY_ROOMS FILTERS API
    path('employees/filter/rooms/', views.filter_employee_by_rooms), # ishlamadi

    # EMPLOYEE BY_TIME FILTERS API
    path('employees/filter/time/', views.filter_employee_by_time),# ishladi

    # EMPLOYEE BY_SECTION FILTERS API
    path('employees/filter/section/', views.filter_employee_by_section),# ishlamadi

    # SECTION API
    path('sections/', views.get_all_sections),# ishladi

    # ROOMS API
    path('rooms/', views.get_all_rooms),# ishladi

    # ROOMS FILTERS BY_CAPACITY API
    path('rooms/filter/capacity/', views.filter_rooms_by_capacity),# bosh 200

    # ROOMS FILTERS BY_GENDER API
    path('rooms/filter/gender/', views.filter_rooms_by_gender),# bu xato boshidan qilish kerak

    # ROOMS FILTERS BY_FREE API
    path('rooms/filter/free/', views.filter_rooms_by_free),# ishladi is free fild qo'shish kerak

    # ROOMS FILTERS BY_NAME API
    path('rooms/filter/name/', views.filter_rooms_by_name),# ishladi

    # ROOMS FILTERS BY_CATEGORY API
    path('rooms/filter/category/', views.filter_rooms_by_category),# bosh 200

    # ROOMS FILTERS BY_STATUS API
    path('rooms/filter/status/', views.filter_rooms_by_status),# ishladi

    # ROOMS FILTERS BY_PRICE API
    path('rooms/filter/price/', views.filter_rooms),# max mini kirg farmat notogri 200

    # ROOMS FILTERS BY_SECTION API
    path('rooms/filter/section/', views.filter_rooms_by_section),# bosh 200

    # PATIENT API
    path('patients/', views.patient_get_all),# ishladi
    path('patients/is_active/', views.patient_is_activete),# ishladi

    # PATIENT FILTERS BY_NAME API
    path('patients/filter/name/', views.filter_patient_by_name),# ishladi

    # PATIENT SEARCH DIAGNOS API
    path('patients/search/diagnos/', views.search_employees_diagnos),#hato tekshirish kerak

    # PATIENT FILTERS BY_GENDER API
    path('patients/filter/gender/', views.filter_patient_by_gender),# ishladi

    # PATIENT FILTERS BY_ROOM API
    path('patients/filter/room/', views.filter_patient_by_room),# bosh 200

    # PATIENT FILTERS BY_DOCTOR API
    path('patients/filter/doctor/', views.filter_patient_by_doctor),# ishladi

    # PATIENT FILTERS BY_CREATE_AT API
    path('patients/filter/create-at/', views.filter_patient_by_create_at),#hato tekshirish kerak

    # PATIENT SEARCH PHONE API
    path('patients/search/phone/', views.search_patient_phone),# ishladi

    # PATIENT SEARCH NAME API
    path('patient/search/name/', views.search_patient_name),# ishladi

    path('patient/filter/attendance/',views.filter_attendance_by_status),

    path('patient/filter/attendance_day/', views.filter_attendance_by_status_day)
]


