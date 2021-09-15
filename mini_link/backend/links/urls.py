from django.urls import path
from .views import LinkCreator
from links.views import RedirectToDestination


urlpatterns = [
    path('create/', LinkCreator.as_view(), name='guest-link-creator'),
    path('<uuid:token>/', RedirectToDestination.as_view(),
         name="url_redirection"),

]
