from django.urls import path
from .views import QDetailView, QListView, QCreateView, QUpdateView, QDeleteView

urlpatterns = [
    path('question/list/', QListView.as_view(), name='question_list'),
    path('question/<int:pk>/', QDetailView.as_view() , name ='question_detail'),
    path('question/new/', QCreateView.as_view(), name='question_new'),
    path('question/<int:pk>/edit/', QUpdateView.as_view(), name='question_edit'),
    path('question/<int:pk>/delete/', QDeleteView.as_view(), name='question_delete')
]