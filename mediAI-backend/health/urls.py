from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('forgot-password/', views.ForgotPasswordView.as_view(),
         name='forgot_password'),
    path('workflow/', views.WorkflowView.as_view(), name='workflow'),
    path('verify-otp/', views.VerifyOtpView.as_view(), name='verify_otp'),
    path('voice-powered/', views.VoicePoweredView.as_view(), name='voice_powered'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('otp-success/', views.OtpSuccessView.as_view(), name='otp_success'),
    path('medical-converse/', views.MedicalConverseView.as_view(),
         name='medical_converse'),
    path('img-diagnosis/', views.ImgDiagnosisView.as_view(), name='img_diagnosis'),
]
