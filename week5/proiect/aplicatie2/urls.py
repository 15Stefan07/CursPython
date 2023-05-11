from django.urls import path

from aplicatie2 import views

app_name = 'companies'

urlpatterns = [
    path('', views.CompanyView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanyView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateCompanyView.as_view(), name='modifica'),
    path('<int:pk>/sterge/', views.delete_company, name='sterge'),
    path('<int:pk>/dezactiveaza', views.deactivate_company, name='dezactiveaza'),
    path('<int:pk>/activeaza/', views.activate_company, name='activeaza'),
]
