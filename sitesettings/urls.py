from django.urls import path
from .views import SmtpView, SmtpDetailView

urlpatterns = [
    path('smtp/',SmtpView.as_view()),
    path('smtp-detail/',SmtpDetailView.as_view()),
]