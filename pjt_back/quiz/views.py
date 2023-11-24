from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import QuizSerializer
from .models import Quiz


# Create your views here.
@api_view(['GET', 'POST'])
def quiz_list(request):
    if request.method == 'GET':
        quiz_all = get_list_or_404(Quiz)
        serializer = QuizSerializer(quiz_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)