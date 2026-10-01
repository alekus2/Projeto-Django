from django.urls import path
from infinitvoid.views import PersonListView

app_name = "infinitvoid"

urlpatterns = [
    path("pessoas/", PersonListView.as_view(), name="/person_list")]
