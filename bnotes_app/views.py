from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from bnotes_app.models import Note
from django.utils import timezone


def index(request):
    template = loader.get_template('bnotes_app/index.html')

    notes_list = Note.objects.all().order_by('-created_date')

    for note in notes_list:
        note.content = note.content.replace('\r\n', '<br>')

    context = {
        'notes_list': notes_list,
    }

    return HttpResponse(template.render(context, request))


def note_new(request):
    template = loader.get_template('bnotes_app/note_new.html')

    context = {}

    return HttpResponse(template.render(context, request))


def note_add(request):
    note_text = request.POST['note_text']

    new_note = Note(content=note_text,
                    created_date=timezone.now())

    new_note.save()

    return HttpResponseRedirect("/notes")


def note_delete(request, note_id):
    note = Note.objects.get(id=note_id)

    if note is not None:
        note.delete()

    return HttpResponseRedirect("/notes")


def note_edit(request, note_id):
    note = Note.objects.get(id=note_id)

    template = loader.get_template('bnotes_app/note_edit.html')

    context = {'note_content': note.content, 'note_id': note.id}

    return HttpResponse(template.render(context, request))

    return HttpResponseRedirect("/notes")


def note_save(request):
    note_text = request.POST['note_text']
    note_id = request.POST['note_id']

    note = Note.objects.get(id=note_id)

    if note is not None:
        note.content = note_text
        note.created_date = timezone.now()

        note.save()

    return HttpResponseRedirect("/notes")
