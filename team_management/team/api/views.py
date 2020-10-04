from django.shortcuts import render
from django.contrib.auth import get_user_model

from .serializers import *
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import authentication, permissions, generics
User = get_user_model()
# Create your views here.
class UserView(APIView):

    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # parser_classes = (FormParser, MultiPartParser)

    def get(self, request, format=None):
        users = User.objects.all()
        data = UserDetailSerializer(users, many=True)
        msg = {'is_success': True,
                'message': None,
                'response_data': data.data}
        return Response(msg,
                        status=status.HTTP_200_OK)

    def post(self, request, format=None):
        post_data = request.data
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.last()
            data = UserDetailSerializer(user)
            msg = {'is_success': True,
                    'message': ["Member Created Successfully!"],
                    'response_data': data.data}
            return Response(msg,
                            status=status.HTTP_200_OK)
        else:
            errors = []
            for field in serializer.errors:
                for error in serializer.errors[field]:
                    if 'non_field_errors' in field:
                        result = error
                    else:
                        result = ''.join('{} : {}'.format(field,error))
                    errors.append(result)
            msg = {'is_success': False,
                    'message': [error for error in errors],
                    'response_data': None }
            return Response(msg,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, format=None):
        id = request.data['id']
        user = User.objects.get(id=id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'is_success': True,
                    'message': ["Member details updated!"],
                    'response_data': serializer.data}
            return Response(msg,
                            status=status.HTTP_200_OK)
        else:
            errors = []
            for field in serializer.errors:
                for error in serializer.errors[field]:
                    if 'non_field_errors' in field:
                        result = error
                    else:
                        result = ''.join('{} : {}'.format(field,error))
                    errors.append(result)
            msg = {'is_success': False,
                    'message': [error for error in errors],
                    'response_data': None }
            return Response(msg,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

class UserDeleteView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        User.objects.get(id=user_id).delete()

        msg = {'is_success': True,
                'message': ["Member Deleted!"],
                'response_data': None}
        return Response(msg,
                        status=status.HTTP_200_OK)
