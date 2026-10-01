from django.views.generic import ListView
from infinitvoid.models import Person


class PersonListView(ListView):
    model = Person
    template_name = "infinitvoid/person_list.html"
    context_object_name = "people"
    paginate_by = 10