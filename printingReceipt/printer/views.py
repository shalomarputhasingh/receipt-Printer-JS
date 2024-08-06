from django.shortcuts import render
from .models import Students, Bills
# Create your views here.
def studentBill(request):
    student = Students.objects.get(name = "Kevin") #Got the particular Student Object
    bills = Bills.objects.get(student_id = student.unique_id)
    context = {'student':student,'bill':bills}
    return render(request,'printer/receipt.html',context)