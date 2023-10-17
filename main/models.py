from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone  = models.CharField(max_length=13, unique=True, blank=True, null=True, validators=[
    RegexValidator(
        regex='^[\+]9{2}8{1}[0-9]{9}$',
        message='Invalid phone number',
        code='invalid_number'
    ),])

    adress = models.CharField(max_length=50,verbose_name="manzil")

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class  Employee(models.Model):
   name = models.CharField(max_length=30)
   phone = models.CharField(max_length=13, blank=False, unique=True, validators=[
       RegexValidator(
           regex='^[\+]9{2}8{1}[0-9]{9}$',
           message='Invalid phone number',
           code='invalid_number'
       ), ])
   employee_status = models.IntegerField( blank=False, choices=
   (
       (1, "doktor"),
       (2, "admin"),
       (3, "boshqaruvchi"),

   )
                                        )
   descriptions = models.TextField(verbose_name="batafsil malumot")
   experience = models.IntegerField(verbose_name="ish tajribasi")
   salary = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name="ish haqi")
   age = models.IntegerField(verbose_name="yoshi")
   room = models.ForeignKey(to="Room", on_delete=models.SET_NULL,verbose_name='xona')
   specialty = models.CharField(max_length=30,verbose_name="mutaxasisligi")
   start_time = models.TimeField()
   end_time = models.TimeField()

   def __str__(self):
        return self.employye.name


class Section(models.Model):
    name = models.CharField(max_length=25,verbose_name="bo'lim nomi")
    descriptioon = models.TextField(verbose_name="to'liq malumot")

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=20,verbose_name="Xona Raqami")
    is_booked = models.BooleanField(default=False)
    room_capacity = models.IntegerField(verbose_name="xona sig'imi")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    section = models.ForeignKey(to=Section, on_delete=models.PROTECT,verbose_name="bolim xonasi ")
    status = models.IntegerField(blank=False,choices= (
       (1, "Forpatient"),
       (2, "for employee"),


   )
                                 )

    category = models.IntegerField(blank=False, choices=(
        (1, "Lux"),
        (2, "Econom"),
        (3,"Operatsiya")
    )
                                   )

    def __str__(self):
        return self.number


class Forpatient(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=13, blank=False, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    photo = models.ImageField(upload_to='Forpatient_image',verbose_name='bemorning rasmi')
    gender = models.IntegerField(verbose_name="bemorning' jinsi",blank=False, choices=(
        (1, "Famele"),
        (2, "Male"),

    )
                                   )
    day = models.IntegerField(null=True,blank=True,verbose_name="bemorning' qancha kun dovolanishi")
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name="bemornig' xonasi")
    doctor = models.ForeignKey(to=Employee, on_delete=models.CASCADE,verbose_name="bemornig' doktori")
    created_time = models.DateTimeField(auto_created=True,verbose_name="bemorning yaratilgan vaqti")

    def __str__(self):
        return self.forpatient.name


class  Operation(models.Model):
    forpatient = models.ForeignKey(to=Forpatient,on_delete=models.PROTECT,verbose_name="bemor")
    doctors = models.ManyToManyField(to=Employee,verbose_name="bemroning' doktorlari")
    duration_time = models.TimeField(verbose_name="operatsiya qancha dovom etish vaqti ")
    operation_time = models.DateTimeField(verbose_name="operatsa kuni va vaqti")
    room = models.ForeignKey(to=Room,on_delete=models.PROTECT,verbose_name="operatsa xonasi")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='operatsa summasi')

    def __str__(self):
        return self.forpatient.name


class Info(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(verbose_name="to'liq malumot ")
    employee_number = models.IntegerField(default=0,verbose_name="ishchilar soni")
    number_of_recovered_orpatient = models.IntegerField(default=0,verbose_name="shifo topgan bemorlar soni")

    def __str__(self):
        return self.name


class Cassa(models.Model):
    password = models.CharField(max_length=15,verbose_name="cassaga kirish uchun password ")
    Balance = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name="umimiy cassada bor summa")


class Report(models.Model):
    benefit = models.DecimalField(default=0, max_digits=10, decimal_places=2,verbose_name="foyda '+'  summalar")
    cost =  models.DecimalField( default=0,max_digits=10, decimal_places=2,verbose_name="chiqim  '-'   summalar")
    description = models.TextField(verbose_name="to'liq malumot")
    date = models.DateField(verbose_name="hisobot chiqarilgan kun")


class Queue(models.Model):
    name = models.CharField(max_length=30)
    doctor = models.ForeignKey(to=Employee,on_delete=models.CASCADE,verbose_name="bemorning' doktori")
    number = models.IntegerField(verbose_name="navbat raqami")
    description = models.TextField(verbose_name="to'liq malumot ")
    created_at = models.TimeField(verbose_name="navbat yaratilgan vaqti ")


class Attendance(models.Model):
    Doctor = models.ForeignKey(to=Employee,on_delete=models.PROTECT,verbose_name= "Davomat uchun doktorni shaxsi ")
    Status = models.BooleanField(default=False)


class Forpatient_payment(models.Model):
    forpatient = models.ForeignKey(to=Forpatient, on_delete=models.PROTECT)
    total = models.IntegerField(verbose_name="umumiy to'lov summa")
    description = models.TextField(null=True)
    created_at = models.DateTimeField(verbose_name=" to'lov yaratilgan vaqti ")
    kod = models.CharField(max_length=20)

    def __str__(self):
          return self.forpatient.name









