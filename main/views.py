from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def add_Employee_view(request):
    employye = Employee.objects.all()
    ser = EmployeeSerializers(employye, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_Employee_by_name(request):
    name = request.GET.get('name')
    employees = Employee.objects.filter(name__icontains=name)
    ser =  EmployeeSerializers(employees, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_status(request):
    status = request.GET.get('status')
    employees = Employee.objects.filter(employee_status=status)
    ser = EmployeeSerializer(employees, many=True)
    return Response(ser.data)


@api_view(['GET'])
def add_Section_view(request):
    section = Section.objects.all()
    ser = SectionSerializers(section,many=True)
    return Response(ser.data)



@api_view(['GET'])
def add_Room_view(request):
    room = Room.objects.all()
    ser = RoomSerializers(room,many=True)
    return Response(ser.data)


@api_view(['GET'])
def Room_is_booked_view(request):
    rooms = Room.objects.all()
    ser = RoomSerializers(rooms, many=True)
    room_data = ser.data
    for room in room_data:
        status = "Band" if room['is_booked'] else "Bo'sh"
        room.update({
            "status": status
        })
    return Response(ser.data)


@api_view(['GET'])
def Room_category_view(request):
    rooms = Room.objects.all()
    ser = RoomSerializers(rooms, many=True)
    category = request.GET.get('category')
    price = request.GET.get('price')
    rooms = Room.objects.filter(room_category=category,room_price=price)
    ser = EmployeeSerializer(rooms, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Room_status_view(request):
    rooms = Room.objects.all()
    ser = RoomSerializers(rooms, many=True)
    status = request.GET.get('status')
    rooms = Room.objects.filter(room_status=status)
    ser = EmployeeSerializer(rooms, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_Room_by_name(request):
    name = request.GET.get('name')
    rooms = Room.objects.filter(name__icontains=name)
    ser =  RoomSerializers(rooms, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Forpatient_view(request):
    forpatient = Forpatient.objects.all()
    ser = ForpatientSerializers(forpatient,many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_Forpatient_by_name(request):
    name = request.GET.get('name')
    forpatient = Bemor.objects.filter(name__icontains=name)
    ser = BemorSerializers(forpatient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Forpatient_status_view(request):
    forpatient = Forpatient.objects.all()
    ser = ForpatientSerializers(forpatient, many=True)
    gender = request.GET.get('gender')
    forpatient = Forpatient.objects.filter(gender_status=gender)
    ser = EmployeeSerializer(gender, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_operation_view(request):
    operations = Operation.objects.all()
    ser = OperationSerializer(operations, many=True)
    return Response(ser.data)


# @api_view(['GET'])
# def get_info_view(request):
#     info = Info.objects.all()
#     ser = InfoSerializers(info, many=True)
#     return Response(ser.data)

@api_view(['POST'])
def create_info_view(request):
    name = request.POST.get('name')
    about = request.POST.get('about')
    employee_number = request.POST.get('employee_number')
    max_number = Info.objects.aggregate(models.Max('number_of_recovered_orpatient'))['number_of_recovered_orpatient__max']
    number_of_recovered_orpatient = max_number + 1 if max_number is not None else 1
    info = Info.objects.create(
        name=name,
        about=about,
        employee_number=employee_number,
        number_of_recovered_orpatient=number_of_recovered_orpatient,
    )
    ser = InfoSerializer(info)
    return Response(ser.data)


@api_view(['GET'])
def cassa_view(request):
    cassa = Cassa.objects.all()
    ser = CassaSerializers(cassa,many=True)
    return Response(ser.data)

#
# @api_view(['GET'])
# def report_view(request):
#     cassa = Report.objects.all()
#     ser = CassaSerializers(cassa,many=True)
#     return Response(ser.data)


@api_view(['POST'])
def create_report_view(request):
    benefit = request.POST.get('benefit')
    cost = request.POST.get('cost')
    description = request.POST.get('description', '')
    date = request.POST.get('date', None)

    report = Report.objects.create(
        benefit=benefit,
        cost=cost,
        description=description,
        date=date
    )

    ser = ReportSerializer(report)
    return Response(ser.data)


# @api_view(['GET'])
# def queue_view(request):
#     cassa = Queue.objects.all()
#     ser = CassaSerializers(cassa,many=True)
#     return Response(ser.data)


@api_view(['POST'])
def create_queue(request):
    doctor_pk = request.POST.get('pk', None)
    description = request.POST.get('description', '')
    created_at = request.POST.get('created_at', None)

    if doctor_pk is None:
        return Response({'error': 'Invalid request'})

    doctor = Employee.objects.get(pk=doctor_pk)

    # Queue modelidan eng katta number ni olib, 1 ga qo'shib yangi Queue obyektiga yozish
    max_number = Queue.objects.aggregate(models.Max('number'))['number__max']
    number = max_number + 1 if max_number is not None else 1

    queue = Queue.objects.create(
        doctor=doctor,
        number=number,
        description=description,
        created_at=created_at
    )

    ser = QueueSerializer(queue)
    return Response(ser.data)


@api_view(['GET'])
def filter_queues_by_name(request):
    name = request.query_params.get('name', None)

    if name is None:
        return Response({'error': 'Invalid request'})

    queues = Queue.objects.filter(name=name)

    ser = QueueSerializer(queues, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Attendance_view(request):
    cassa = Attendance.objects.all()
    ser = CassaSerializers(cassa,many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_attendance_view(request):
    doctor_pk = request.query_params.get('doctor_pk', None)

    if doctor_pk is None:
        return Response({"it's a pity ": " He didn't come today "})

    attendances = Attendance.objects.filter(Doctor=doctor_pk, Status=True)

    ser = AttendanceSerializer(attendances, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_forpatient_payment(request, pk):
    forpatient = Forpatient.objects.get(pk=pk)
    total = forpatient.total_price
    cassa = Cassa.objects.get(pk=1)
    cassa.balance += total
    cassa.save()
    create_forpatient_payment = Forpatient_payment.objects.create(
        forpatient=forpatient.pk,
        total=total,
        description=request.data.get('description', None),
        created_at=request.data.get('created_at', None),
        kod=request.data.get('kod', None)
    )

    ser = ForpatientPaymentSerializer(create_forpatient_payment)
    return Response(ser.data)





