from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),
    path('current/',views.getCurrentUser),
    path('change/',views.changePassword),
    path('reset/',views.resetPassword),
    path('confirm/',views.userConfirm),
    path('interns/get/',views.getInterns),
    path('interns/post/',views.postInterns),
    path('ras/get/',views.getRAs),
    path('ras/post/',views.postRAs),
    path('forum/get/',views.getForum),
    path('favourite/get/',views.getFavourite),
    path('deleteFavourite/post/',views.deleteFavourite),
    path('addFavourite/post/',views.addFavourite),
    path('research/get/',views.getResearches),
    path('research/post/',views.postResearches),
    ]