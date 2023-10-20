from main.models import User,Employee,Section,Room,Patient,Operation,Cassa,Report,Queue,Attendance,Payment,Informations
from main.serializers import UserSerializers, EmployeeSerializers,SectionSerializers,RoomSerializers,PatientSerializers,OperationSerializers,CassaSerializers,ReportSerializers,QueueSerializers,AttendanceSerializers,PaymentSerializers,InformationsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView

#START CRUD ALL MODELS #
#START USER GENERICS API #
# class CreateUser(CreateAPIView):
#     queryset = User.objects.all()
#     serilizer_class = UserSerializers
#
#
#
# class UpadteUser(UpdateAPIView):
#     queryset = User.objects.all()
#     serializers_class = UserSerializers
#
#
# class DeleteUser(DestroyAPIView):
#     queryset = User.objects.all()
#     serializers_class = UserSerializers

#END USER GENERICS API #

#START EMPLOYYE GENERICS API #
class CreateEmployye(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class UpadteEmployye(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class DeleteEmployye(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

#END EMPLOYEE GENERICS API #

# START  SECTION GENERICS API #
class CreateSection(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class UpadteSection(UpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers


class DeleteSection(DestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializers

# END SECTION GENERICS API #

# START  ROOM GENERICS API #
class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class UpadteRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

# END ROOM GENERICS API #

# START  PATIENT GENERICS API #
class CreatePatienent(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class UpdatePatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

# END PATIENT GENERICS API #

# START  OPERATION GENERICS API #
class CreateOperation(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class UpadteOperation(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers

# END OPERATION GENERICS API #

# START  INFORMATIONS GENERICS API #
class CreateInformations(ListCreateAPIView):
    queryset = Informations.objects.all()
    serializer_class = InformationsSerializers


class UpadteInformations(UpdateAPIView):
    queryset = Informations.objects.all()
    serializer_class = InformationsSerializers


class DeleteInformations(DestroyAPIView):
    queryset = Informations.objects.all()
    serializers_class = InformationsSerializers

# END INFORMATIONS GENERICS API #

# START  CASSA GENERICS API #
class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class UpdateCassa(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class DeleteCassa(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers

# END CASSA GENERICS API #

# START  REPORT GENERICS API #

class CreateReport(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


class UpdateReport(UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


class DeleteReport(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers

# END REPORT GENERICS API #

# START  QUEUE GENERICS API #
class CreateQueue(ListCreateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers


class UpdateQueue(UpdateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers


class DeleteQueue(DestroyAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializers

# END QUEUE GENERICS API #

# START  ATENDANCE GENERICS API #
class CreateAttdence(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class UpdateAttdence(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class DeleteAttdence(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers

# END ATTENDANCE GENERICS API #

# START  PAYMENT GENERICS API #
class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

# END PAYMENTGENERICS API #
# END CRUD ALL MODELS #


