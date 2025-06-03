from django.shortcuts import render

# Create your views here.
def main_page(request):
    

    context = {
        "data": "Привіт з джанго!"
    }

    return render(request, "index.html", context)