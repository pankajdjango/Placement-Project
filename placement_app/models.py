from django.db import models

class Students(models.Model):
    roll_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email =models.EmailField(max_length=80)
    branch = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    def __str__(self):
        return self.name
    

class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    co_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.co_name

class Interviews(models.Model):
    interview_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    interview_date = models.DateField()
    interview_status = models.CharField(max_length=50)
    interview_feedback = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.company.co_name}"


class Placements(models.Model):
    placement_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interviews, on_delete=models.CASCADE)
    placement_date = models.DateField()
    offered_salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.student.name} - {self.company.co_name} - {self.offered_salary}"
    
