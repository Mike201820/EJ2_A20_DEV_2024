# stringapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import StringCalculation
from .serializers import StringCalculationSerializer

@api_view(['GET'])
def get_all_calculations(request):
    calculations = StringCalculation.objects.all()
    serializer = StringCalculationSerializer(calculations, many=True)
    return Response(serializer.data)


def count_substrings(s, sub):
    count = start = 0
    while start < len(s):
        start = s.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            break
    return count

def calculate_f(s, t):
    count_s = count_substrings(t, s)
    count_reverse_s = count_substrings(t, s[::-1])
    return max(len(s) * count_s, len(s) * count_reverse_s)

@api_view(['POST'])
def max_f_value(request):
    t = request.data.get('t')
    n = len(t)
    max_value = 0

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            s = t[start:start + length]
            max_value = max(max_value, calculate_f(s, t))

    # Guardar los datos en la base de datos
    StringCalculation.objects.create(input_string=t, max_f_value=max_value)

    return JsonResponse({'max_f_value': max_value})
