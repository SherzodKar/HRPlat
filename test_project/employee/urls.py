from django.urls import path, include
from . import views
from .views import (
    EmployeeProfileListView,
    GetObject,
    GetEmployeeGoal,
    NoteList, 
    NoteCreateView, 
    EmployeeDetailView, 
    NoteDetailView, 
    EmployeeProfileCreateView, 
    EmployeeProfileRetrieveView,
    EmployeeProfileUpdateView,
    EmployeeProfileDeleteView,
    EmployeeGoalsCreateView, 
    EmployeeGoalsRetrieveView,
    EmployeeGoalsUpdateView,
    EmployeeGoalsDeleteView)

urlpatterns = [
    path('', EmployeeProfileListView.as_view(), name = 'home'),
    path('<int:pk>/', GetObject.as_view(template_name='employee/object.html'), name='object'),
    path('objective/<int:pk>/', GetEmployeeGoal.as_view(template_name='employee/goals.html'), name='goals'),
    path('note/', NoteList.as_view(), name='note-form'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/create/', NoteCreateView.as_view(), name='create-view'),
    path('employee/create/', EmployeeProfileCreateView.as_view(), name='employee-create'),
    path('employee/retrieve/<int:pk>/', EmployeeProfileRetrieveView.as_view(), name='employee-detail'),
    path('employee/update/<int:pk>/', EmployeeProfileUpdateView.as_view(), name='employee-update'),
    path('employee/delete/<int:pk>/', EmployeeProfileDeleteView.as_view(), name='employee-delete'),
    path('goals/create/', EmployeeGoalsCreateView.as_view(), name='goals-create'),
    path('goals/retrieve/<int:pk>/', EmployeeGoalsRetrieveView.as_view(), name='goals-detail'),
    path('goals/update/<int:pk>/', EmployeeGoalsUpdateView.as_view(), name='goals-update'),
    path('goals/delete/<int:pk>/', EmployeeGoalsDeleteView.as_view(), name='goals-delete')
]   