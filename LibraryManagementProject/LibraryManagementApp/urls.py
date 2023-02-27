from django.urls import path
from LibraryManagementApp import views

urlpatterns = [

    # Admin urls

    path('', views.login_fun, name='log'),
    path('register', views.reg_fun, name='register'),

    path('home', views.home_fun, name='home'),

    path('addbook', views.addbook_func, name="addbook"),
    path('displaybook', views.displaybook_func, name="displaybook"),
    path('update/<int:id>', views.update_book_fun, name='up'),
    path('delete/<int:id>', views.delete_book_fun, name='del'),

  # path('getstudent', views.get_Student_fun, name='getstudent'),
    path('assignbook', views.assignbook_fun, name='assignbook'),

    path('displayassign', views.display_assign_fun, name='displayassign'),
    path('del_issue/<int:id>', views.delete_issue_fun, name='del_issue'),
    path('updt_issue/<int:id>', views.updt_issue_fun, name='updt_issue'),

    # student page urls
    path('addstud', views.add_stud_fun, name="addstud"),
    path('studhome', views.stud_home_fun, name='studhome'),
    path('stud_books', views.stud_books_fun, name='stud_books'),
    path('getprofile', views.get_prof_fun, name='getprof'),
    path('updateprof/<int:id>', views.update_prof_fun, name='updtprof'),

    path('log_out', views.log_out_fun, name='log_out')

]