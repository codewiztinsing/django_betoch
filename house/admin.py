from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import House,Category

admin.site.unregister(Group)

#admin.site.register(House)
admin.site.register(Category)

class IsCheapFilter(admin.SimpleListFilter):
    title = 'cheap'
    parameter_name = 'cheap'


    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Cheap'),
            ('No', 'Expensive'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(price__gt=75)
        elif value == 'No':
            return queryset.exclude(price__lte=3333)
        return queryset




@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    actions=['make_cheap','make_expensive']
    list_display = ("id","title", "slug","price","owner",'category')
    list_filter = ("is_published", "price",IsCheapFilter,'category')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    def make_cheap(self,request,queryset):
        return queryset.update(price=77)

    def make_expensive(self,request,queryset):
        return queryset.update(price=768)

admin.site.site_header ="Well come to Betoch Admin"
admin.site.site_title  = "betoch admin"
admin.site.index_title = "Welcome to Betoch online rent and sell"


