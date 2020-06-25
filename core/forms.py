from django  import forms
from django.core.validators import MaxValueValidator


class Buyer_request(forms.Form):
    email = forms.CharField()
    moblie = forms.CharField(max_length=10)

class Rent_request(forms.Form):
    mobile=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=256)
    addhar_id=forms.CharField(max_length=12)
    residence_address=forms.CharField(max_length=300)
    CHOICE=(
        ('student','student'),
        ('employee','employee'),
        ('worker','worker'),
    )
    profession=forms.ChoiceField(choices=CHOICE)
    voter_id=forms.CharField(max_length=6)

class Comments(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : "5",
        'cols' :'10'
    }))

class Up(forms.Form):
    STATUS=(
        ('Sale','Sale'),
        ('Rent','Rent'),
    )
    status=forms.ChoiceField(choices=STATUS)
    swimming_pool=forms.ImageField(required=False)
    price=forms.FloatField()
    squarefoot=forms.FloatField()
    city=forms.CharField(max_length=25)
    Full_address=forms.CharField(max_length=100)
    bedroom=forms.IntegerField()
    bedroom_img=forms.ImageField()
    kitchen_img=forms.ImageField()
    let_bath=forms.IntegerField()
    pro_image=forms.ImageField()
    property_structure=forms.ImageField()
    CHOICE=(
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
        ('4BHK','4BHK'),
    )
    property_type=forms.ChoiceField(choices=CHOICE)

class Test(forms.Form):
    name= forms.CharField(max_length=10)
    id=forms.IntegerField()





