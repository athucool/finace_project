from django.shortcuts import render,redirect,get_object_or_404
from .models import FinanceManager
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .forms import FinanceManagerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.http import HttpResponse
import csv
from django.utils import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test



@permission_required('Account.Finance_Manager','index')
def FinanceManagerCreate_view(request):
    
    template_name = 'Finance_Manager/finance_manager.html'
    if request.method == 'POST':
        form = FinanceManagerForm(data=request.POST)
        if form.is_valid():
            print("form-",form)
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('financeManager:success')
    else:
        form=FinanceManagerForm()

    return render(request, template_name, {'form': form})



class FinanceManagercompleted(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    template_name="Finance_Manager/succ.html"
    permission_required = 'Account.Finance_Manager'
