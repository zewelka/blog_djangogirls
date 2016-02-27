from django.shortcuts import render

# Create your views here. View - funkcja ta sie wykona gdy wejdziemy pod adres mojego bloga
def post_list(request):# request - zbiór danych z info o zapytaniu
    return render(request, 'blog/post_list.html', {}) # wywołanie funkcji render; wygenerowanie (wyrenderowanie) odpowiedzi dla przegladarki