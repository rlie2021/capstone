from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.
# CarModelAdmin class
#class CarModelAdmin(admin.ModelAdmin):
##    model = CarModel
    #sortable_field_name = "name"
#    extra = 5
# CarMakeAdmin class with CarModelInline
#class CarMakeAdmin(admin.ModelAdmin):
#    model = CarMake
#    #sortable_field_name = "name"
#    extra = 5
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    #sortable_field_name = "name"
    extra = 5
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
#admin.site.register(CarModelAdmin)

#admin.site.register(CarMakeAdmin)
#admin.site.register(CarModelInline)