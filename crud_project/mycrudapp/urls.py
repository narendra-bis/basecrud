from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('show/',views.show_records, name='show'),
    path('edit/<int:pk>',views.edit_record,name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.destroy, name='delete'),
    path('signup/',views.signup, name='signup')
    
]
