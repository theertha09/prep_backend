# from rest_framework import serializers
# from .models import courseCategory, SubjectCategory,SectionCategory

# class courseCategorySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = courseCategory
#         fields = '__all__'

# class SubjectCategorySerializer(serializers.ModelSerializer):
#     course_name = serializers.CharField(source='course.category', read_only=True)

#     class Meta:
#         model = SubjectCategory
#         fields = ['id', 'course', 'course_name', 'subject_name']
# class SectionCategorySerializer(serializers.ModelSerializer):
#     subject_name = serializers.CharField(source='subject.subject_name', read_only=True)

#     class Meta:
#         model = SectionCategory
#         fields = ['id', 'subject', 'subject_name', 'section_name']
