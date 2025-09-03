from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import TaskSerializer
from tasks.models import Task
# Create your views here.



class TaskList(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Task.objects.filter(user=user)

        d = self.request.query_params.get('d') #type:ignore
        q = self.request.query_params.get('q') #type:ignore

        if d is not None and d.lower() not in ('true', 'false', '1', '0'):
            raise ValidationError({'d': 'Invalid value; use true/false or 1/0'})
        
        if d is not None:
            qs = qs.filter(done=d.strip().lower() in ('true', '1'))

        if q:
            q = q.strip()
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))

        return qs




class TaskDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)