from django.shortcuts import render
from . import forms
from .models import *


# Create your views here.
def home(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(session_key)
    event = Event.objects.filter(event_state=2)[0]
    error = ''
    # team = Team.object.
    form_introduce = forms.Introduce(request.POST or None)
    if request.method == 'POST':
        # form_introduce.data.append('event', event.id)
        print(form_introduce.data)
        # form_introduce.fields.
        if form_introduce.is_valid():
            form_introduce.save()
        else:
            error = 'Форма заполнена неверно'

    context = {
        'title': 'Квиз! ' + str(event),
        'event': event,
        'session_key': session_key,
        'form': form_introduce,
        'error': error
    }
    return render(request, 'quizApp/introduce.html', context)


def leader(request):
    event = Event.objects.filter(event_state=2)[0]
    # tour = Tour.objects.filter(quiz=event.quiz).order_by('num')
    stage = Stage.objects.filter(event=event)
    return render(request, 'quizApp/leader.html', {'title': 'Управление Квизом',
                                                   'event': event,
                                                   # 'tour': tour,
                                                   'stage': stage})
