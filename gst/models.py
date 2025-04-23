from django.db import models

# Create your models here.
class PaymentSettings(models.Model):
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Payment Settings - {self.razorpay_key_id}"
