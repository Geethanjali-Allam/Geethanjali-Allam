from django.urls import path
from . import views 



app_name = "Management"
urlpatterns=[
    path("", views.index, name="Home"),
    path("fav/", views.view_fav, name="View_Favourite"),
    path("addfav/", views.add_fav, name="Add_Favourite"),
    path("addcompl/", views.add_complaint, name="Add_Complaint"),
    path("compl/", views.view_complaint, name="View_Complaint"),
    path('update_complaint/<int:complaint_id>/', views.update_complaint, name='Update_Complaint'),
    path('delete_complaint/<int:complaint_id>/', views.delete_complaint, name='Delete_Complaint'),
    path("search/", views.search, name="Search"),
    path("signup/", views.sign_up, name="Sign_Up"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]