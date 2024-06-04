from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appointment, Reexamination
from .serializers import AppointmentSerializer, ReexaminationSerializer, ReadAppointmentSerializer

class AppointmentListCreateView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = ReadAppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AppointmentListOfUserView(APIView):
    def get(self, request, patient_id):
        appointments = Appointment.objects.filter(patient_id=patient_id)
        serializer = ReadAppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentDetailView(APIView):
    def get(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = ReadAppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReexaminationListCreateView(APIView):
    def get(self, request):
        reexaminations = Reexamination.objects.all()
        serializer = ReexaminationSerializer(reexaminations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReexaminationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReexaminationDetailView(APIView):
    def get(self, request, pk):
        try:
            reexamination = Reexamination.objects.get(pk=pk)
            serializer = ReexaminationSerializer(reexamination)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reexamination.DoesNotExist:
            return Response({'error': 'Reexamination not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            reexamination = Reexamination.objects.get(pk=pk)
        except Reexamination.DoesNotExist:
            return Response({'error': 'Reexamination not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReexaminationSerializer(reexamination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            reexamination = Reexamination.objects.get(pk=pk)
        except Reexamination.DoesNotExist:
            return Response({'error': 'Reexamination not found'}, status=status.HTTP_404_NOT_FOUND)
        reexamination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
