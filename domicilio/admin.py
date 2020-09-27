from django.contrib import admin
from .models import Cargo, Usuario, Cliente, Orden

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Orden)