from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class ForpatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Forpatient
        fields = "__all__"


class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"


class  ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class QueueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = "__all__"


class Forpatient_paymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Forpatient_payment
        fields = "__all__"



