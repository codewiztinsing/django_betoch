from django.contrib import admin
from .models import Listing

class ListAdmin(admin.ModelAdmin):
	list_display = ('id','title','published','price','realtor')
	list_display_links = ('title',)
	list_filter = ('realtor',)
	list_editable = ('published',)
	search_fields = ('title','address','city','price') 
	repopulated_fields = {'slug': ('title',)}
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Listing,ListAdmin)
