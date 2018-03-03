from django.conf.urls import url
from expenses import views

urlpatterns = [
    url(r'^new$', views.new_expense, name='new_expense'),
    # url(r'^(.)/$', views.view_expense, name='view_expense'),
]
