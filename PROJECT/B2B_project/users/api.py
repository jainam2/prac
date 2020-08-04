from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class Userlist(APIView):

	def get(self, request):
		model = Users.objects.all()
		serializer = UsersSerializer(model, many=True)
		return Response(serializer.data)

	def post(self, request):
		model = Users.objects.all()
		serializer = UsersSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAS_REQUEST)

class UserDetail(APIView):

	def get_user(self, user_id):
	
		model = Users.objects.get(id=user_id)
		return model
		
	def get(self, request, user_id):
		try:
			serializer = UsersSerializer(self.get_user(user_id), many=False)
			return Response(serializer.data)
		except:
			return Response(f"User with id = {user_id} does not exist!", status=status.HTTP_404_NOT_FOUND)

	def put(self, request, user_id):

		serializer = UsersSerializer(self.get_user(user_id), data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQEUST)

	def delete(self, request, user_id):
		try:
			model = self.get_user(user_id)
			model.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)
