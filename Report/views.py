from django.shortcuts import render,redirect,get_object_or_404
from .models import Finance_Report
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import Finance_TotalForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.http import HttpResponse
import csv
from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

 

class Finance_report_completed(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    template_name="Report/succ.html"
    permission_required = 'Account.Analyst'


 
@permission_required('Account.Analyst','index')
def Report_Create_view(request):
    
    template_name = 'Report/finance_report_form.html'
    if request.method == 'POST':
        form = Finance_TotalForm(data=request.POST)
        if form.is_valid():
            print("form-",form)
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('report:finance-report')
    else:
        form=Finance_TotalForm()

    return render(request, template_name, {'form': form})


class Finance_Report_list(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Finance_Report
    permission_required = 'Account.Analyst'

    
class FinanceReportDetailsView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=Finance_Report
    template_name='Report/finance_details.html'
    context_object_name='finance'
    permission_required = 'Account.Analyst'

class FinanceReportUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Finance_Report
    fields=('salary','investment','total',"payment")
    permission_required = 'Account.Analyst'

@login_required
@permission_required('Account.Analyst','index')
def DownloadFinanceReport(request,pk):
    print("pk",pk)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filename.csv"'
    writer = csv.writer(response)
    writer.writerow(['user','salary','investment','total'])
    print("request-kwarg",pk)
    data =Finance_Report.objects.filter(pk=pk)
     
    for row in data:
        rowobj = [row.user,row.salary,row.investment,row.total]
        writer.writerow(rowobj)
    return response 