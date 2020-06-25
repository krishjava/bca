from django.shortcuts import render,redirect, get_object_or_404
from .models import Uploaded,Item,Comment,Property_Buy,Property_Rent,Apartment_All,User_Profile
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView,View
from django.utils import timezone
from .forms import Rent_request,Comments,Buyer_request,Up,Test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views her

 

class Home (ListView):
    model  = Item
    template_name = "index.html"
    paginate_by = 4

@login_required
# def item_detail(request,id):
#     today = timezone.now().now()
#     product = get_object_or_404(Item, pk=id)
#     comment = Comments(request.POST or None)
#     com = Comment.objects.filter(post_id = id)

#     if comment.is_valid():
#         user = request.user
#         post_id = id
#         message = comment.cleaned_data.get('message')
#         comment_date = today

#         #add item in table comment
#         comment_data = Comment()
#         comment_data.user= user
#         comment_data.post_id_id = post_id
#         comment_data.message = message
#         comment_data.comment_date =comment_date
#         comment_data.save()
#         messages.success(request,"Thanks for feedback")
#         return redirect("/item_detail/%d/" %id )
        
#     rent_qs = Item.objects.filter(status="R",id=id,on_rant=False)
#     print(rent_qs)
#     if rent_qs.exists():
#         item = rent_qs[0]
#         if item.status =="R" and item.id==id:
#             form1 = Rent_request()
#             context1 = {
#             'form':form1,
#             'comment':comment,
#             "product":product,
#             }
#             form  = Rent_request(request.POST or None)
#             if form.is_valid():
#                 voter_id = form.cleaned_data.get('voter_id')
#                 addhar_no = form.cleaned_data.get('addhar_no')
#                 profession = form.cleaned_data.get('profession')
#                 moblie = form.cleaned_data.get('moblie')
#                 try:
#                     rent = Rent()
#                     rent.user = request.user
#                     rent.voter_id = voter_id
#                     rent.addhar_no = addhar_no
#                     rent.profession = profession 
#                     rent.moblie = moblie
#                     rent.save()
#                     property = Item.objects.filter(id=id)
#                     if property.exists():
#                         rent_item = property[0]
#                         rent_item.status = "O"
#                         rent_item.on_rant=True
#                         rent_item.save()
#                         messages.success(request,"your request is successfully registred")
#                         return redirect("/item_detail/%d/" %id )
#                     else:
#                         messages.warning(request,"sorry this property already on rented")
#                         return redirect("/item_detail/%d/" %id )
#                 except ObjectDoesNotExist:
#                     messages.info(request,"sorry invalid request please try again")
#                     return redirect("/item_detail/%d/" %id )
#         elif item.status =="O":
#             item.status ="O"
#             item.save()
#             return redirect("/item_detail/%d/" %id )
#         return render(request,"detail.html",context1)
    
#     context = {
#         "product":product,
#         'comment':comment,
#         'com':com

#     }
#     return render(request,"detail.html",context)

def item_detail(request,id):
    product = get_object_or_404(Item, pk=id)
    # check_rent=Property_Rent.objects.filter(property_id=product.id)
    # if check_rent.exists():
    #     print('id avaliable')
    # else:
        # print('not ava')
    print(product.status)
    print(product.id)
    context={
        'product':product,
    }
    if product.status == 'Rent':
        rent_q_set=Property_Rent.objects.filter(status="Rented",property_id=id)
        print(rent_q_set)
        if not rent_q_set.exists():
            context1={
                'product':product,
                'form1':Rent_request()
            }
            rent_form = Rent_request(request.POST or None)
            if request.method == 'POST':
                if rent_form.is_valid():
                    mobile = rent_form.cleaned_data.get('mobile')      
                    email = rent_form.cleaned_data.get('email')     
                    addhar_id = rent_form.cleaned_data.get('addhar_id')     
                    residence_address = rent_form.cleaned_data.get('residence_address')     
                    profession = rent_form.cleaned_data.get('profession')     
                    voter_id = rent_form.cleaned_data.get('voter_id') 
                    try:
                        item = Item.objects.filter(id=id)
                        rent=Property_Rent()
                        rent.user=request.user
                        rent.mobile=mobile
                        rent.email=request.user.email
                        rent.addhar_id=addhar_id
                        rent.residence_address=residence_address
                        rent.profession=profession
                        rent.voter_id=voter_id
                        rent.image=item[0].image
                        rent.status="Rented"
                        rent.price=item[0].price
                        rent.property_type=item[0].property_type
                        rent.property_id=item[0].id 
                        rent.on_rent=True
                        rent.save()
                        return redirect("/")
                    except ObjectDoesNotExist:
                        messages.info(request,"sorry invalid request please try again")
                        return render(request,"detail.html")
                return render(request,"detail.html",context1)
            return render(request,"detail.html",context1)
        else:
            return render(request,"detail.html",context)
    
    elif product.status == 'Sale':
        buy_q_set=Property_Buy.objects.filter(status="Buy",property_id=id)
        print(buy_q_set)
        if not buy_q_set.exists():
            context2={
                'product':product,
                'form2':Buyer_request()
            }
            buyer_form = Buyer_request(request.POST or None)
            if request.method == 'POST':
                if buyer_form.is_valid():
                    mobile = buyer_form.cleaned_data.get('moblie')      
                    email = buyer_form.cleaned_data.get('email')     
                    try:
                        item = Item.objects.filter(id=id)
                        buy=Property_Buy()
                        buy.user=request.user
                        buy.email=request.user.email
                        buy.moblie=mobile
                        buy.status="Buy"
                        buy.property_image=item[0].image
                        buy.price=item[0].price
                        buy.property_type=item[0].property_type
                        buy.property_id=item[0].id
                        buy.on_buy=True
                        buy.save()
                        return redirect("/")
                    except ObjectDoesNotExist:
                        messages.info(request,"sorry invalid request please try again")
                        return render(request,"detail.html")
                return render(request,"detail.html",context2)
            return render(request,"detail.html",context2)
        else:
            return render(request,"detail.html",context)
    return render(request,"detail.html",context)
