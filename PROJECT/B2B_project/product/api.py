from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class Productlist(APIView):

	def get(self, request):
		model = product.objects.all()
		serializer = ProductSerializer(model, many=True)
		return Response(serializer.data)

	def post(self, request):
		model = product.objects.all()
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAS_REQUEST)
