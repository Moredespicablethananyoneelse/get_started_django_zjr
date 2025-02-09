from django.urls import path
from . import views

from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    #ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    #ex: /polls/5/results
    path("<int:question_id>/results", views.results, name="results"),
    #ex
    path("<int:question_id>/vote",views.vote, name="vote"),

]

if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()