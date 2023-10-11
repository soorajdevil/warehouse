from django.urls import path
from . import views

urlpatterns=[
    path('',views.main_index, name='main_index_Page'),
    #path('login',views.login),
    path('home',views.home, name='home'),
    path('home_manager',views.homemanager, name='home_manager'),
    path('profile_manager/', views.profile_manager, name='profile_manager'),
    #path('indexPage/',views.indexPage, name='indexPage/'),
    #path('login/',views.indexPage,name='login/'),
    path('home_supervisor',views.homesupervisor, name='home_supervisor'),
    path('login/<str:UserType>/',views.Signin_Super,name='login'),
    path('logout/',views.logout_Super,name='logout'),
    path('edit_profile/<int:supervisor_id>/', views.edit_profile, name='edit_profile'),
    
    path('homeEmploye',views.home_employee, name='homeEmploye'),
    path('profile_employe/<int:id>/', views.updatee, name='profile_employe'),


    
    path('add_employe',views.register_employee, name='add_employe'),
    path('view_employee',views.viewemployee, name='view_employee'),
    path('edit_employee/<int:id>/', views.editemployee, name='edit_employee'),
    path('delete/<int:id>/', views.deleteemployee, name='delete'),
    path('add_supervisor',views.addsupervisor, name='add'),
    path('view_supervisor',views.viewsupervisor, name='view_supervisor'),
    
    path('edit_supervisor/<int:pk>/', views.editsupervisor, name='edit_supervisor'),
    path('delete_supervisor/<int:id>/', views.deletesupervisor, name='delete'),
    
    path('add_manager',views.addmanager, name='form element'),
    path('view_manager',views.viewmanager, name='view_manager'),
    path('edit_manager/<int:id>/', views.editmanager, name='edit_manager'),
    # path('view_manager/<int:id>/', views.editmanager, name='Edit'),
    path('delete_manager/<int:id>/', views.deletemanager, name='delete'),
    path('add_building',views.addbuilding, name='add_building'),
    path('view_building',views.viewbuilding, name='view_building'),
    path('delete_building/<int:id>/', views.deletebuilding, name='delete'),
    path('edit/<int:id>/', views.editbuild, name='edit'),
    
    path('add_rack/<int:id>/',views.addrack, name='add_rack'),
    path('view_rack/<int:id>/',views.viewrack, name='view_rack'),
    path('edit_rack/<int:rack_id>/', views.editrack, name='edit_rack'),
    #path('edit_rack/<int:id>/', views.editrack, name='edit'),
    path('delete_rack/<int:rack_id>/', views.delete_rack, name='delete_rack'),
    
    path('add_job',views.addjob, name='add_job'),
    path('view_job',views.viewjob, name='view_job'),
    path('add_job/<int:id>/', views.editjob, name='add'),
    path('delete_jobs/<int:id>/', views.jobdelete, name='delete'),
    path('add_vehicle',views.addvehicle, name='add_vehicle'),
    path('view_vehicle',views.viewvehicle, name='view_vehicle'),
    path('edit_vehicle/<int:id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete_vehicle/<int:id>/', views.delete_vehicle, name='delete_vehicle'),
    
    path('add_product',views.addProduct, name='add_product'),
    path('view_product',views.viewProduct, name='view_product'),
    path('edit_product/<int:id>/', views.editProduct, name='edit_product'),
    path('delete_Product/<int:id>/', views.deleteProduct, name='delete'),
    path('table_product',views.TableProduct, name='table_product'),
    # path('s1_attendence',views.attendencePage, name='s1_attendence'),
    
    #path('attendence_add/<int:employee_id>/', views.add_attendance, name='attendence_add'),
   

    
    
    # path('attendence_add/<int:id>/',views.take_attendence, name='attendence_add'),
    # path('attendance_add/<int:employee_id>/', views.add_attendence, name='attendance_add'),
    
    # path('attendance_add/<int:id>/view_attendance/<int:employee_id>/',views.view_attendence, name='view_attendence'),
    # #path('employee_attendence/<int:id>/',views.employee_attendance, name='employee_attendence'),
    
    path('add_box',views.add_box, name='add_box'),
    path('view_box',views.view_box, name='view_box'),
    path('Delete_box/<int:box_id>/',views.delete_box, name='delete_box'),
    
   
    
    path('Building_Space/', views.BuildingSearch, name='Building_Space'),
    # path('box_transit/', views.transit_box_view, name='box_transit'),
    path('view_box_transit/', views.view_transit_box, name='view_box_transit'),
    path('update_box/', views.update_box, name='update_box'),
    path('box_transit/', views.box_transit_view, name='box_transit'),
    path('update_attendance/', views.update_attendance, name='update_attendance'),
    path('view_attendence/', views.view_attendance, name='view_attendence'),
    # path('attendance_list_view/', views.attendance_list_view, name='attendance_list_view'),

    path('employee_box_view/',views.employee_view_box, name='employee_box_view'),
    path('employee_product_view/',views.employee_view_Product, name='employee_product_view'),
    path('employee_boxtransit_view/', views.employee_view_transit_box, name='employee_boxtransit_view'),
    path('employee_vehicle_view/',views.employee_view_vehicle, name='employee_vehicle_view'),
    path('employee_building_view/',views.employee_view_building, name='employee_building_view'),
    
    
    
    # path('chatbot/', views.chatbot_view, name='chatbot'),
]

      
    


