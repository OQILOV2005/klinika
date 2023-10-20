from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime

# START MAIN ALGORITMS HOME PAGE #
# START API VIEW #

# START PATIENT NUMBERS API #
@api_view(['GET'])
def filter_patients_created_within_1_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=1)
    patients = Report.objects.filter(created_at__range=(start_datetime, current_datetime))
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patients_created_within_30_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=30)
    patients = Patient.objects.filter(created_at__range=(start_datetime, current_datetime))
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patients_created_within_365_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=365)
    patients = Patient.objects.filter(created_at__range=(start_datetime, current_datetime))
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)


@api_view(['GET'])
def created_count_total_patients(request):
    total_patients = Patient.objects.aggregate(total=Count('pk'))
    return Response(total_patients)

# END PATIENT NUMBER API #

# START REPORT API #
@api_view(['GET'])
def filter_report_created_within_1_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=1)
    reports = Report.objects.filter(data__range=current_datetime)
    ser = PatientSerializers(reports, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_report_created_within_30_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=30)
    reports = Report.objects.filter(data__range=(start_datetime, current_datetime))
    ser = PatientSerializers(reports, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_report_created_within_365_days(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(days=365)
    reports = Report.objects.filter(data__range=(start_datetime, current_datetime))
    ser = PatientSerializers(reports, many=True)
    return Response(ser.data)


@api_view(['GET'])
def created_count_total_report(request):
    total_reports = Report.objects.aggregate(total=Count('pk'))
    return Response(total_reports)

# END REPORT API #

# START EMPLOYEE  API #
@api_view(['GET'])
def get_all_employees(request):
    employees = Employee.objects.all()
    ser = EmployeeSerializers(employees, many=True)
    return Response(ser.data)

# END EMPLOYEE API #

# START EMPLOYEE BY_NAME FILTERS API #
@api_view(['GET'])
def filter_employee_by_name(request):
    name = request.GET.get('name')
    employees = Employee.objects.filter(name__icontains=name)
    ser =  EmployeeSerializers(employees, many=True)
    return Response(ser.data)

# END EMPLOYEE BY_NAME FILTERS API#

# START EMPLOYYE BY_SPECIALTY FILTERS API #
@api_view(['GET'])
def filter_employee_by_specialty(request):
    specialty = request.GET.get('specialty')
    employees = Employee.objects.filter(employee_specialty=specialty)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# END EMPLOYYE BY _SPECIALTY FILTERS API #

# START EMPLOYYE BY_STATUS FILTERS API #
@api_view(['GET'])
def filter_employee_by_status(request):
    employee_status = request.GET.get('employee_status')
    employees = Employee.objects.filter(employye_status=status)
    ser = EmployeeSerializer(employees, many=True)
    return Response(ser.data)

# END EMPLOYEE BY_STATUS FILTERS API #

# START EMPLOYEE BY_ROOMS FILTERS API #
@api_view(['GET'])
def filter_employee_by_rooms(request):
    room = request.GET.get('room')
    employees = Employee.objects.filter(employye_room=room)
    ser =  EmployeeSerializers(employees, many=True)
    return Response(ser.data)

# END EMPLOYYE BY_ROOMS FILTERS API #

# START EMPLOYEE BY_TIME FILTERS API #
@api_view(['GET'])
def filter_employee_by_time(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    employees = Employee.objects.filter(start_time=start_time,end_time=end_time)
    ser =  EmployeeSerializers(employees, many=True)
    return Response(ser.data)

# END EMPLOYEE BY_TIME FILTERS API #

# START EMPLOYEE BY_SECTION FILTERS API #
@api_view(['GET'])
def filter_employee_by_section(request):
    section = request.GET.get('section')
    employees = Employee.objects.filter(room_section=section)
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# END EMPLOYEE BY_SECTION FILTERS API #

# START SECTION API #
@api_view(['GET'])
def get_all_sections(request):
    sections = Section.objects.all()
    ser = SectionSerializers(sections,many=True)
    return Response(ser.data)

# END SECTION API #

# START ROOMS API #
@api_view(['GET'])
def get_all_rooms(request):
    rooms = Room.objects.all()
    ser = RoomSerializers(rooms,many=True)
    return Response(ser.data)
# END ROOMS API #

# START ROOMS FILTERS BY_CAPACITY API #
@api_view(['GET'])
def filter_rooms_by_capacity(request):
    room_capacity = request.GET.get('room_capacity')
    rooms = Room.objects.filter(room_capacity=room_capacity)
    ser =  RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_CAPACTIY API #

# START FILTERS BY_GENDER API #
@api_view(['GET'])
def filter_rooms_by_gender(request):
    gender = request.GET.get('patient_gender')
    rooms = Room.objects.filter(patient_gender=gender)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS  BY_GENDER API #

# START ROOMS FILTERS BY_FREE API #
@api_view(['GET'])
def filter_rooms_by_free(request):
    is_booked = request.GET.get('is_booked')
    rooms = Room.objects.filter(is_booked=is_booked)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_FREE API #

# START ROOMS FILTERS BY_NAME API #
@api_view(['GET'])
def filter_rooms_by_name(request):
    name = request.GET.get('name')
    rooms = Room.objects.filter(name=name)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_NAME API #

# START ROOMS FILTERS BY_CATEGORY API #
@api_view(['GET'])
def filter_rooms_by_category(request):
    category = request.GET.get(' category')
    rooms = Room.objects.filter(category=category)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_CATEGORY API #

# START ROOMS FILTERS BY_STATUS API #
@api_view(['GET'])
def filter_rooms_by_status(request):
    status = request.GET.get('status')
    rooms = Room.objects.filter(status=status)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_STATUS API #

# START ROOMS FILTERS BY_PRICE API #
@api_view(['GET'])
def filter_rooms(request):
    min_price = request.query_params.get('min_price')
    max_price = request.query_params.get('max_price')

    if not min_price or not max_price:
        return Response({"error": "Minimum and maximum prices are required."})

    rooms = Room.objects.filter(price__range=[min_price, max_price], is_booked=False)
    ser = RoomSerializer(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_PRICE API #

# START ROOMS FILTERS BY_SECTION API #
@api_view(['GET'])
def filter_rooms_by_section(request):
    section = request.GET.get('section')
    rooms = Room.objects.filter(section=section)
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_SECTION API #

# START PATIENT API #
@ api_view(['GET'])
def patient_get_all(request):
    patient = Patient.objects.all()
    ser = PatientSerializers(patient,many=True)
    return Response(ser.data)

# END PATIENT API #

# START PATIENT IS ACTIVETE API #
@api_view(['GET'])
def patient_is_activete(request):
    patient = Patient.objects.all()
    ser = PatientSerializers(patient, many=True)
    patient_data = ser.data
    for patient in patient_data:
        status = "Activ" if patient['is_active'] else "no_activ"
        patient.update({
            "status": status
        })
    return Response(ser.data)

# END PATIENT IS ACTIVETE API #

# START PATIENT FILTERS BY_NAME API #
@api_view(['GET'])
def filter_patient_by_name(request):
    name = request.GET.get('name')
    patient = Patient.objects.filter(name__icontains=name)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)
# END PATIENT FILTERS BY_NAME API #

# START PATIENT SEARCH DIAGNOST API #
@api_view(['GET'])
def search_employees_diagnos(request):
    diagnos = request.GET.get('diagnos')
    employees = Employee.objects.filter(diagnos__icontains=diagnos)
    ser = EmployeeSerializer(employees, many=True)
    return Response(ser.data)
# END PATIENT SEARCH DIAGNOST API #

# START PATIENT FILTERS BY_GENDER API #
@api_view(['GET'])
def filter_patient_by_gender(request):
    gender = request.GET.get('gender')
    patient = Patient.objects.filter(gender=gender)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

# END PATIENT FILTERS BY_GENDER API #

# START PATIENT FILTERS BY_ROOM API #
@api_view(['GET'])
def filter_patient_by_room(request):
    room = request.GET.get('room')
    patient = Patient.objects.filter(room=room)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

# END PATIENT FILTERS BY_ROOM API #

# START PATIENT FILTERS BY_DOCTOR API #
@api_view(['GET'])
def filter_patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor=doctor)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

# END PATIENT FILTERS BY_DOCTOR API #

# START PATIENT FILTERS BY_CREATE_AT API #
@api_view(['GET'])
def filter_patient_by_create_at(request):
    create_at = request.GET.get('create_at')
    patients = Patient.objects.filter(create_at=create_at)
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)

# END PATIENT FILTERS BY_CREATE_AT API #


# START PATIENT SERACH PHONE API #
@api_view(['GET'])
def search_patient_phone(request):
    phone = request.GET.get('phone')
    patients = Patient.objects.filter(phone__icontains=phone)
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)

# END PATIENT SEARCH PHONE API #


# START PATIENT SEARCH NAME API #
@api_view(['GET'])
def search_patient_name(request):
    name = request.GET.get('name')
    patients = Patient.objects.filter(name__icontains=name)
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)

# END PATIENT  SEARCH NAME  API #
