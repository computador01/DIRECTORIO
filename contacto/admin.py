from django.contrib import admin
from .models import Contacto

# Register your models here.
class ContantoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Contacto, ContantoAdmin)
