from django.contrib import admin
from django.urls import include,path
from APIView_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),

    # path('studentcreate/', views.StudentCreate.as_view()),
    # path('studentretrive/<int:pk>', views.StudentRetrieve.as_view()),
    # path('studentupdate/<int:pk>', views.StudentUpdate.as_view()),
    # path('studentdestroy/<int:pk>', views.StudentDestroy.as_view()),
]
