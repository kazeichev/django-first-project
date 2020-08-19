from django.views import View
from django.shortcuts import render
from django_first_project.calc.models import History


class IndexView(View):
    def get(self, request, a, b):
        sum = a + b

        history = History()
        history.value = sum
        history.save()

        return render(request, 'index.html', {'a': a, 'b': b, 'sum': sum})


class HistoryView(View):
    def get(self, request):
        return render(request, 'history.html', {'histories': History.objects.all()})
