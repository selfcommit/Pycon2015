from django.contrib import admin
from django.contrib import auth
from tutorial.restaurantapi.models import Menu, MenuItem

class MenuAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'description', 'chef', 'available']
	pass

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'description', 'cost_to_make', 'sale_price', 'available', 'menu']
	pass

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)