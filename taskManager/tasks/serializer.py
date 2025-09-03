from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['id', 'title', 'done', 'user'] 
        read_only_fields = ['id']


