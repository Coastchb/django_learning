# -*- coding:utf-8 -*- 
# @Time		:2019/5/11 12:27 AM
# @Author	:Coast Cao

from django.urls import path
from . import views

app_name = "polls"

'''old fashion
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:question_id>/', views.detail, name = 'detail'),
	path('<int:question_id>/results', views.results, name = 'results'),
	path('<int:question_id>/vote', views.vote, name = 'vote'),
]
'''

# new fashion
urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
	path('<int:pk>/results', views.ResultsView.as_view(), name = 'results'),
	path('<int:question_id>/vote', views.vote, name = 'vote'),
]
