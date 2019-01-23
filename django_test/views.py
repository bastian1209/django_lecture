from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def hello_view(request):
    if request.method=='POST':
        print('post 요청이 들어왔습니다.')
        print(request.POST)
    else:
        print("post 외의 요청이 들어왔습니다.")

    hello=request.GET.get('hello')
    context={
        'counts':range(10),
        'hello':hello,
        'request_method':request.method,
    }

    return render(request,'ex.html',context)
