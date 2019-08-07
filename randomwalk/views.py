from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import SampleData, BlackScholes
from .serializers import SampleInputSerializer, BlackScholesSerializer

from .functions.princeton_black_scholes import callPrice

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

    def create(self, request):
        serializer = BlackScholesSerializer(data=request.data)
        if serializer.is_valid():
            d = serializer.validated_data
            # print(d)
            c = callPrice(s=d['price'], x=d['strike'], r=d['interest_rate'], sigma=d['volatility'], t=d['time_to_exp'])
            serializer.save()
            return Response({'message':'success', 'call price': c, 'params': d})
        return Response({'message':'error'})