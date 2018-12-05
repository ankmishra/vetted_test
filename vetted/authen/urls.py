from django.conf.urls import url
from authen import views
# SET THE NAMESPACE!
app_name = 'authen'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^update/$',views.update,name='update'),
    url(r'^remove/$',views.removeCompany,name='removecompany'),
    url(r'^removeemployee/$',views.removeEmployee,name='removeemployee'),
    url(r'^addadmin/$',views.addadmin,name='addadmin'),
    url(r'^addcompany/$',views.addCompany,name='addcompany'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
