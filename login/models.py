import uuid
from django.db import models
from decimal import Decimal
from phone.models import PhoneNumber

from django.db import models
import uuid

class form(models.Model):  # PascalCase naming
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15, unique=True)  # Fixed field name
    dob = models.DateField(null=True, blank=True)  # New
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])  # Fixed typo
    location = models.CharField(max_length=255, null=True, blank=True)  # New
    exam_target = models.CharField(max_length=255, null=True, blank=True)  # New
    program = models.CharField(max_length=255, null=True, blank=True)  # New
    firebase_user_id = models.CharField(max_length=255)  # Required field

    def __str__(self):
        return self.full_name

class UserForm(models.Model):
    user = models.ForeignKey(form, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='userform/')
    course = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return self.title

class Payment(models.Model):
    PAYMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed')
    )
    
    user = models.ForeignKey(form, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(UserForm, on_delete=models.CASCADE, related_name='course_payments')
    gst_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"

    def save(self, *args, **kwargs):
        # Ensure the course is set before calculating the amount
        if self.course:
            # Reference the amount from the related course (UserForm model)
            self.gst_amount = (self.course.amount * Decimal('0.18')).quantize(Decimal('0.01'))
            self.total_amount = self.course.amount + self.gst_amount
        super().save(*args, **kwargs)
