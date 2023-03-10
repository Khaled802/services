from django.contrib import admin

from .models import Bank, Hotal, Restraunt

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 
        'description', 'link', 'telephone')

class HotalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 
        'description', 'review')

class RestrauntAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 
        'description', 'website')

admin.site.register(Bank, BankAdmin)
admin.site.register(Hotal, HotalAdmin)
admin.site.register(Restraunt, RestrauntAdmin)
    
