from django.shortcuts import render,redirect, get_object_or_404
from .models import Item,Comment,Rent
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView
from django.utils import timezone
# Create your views her

class Home (ListView):
    model  = Item
    template_name = "index.html"
    paginate_by = 4


    
@login_required
def item_detail(request,id):
    today=timezone.datetime.now()
    if request.method == "POST" :
        if  request.POST["message"]:              
            comment = Comment()
            comment.message = request.POST['message']
            comment.user = request.user
            comment.post_id_id = id
            comment.comment_date= timezone.datetime.now()
            comment.save()
            return redirect("/item_detail/%d/" %id )
        
    com = Comment.objects.all().filter(post_id = id)
    product = get_object_or_404(Item, pk=id)
    return render(request,"detail.html",{"product":product, 'comment':com})

def search(request):  
    if request.method == 'POST':
        city =  request.POST['search']
        if city:
            result = Item.objects.all().filter(city=city)  
            if result:           
                return render(request,"search.html",{'result': result})
            else:
                return render(request,"search.html",{'results': 'error sorry location not found or dont have plot on this location'})
            
    return render(request,"index.html")



def create(request):
    if request.method== 'POST':
        item=Item()
        if request.FILES['image'] and request.POST['status'] and request.FILES['kit_img'] and request.POST['kitchen'] and request.POST['squrefoot'] and request.POST['city'] and request.POST['address'] and request.FILES['bed_img'] and request.POST['bed'] and request.POST['let_bath'] and request.FILES['swimming'] and request.POST['price']: 
            item.user = request.user
            item.image=request.FILES['image']
            item.status=request.POST['status']
            item.kitchen_img=request.FILES['kit_img']
            item.kitchen=request.POST['kitchen']
            item.squrefoot=request.POST['squrefoot']
            item.city=request.POST['city']
            item.town_address=request.POST['address']
            item.bedroom_img=request.FILES['bed_img']
            item.bedroom=request.POST['bed']
            item.let_bath=request.POST['let_bath']
            item.swimming_pool=request.FILES['swimming']
            item.price=request.POST['price']
            item.save()
            return redirect('/desh/%d'%request.user.id)   
        else:
            return render(request,'create.html',{'error': 'please fill all the details'})         
    return render(request,'create.html')         



    


def deshboard(request,id):
    item  =  Item.objects.all().filter(user =request.user)
    return render(request,"deshboard.html",{'items':item})

def check_rent(request,id):
    p=get_object_or_404(Rent,pk=id ) 
    if request.method=="POST":
        if request.POST['voterid'] and request.POST['addharcard'] and request.POST['profession'] and request.POST['moblie']:
            rent=Rent()
            rent.user=request.user
            rent.rent_id_id = id
            rent.voter_id =  request.POST['voterid']
            rent.addhar_no =request.POST['addharcard'] 
            rent.profession=request.POST['profession']
            rent.moblie=request.POST['moblie']           
            rent.save()
            return redirect("/item_detail/%d/" %id)  
        else: 
            return render(request,'detail.html',{'error' : 'some thing went wrong'})
    return render(request,"/",{'pro':p})
        

           
