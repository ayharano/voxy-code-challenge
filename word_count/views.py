from django.http import HttpResponse
from django.shortcuts import render


def word_count(request):
    if request.method == 'POST':
        if not request.POST['textbox']:
            return HttpResponse(status=400)

        return HttpResponse()

    return render(request, 'word_count/word_count.html')
