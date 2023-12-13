from django.shortcuts import render

def home_page(Request):
    return render(Request,'index.html')

def about_page(Request):
    return render(Request,'about.html')

def blog_details_page(Request):
    return render(Request,'blog-details.html')

def blog_right_sidebar_page(Request):
    return render(Request,'blog-right-sidebar.html')
    
def blog_page(Request):
    return render(Request,'blog.html')
    
def coming_soon_page(Request):
    return render(Request,'coming-soon.html')
    
def contact_page(Request):
    return render(Request,'contact.html')
    
def error_404_page(Request):
    return render(Request,'error-404.html')
    
def event_booking_page(Request):
    return render(Request,'events-booking.html')
    
def event_details_page(Request):
    return render(Request,'events-details.html')
    
def events_page(Request):
    return render(Request,'events.html')
    
def faq_page(Request):
    return render(Request,'faq.html')
    
def features_page(Request):
    return render(Request,'features.html')
    
def gallery_page(Request):
    return render(Request,'gallery.html')
    
def index2_page(Request):
    return render(Request,'index-2.html')
   
def index3_page(Request):
    return render(Request,'index-3.html')
   
def login_page(Request):
    return render(Request,'login.html')
   
def pricing_page(Request):
    return render(Request,'pricing.html')
 
def privacy_policy_page(Request):
    return render(Request,'privacy-policy.html')
 
def register_page(Request):
    return render(Request,'register.html')

def services_page(Request):
    return render(Request,'services.html')
    
 
def services_details_page(Request):
    return render(Request,'services-details.html')
 
def team_page(Request):
    return render(Request,'team.html')
 
def terms_of_service_page(Request):
    return render(Request,'terms-of-service.html')
 
def workspaces_page(Request):
    return render(Request,'workspaces.html')
