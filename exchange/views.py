import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExchangeRateSerializer
@api_view(['GET'])
def exchange_rate_api(request):
    import datetime
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    
    # 환율 정보를 가져오는 로직
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=jhcLohJgtsaKbnryhPOsT6HnUeBuJI5E&searchdate={current_date}&data=AP01"
    response = requests.get(url)
    exchange_rates = response.json()
    
    # Serializer를 사용하여 데이터 직렬화
    serializer = ExchangeRateSerializer(exchange_rates, many=True)
    
    return Response(serializer.data)
