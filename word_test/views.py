from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def start_page(request):
    return render(request,'start.html')

def word_test(request):
    step = request.GET.get('step')
    name = request.GET.get('name')
    answer = request.GET.get('answer')

    # print(step)

    words = {
        "hello": "used as a greeting when you meet somebody, when you answer the telephone or when you want to attract somebody’s attention",
        "ninja": "a person trained in traditional Japanese skills of fighting and moving quietly",
        "owl": "a bird of prey (= a bird that kills other creatures for food) with large round eyes, that hunts at night. Owls are traditionally thought to be wise.",
        "programmer": "a person whose job is writing programs for computers",
        "laptop": "a small computer that can work with a battery and be easily carried"
    }
    if int(step)==0:
        answer_list=None


    elif int(step)==1:
        answer_list = answer

    else:
        answer_list = request.GET.get('answer_list')
        answer_list += ',' + answer

    if int(step)!=5:
        ctx = {
            'word': list(words.keys())[int(step)],
            'meaning': list(words.values())[int(step)],
            'counts': range(5),
            'step': int(step) + 1,
            'name': name,
            'answer': answer,
            'answer_list': answer_list
        }
        return render(request, 'test.html',ctx)

    else:
        answer_list = request.GET.get('answer_list')
        answer_list += ',' + answer
        print(answer_list)
        answer_list=answer_list.split(',')
        sol=list(words.keys())
        result=''
        for i in range(5):
            if sol[i]==answer_list[i]:
                result+=str(i+1)+'번 정답 : {} '.format(sol[i])+\
                              ' 제출한 답 : {}  ==>  '.format(answer_list[i])+'맞았습니다 <br /> <br /> '
            else:
                result+=str(i+1)+'번 정답 : {} '.format(sol[i])+\
                              ' 제출한 답 : {}  ==>  '.format(answer_list[i])+'틀렸습니다 <br /> <br />'
        ctx={
            'name':name,
            'word':list(words.keys()),
            'result': result
        }
        return render(request,'result.html',ctx)




