from django.shortcuts import render  # noqa
from django.http import HttpResponse  # noqa
from group.models import Group  # noqa
from forms import GroupCreateForm  # noqa


def show_groups(request) -> HttpResponse:
    groups = Group.objects.all()
    response = ''
    for group in groups:
        response += group.info() + '<br/>'
    return HttpResponse(response)


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {
        'form_name': 'CREATE GROUP',
        'create_form': form
    }
    return render(request, 'create.html', context=context)
