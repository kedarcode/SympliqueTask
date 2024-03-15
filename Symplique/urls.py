from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('activate/<str:uid>/<str:token>', views.AccountStuff.as_view(),name='activate'),
        path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('setreminder/', views.ReminderView.as_view(), name='setreminder'),

]
