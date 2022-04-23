from rest_framework.views import APIView
from django.shortcuts import render


class Sub(APIView):
    def get(self,request):
        print("get으로 호출")
        return render(request,"Oven_Art/main.html")

    def post(self,request):
        print("post으로 호출")
        return render(request,"Oven_Art/main.html")
