from checklist import views
from django.urls import path

app_name = 'checklist'
urlpatterns = [
    path('board/take', views.take_board),
    path('update/task', views.update_task),
    path('', views.index, name='index'),
]
