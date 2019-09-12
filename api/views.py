from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from pets.models import Pet
from api.serializers import UserSerializer, PetSerializer





@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    Login method 
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



@csrf_exempt
@permission_classes((IsAuthenticated,))
def user(request):
    """
    Retrieve, update user details by user.
    """
    try:
        user = User.objects.filter(username=request.user)
    except User.DoesNotExist:
        return Response({'error': 'User not found'},
                        status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def pets(request):
    """
    List all pets beloging  
    to the authenticated user
    """
    try:
        user = User.objects.filter(username=request.user)
    except User.DoesNotExist:
        return Response({'error': 'User not found'},
                        status=HTTP_404_NOT_FOUND)

    pets = Pet.objects.filter(owner=user).all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data, status=HTTP_200_OK)



@csrf_exempt
@permission_classes((IsAuthenticated,))
def add_pet(request):
    """
    Add a pet 
    """
    try:
        user = User.objects.filter(username=request.user)
    except User.DoesNotExist:
        return Response({'error': 'User not found'},
                        status=HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = PetSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)




@csrf_exempt
@permission_classes((AllowAny,))
def pet(request, pk):
    """
    Retrieve, update or delete a pet.
    """
    try:
        pet = pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PetSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pet.delete()
        return HttpResponse(status=204)

