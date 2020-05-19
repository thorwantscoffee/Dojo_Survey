from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request):
    return render(request, "index.html")

def form_submission(request):
    if request.method == "POST":
        context = {
            "yourname" :request.POST['yourname'],
            "location": request.POST['location'],
            "language": request.POST['language']
        }
        return render(request, 'result.html', context)
    else:
        return redirect('/')