def search(request):  
    if request.method == 'POST':
        status=request.POST['pro_status']
        type_por=request.POST['pro_type']
        city=request.POST['city']
        if city:
            result = Item.objects.all().filter(city=city)  
            if result:           
                return render(request,"search.html",{'result': result})
            else:
                return render(request,"search.html",{'results': 'error sorry location not found or do not have plot on this location'})
    return render(request,"index.html")



def create(request):
    form=Up()
    context={
             'form':form
         }
    check=Up(request.POST, request.FILES or None)
    if request.method == 'POST':
        if check.is_valid():
           swimming_pool=check.cleaned_data.get('swimming_pool')
           status=check.cleaned_data.get('status')
           price=check.cleaned_data.get('price')
           squarefoot=check.cleaned_data.get('squarefoot')
           city=check.cleaned_data.get('city')
           Full_address=check.cleaned_data.get('Full_address')
           bedroom=check.cleaned_data.get('bedroom')
           bedroom_img=check.cleaned_data.get('bedroom_img')
           kitchen_img=check.cleaned_data.get('kitchen_img')
           let_bath=check.cleaned_data.get('let_bath')
           pro_image=check.cleaned_data.get('pro_image')
           property_structure=check.cleaned_data.get('property_structure')
           property_type=check.cleaned_data.get('property_type')
           print('create')
           print(swimming_pool)
           print(status)
           try:
               up=Item()
               if swimming_pool==None:
                 up.swimming_pool='/media/default/item_default.png'
               else:
                   up.swimming_pool=swimming_pool
               up.status=status
               up.user=request.user
               up.image=pro_image
               up.price=price
               up.squarefoot=squarefoot
               up.city=city
               up.town_address=Full_address
               up.bedroom=bedroom
               up.bedroom_img=bedroom_img
               up.kitchen_img=kitchen_img
               up.let_bath=let_bath
               up.image=pro_image
               up.property_structure=property_structure
               up.property_type=property_type
               up.save()
           except ObjectDoesNotExist:
                return render(request,"create.html",context)
        return render(request,"create.html",context)
    return render(request,'create.html',context)         
            
    # if request.method== 'POST':  
    #     item=Item()
    #     if request.POST['status'] and request.FILES['pro_image'] and request.FILES['kit_img'] and request.POST['kitchen'] and request.POST['squrefoot'] and request.POST['city'] and request.POST['address'] and request.FILES['bed_img'] and request.POST['bed'] and request.POST['let_bath'] and request.FILES['swimming'] and request.POST['price']: 
    #         item.user = request.user
    #         item.image=request.FILES['pro_image']
    #         item.status=request.POST['status']
    #         item.kitchen_img=request.FILES['kit_img']
    #         item.kitchen=request.POST['kitchen']
    #         item.squrefoot=request.POST['squrefoot']
    #         item.city=request.POST['city']
    #         item.town_address=request.POST['address']
    #         item.bedroom_img=request.FILES['bed_img']
    #         item.bedroom=request.POST['bed']
    #         item.let_bath=request.POST['let_bath']
    #         item.swimming_pool=request.FILES['swimming']
    #         item.price=request.POST['price']
    #         item.save()
    #         return redirect('/')   
    #     else:
    #         return render(request,'create.html',{'error': 'please fill all the details'})         

@login_required
def apartment(request):
    apt_list=Apartment_All.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(apt_list, 4)
    try:
        apt = paginator.page(page)
    except PageNotAnInteger:
        apt = paginator.page(1)
    except EmptyPage:
        apt = paginator.page(paginator.num_pages)

    return render(request,'apt.html',{'apt':apt})

def apt_detail(request):
    return render(request,'apt_detail.html')


# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'core/user_list.html', { 'users': users })

def about(request):
    return render(request,'sig.html')     

def official(request):
    form=Test()
    test=Test(request.POST or None)
    if request.method == 'POST':
        if test.is_valid():
           name=test.cleaned_data.get('name')
           id=test.cleaned_data.get('id')
           print(name)
           print(id)
    return render(request,"official.html",{'form':form})

def desh(request):
    items=Item.objects.all().filter(user=request.user) 
    profile=User_Profile.objects.all().filter(user=request.user)
    end=request.user.last_login
    print('last')
    print(end)
    context={
        'user_name':request.user,
        'user_email':request.user.email,
        'items':items,
        'image':profile,
        'end':end
    }
    return render(request,"deshboard.html",context)