from django.shortcuts import render

# Create your views here.

def index(request):
    # listings haven't down yet
    context = {'listings': listings,
            "title":title,
            "type":type,
            "budget":budget
            }
    return render(request,'pages/index.html',context)