
from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name="home_page"),
    path('about/',views.about_page, name="about_page"),
    path('blog/',views.blog_page, name="blog_page"),
    path('blog-details/',views.blog_details_page, name="blog_details_page"),
    path('blog-right-sidebar/',views.blog_right_sidebar_page, name="blog_right_sidebar_page"),
    path('coming-soon/',views.coming_soon_page, name="coming_soon_page"),
    path('contact/',views.contact_page, name="contact_page"),
    path('error-404/',views.error_404_page, name="error_404_page"),
    path('events-booking/',views.event_booking_page, name="event_booking_page"),
    path('events-details/',views.event_details_page, name="event_details_page"),
    path('events/',views.events_page, name="events_page"),
    path('faq/',views.faq_page, name="faq_page"),
    path('features/',views.features_page, name="features_page"),
    path('gallery/',views.gallery_page, name="gallery_page"),
    path('index-2/',views.index2_page, name="index2_page"),
    path('index-3/',views.index3_page, name="index3_page"),
    path('login/',views.login_page, name="login_page"),
    path('pricing/',views.pricing_page, name="pricing_page"),
    path('privacy-policy/',views.privacy_policy_page, name="privacy_policy_page"),
    path('register/',views.register_page, name="register_page"),
    path('services/',views.services_page, name="services_page"),
    path('services-details/',views.services_details_page, name="services_details_page"),
    path('team/',views.team_page, name="team"), 
    path('terms-of-service/',views.terms_of_service_page, name="terms_of_service_page"),
    path('workspaces/',views.workspaces_page, name="workspaces_page"),
    
    
]
