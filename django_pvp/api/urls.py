from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^tournaments$', views.TournamentsView.as_view(), name="tournaments"),
]

