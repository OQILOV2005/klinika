from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime,timedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

# START MAIN ALGORITMS HOME PAGE #
# START API VIEW #

# START PATIENT NUMBERS API #
@api_view(['GET'])
def filter_patients_created_within_1_days(request):
    current_datetime = datetime.now()
    patients = Patient.objects.filter(created_at=current_datetime)
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patients_created_within_30_days(request):
    current_datetime = datetime.now()
    a = current_datetime.strftime("%m")
    patient = Patient.objects.all()
    monthly_patient = []
    for i in patient:
        b = str(i.created_at)[5:7]
        if int(b) == int(a):
            monthly_patient.append(i)
    ser = PatientSerializers(monthly_patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patients_created_within_365_days(request):
    current_datetime = datetime.now()
    a = current_datetime.strftime("%Y")
    patient = Patient.objects.all()
    year_patient = []
    for i in patient:
        b = str(i.created_at)[:5]
        if int(b) == int(a):
            year_patient.append(i)
    ser = PatientSerializers(year_patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def created_count_total_patients(request):
        patients = Patient.objects.all()
        ser = PatientSerializers(patients, many=True)
        return Response(ser.data)

# END PATIENT NUMBER API #

# START REPORT API #
@api_view(['GET'])
def filter_report_created_within_1_days(request):
    current_datetime = datetime.now()
    reports = Report.objects.filter(created_at=current_datetime)
    ser = ReportSerializers(reports, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_report_created_within_30_days(request):
    current_datetime = datetime.now()
    a = current_datetime.strftime("%m")
    report = Report.objects.all()
    monthly_report = []
    for i in report:
        b = str(i.created_at)[5:7]
        if int(b) == int(a):
            monthly_report.append(i)
    ser = ReportSerializers(monthly_report, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_report_created_within_365_days(request):
    current_datetime = datetime.now()
    a = current_datetime.strftime("%Y")
    report = Report.objects.all()
    year_report = []
    for i in report:
        b = str(i.created_at)[:5]
        if int(b) == int(a):
            year_report.append(i)
    ser = ReportSerializers(year_report, many=True)
    return Response(ser.data)


@api_view(['GET'])
def created_count_total_report(request):
    reports = Report.objects.all()
    ser = ReportSerializers(reports, many=True)
    return Response(ser.data)

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
    if not specialty:
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(specialty=specialty)
    serializer = EmployeeSerializers(employees, many=True)
    data = [{"name": employee.name, "specialty": employee.specialty} for employee in employees]
    return Response(data)

# END EMPLOYYE BY _SPECIALTY FILTERS API #

# START EMPLOYYE BY_STATUS FILTERS API #
@api_view(['GET'])
def filter_employee_by_status(request):
    status = request.GET.get('status')
    employees = Employee.objects.filter(status=status)
    ser = EmployeeSerializers(employees, many=True)
    return Response(ser.data)

# END EMPLOYEE BY_STATUS FILTERS API #

# START EMPLOYEE BY_ROOMS FILTERS API #
@api_view(['GET'])
def filter_employee_by_rooms(request):
    room = request.GET.get('room')
    employees = Employee.objects.filter(room=room)
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
    employees = Employee.objects.filter(room__section=section)
    data = []
    for employee in employees:
        if employee.room:
            data.append({"name": employee.name, "room": employee.room.name, "section": employee.room.section})
        else:
            data.append({"name": employee.name, "room": None, "section": None})
    return Response(data)

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
    ser = RoomSerializers(rooms, many=True)
    return Response(ser.data)

# END ROOMS FILTERS BY_CAPACTIY API #

# START FILTERS BY_GENDER API #
@api_view(['GET'])
def filter_rooms_by_gender(request):
    gender = request.GET.get('gender')
    rooms = Room.objects.filter(patient__gender=gender)
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
    category = request.GET.get('category')
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
    ser = RoomSerializers(rooms, many=True)
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
    employees = Employee.objects.filter(name__icontains=diagnos)
    ser = EmployeeSerializers(employees, many=True)
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
def filter_patients_by_room(request):
    room = request.GET.get('room')
    patients = Patient.objects.filter(room=room)
    ser = PatientSerializers(patients, many=True)
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
def filter_patients_by_create_at(request, pk):
    patient = Patient.objects.get(pk=pk)
    created_at = patient.created_at
    patients = Patient.objects.filter(created_at=created_at)
    ser = PatientSerializers(patients, many=True)
    return Response(ser.data)

# END PATIENT FILTERS BY_CREATE_AT API #


# START PATIENT SERACH PHONE API #
@api_view(['GET'])
def search_patient_phone(request):
    phone = request.GET.get('phone')
    patients = Patient.objects.filter(phone__icontains=phone)
    ser = PatientSerializers(patients, many=True)
    attendance_data = ser.data
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

# START ATTENDENCE FILTER STATUS DAY API #

@api_view(['GET'])
def filter_attendance_by_status_date(request):
    target_date = timezone.now().date() - timedelta(days=1)
    attendance = Attendance.objects.filter(date=target_date)
    if not attendance:
        return Response({'ok'})  # Bo'sh ro'yhatni qaytarish
    ser = AttendanceSerializers(attendance, many=True)
    for record in ser.data:
        record['status'] = "Came" if record['status'] else "Did not come"
    return Response(ser.data)


@api_view(['GET'])
def filter_attendance_by_status_date_come_true(request):
    last_24_hours = timezone.now() - timedelta(hours=24)
    attendance = Attendance.objects.filter(date__gte=last_24_hours, status=True)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_attendance_by_status_day_false_come(request):
    last_24_hours = timezone.now() - timedelta(hours=24)
    attendance = Attendance.objects.filter(date__gte=last_24_hours, status=False)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_attendance_by_status_monthly(request,pk):
    last_30_days = timezone.now() - timedelta(days=30)
    attendance = Attendance.objects.filter(date__gte=last_30_days)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_attendance_by_employee_last_30_days(request, doctor):
    employee_attendance = Attendance.objects.filter(pk=doctor)
    last_30_days = timezone.now() - timedelta(days=30)
    recent_attendance = employee_attendance.filter(date__gte=last_30_days)
    ser = AttendanceSerializers(recent_attendance, many=True)
    return Response(ser.data)

# END ATTENDENCE FILTER STATUSC DAY API #

# STAR CASSA API #
@api_view(['GET'])
def get_cassa_balance(request, password):
    try:
        cassa = Cassa.objects.get(password=password)
        ser = CassaSerializers(cassa)
        return Response(ser.data)
    except Cassa.DoesNotExist:
        return Response({'message': 'Code not found'})

# END CASSA API #

# START INFIRMATIONS API #
@api_view(['GET'])
def informations_get_all(request):
    informations = Informations.objects.all()
    ser = InformationsSerializers(informations)
    return Response(ser.data)

# END INFIRMATIONS API #

# START PAYMENT API #
@api_view(['GET'])
def daily_payments(request):
    current_datetime = datetime.now()
    start_datetime = current_datetime - timedelta(hours=24)
    payments = Payment.objects.filter(created_at__gte=start_datetime, created_at__lte=current_datetime)
    serializer = PaymentSerializers(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def date_filtered_payments(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    payments = Payment.objects.filter(created_at__range=[start_date, end_date])
    serializer = PaymentSerializers(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def code_filtered_payments(request, code):
    payments = Payment.objects.filter(code=code)
    serializer = PaymentSerializers(payments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_payments(request):
    payments = Payment.objects.all()
    ser = PaymentSerializers(payments, many=True)
    return Response(ser.data)

# END PAYMENT API #

# START OPERATIONS API #
@api_view(['GET'])
def all_doctors_in_operations(request):
    operations = Operation.objects.all()
    doctors = Employee.objects.filter(operation__in=operations)
    ser = EmployeeSerializers(doctors, many=True)
    return Response(ser.data)


@api_view(['GET'])
def all_transactions(request):
    operations = Operation.objects.all()
    ser = OperationSerializers(operations, many=True)
    return Response(ser.data)

# END OPERATION API #

#START QUEUE API #
@api_view(['GET'])
def queues_by_doctor(reuest, pk):
     patient_operations = Operation.objects.filter(pk=pk)
     doctors = Employee.objects.filter(operation__in=patient_operations)
     serializer = OperationSerializer(doctors, many=True)
     return Response(serializer.data)


@api_view(['GET'])
def get_all_queue(request):
    queues = Queue.objects.all()
    serializer = QueueSerializers(queues, many=True)
    return Response(serializer.data)

#END  QUEUE API #

# END MAIN ALGORITMS HOME PAGE #
# END API VIEW #