from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')



class StudentAddView(View):
    def get(self, request):
        return render(request, 'student_add.html')



class StudenPrintView(View):
    def get(self, request):
        return render(request, 'print_admission_form.html')


class StudenMigrations(View):
    def get(self, request):
        return render(request, 'student_migration.html')