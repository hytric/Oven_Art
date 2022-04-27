from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed

# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id')   # 쿼리셋 select * from
        return render(request, 'Oven_Art/main.html', context=dict(feed_list=feed_list))