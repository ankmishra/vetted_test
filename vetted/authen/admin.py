from django.contrib import admin
from authen.models import UserProfileInfo, User, CompanyInfo, AdminProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CompanyInfo)
admin.site.register(AdminProfileInfo)
