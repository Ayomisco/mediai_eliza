from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class ForgotPasswordView(TemplateView):
    template_name = 'forgot-password.html'


class WorkflowView(TemplateView):
    template_name = 'workflow.html'


class VerifyOtpView(TemplateView):
    template_name = 'verify-otp.html'


class VoicePoweredView(TemplateView):
    template_name = 'voice-powered.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'


class OtpSuccessView(TemplateView):
    template_name = 'otp-success.html'


class MedicalConverseView(TemplateView):
    template_name = 'medical-converse.html'


class ImgDiagnosisView(TemplateView):
    template_name = 'img-diagnosis.html'
