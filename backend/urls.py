
from django.urls import path
from . import views

urlpatterns = [
    #### main dashboard
    path('', views.index, name="dashboard"),

    #### News blog
    path('news_blog/', views.news_blog, name="system_news_blog"),
    path('news_blog/add/', views.add_news_blog, name="add_news_blog"),
    path('news_blog/update/<str:id>', views.update_news_blog, name="update_news_blog"),
    path('update_news_image/<str:id>', views.update_news_image, name="update_news_image"),
    path('change_publish_status/', views.change_publish_status, name="change_publish_status"),
    path('change_news_blog_allow_comment_status/', views.change_news_allow_comment_status, name="change_news_blog_allow_comment_status"),
    
    #### Executives
    path('executives/', views.executives, name="system_executives"),
    path('executive/add/', views.add_executive, name="add_executive"),
    path('executive/update/<str:id>', views.update_executive, name="update_executive"),
    path('executive/delete/<str:id>', views.delete_executive, name="delete_executive"),
    path('update_executive_image/<str:id>', views.update_executive_image, name="update_executive_image"),
    path('change_executive_publish_status/', views.change_executive_publish_status, name="change_executive_publish_status"),


    #### Volunteers
    path('volunteers/', views.volunteers, name="system_volunteers"),
    path('volunteer/add/', views.add_volunteer, name="add_volunteer"),
    path('volunteer/update/<str:id>', views.update_volunteer, name="update_volunteer"),
    path('volunteer/delete/<str:id>', views.delete_volunteer, name="delete_volunteer"),
    path('update_volunteer_image/<str:id>', views.update_volunteer_image, name="update_volunteer_image"),
    path('change_volunteer_publish_status/', views.change_volunteer_publish_status, name="change_volunteer_publish_status"),


    #### Testimonials
    path('testimonials/', views.testimonial, name="system_testimonials"),
    path('testimonial/add/', views.add_testimonial, name="add_testimonial"),
    path('testimonial/update/<str:id>', views.update_testimonial, name="update_testimonial"),
    path('testimonial/delete/<str:id>', views.delete_testimonial, name="delete_testimonial"),
    path('change_testimonial_publish_status/', views.change_testimonial_publish_status, name="change_testimonial_publish_status"),


    #### Slides
    path('slides/', views.slides, name="system_slides"),
    path('slide/add/', views.add_slide, name="add_slide"),
    path('slide/update/<str:id>', views.update_slide, name="update_slide"),
    path('slide/delete/<str:id>', views.delete_slide, name="delete_slide"),
    path('change_slide_publish_status/', views.change_slide_publish_status, name="change_slide_publish_status"),

    #### Sponsors
    path('sponsors/', views.sponsors, name="system_sponsors"),
    path('sponsor/add/', views.add_sponsor, name="add_sponsor"),
    path('sponsor/update/<str:id>', views.update_sponsor, name="update_sponsor"),
    path('sponsor/delete/<str:id>', views.delete_sponsor, name="delete_sponsor"),
    path('change_sponsor_publish_status/', views.change_sponsor_publish_status, name="change_sponsor_publish_status"),

    #### Causes
    path('causes/', views.causes, name="system_causes"),
    path('cause/add/', views.add_cause, name="add_cause"),
    path('cause/update/<str:id>', views.update_cause, name="update_cause"),
    path('cause/delete/<str:id>', views.delete_cause, name="delete_cause"),
    path('change_cause_publish_status/', views.change_cause_publish_status, name="change_cause_publish_status"),

    #### Upcoming event
    path('upcoming_events/', views.upcoming_events, name="system_upcoming_events"),
    path('upcoming_event/add/', views.add_upcoming_event, name="add_upcoming_event"),
    path('upcoming_event/update/<str:id>', views.update_upcoming_event, name="update_upcoming_event"),
    path('upcoming_event/delete/<str:id>', views.delete_upcoming_event, name="delete_cause"),
    path('change_upcoming_event_publish_status/', views.change_upcoming_event_publish_status, name="change_upcoming_event_publish_status"),


    #### Settings
    path('settings/', views.settings, name="system_settings"),


    #### main template example link (should be disable in production)
    path('template/', views.template, name="template"),


]