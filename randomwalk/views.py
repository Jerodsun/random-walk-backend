from rest_framework import viewsets
from rest_framework.response import Response

from .models import SampleData, BlackScholes
from .serializers import SampleInputSerializer, BlackScholesSerializer

# Create your views here.

class SampleDataView(viewsets.ModelViewSet):
    """ This shows up in the title. """
    serializer_class = SampleInputSerializer
    queryset = SampleData.objects.all()
    http_method_names = ['get', 'post']

    def create(self, request):
        serializer = SampleInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip_address=self.get_client_ip(request))
            return Response({'message':'success', 'params':serializer.validated_data})
        # catch errors
        return Response({'message':'error'})
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class BlackScholesView(viewsets.ModelViewSet):
    
    serializer_class = BlackScholesSerializer
    queryset = BlackScholes.objects.all()
    http_method_names = ['get', 'post']
