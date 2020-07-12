from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name = "index"),
    path("signup/", views.Signup.as_view(), name = "signup"),
    path("logout/", views.Logout.as_view(), name = "logout"),
    path("init_mypage/", views.init_mypage, name = "init_mypage"),
    path("mypage/", views.mypage, name = "mypage"),
    path("comment/<str:name>/", views.comment_list, name = "comment_list"),
    path("add_fav_clas/<str:facul>/<str:clas>/<int:sign>/", views.add_fav_class, name = "add_fav_class"),
    path("comment/like/<str:facul>/<int:pk>/<int:sign>/", views.add_like, name = "add_like"),
]