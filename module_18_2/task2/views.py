from django.shortcuts import render
from django.views.generic import TemplateView



def func_ht(request):
    return render(request, 'temp2.html')


class temp_ht(TemplateView):
    template_name = 'temp1.html'

