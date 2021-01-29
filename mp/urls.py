from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
    path('board_type/new', views.boardTypeResult, name='add-board-type'),
    path('board_type/<int:board_type_id>/fault', views.board_fault, name='new_board'),
    path('board_type/<int:board_type_id>/boards/fults',views.repair_record_history,name='repair_record_history'),
    path('board_type/<int:board_type_id>/faults_counts',views.faultCount,name='faults'),
    path('board_type/<str:board_type_id>/detail',views.board_type_detail,name='board_type_history'),
    path('board_type/<str:board_type_id>/delete',views.deleteType, name='delete_board_type'),
    path('board_type/<str:board_issue>/<str:board_type>/edit_fault', views.updateTypeFault,name='edit_board_type_fault'),
    
    path('repair_record/<str:repair_record_id>/progress', views.repair_record_progress,
         name='repair_record_progress'),

    path('board', views.boardresult, name='board'),  
    path('board/<int:board_id>/update', views.update, name='update'), 
    path('board/<int:board_id>/delete', views.delete, name='delete'),
    path('search/board',views.searchBoard,name='search_board'),
    path('board/mac_search',views.searchByMac,name='search_board_by_mac'),
    path('board/<str:board_id>/detail',views.detail,name='board_history'),
    path('board/<str:serialNum>/repair_record',views.repair,name='rrepair'),
    path('board/<str:board_id>/board_type',views.getBoardTypefromSerial, name='getBoardTypefromSerial')
]
