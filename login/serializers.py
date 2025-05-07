# serializers.py
from rest_framework import serializers
from .models import form, UserForm, UserFormPayment,SectionCategory,courseCategory,SubjectCategory

class courseCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = courseCategory
        fields = '__all__'

class SubjectCategorySerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.category', read_only=True)

    class Meta:
        model = SubjectCategory
        fields = ['id', 'course', 'course_name', 'subject_name']
class SectionCategorySerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.subject_name', read_only=True)

    class Meta:
        model = SectionCategory
        fields = ['id', 'subject', 'subject_name', 'section_name']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = '__all__'

class UserFormSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.category', read_only=True)
    section_name = serializers.CharField(source='section.section_name', read_only=True)

    class Meta:
        model = UserForm
        fields = [
            'id', 'uuid', 'course', 'course_name', 'section', 'section_name',
            'title', 'description', 'course_features', 'image',
            'course_description', 'duration', 'amount'
        ]

# serializers.py
class PaymentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.name', read_only=True)
    course_name = serializers.CharField(source='userform.title', read_only=True)

    class Meta:
        model = UserFormPayment
        fields = '__all__'  # This includes all original model fields
        # You can also use a manual list like below:
        # fields = ['id', 'user', 'userform', 'amount', 'razorpay_order_id', 'payment_status', 'username', 'course_name']
class PaymentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.name', read_only=True)
    course_name = serializers.CharField(source='userform.title', read_only=True)

    class Meta:
        model = UserFormPayment
        fields = '__all__'  # Keep all fields, including IDs
