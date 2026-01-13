from django.shortcuts import render

# Create your views here.

def index(request):
# listings haven't down yet,
# 要从listing model那里拉title,job type and budget 的资料
        context = {'listings': listings,
        "title":title,
        "type":type,
        "budget":budget
        }
        return render(request,'pages/index.html',context)