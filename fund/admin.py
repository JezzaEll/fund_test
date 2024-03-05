from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ExportMixin, ImportMixin

# Register your models here.
from .models import Fund

class FundAdmin(ImportExportModelAdmin):
    list_display = ('name', 'strategy', 'aum', 'inception_date')
    
    list_filter = ( ('strategy'),
    )
    
admin.site.register(Fund, FundAdmin)
