from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class Sellerlist(APIView):

	def get(self, request):
		model = seller_profile.objects.all()
		serializer = SellerSerializer(model, many=True)
		return Response(serializer.data)

	def post(self, request):
		model = seller_profile.objects.all()
		serializer = SellerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAS_REQUEST)


class SellerDetail(APIView):

	def get_seller(self, seller_id):
	
		model = seller_profile.objects.get(id=seller_id)
		return model
		
	def get(self, request, seller_id):
		try:
			serializer = SellerSerializer(self.get_seller(seller_id), many=False)
			return Response(serializer.data)
		except:
			return Response(f"Seller with id = {seller_id} does not exist!", status=status.HTTP_404_NOT_FOUND)

	def put(self, request, seller_id):

		serializer = SellerSerializer(self.get_seller(seller_id), data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQEUST)

	def delete(self, request, seller_id):
		try:
			model = self.get_seller(seller_id)
			model.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
			