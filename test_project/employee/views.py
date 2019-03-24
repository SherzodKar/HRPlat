from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import EmployeeProfile, EmployeeGoals, Note
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .serializers import EmployeeProfileSerializer, EmployeeGoalsSerializer, NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView


class EmployeeProfileListView(ListView):
    models = [EmployeeProfile, EmployeeGoals]
    template_name = 'employee/home.html'
    #context_object_name = 'employee_info'
    queryset = EmployeeProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_info'] = EmployeeProfile.objects.all()
        context['employee_goals'] = EmployeeGoals.objects.all()
        return context

class EmployeeDetailView(DetailView):
    models = [EmployeeProfile, Note]
    template_name = 'employee/object.html'
    queryset = EmployeeProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_obj'] = EmployeeProfile.objects.filter(worker=self.request.user).first()
        context['note_obj'] = Note.objects.filter(author=self.request.user).first()
        return context

class EmployeeGoalsListView(ListView):
    model = EmployeeGoals
    context_object_name = 'employee_dreams'

class GetEmployeeGoal(DetailView):
    model = EmployeeGoals
    context_object_name = 'employee_goal'
    
class GetObject(DetailView):
    model = EmployeeProfile
    context_object_name = 'employee_obj'
    
    
class NoteList(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(ListAPIView):
    queryset = Note.objects.all()
    context_object_name = 'note_obj'
    serializer_class = NoteSerializer  

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)  

class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class EmployeeProfileCreateView(CreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

class EmployeeProfileRetrieveView(RetrieveAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer    
    
class EmployeeProfileUpdateView(UpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

class EmployeeProfileDeleteView(DestroyAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer    

class EmployeeGoalsCreateView(CreateAPIView):
    queryset = EmployeeGoals.objects.all()
    serializer_class = EmployeeGoalsSerializer

    def get_queryset(self):
        user = self.request.user
        return EmployeeGoals.objects.filter(worker=user) 

class EmployeeGoalsRetrieveView(RetrieveAPIView):
    queryset = EmployeeGoals.objects.all()
    serializer_class = EmployeeGoalsSerializer   

    def get_queryset(self):
        user = self.request.user
        return EmployeeGoals.objects.filter(worker=user)  
    
class EmployeeGoalsUpdateView(UpdateAPIView):
    queryset = EmployeeGoals.objects.all()
    serializer_class = EmployeeGoalsSerializer

    def get_queryset(self):
        user = self.request.user
        return EmployeeGoals.objects.filter(worker=user) 

class EmployeeGoalsDeleteView(DestroyAPIView):
    queryset = EmployeeGoals.objects.all()
    serializer_class = EmployeeGoalsSerializer    

    def get_queryset(self):
        user = self.request.user
        return EmployeeGoals.objects.filter(worker=user)     