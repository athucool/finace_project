from django.urls import path
from . import views

app_name="financeManager"
 
urlpatterns = [
    path('approve_payment/',views.FinanceManagerCreate_view,name='create'),
    path('success/',views.FinanceManagercompleted.as_view(),name="success"), 

]



