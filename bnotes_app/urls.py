from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.note_new, name='note_new'),
    path('add', views.note_add, name='note_add'),
    path('<int:note_id>/edit', views.note_edit, name='note_edit'),
    path('save', views.note_save, name='note_save'),
    path('<int:note_id>/delete', views.note_delete, name='note_delete')
]