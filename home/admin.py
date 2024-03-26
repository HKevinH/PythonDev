from django.contrib import admin
from .models import Client, Transaction
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Transaction, Client
from django.db.models import Count, Q
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "Administración de Mi Sitio"
admin.site.site_title = "Sitio de Admin"
admin.site.index_title = "Bienvenido al Portal de Administración"

class TransaccionInline(admin.TabularInline): 
    model = Transaction
    extra = 0  
@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'num_transactions_for_month')
    inlines = [TransaccionInline,]
    actions = ['custom_action']
    list_filter = (
        ('transaction__created_at', admin.DateFieldListFilter),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        year = request.GET.get('transaction__created_at__year', 2024)
        month = request.GET.get('transaction__created_at__month', 3)
        if year and month:
            qs = qs.annotate(
                num_transactions_for_month=Count(
                    'transaction',
                    filter=Q(transaction__created_at__year=year, transaction__created_at__month=month)
                )
            ).order_by('-num_transactions_for_month')
        return qs
    
    
    def num_transactions_for_month(self, obj):
        return obj.num_transactions_for_month
    num_transactions_for_month.admin_order_field = 'num_transactions_for_month'
    num_transactions_for_month.short_description = _('Transacciones (Mes Específico)')

    def custom_action(self, request, queryset):
        queryset = queryset.annotate(
            num_transactions_for_month=Count(
                'transaction',
                filter=Q(transaction__created_at__year=request.GET.get('transaction__created_at__year', 2024),
                         transaction__created_at__month=request.GET.get('transaction__created_at__month', 3))
            )
        ).order_by('-num_transactions_for_month')
        
        response = ''
        for client in queryset:
            response += f'{client.name} - Transacciones: {client.num_transactions_for_month}\n'
        
        self.message_user(request, response)
    custom_action.short_description = _('Ordenar clientes por número de transacciones')
