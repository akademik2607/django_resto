import json


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from config.settings import ROLES
from users.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def auth(request):
    if request.method == 'POST':
        print(request.data)
        data = request.data
        user = User.objects.filter(email=data['email']).first()


        print(user.check_password(data['password']))
        for role in ROLES:
            print(role)

        result = {
            'username': user.first_name,
            'email': user.email,
            'roles': [role for role in ROLES if role[0] in user.role]
        }

        print(result)
        return Response({"message": "success", "data": result})
    return Response({"message": "Hello, world!"})


