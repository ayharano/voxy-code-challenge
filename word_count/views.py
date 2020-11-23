from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def word_count(request):
    if request.method == 'POST':
        if not request.POST['textbox']:
            return HttpResponse(status=400)

        content = logic.word_count(request.POST['textbox'])

        if not content:
            return HttpResponse(status=400)

        word_count_as_string = logic.word_count(request.POST['textbox'])

        return HttpResponse(content=word_count_as_string, status=200)

    return render(request, 'word_count/word_count.html')
