from django.urls import path
from .views import DepositeMoneyView, WithdrawalMoneyView, LoanRequestView, TransctionReportView, PayLoanView, LoanListView,TransferBalanceView

urlpatterns = [
    path('deposit/', DepositeMoneyView.as_view(), name = 'deposit_money'),
    path('withdraw/', WithdrawalMoneyView.as_view(), name = 'withdraw_money'),
    path('loan_request/', LoanRequestView.as_view(), name = 'loan_request'),
    path('report/', TransctionReportView.as_view(), name = 'transction_report'),
    path('loans/<int:loan_id>/', PayLoanView.as_view(), name = 'pay'),
    path('loans/', LoanListView.as_view(), name = 'loan_list'),
    path('transfer/', TransferBalanceView.as_view(), name = 'transfer_balance'),
]