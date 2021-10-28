from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)

# Create your views here.
