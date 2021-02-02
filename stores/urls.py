from django.urls import path
from . import views

urlpatterns=[path('',views.PizzeriaListAPIView.as_view(),
name='pizzeria_list'),
path('<int:id>/',views.PizzaDetailViewById.as_view(),
name='pizzeria_detail_List'),
path('create/',views.CreatePizzaView.as_view(),
name='pizzeria_create_List'),
path('update/<int:id>/',views.UpadatePizza.as_view(),
name='pizzeria_update_List'),
path('delete/<int:id>/',views.DeletePizza.as_view(),
name='pizzeria_delete_List'),

]