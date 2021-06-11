from django.http import HttpResponse


# Create your views here.
from groups.models import Group

from students.utils import format_records


def get_groups(request):
    groups = Group.objects.all()
    records = format_records(groups)
    return HttpResponse(records)
