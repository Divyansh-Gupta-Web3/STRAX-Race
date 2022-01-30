from django.contrib import admin
from django.urls import path, include
from wallet import views

urlpatterns = [
    path("",views.loginpage, name='wallet'),
    path("index/",views.index, name='wallet'),
    path("main/",views.main,name='main'),
    path("newTxn/",views.newTxn,name='newTxn'),
    path("oldTxns/",views.oldTxns,name='oldTxns'),
    path("profile/",views.profile,name='profile'),
    path("wallet/",views.wallet,name='wallet'),
    path("signup/",views.register , name="register"),
    path("login/",views.loginpage,name="login"),
    path("logoutpage/",views.logoutpage,name="logout"),
    path("address/",views.address,name="address"),
    path("qwertyuiop/",views.qwertyuiop,name="qwertyuiop")
]