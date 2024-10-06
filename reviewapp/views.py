from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'reviewapp/index.html')

def about(request):
    return render(request, 'reviewapp/about.html')

def blog(request):
    return render(request, 'reviewapp/blog.html')

def contacts(request):
    return render(request, 'reviewapp/contacts.html')

def faq(request):
    return render(request, 'reviewapp/faq.html')

def login(request):
    return render(request, 'reviewapp/login.html')

def register(request):
    return render(request, 'reviewapp/register.html')

def not_found(request):
    return render(request, 'reviewapp/404.html')

def help(request):
    return render(request, 'reviewapp/help.html')

def categories(request):
    return render(request, 'reviewapp/all-categories.html')

def companies(request):
    return render(request, 'reviewapp/companies-landing.html')

def filterstop(request):
    return render(request, 'reviewapp/category-companies-listings-filterstop.html')

def home2(request):
    return render(request, 'reviewapp/index-2.html')

def home3(request):
    return render(request, 'reviewapp/index-3.html')

def write_review(request):
    return render(request, 'reviewapp/write-review.html')