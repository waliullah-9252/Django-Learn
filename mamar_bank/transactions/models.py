from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name="transactions", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null= True, blank=True)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approved = models.BooleanField(default=False, null = True, blank=True)
    

    class Meta:
        ordering = ['-timestamp']


    

