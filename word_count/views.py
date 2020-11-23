from django.shortcuts import render


def word_count(request):
    return render(request, 'word_count/word_count.html')
