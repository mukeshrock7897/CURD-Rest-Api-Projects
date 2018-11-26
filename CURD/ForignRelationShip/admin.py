from django.contrib import admin

from ForignRelationShip.models import Employee,Company,Person


#Customizing the Admin panel

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name','address']
    search_fields = ['name']
    list_display = ('name','address')
    list_filter = ['name']

#Adding related objects

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 2

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company)
admin.site.register(Person)