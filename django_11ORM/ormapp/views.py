from django.shortcuts import render
from .models import *
from faker import Faker
import random
from django.db.models import *
from django.db.models.functions import *
# Create your views here.
fake = Faker()
def addStudent():
    st = Student()
    st.name= fake.name()
    st.aggregate=round(random.uniform(33.0,100.0),2)
    st.city = fake.city()
    st.joindate = fake.date()
    st.save()

#addStudent()

def getdata():
    # st = Student.objects.all()
    # st = Student.objects.get(id=1)
    # for s in st:
    #     print(s)
    # print(st.name)

    # st = Student.objects.filter(id__lt=10)
    # st = Student.objects.filter(id__gte=10)
    # st = Student.objects.get(name__exact='Suzanne Ortega')
    # st = Student.objects.get(name__iexact='suzanne Ortega')
    # st = Student.objects.filter(name__contains='c')
    # st = Student.objects.filter(name__icontains='c')
    # st = Student.objects.filter(name__in=['Catherine Bernard','Dr'])
    # st = Student.objects.filter(name__startswith='B')
    # st = Student.objects.filter(name__endswith='A')
    # st = Student.objects.filter(joindate__range=('2010-02-24','2015-10-06'))
    # st = Student.objects.filter(aggregate__range=(90.9,100))
    #
    # st = Student.objects.filter(aggregate__range=(90.9,100))
    # # print(st.name)
    # for s in st:
    #     print(s.name)
    pass

# getdata()

def queries():
    st = Student.objects.filter(name__istartswith="A") | Student.objects.filter(aggregate__lt=56)
    # st = Student.objects.filter(Q(name__istartswith="A")|Q(aggregate__lt=56))
    #AND IMPLEMENTATION
    # st = Student.objects.filter(name__istartswith="A") & Student.objects.filter(aggregate__lt=56)
    # st = Student.objects.filter(name__istartswith="A",aggregate__lt=89)
    # st = Student.objects.filter(Q(name__istartswith="A"),Q(aggregate__lt=89))

    #NOT BASED QUERIES
    # st = Student.objects.filter(Q(name__istartswith="A"),~Q(aggregate__lt=89))
    st = Student.objects.exclude(aggregate__lt=89)
    # print(st)

    #Query Unions

    # st1 = Student.objects.filter(city__in=['Ronaldfort',"Allenshire,""North Connie","New Matthewburgh","Brianhaven","Port Rita","West Shannon","East Vincentfort","North Christineton"])
    # st2 = Student.objects.filter(aggregate__lt=50)
    # st3 = st1.union(st2)

    #selecting required columns or fields

    # st = Student.objects.all().values('name','aggregate')
    # st = Student.objects.all().values_list('name','aggregate')
    st = Student.objects.all().only('name','aggregate')
    print(st)
    for s in st:
        #values() returns a tuple with specified fields, only() returns a query set with id column
        print(s.id,s.name)
        # print(s)

# queries()

def aggregators():
    #get minimum,maximum,avg,count,sum values
    min = Student.objects.all().aggregate(Min('aggregate'))
    max = Student.objects.all().aggregate(Max('aggregate'))
    avg = Student.objects.all().aggregate(Avg('aggregate'))
    sum = Student.objects.all().aggregate(Sum('aggregate'))
    count = Student.objects.all().aggregate(Count('aggregate'))

    print(min)
    print(max)
    print(avg)
    print(sum)
    print(count)
    #these data can be sent as context or json data to the html or an API consumer


# aggregators()

def cruds():
    #crud ops
    #Retrieve
    # st = Student.objects.all()
    # #create
    # st = Student(name="Chetan",aggregate=99.76,city="Bangalore",joindate="2020-01-20")
    # st.save()
    # #save on the spot
    # st = Student.objects.create(name="Dheeru",aggregate=92.76,city="Bangalore",joindate="2020-01-20")
    # st = Student.objects.all()
    # print(st[33].name)

    #add bulk data
    #takes list of Student objects
    data = [
        Student(name="Ajay",aggregate=88,city="Chennai",joindate="2015-10-09"),
        Student(name="Abhi",aggregate=45,city="Chennai",joindate="2016-10-09"),
        Student(name="Jai",aggregate=45,city="Bhopal",joindate="2018-10-05"),
        Student(name="Veeru",aggregate=45,city="Chambal",joindate="2018-10-09"),
        Student(name="gabbar",aggregate=88,city="Jharkhand",joindate="2019-10-09"),
        Student(name="Jisna",aggregate=24,city="Lucknow",joindate="2014-10-09"),
        Student(name="Chandru",aggregate=22,city="Surat",joindate="2011-10-09"),
        Student(name="Dil",aggregate=78,city="Vizag",joindate="2012-10-09"),
    ]
    # st = Student.objects.bulk_create(data)
    # print(st)

    #delete one or more or all row or data tuple or a record in database table
    # st = Student.objects.filter(name__contains='c')
    # st = Student.objects.filter(name='Jisna')
    # print(st.count())
    # st.delete()
    # print(st.count())
    # st = Student.objects.all()
    # st.delete()

    #update data
    # st = Student.objects.get(pk=123)
    # st.name="Pradyuman"
    # st.city="Borivali"
    # st.save()



# cruds()


def ordering():
    #to order or sort data
    #asc order
    st = Student.objects.all().order_by('name')
    #desc order
    st = Student.objects.all().order_by('-name')

    #top 3 names
    st = Student.objects.all().order_by('-name')[:3]

    # top 3 performers
    st = Student.objects.all().order_by('-aggregate')[:3]

    # bottom 3 performers
    st = Student.objects.all().order_by('aggregate')[:3]

    #recent 3 joinees
    st = Student.objects.all().order_by('-joindate')[:3]

    # oldest 3 joinees
    st = Student.objects.all().order_by('joindate')[:3]

    # alphabetical order sort cleaning
    #Lower casing removes ambiguity of sorting names which are usually strings
    st = Student.objects.all().order_by(Lower('name'))

    for s in st:
        print(s.name)

ordering()