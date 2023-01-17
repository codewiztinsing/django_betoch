from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','phone','top_seller','email')
	list_display_links = ('name','email',)
	list_filter = ('name','top_seller')
	# list_editable = ('email',)
	search_fields = ('name','phone','email',) 
	#prepopulated_fields = {'slug': ('title',)}


admin.site.register(Realtor,RealtorAdmin)
