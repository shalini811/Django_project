from django.shortcuts import render
from .models import Popularplaces
# Create your views here.

def index(request):

    pop1=Popularplaces()
    pop1.name='India'
    pop1.contname='Asia'
    pop1.price=1000
    pop1.days=10
    pop1.review=25
    pop1.img='4.png'
    pop1.offer=False

    pop2=Popularplaces()
    pop2.name='Paris'
    pop2.contname='Europe'
    pop2.price=2000
    pop2.days=8
    pop2.review=20
    pop2.img='5.png'
    pop2.offer=False

    pop3=Popularplaces()
    pop3.name='Tokyo'
    pop3.contname='Asia'
    pop3.price=600
    pop3.days=12
    pop3.review=25
    pop3.img='6.png'
    pop3.offer=True

    pops=[pop1,pop2,pop3]

    return render(request,'index.html',{'pops':pops})