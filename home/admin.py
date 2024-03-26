from django.contrib import admin
from .models import Client, Transaction
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Transaction, Client
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.

admin.site.site_header = "Administración de Mi Sitio"
admin.site.site_title = "Sitio de Admin"
admin.site.index_title = "Bienvenido al Portal de Administración"

class TransaccionInline(admin.TabularInline): 
    model = Transaction
    extra = 0  
@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    inlines = [TransaccionInline,]
# Re-registrar UserAdmin
