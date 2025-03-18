from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from ..models import  Trainee
from ..api.serializers import TraineeSerializer

#List & Create Trainee (classBased)

class TraineeList_create(APIView):
    def get(self,request):
        trainees=Trainee.objects.all()
        serializer=TraineeSerializer(trainees,many=True)
        return Response(
            {'message':'Trainee retrived successfully','data':serializer.data},
            status=status.HTTP_200_OK
        )
    def post(self,request):
        serializer=TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Trainee created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Failed to create trainee", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
# update & delete (Generic view)
class TraineeUpdate_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Trainee updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Failed to update trainee", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        instance.delete()
        return  Response(
            {"message": "Trainee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )