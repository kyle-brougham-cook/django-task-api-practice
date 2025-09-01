from django.db import connection
from django.db.models import Q
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import TaskSerializer
from tasks.models import Task
# Create your views here.



# class TaskList(APIView):
    
#     def validate_query_params(self):
#         done = self.request.query_params.get('d') # type: ignore
#         search = self.request.query_params.get('q') # type: ignore

#         if done is not None and done.lower() not in ['true', 'false', '1', '0']:
#             raise ValidationError({"d": "Invalid value. use true/false or 1/0 "})

#         if search is not None and len(search) > 100:
#             raise ValidationError({'q': 'Search query too long. Max 100 characters.'})



#     def filter_queryset(self, queryset):
#         self.validate_query_params()

#         done = self.request.query_params.get('d') # type: ignore
#         search = self.request.query_params.get('q') # type: ignore

#         if done is not None:
#             done_bool = done.strip().lower() in ['true', '1']
#             queryset = queryset.filter(done=done_bool)
        
#         if search:
#             search = search.strip()
#             queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))

#         return queryset


#     def get(self, request):
#         tasks = self.filter_queryset(Task.objects.all())
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class TaskDetail(APIView):

#     def initial(self, request, *args, **kwargs):
#         super().initial(request, *args, **kwargs)

#         pk = kwargs.get('pk')
#         try:
#             self.task = Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             raise NotFound(detail=f"Task with id {pk} not found")


#     def get(self, request, pk):   
#             serializer = TaskSerializer(self.task)
#             return Response(serializer.data, status=status.HTTP_200_OK)


#     def delete(self, request, pk):              
#         self.task.delete()        
#         return Response(status=status.HTTP_204_NO_CONTENT)


#     def put(self, request, pk):       
#         serializer = TaskSerializer(self.task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def patch(self, request, pk):           
#         serializer = TaskSerializer(self.task, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskList(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = Task.objects.all()

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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

