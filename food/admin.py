from django.contrib import admin
from mptt.admin import MPTTModelAdmin  

from .models import *
# Register your models here.



admin.site.register(Recipe)
admin.site.register(Setting)
admin.site.register(Menu)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Coment)
admin.site.register(Cheks)
admin.site.register(CheksDetail)
admin.site.register(Bron)
admin.site.register(Stol)
