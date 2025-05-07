import uuid
from django.db import models
from decimal import Decimal
from phone.models import PhoneNumber
from django.utils.timezone import now


# ------------------------
# Category Models
# ------------------------

class courseCategory(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category


class SubjectCategory(models.Model):
    course = models.ForeignKey(courseCategory, on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subject_name} ({self.course.category})"


class SectionCategory(models.Model):
    subject = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE, related_name='sections')
    section_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.section_name} ({self.subject.subject_name})"


# User Registration Form

class form(models.Model):  # Consider renaming to `Form` (PascalCase)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    location = models.CharField(max_length=255, null=True, blank=True)
    exam_target = models.CharField(max_length=255, null=True, blank=True)
    program = models.CharField(max_length=255, null=True, blank=True)
    firebase_user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


# User Course Form

class UserForm(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_features = models.CharField(max_length=255)
    image = models.ImageField(upload_to='userform/')
    course_description = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    course = models.ForeignKey(courseCategory, on_delete=models.CASCADE, related_name='user_forms')
    section = models.ForeignKey(SectionCategory, on_delete=models.CASCADE, related_name='user_forms')

    def __str__(self):
        return self.title



# Payment Info

class UserFormPayment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(form, on_delete=models.CASCADE)
    userform = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.user.full_name} - Payment for {self.userform.title}'
