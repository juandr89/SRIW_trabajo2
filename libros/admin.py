from django.contrib import admin
from .models import Libro, Calificacion, Score


# Filters
class UrlListFilter(admin.SimpleListFilter):
    title = 'Url'
    parameter_name = 'has_url'
    default_value = None

    def lookups(self, request, model_admin):
        return(
            ('yes', 'Si'),
            ('no', 'No')
        )
    
    def queryset(self, request, queryset):
       if self.value() == 'yes':
            return queryset.filter(url__isnull=False)
       if self.value() == 'no':
            return queryset.filter(url__isnull=True)

class PriceListFilter(admin.SimpleListFilter):
    title = 'Precio'
    parameter_name = 'range_price'
    default_value = None

    def lookups(self, request,  model_admin):
        return(
            ('op1', 'Menor a 20000'),
            ('op2', '[20000 - 40000)'),
            ('op3', '[40000 - 60000)'),
            ('op4', '[60000 - 80000)'),
            ('op5', '[80000 - 100000)'),
            ('op6', 'Mayor a 100000')
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'op1':
            return queryset.filter(precio__lt=20000)
        elif self.value() == 'op2':
            return queryset.filter(precio__gte=20000, precio__lt=40000)
        elif self.value() == 'op3':
            return queryset.filter(precio__gte=40000, precio__lt=60000)
        elif self.value() == 'op4':
            return queryset.filter(precio__gte=60000, precio__lt=80000)
        elif self.value() == 'op5':
            return queryset.filter(precio__gte=80000, precio__lt=100000)
        elif self.value() == 'op6':
            return queryset.filter(precio__gt=100000)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'precio')
    list_filter = [UrlListFilter, PriceListFilter]
    search_fields = ('nombre', 'autor')


# Register your models here.
# admin.site.register(Libro, LibroAdmin)
admin.site.register(Calificacion)
admin.site.register(Score)