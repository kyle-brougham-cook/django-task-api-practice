from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    def validate_title(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Title cannot be empty or whitespace")
        if len(cleaned_value) > 50:
            raise serializers.ValidationError("The Title cannot be more than 50 characters")
        return cleaned_value
    

    def validate_description(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Description cannot be empty or whitespace")
        if len(cleaned_value) > 150:
            raise serializers.ValidationError("Description cannot be more than 150 characters in length")
        if len(cleaned_value) < 10:
            raise serializers.ValidationError("Description cant be less than 10 characters in length")        
        return cleaned_value


    def validate_done(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Done must be either true or false")
        return value


    class Meta:
        model = Task
        fields = ['id', 'title', 'done', 'user', 'description'] 
        read_only_fields = ['id']
        extra_kwargs = {
            'title': {'max_length': 50},
            'description': {'max_length': 150, 'min_length': 10}
        }


