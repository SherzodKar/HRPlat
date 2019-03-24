from  rest_framework import serializers
from .models import EmployeeProfile, EmployeeGoals, Note

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeProfile
        fields=('EmployeeID','First_Name','Last_Name','Nickname','Prefix','Gender','Birth_date','Job_Title','Business_Phone','Location','Hire_Date','Record_Status','worker', 'profession', 'date_posted')

class EmployeeGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeGoals
        fields=('worker', 'GoalsName', 'Metrics', 'Percent', 'Weight', 'StartDate', 'Status', 'Actual', 'Target')

class NoteSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Note
        fields=('note', 'author')    
