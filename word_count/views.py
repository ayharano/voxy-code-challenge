from django.http import HttpResponse


def word_count(request):
    return HttpResponse('<html><body><form><textarea><input type="submit"></form></body></html>')
