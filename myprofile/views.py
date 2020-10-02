from django.shortcuts import render

def top(request):
    context = {
        'name': 'たろう',
    }
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')
