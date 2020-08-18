from django.shortcuts import render  # noqa
from django.http import HttpResponse  # noqa
from group.models import Group  # noqa


def show_groups(request) -> HttpResponse:
    groups = Group.objects.all()
    response = ''
    for group in groups:
        response += group.info() + '<br/>'
    return HttpResponse(response)
