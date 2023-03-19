from . import views
from django.urls import path
from django.urls import include

urlpatterns = [
    path('create', views.createpost,name="create"),
    path('', views.home,name="home"),
    path('login', views.login,name="login"),
    #path('post_d', views.post_d,name="post_d"),
    path('admin@post',views.admin_post,name="admin@post"),
    path('iqac',views.iqac,name="iqac"),
    path('logout',views.logout,name="logout"),
    #path('filter', views.filter,name="filter")
    path('delete/<str:id>/',views.delete,name="delete"),
    path('approve/<str:id>/',views.approve,name="approve"),
    path('detail/<str:id>/',views.detail,name="detail"),
    path('reqdetail/<str:id>/',views.reqdetail,name="reqdetail"),
    #path('active',views.active,name="active"),
    #ath('posactive',views.active,name="posactive"),
    path('ac/<str:id>/',views.ac,name="ac"),
]