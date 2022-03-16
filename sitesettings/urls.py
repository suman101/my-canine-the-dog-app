from django.urls import path
from .views import SmtpView, SmtpDetailView, ContactUsListView, ContactUsCreateView, ContactUsDetailView, ContactUsUpdateView, ContactUsDeleteView

urlpatterns = [
    path('smtp/',SmtpView.as_view()),
    path('smtp-detail/',SmtpDetailView.as_view()),

    path('contact-us-list/', ContactUsListView.as_view()),
    path('contact-us-create/', ContactUsCreateView.as_view()),
    path('contact-us-detail/<int:pk>/', ContactUsDetailView.as_view()),
    path('contact-us-update/<int:pk>/', ContactUsUpdateView.as_view()),
    path('contact-us-delete/<int:pk>/', ContactUsDeleteView.as_view()),
]