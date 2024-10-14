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

def icon_pack_1(request):
    return render(request, 'reviewapp/icon-pack-1.html')

def icon_pack_2(request):
    return render(request, 'reviewapp/icon-pack-2.html')

def icon_pack_3(request):
    return render(request, 'reviewapp/icon-pack-3.html')

def icon_pack_4(request):
    return render(request, 'reviewapp/icon-pack-4.html')

def reviews_page(request):
    return render(request, 'reviewapp/reviews-page.html')

def confirm(request):
    return render(request, 'reviewapp/confirm.html')

def dashboard(request):
    return render(request, 'reviewapp/user-dashboard.html')

def user_settings(request):
    return render(request, 'reviewapp/user-settings.html')

def row_listings_filterscol(request):
    return render(request, 'reviewapp/row-listings-filterscol.html')

def grid_listings_filterscol(request):
    return render(request, 'reviewapp/grid-listings-filterscol.html')

def grid_listings_filterstop(request):
    return render(request, 'reviewapp/grid-listings-filterstop.html')

def pricing(request):
    return render(request, 'reviewapp/pricing.html')



