from django.urls import path
from .views import (
    DoctorListCreateView, DoctorDetailView,
    PatientListCreateView, PatientDetailView,
    PatientRecordListCreateView, PatientRecordDetailView,
    DepartmentListCreateView, DepartmentDoctorListView, DepartmentPatientListView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('doctors', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>', DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
    path('patient_records', PatientRecordListCreateView.as_view(), name='patient-record-list-create'),
    path('patient_records/<int:pk>', PatientRecordDetailView.as_view(), name='patient-record-detail'),
    path('departments', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/doctors', DepartmentDoctorListView.as_view(), name='department-doctor-list'),
    path('departments/<int:pk>/patients', DepartmentPatientListView.as_view(), name='department-patient-list'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
