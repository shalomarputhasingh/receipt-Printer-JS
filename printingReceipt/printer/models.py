from django.db import models

# Create your models here.

#Basic Student Model

#In the admin panel you can add new Students
class Students (models.Model):
    unique_id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=200)
    def __int__(self):
        return self.unique_id
#Basic Bill Structure
class Bills(models.Model):
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    description = models.TextField(null=False)
    date = models.DateField(null=False)