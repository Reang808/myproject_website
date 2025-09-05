
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'inquiry_type', 'plan', 'created_at')
	list_filter = ('inquiry_type', 'plan', 'created_at')
	search_fields = ('name', 'email', 'phone', 'message')
