from django.shortcuts import render
from qwerty import models


def first_page(self):
    persons = models.Person.objects.all()
    data = {
            "asd": persons
        }
    return render(self, 'index.html', data)

#hello world
def second_page(self):
    persons = models.Bank.objects.all()
    data = {
            "qwe": persons
        }
    return render(self, 'index1.html',data)



def second2_page(self):
    persons = models.Lombard.objects.all()
    data = {
        "zxc": persons
    }
    return render(self, 'index2.html',data)



def third_page(self):
    persons = models.Cars.objects.all()
    data = {
        "iop":persons
    }
    return render(self, 'index3.html',data)


def fourth_page(self):
    return render(self, 'index4.html')