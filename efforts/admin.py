from django.contrib import admin
from efforts.models import Customer,Product,Project,Employee,Team,Effort
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Effort)