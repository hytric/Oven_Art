from rest_framework.views import APIView
from django.shortcuts import render
from content.models import Feed


class Sub(APIView):
    def get(self,request):
        feed_list = Feed.objects.all()
        return render(request, 'Oven_Art/main.html', context=dict(feed_list=feed_list))

    def post(self,request):
        print("post으로 호출")
        return render(request,"Oven_Art/main.html")
