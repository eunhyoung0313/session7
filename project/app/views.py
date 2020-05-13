from django.shortcuts import render

# Create your views here.


def count(request):
    return render(request, 'count.html')
def result(request):
    text = request.POST['text']
    total_len =len(text)
    exclude_space = len(text.replace(" ",""))
    word_count= len(text.split(" ")) 
   
   
    return render(request,'result.html',{
        'text' : text,
        'total_len': total_len,
        'exclude_space': exclude_space,
        'word_count': word_count
    })
