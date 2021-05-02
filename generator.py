#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudDemo.settings')

import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *
faker = Faker()

def generator(n):
    for i in range(n):
        fempno = randint(1, 10000)
        fempname = faker.name()
        fempexp = randint(100, 10000)
        fempaddress = faker.city
        emp_record = Employee.objects.get_or_create(empno=fempno, empname=fempname, empexp=fempexp, empaddress=fempaddress)

generator(20)        
