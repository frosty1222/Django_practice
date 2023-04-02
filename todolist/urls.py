from django.urls import path

from . import views
app_name = 'todolist'
urlpatterns = [
# ex: /polls/
    path('', views.index, name='index'),
    path('<int:id>/', views.update, name='update'),
    path('<int:id>/update',views.updateStatus, name= 'updateStatus'),
    path('<int:id>/delete',views.delete, name= 'delete'),
    path('add',views.addTask, name= 'addTask'),
    path('search_results',views.searchResult,name="search_results")
]