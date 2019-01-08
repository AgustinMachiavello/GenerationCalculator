from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from GenerationCalculator.Apps.Generations.forms import HomeForm
from GenerationCalculator.Apps.Generations.calculator import calculate


# Create your views here.

class HomeView(TemplateView):

    template_name = 'index.html'

    def get(self, request):
        form = HomeForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            birthyear = form.cleaned_data['birthyear']
            if birthyear.isdigit():
                generations = calculate(int(birthyear))
                args = {'form': form, 'generation': generations}
            else:
                args = {'form': form}
            return render(request, 'index.html', args)
        else:
            return render(request, 'index.html')