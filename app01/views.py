from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class DogView(View):
    def get(self, request):
        return render(request, 'dog/dog.html')


class FlexView(View):
    def get(self, request):
        return render(request, 'remove/index.html')