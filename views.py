from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from . forms import employee, Attendence
from . models import User
from . forms1 import supervisor,LoginForm
from . forms2 import Build
from . forms3 import Stock
from . forms4 import JobScheduling
from . forms6 import Ww
from . forms7 import Prod
from . forms8 import TakeAttendence
from . forms9 import BoxForm,BuildingSearchForm,BoxTransit
from . models1 import Supervise,Signin_Supervisor,Signin_Admin
from . models2 import Manager
from . models3 import Building, Racks

from . models5 import Job
from . models6 import Veh
from . models7 import Products
from . models8 import AttendenceForm
from . models9 import Box

from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models import Count
from django.urls import path
from . import views


# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def main_index(request):
    template = loader.get_template('main_index_Page.html')
    return HttpResponse(template.render())


def Signin_Super(request, UserType):
    if UserType == 'Supervisor':
        user_model = Supervise
        home_page = 'home_supervisor'
    elif UserType == 'Employee':
        user_model = User
        home_page = 'homeEmploye'
    elif UserType == 'Manager':
        user_model = Manager
        home_page = 'home_manager'
        
    elif UserType == 'Signin_Admin':
        user_model = Signin_Admin
        home_page = 'home'
    else:
        # Handle unknown UserType here (optional)
        return render(request, 'login.html', {'message': 'Unknown UserType'})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # print(email)
            users= user_model.objects.filter(email=email, password=password)
            # user= Signin_Admin.objects.filter(email=email, password=password)
            if users.exists():
                user = users.first()
                request.session['user_id'] = user.pk  # Use user.pk instead of user.id
                return redirect(home_page)
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'formz': form})



def logout_Super(request):
    logout(request)
    return redirect('main_index_Page')  # Replace 'Supervisor' with the desired default UserType

