from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)

    # used in issue book
    def __str__(self):
        return self.user.first_name + '[' + str(self.enrollment) + ']'

    @property
    def get_name(self):
        return self.user.first_name

    @property
    def getuserid(self):
        return self.user.id

    class Meta:
        unique_together = ('user', 'enrollment', 'branch')


class Book(models.Model):
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
    ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField(unique=True)
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30, choices=catchoice, default='education')

    def __str__(self):
        return str(self.name) + "[" + str(self.isbn) + ']'


def get_expiry():
    return datetime.today() + timedelta(days=15)


class IssuedBook(models.Model):
    user = models.ForeignKey(StudentExtra, on_delete=models.CASCADE, null=True, blank=True)
    # moved this in forms.py
    # enrollment=[(student.enrollment,str(student.get_name)+' ['+str(student.enrollment)+']') for student in StudentExtra.objects.all()]
    enrollment = models.CharField(max_length=30)
    # isbn=[(str(book.isbn),book.name+' ['+str(book.isbn)+']') for book in Book.objects.all()]
    isbn = models.CharField(max_length=30)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return self.enrollment

    class Meta:
        unique_together = ('user', 'isbn')

class ReturnedBookDetail(models.Model):
    user = models.ForeignKey(StudentExtra, on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.CharField(max_length=30)
    issued_date = models.DateField()
    returned_date = models.DateField(auto_now_add=True)
    fine = models.FloatField(default=0)

    @property
    def get_student_name(self):
        return self.user.user.first_name

    @property
    def get_book_name(self):
        return Book.objects.get(isbn=self.isbn).name

    @property
    def get_issued_date(self):
        return self.issued_date + timedelta(hours=5,minutes=45)

    @property
    def get_returned_date(self):
        return self.returned_date + timedelta(hours=5, minutes=45)

