from django.contrib import admin

# Register your models here.


from test_rbac.models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
