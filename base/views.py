from django.shortcuts import render
# Create your views here.


rooms = [
    {'id':1, 'name':'Lets learn py!'},
    {'id':1, 'name':'Design!'},
    {'id':1, 'name':'Devs'},

]





def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')