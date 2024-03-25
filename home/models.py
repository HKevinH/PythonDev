from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name', unique=True)
    email = models.EmailField(verbose_name='Email Address')
    password = models.CharField(max_length=500, verbose_name='Password', default='123456')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    address = models.CharField(max_length=100, verbose_name='Street Address')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=10, verbose_name='State')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        clientFull = [self.name, self.email, self.phone, self.address, self.city, self.state, self.zip_code]
        return clientFull
    
# Model Abstract For Account

class Account(models.Model): 
    number_account = models.CharField(max_length=10, verbose_name='Account Number', unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Balance')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    class Meta:
        abstract =False 
        
    def deposit(self, value):
        self.balance += value
        self.save()
        
    def withdraw(self, value):
        self.balance -= value
        self.save()
    
    def generated_report_month(self):
        pass
    
    

#  Class Account Saving
# Inheritance from Account
class AccountSaving(Account):
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default="0.5", verbose_name='Interest Rate')
    
    def __str__(self):
        return self.number_account

#  Model Account Current
# Inheritance from Account

class AccountCurrent(Account):
    limit = models.DecimalField(max_digits=10, decimal_places=2, default="0.5", verbose_name='Limit')
    
    def __str__(self):
        return self.number_account
#  Model Transaction

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Value')
    type = models.CharField(max_length=1, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    
    def __str__(self):
        return f'{self.account} - {self.value}'
    
    def save(self, *args, **kwargs):
        if self.type == 'D':
            self.account.deposit(self.value)
        else:
            self.account.withdraw(self.value)
        super(Transaction, self).save(*args, **kwargs)
        
#  Model Report
class Reports(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Account')
    month = models.IntegerField(verbose_name='Month')
    year = models.IntegerField(verbose_name='Year')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    
    
    @staticmethod
    def generated_report_month(account, month, year):
        pass
    
    @staticmethod
    def generated_report_year(account, year):
        pass
