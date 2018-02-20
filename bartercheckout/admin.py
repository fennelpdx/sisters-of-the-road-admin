from django.contrib import admin

# Register your models here.
from .models import BarterEvent
from .models import BarterAccount


class BarterEventAdmin(admin.ModelAdmin):
	"""
	This is where you modify the view of a BarterEvent in the admin page.
	"""
	
class BarterAccountAdmin(admin.ModelAdmin):
	"""
	This is where you modify the view of a BarterAccount in the admin page.
	"""
	list_display = ['customer_name', 'account_balance']
	fields = ['customer_name','balance','last_add','last_subtract']
	readonly_fields = ['last_add','last_subtract']
	
admin.site.site_header = 'Sisters of the Road Cafe Admin'
admin.site.index_title = 'Sisters of the Road Checkout Administration'
admin.site.register(BarterAccount, BarterAccountAdmin)
admin.site.register(BarterEvent)