def homesupervisor(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    try:
        user = Supervise.objects.get(pk=user_id) 
        return render(request, 'home_supervisor.html', {'ser': user})# Use pk instead of id
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

    

def edit_profile(request, supervisor_id):  # Use 'id' instead of 'pk'
    user_id = request.session.get('user_id')
    
    if user_id is None:
        return redirect('login') 
    
    if request.method == 'POST':
        mydata = Supervise.objects.get(supervisor_id=supervisor_id)
        fm = supervisor(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata = Supervise.objects.get(supervisor_id=supervisor_id)
        fm = supervisor(instance=mydata)
        
    return render(request, 'edit_profile.html', {'ser': fm})




def homemanager(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    try:
        user = Manager.objects.get(pk=user_id)  # Use pk instead of id
        return render(request, 'home_manager.html', {'ser': user})
    except Manager.DoesNotExist:
        return redirect('main_index_Page')

    


def profile_manager(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    try:
        user = Manager.objects.get(pk=user_id)
    except Manager.DoesNotExist:
        return redirect('login')
    
    if request.method == 'POST':
        user.Name = request.POST.get('Name')
        #user.Email = request.POST.get('email')
        user.Gender = request.POST.get('Gender')
        #user.Date_of_Birth = request.POST.get('DateofBirth')
        user.Mobile = request.POST.get('Mobile')
        user.password = request.POST.get('password')
        # Update other profile fields similarly
        
        user.save()
        return redirect('home_manager')  # Redirect to profile page or wherever needed
    
    return render(request, 'profile_manager.html', {'user': user})


#def indexPage(request):
    #template = loader.get_template('indexPage.html')
    #return HttpResponse(template.render())

    
def home_employee(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    try:
        user = User.objects.get(employee_id=user_id)  # Use pk instead of id
        print("jokj",user.employee_id)
        return render(request, 'homeEmploye.html', {'ser': user})
    except User.DoesNotExist:
        return redirect('main_index_Page')

    

#  @login_required
def updatee(request, id):
    user_id = request.session.get('user_id')
    
    if user_id is None:
        return redirect('login') 
    
    

    if request.method == 'POST':
        mydata = User.objects.get(employee_id=id)
        form = employee(request.POST, instance=mydata)
        if form.is_valid():
            form.save()
    else:
        mydata = User.objects.get(employee_id=id)
        form = employee(instance=mydata)
        
    return render(request, 'profile_employe.html', {'form': form}) 




#def login(request):
   # template = loader.get_template('login.html')
   # return HttpResponse(template.render())

def register_employee(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            form = employee(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_employe')  # Corrected the URL name
        else:
            form = employee()

        stu = User.objects.all().values()  # You can adjust this query as needed
        return render(request, 'add_employe.html', {'formm': form, 'stu': stu})
    except User.DoesNotExist:
        return redirect('main_index_Page')
    

def viewemployee(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        stu=User.objects.all().values()
        return render(request,'view_employee.html',{'stu':stu})
    except User.DoesNotExist:
        return redirect('main_index_Page')

def editemployee(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')

    try:
        if request.method == 'POST':
            mydata = User.objects.get(pk=id)
            fm = employee(request.POST, instance=mydata)
            if fm.is_valid():
                fm.save()
        else:
            mydata = User.objects.get(pk=id)
            fm = employee(instance=mydata)

        return render(request, 'edit_employee.html', {'form': fm})
    except User.DoesNotExist:
        return redirect('main_index_Page')

def deleteemployee(request,id):
    obj1=User.objects.get(pk=id)
    obj1.delete()
    return HttpResponseRedirect(reverse('view_employee'))

def addsupervisor(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    try:
        if request.method == 'POST':
            form = supervisor(request.POST)
            
            if form.is_valid():
                form.save()
            # Redirect back to the same page
                return HttpResponseRedirect(request.path)
        else:
            form = supervisor()
    
        supervisors = Supervise.objects.all().values()
        return render(request, 'add_supervisor.html', {'formm': form, 'stu': supervisors})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def viewsupervisor(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    try:
        stu=Supervise.objects.all().values()
        return render(request,'view_supervisor.html',{'stu':stu})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def deletesupervisor(request,id):
    obj2=Supervise.objects.get(pk=id)
    obj2.delete()
    return redirect('view_supervisor')


def editsupervisor(request, pk):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            mydata = get_object_or_404(Supervise, pk=pk)
            fm = supervisor(request.POST, instance=mydata)
            
            if fm.is_valid():
                fm.save()
        else:
            mydata = get_object_or_404(Supervise, pk=pk)
            fm = supervisor(instance=mydata)
        
        return render(request, 'edit_supervisor.html', {'form': fm})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def addmanager(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('home')

    try:
        if request.method == "POST":
            Name = request.POST["Name"]
            Email = request.POST["email"]
            Gender = request.POST["Gender"]
            Date_of_Birth = request.POST["DateofBirth"]
            Mobile = request.POST["Mobile"]
            password = request.POST["password"]
            RePassword = request.POST["ConfirmPassword"]

            obj1 = Manager()
            obj1.Name = Name
            obj1.email = Email
            obj1.Gender = Gender
            obj1.Date_of_Birth = Date_of_Birth
            obj1.Mobile = Mobile
            obj1.password = password
            obj1.RePassword = RePassword
            obj1.save()

        return render(request, 'add_manager.html')

    except Manager.DoesNotExist:
        return redirect('home')



def viewmanager(request):
    stu=Manager.objects.all().values()
    return render(request,'view_manager.html',{'stu':stu})

def editmanager(request, id):
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return HttpResponseRedirect(reverse('view_manager'))  # Redirect to a manager list view or another appropriate URL
    
    if request.method == "POST":
        manager.Name = request.POST.get("Name")
        manager.email = request.POST.get("email")
        manager.Gender = request.POST.get("Gender")
        manager.Date_of_Birth = request.POST.get("DateofBirth")
        manager.Mobile = request.POST.get("Mobile")
        manager.password = request.POST.get("password")  # Note the capital 'P'
        # manager.RePassword = request.POST.get("RePassword")
        manager.save()
        
    return render(request, 'edit_manager.html', {'manager': manager})

def deletemanager(request,id):
    obj1=Manager.objects.get(id=id)
    obj1.delete()
    return HttpResponseRedirect(reverse('view_manager'))




def addbuilding(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            form = Build(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = Build()
        
        buildings = Building.objects.all().values()
        
        return render(request, 'add_building.html', {'formm': form, 'stu': buildings})
    
    except Manager.DoesNotExist:
        return redirect('main_index_Page')
    

def viewbuilding(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        buildings = Building.objects.all()

        for building in buildings:
            total_racks = building.Total_No_Racks

            if total_racks is not None:
                # racks_data = Racks.objects.filter(foreign_key_field=building)
                racks_data = Racks.objects.filter(foreign_key_fied=building)

                total_racks_stored = racks_data.count()
                available_racks = total_racks - total_racks_stored
            else:
                total_racks_stored = 0
                available_racks = 0
            
            building.total_racks_stored = total_racks_stored
            building.available_racks = available_racks

        return render(request, 'view_building.html', {'buildings': buildings})
    except Building.DoesNotExist:
        return redirect('main_index_Page')


def editbuild(request, id):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            mydata = Building.objects.get(id=id)
            fm = Build(request.POST, instance=mydata)
            if fm.is_valid():
                fm.save()
        else:
            mydata = Building.objects.get(id=id)
            fm = Build(instance=mydata)
        return render(request, 'edit_building.html', {'form': fm})
    except Building.DoesNotExist:
        return redirect('main_index_Page')



def deletebuilding(request,id):
    obj1=Building.objects.get(id=id)
    obj1.delete()
    return HttpResponseRedirect(reverse('view_building'))



def addrack(request,id):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method=='POST':
            mydata=Building.objects.get(id=id)
            tem1 = Stock(request.POST)
            if tem1.is_valid():
                tem2 = tem1.save(commit=False)
                tem2.foreign_key_fied_id= mydata.id
                tem2.save()
                return redirect('add_rack', id=id)
        else:
            mydata=Building.objects.get(id=id)
            tem2=Stock()
        stu=Racks.objects.all().values()  
        return render(request,'add_rack.html',{'formm':tem2,'stu':stu})
    except Manager.DoesNotExist:
        return redirect('main_index_Page')


def viewrack(request, id):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        stu = Racks.objects.all().values()
        return render(request, 'view_rack.html', {'stu': stu})
    except Manager.DoesNotExist:
        return redirect('main_index_Page')

def editrack(request, rack_id):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            myrack = Racks.objects.get(id=rack_id)
            form = Stock(request.POST, instance=myrack)
            if form.is_valid():
                form.save()
                return redirect('view_rack', id=myrack.foreign_key_fied.id)  # Correct field name
        else:
            myrack = Racks.objects.get(id=rack_id)
            form = Stock(instance=myrack)
    
        return render(request, 'edit_rack.html', {'form': form})
    except Racks.DoesNotExist:
        return redirect('main_index_Page')


def delete_rack(request, rack_id):
    obj1 = Racks.objects.get(id=rack_id)
    obj1.delete()
    return HttpResponseRedirect(reverse('view_rack', args=(obj1.foreign_key_fied.id,)))

def addjob(request):
    if request.method=='POST':
        tem1 = JobScheduling(request.POST)
        if tem1.is_valid():
            tem1.save()
    else:
        tem1=JobScheduling()
    stu=Job.objects.all().values()
    return render(request,'add_job.html',{'formm':tem1,'stu':stu})



def viewjob(request):
    stu=Job.objects.all().values()
    return render(request,'view_job.html',{'stu':stu})

def editjob(request,id):
    if request.method=='POST':
        mydata=Job.objects.get(id=id)
        fm=JobScheduling(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata=Job.objects.get(id=id)
        fm=JobScheduling(instance=mydata)
    return render(request,'edit_rack.html',{'form':fm})

def jobdelete(request,id):
    fm=Job.objects.get(id=id)
    fm.delete()
    return HttpResponseRedirect(reverse('view_job'))


def addvehicle(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            tem1 = Ww(request.POST)
            if tem1.is_valid():
                tem1.save()
                # Redirect to the same page after successful submission
                return HttpResponseRedirect(reverse('add_vehicle'))
        else:
            tem1 = Ww()
        
        stu = Veh.objects.all().values()
        
        return render(request, 'add_vehicle.html', {'formm': tem1, 'stu': stu})
    except Manager.DoesNotExist:
        return redirect('main_index_Page')


def viewvehicle(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        stu=Veh.objects.all().values()
        return render(request,'view_vehicle.html',{'stu':stu})
    except Manager.DoesNotExist:
        return redirect('main_index_Page')
    
    
def edit_vehicle(request,id):
    if request.method=='POST':
        mydata=Veh.objects.get(id=id)
        fm=Ww(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
    else:
        mydata=Veh.objects.get(id=id)
        fm=Ww(instance=mydata)
    return render(request,'edit_vehicle.html',{'form':fm})

def delete_vehicle(request,id):
    fm=Veh.objects.get(id=id)
    fm.delete()
    return HttpResponseRedirect(reverse('view_vehicle'))

   


def addProduct(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            tem1 = Prod(request.POST)
            if tem1.is_valid():
                tem1.save()
        else:
            tem1 = Prod()
        
        stu = Products.objects.all().values()
        
        return render(request, 'add_product.html', {'formm': tem1, 'stu': stu})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def viewProduct(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        stu=Products.objects.all().values()
        return render(request,'view_product.html',{'stu':stu})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def editProduct(request, id):
    if request.method == 'POST':
        mydata = Products.objects.get(id=id)
        fm = Prod(request.POST, instance=mydata)
        if fm.is_valid():
            fm.save()
            # Redirect back to the same page
            return HttpResponseRedirect(reverse('edit_product', args=[id]))
    else:
        mydata = Products.objects.get(id=id)
        fm = Prod(instance=mydata)

    return render(request, 'edit_product.html', {'form': fm})

def deleteProduct(request,id):
    fm=Products.objects.get(id=id)
    fm.delete()
    return HttpResponseRedirect(reverse('view_product'))

def TableProduct(request):
    stu=Products.objects.all().values()
    return render(request,'table_product.html',{'stu':stu})

def attendencePage(request):
    employees=User.objects.all().values()
    return render(request,'update_attendance.html',{'stu':stu})


# def add_attendance(request, employee_id):
#     # Fetch the user based on the provided employee_id
#     try:
#         # Fetch the user based on the provided employee_id
#         stu = User.objects.get(pk=employee_id)  # Assuming 'User' is the model for employee data
#
#         if request.method == 'POST':
#             form = TakeAttendance(request.POST)  # Use the attendance form
#             print("form",form)
#             if form.is_valid():
#                 attendance_instance = form.save(commit=False)
#                 attendance_instance.current_date = date.today()
#                 attendance_instance.employee = stu
#                 attendance_instance.save()
#                 # Add success message if needed
#                 # messages.success(request, 'Attendance recorded successfully.')
#                 return redirect('s1_attendance', employee_id=employee_id)
#             # Add error message if needed
#             # else:
#             #     messages.error(request, 'Attendance could not be recorded. Please check the form data.')
#
#         else:
#             form = TakeAttendance()
#
#         return render(request, 's1_attendance.html', {'form': form, 'stu': stu})
#
#     except User.DoesNotExist:
#         # Handle the case where the employee does not exist
#         # You can customize this error handling as needed
#         return render(request, 'update_attendance.html')


def update_attendance(request):
    
    stu = User.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        attendance_status = request.POST.get('attendance_status')

        # Check if both fields are provided
        if employee_id and attendance_status:
            user = User.objects.get(pk=employee_id)
            # Create a new AttendenceForm object and save it to the database
            attendence_form = AttendenceForm(
                employee=user,
                attendance_status=attendance_status
                
            )
            attendence_form.save()

            # Redirect to a success page or wherever you want
            return redirect('update_attendance')

    return render(request, 'update_attendance.html', {'employees': User.objects.all()})


# def view_attendance(request):
#     employees=User.objects.all()
#     try:
#         # Retrieve the employee based on the provided employee_id
#         stu = User.objects.filter(employee_id=employee_id).values()
#         print("stu",stu)
#         atten = AttendenceForm.objects.values().all()
#         # print(atten)
#         # Retrieve attendance records for the specified employee
#         attendances = AttendenceForm.objects.filter(employee_id=employee_id).values()
#         print("Employ",attendances)
#         context = {
#             'stu': stu,
#             'attendances': attendances,
#         }
#
#
#         return render(request, 'view_attendence.html', context)
#     except User.DoesNotExist:
#         # Handle the case where the employee does not exist
#         # You can customize this error handling as needed
#         return render(request, 'view_attendence.html')


#fix the code of attendence Maintenance

# def attendance_list_view(request):
#     if request.method == 'POST':
#         employee_id = request.POST.get('id')
#         print("Employee id: ", employee_id)
#         # Check if both fields are provided
#         if employee_id:
#             stu = User.objects.filter(employee_id=employee_id).values()
#             print("stu", stu)

#             # Retrieve attendance records for the specified employee
#             attendances = AttendenceForm.objects.filter(employee_id=employee_id).values()
#             print("Employ", attendances)
            
#             # Calculate total attendance days, absent days, and working days for the specified employee
#             total_attendance_days = AttendenceForm.objects.filter(employee_id=employee_id, attendance_status='Present').count()
#             total_absent_days = AttendenceForm.objects.filter(employee_id=employee_id, attendance_status='Absent').count()
#             total_working_days = total_attendance_days + total_absent_days

#             # Retrieve details for all employees
#             all_employees = User.objects.all().values()
            
#             context = {
#                 'stu': stu,
#                 'attendances': attendances,
#                 'total_attendance_days': total_attendance_days,
#                 'total_absent_days': total_absent_days,
#                 'total_working_days': total_working_days,
#                 'all_employees': all_employees,  # Include details for all employees
#             }

#             return render(request, 'attendance_list_view.html', context)

#     # If no specific employee is selected, display all employees
#     all_employees = User.objects.all().values()
#     context = {
#         'all_employees': all_employees,
#     }
#     return render(request, 'attendance_list_view.html', context)



def view_attendance(request):

    if request.method == 'POST':
        employee_id = request.POST.get('id')
        print("Employee id: ", employee_id)
        # Check if both fields are provided
        if employee_id:
            stu = User.objects.filter(employee_id=employee_id).values()
            print("stu", stu)

            # Retrieve attendance records for the specified employee
            attendances = AttendenceForm.objects.filter(employee_id=employee_id).values()
            print("Employ", attendances)
            
            # Calculate total attendance days, absent days, and working days for the specified employee
            total_attendance_days = AttendenceForm.objects.filter(employee_id=employee_id, attendance_status='Present').count()
            total_absent_days = AttendenceForm.objects.filter(employee_id=employee_id, attendance_status='Absent').count()
            total_working_days = total_attendance_days + total_absent_days

            # Retrieve details for all employees
            all_employees = User.objects.all().values()
            
            context = {
                'stu': stu,
                'attendances': attendances,
                'total_attendance_days': total_attendance_days,
                'total_absent_days': total_absent_days,
                'total_working_days': total_working_days,
                'all_employees': all_employees,  # Include details for all employees
            }
            all_employees = User.objects.all().values()
            contextt = {
              'all_employees': all_employees,
                      }

            return render(request, 'view_attendence.html', context)

    # If no specific employee is selected, display all employees
    all_employees = User.objects.all().values()
    context = {
        'all_employees': all_employees,
    }
    return render(request, 'view_attendence.html', context)
    
    

# def employee_attendance(request, id):
   
#      # Retrieve all attendance records
#     all_attendances = AttendenceForm.objects.all()

#     # Count the total attendance days (days marked as 'P' for present)
#     total_attendance_days = all_attendances.filter(Attendence='P').count()

#     # Count the total absent days (days marked as 'A' for absent)
#     total_absent_days = all_attendances.filter(Attendence='A').count()

#     # Calculate the total working days (sum of attendance and absent days)
#     total_working_days = total_attendance_days + total_absent_days

#     context = {
#         'all_attendances': all_attendances,
#         'total_attendance_days': total_attendance_days,
#         'total_absent_days': total_absent_days,
#         'total_working_days': total_working_days,
#     }

#     return render(request, 'employee_attendence.html', context)




def add_box(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    try:
        if request.method == 'POST':
            form = BoxForm(request.POST)
            if form.is_valid():
                building_name = form.cleaned_data['building_id']
                product_name = form.cleaned_data['product_id']
                rack_name = form.cleaned_data['rack_id']
                box_name = form.cleaned_data['Box_Name']

                building, _ = Building.objects.get_or_create(Building_Name=building_name)
                product, _ = Products.objects.get_or_create(Product_Name=product_name)
                rack, _ = Racks.objects.get_or_create(rack_name=rack_name)

                # Create a new Box instance
                box = Box(
                    building_id=building,
                    product_id=product,
                    rack_id=rack,
                    Box_Name=box_name,
                    Current_Date=date.today()
                )
                box.save()

                request.session['box_id'] = box.Box_id

                return redirect('add_box')
        else:
            form = BoxForm()
        return render(request, 'add_box.html', {'form': form})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')


def view_box(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    try:
        boxes = Box.objects.all()  # Get all Box instances
        return render(request, 'view_box.html', {'boxes': boxes})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def delete_box(request, box_id):
    try:
        box = Box.objects.get(Box_id=box_id)
        box.delete()
        return redirect('view_box')  # Redirect to the view_box page after successful deletion
    except Box.DoesNotExist:
        # Handle the case where the box doesn't exist
        pass  # You can add appropriate error handling here
    
    

    
    
def BuildingSearch(request):
    form = BuildingSearchForm(request.GET)
    
    selected_building = None
    racks_data = None
    available_racks = 0
    
    if form.is_valid():
        selected_building = form.cleaned_data['building']
        
        if selected_building:
            racks_data = Racks.objects.filter(foreign_key_fied=selected_building)
            total_racks_stored = racks_data.count()
            total_racks = selected_building.Total_No_Racks
            available_racks = total_racks - total_racks_stored
    
    buildings = Building.objects.all()
    
    return render(request, 'Building_Space.html', {
        'form': form,
        'buildings': buildings,
        'selected_building': selected_building,
        'racks_data': racks_data,
        'available_racks': available_racks
    })





def transit_box_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        if request.method == 'POST':
            form = BoxTransit(request.POST)
            print(form)
            
            if form.is_valid():
                # Process valid form data and save it to the database
                box_name = form.cleaned_data['box_select']
                selected_box = Box.objects.get(Box_Name=box_name)
                vehicle_transit = form.cleaned_data['vehicle_transit']
                action = form.cleaned_data['box_action']
                
                # Update the BoxTransit instance
                box_transit = BoxTransit(
                    Box=selected_box,
                    product_id=selected_box.product_id,
                    building_id=selected_box.building_id,
                    rack_id=selected_box.rack_id,
                    vehicle_id=vehicle_transit,
                    Box_Name=box_name,
                    vehicle_transit=vehicle_transit,
                    Action=action
                )
                box_transit.save()

                # Redirect to the desired page
                return redirect('box_transit')  # Ensure you have defined this URL pattern
            else:
                print("Box is invalid")
                form = BoxTransit()
                # Handle the case when the form is invalid (e.g., redisplay the form with error messages)
                boxes = Box.objects.all()
                vehicles = Veh.objects.all()

                context = {
                    'boxes': boxes,
                    'vehicles': vehicles,
                    'form': form  # Pass the invalid form back to the template for error messages
                }

                return render(request, 'box_transit.html', context)
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')



def update_box(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        vehicles = Veh.objects.all()
        print('vehicles',vehicles)
        if request.method == 'POST':
            for key, value in request.POST.items():
                if key.startswith('box_id_'):
                    box_id = value
                    print('box_id',box_id)
                    vehicle_transit = request.POST.get('vehicle_transit_' + box_id)
                    print('vehicle:',vehicle_transit)
                    action = request.POST.get('box_action_' + box_id, '')

                # Update the Box object with the selected vehicle_transit and action
                    box = Box.objects.get(pk=box_id)
                    box.vehicle_transit = vehicle_transit
                    box.Action = action
                    box.save()  # Save the changes to the database

            print('Update success', Box.objects.all().values())
        return redirect('box_transit')  # Redirect to the appropriate page after updating
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def box_transit_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        # Add any logic you need to retrieve data from the database
        # For example:
        boxes = Box.objects.all()  # You can modify this query as needed
        vehicles = Veh.objects.all()
        return render(request, 'box_transit.html', {'boxes': boxes, 'vehicles': vehicles})
    except Supervise.DoesNotExist:
        return redirect('main_index_Page')

def view_transit_box(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('main_index_Page')
    
    try:
        # Assuming you have a way to determine the selected box, for example, using the box id
        selected_box_id = 1  # Replace with the actual selected box id

        try:
            selected_box = Box.objects.get(Box_id=selected_box_id)
            vehicle_transit = selected_box.vehicle_transit
            action = selected_box.Action
        except Box.DoesNotExist:
            selected_box = None
            vehicle_transit = None
            action = None

        boxes = Box.objects.all()

        context = {
            'boxes': boxes,
            'selected_box': selected_box,
            'vehicle_transit': vehicle_transit,
            'action': action,
        }

        return render(request, 'view_box_transit.html', context)

    except Supervise.DoesNotExist:
        return redirect('main_index_Page')





def employee_view_box(request):
    boxes = Box.objects.all()  # Get all Box instances
    return render(request, 'employee_box_view.html', {'boxes': boxes})


def employee_view_Product(request):
    stu=Products.objects.all().values()
    return render(request,'employee_product_view.html',{'stu':stu})


def employee_view_transit_box(request):
    # Assuming you have a way to determine the selected box, for example, using the box id
    selected_box_id = 1  # Replace with the actual selected box id

    try:
        selected_box = Box.objects.get(Box_id=selected_box_id)
        vehicle_transit = selected_box.vehicle_transit
        action = selected_box.Action
    except Box.DoesNotExist:
        selected_box = None
        vehicle_transit = None
        action = None

    boxes = Box.objects.all()

    context = {
        'boxes': boxes,
        'selected_box': selected_box,
        'vehicle_transit': vehicle_transit,
        'action': action,
    }

    return render(request, 'employee_boxtransit_view.html', context)


def employee_view_vehicle(request):
    stu=Veh.objects.all().values()
    return render(request,'employee_vehicle_view.html',{'stu':stu})

def employee_view_building(request):
    buildings = Building.objects.all()

    for building in buildings:
        total_racks = building.Total_No_Racks

        if total_racks is not None:
            racks_data = Racks.objects.filter(foreign_key_fied=building)
            total_racks_stored = racks_data.count()
            available_racks = total_racks - total_racks_stored
        else:
            total_racks_stored = 0
            available_racks = 0
        
        building.total_racks_stored = total_racks_stored
        building.available_racks = available_racks

    return render(request, 'employee_building_view.html', {'buildings': buildings})





























