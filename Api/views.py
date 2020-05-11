from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime


# Create your views here.

class BodyView(APIView):
	#returns request body and request time

	def post(self,request):
		content = {'Body-content': request.body,
					'request-time':datetime.datetime.now()
		}
		return Response(content) 


