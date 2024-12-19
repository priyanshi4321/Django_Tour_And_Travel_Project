from django.shortcuts import render
from django.http import HttpResponse
from place.models import Employeedata
# Create your views here.
def home(request):
    return HttpResponse("home page")
def aboutus(request):
    msg="<h1>about us page<h1>"
    return HttpResponse(msg)        

def homepage(request):
    print("hello")
    if request.method=="POST" and 'subBtn' in request.POST:
        print("button clicked")
    context={'user':"sparshi",'email':"sparshi123@gmail.com",'marks':[23,78,89]}
    return render(request,"homepage.html",context)
def abtus(request):
    data=[{'eid':101,'ename':"sparshi",'e_email':"sparshi123@gmail.com"},
          {'eid':101,'ename':"sparshi",'e_email':"sparshi123@gmail.com"},
          {'eid':101,'ename':"sparshi",'e_email':"sparshi123@gmail.com"},
          {'eid':101,'ename':"sparshi",'e_email':"sparshi123@gmail.com"}]
    
    context={"userdata":data}
    return render(request,"abtus.html",context)
def table(request):
    return render(request,"table.html")
def tour(request):
    return render(request,"tour.html")
def travel(request):
    return render(request,"travel.html")
def london(request):
    return render(request,"london.html")
def paris(request):
    return render(request,"paris.html")
def nepal(request):
    return render(request,"nepal.html")
def mexico(request):
    return render(request,"mexico.html")
def thailand(request):
    return render(request,"thailand.html")
def singapore(request):
    return render(request,"singapore.html")
def malaysia(request):
    return render(request,"malaysia.html")
def turkey(request):
    return render(request,"turkey.html")
def demo(request):
    return render(request,"demo.html")
def location(request):
    if request.method=="POST" and 'submit' in request.POST:
        # nm= request.POST.get('unm')
        # print(nm)
        user = Employeedata (
            emp_name=request.POST.get('unm'),
            emp_pwd=request.POST.get('pwd'),
            emp_email=request.POST.get('em'),
            emp_mob=request.POST.get('mob'),
            emp_dept=request.POST.get('dept'),
            emp_dob=request.POST.get('dob'),
            emp_img = request.FILES.get('img')
        )
        user.save()
        print(user)
    return render(request,"register.html")
def show(request):
    if request.method=="POST" and 'showbtn' in request.POST:
        userData=Employeedata.objects.all().values()
        # print(users,users[0])
        # for user in users:
        #     for u in user:
        #         print(user.get(u))
        return render(request,"showdata.html",{'users':userData})    
    return render(request,"showdata.html")    
def showall(request):
    if request.method=="POST" and 'showbtn' in request.POST:
        userData=Employeedata.objects.all().values()
        return render(request,"showalldata.html",{'userData':userData})    
    return render(request,"showalldata.html")

def edit(request,id):    
    userData=Employeedata.objects.get(id=id)
    return render(request,"edit.html",{'userData':userData})