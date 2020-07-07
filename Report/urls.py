from django.urls import path
from . import views

app_name="report"
 
urlpatterns = [
    path('report/create',views.Report_Create_view,name='report_create'),
    path('success/',views.Finance_report_completed.as_view(),name="finance-report") , 
    path('listof report/',views.Finance_Report_list.as_view(),name="list"),
    path('update/<int:pk>',views.FinanceReportUpdateView.as_view(),name="update"),
    path('<int:pk>',views.FinanceReportDetailsView.as_view(),name="details"),
    path('download/<int:pk>',views.DownloadFinanceReport,name="download")


]



