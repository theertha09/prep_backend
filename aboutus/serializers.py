from rest_framework import serializers
from .models import MetaTagsAboutUs
from rest_framework import serializers
from .models import Question, Option, UserResponse



class MetaTagsAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsAboutUs
        fields = "__all__"


from rest_framework import serializers
from .models import Question, Option, UserResponse

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ["id", "text", "options"]

    def get_options(self, obj):
        return OptionSerializer(obj.options.all(), many=True).data

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "question", "text"]

class UserResponseSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source="question.text", read_only=True)
    selected_option_text = serializers.CharField(source="selected_option.text", read_only=True)

    class Meta:
        model = UserResponse
        fields = [
            "id",  # Assuming you want to include the ID of the response
            "full_name", 
            "email", 
            "phone_number", 
            "school_name", 
            "location", 
            "question", 
            "question_text", 
            "selected_option", 
            "selected_option_text",
            "class_type"
        ]
