from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Patient, Doctor, Appointment

@require_http_methods(["GET"])
def dashboard(request):
    """API endpoint for dashboard data"""
    try:
        data = {
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_appointments': Appointment.objects.count(),
            'status': 'success'
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e), 'status': 'error'}, status=500)
