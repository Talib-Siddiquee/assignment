from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientRecord, Department
from .serializers import PatientSerializer, DoctorSerializer, PatientRecordSerializer, DepartmentSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        if request.user != doctor.user:
            return Response(status=403)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        if request.user != doctor.user:
            return Response(status=403)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        if request.user != doctor.user:
            return Response(status=403)
        doctor.delete()
        return Response(status=204)

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        if request.user != patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        if request.user != patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        if request.user != patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        patient.delete()
        return Response(status=204)

class PatientRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Doctors').exists():
            doctor = Doctor.objects.get(user=user)
            return PatientRecord.objects.filter(department=doctor.department)
        return PatientRecord.objects.none()

class PatientRecordDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        record = get_object_or_404(PatientRecord, pk=pk)
        if request.user != record.patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        serializer = PatientRecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk):
        record = get_object_or_404(PatientRecord, pk=pk)
        if request.user != record.patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        serializer = PatientRecordSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        record = get_object_or_404(PatientRecord, pk=pk)
        if request.user != record.patient.user and not request.user.groups.filter(name='Doctors').exists():
            return Response(status=403)
        record.delete()
        return Response(status=204)

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDoctorListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        doctors = Doctor.objects.filter(department=department)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class DepartmentPatientListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        department = get_object_or_404(Department, pk=pk)
        patients = Patient.objects.filter(department=department)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
