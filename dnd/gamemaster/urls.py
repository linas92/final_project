from django.urls import path
from . import views

urlpatterns = [
    
    path("search/", views.search, name="search" ),
    path('<slug:type_slug>/<slug:slug>/', views.detail, name='monster_detail'),
    path("<slug:slug>/", views.type, name="type_detail"), 

]
