# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:pk>/contact/', views.contact_agent, name='contact_agent'),
    path('contact/<int:pk>/', views.contact_agent, name='contact'),
    path('post_property/', views.post_property, name='post_property'),
    path("delete_property/<int:pk>/", views.delete_property, name="delete_property"),
    path('interested_users/<int:property_id>/', views.interested_users, name='interested_users'),
]
