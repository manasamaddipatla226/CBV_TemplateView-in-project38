from django.shortcuts import render
from django.views.generic import TemplateView
from typing import Any,Dict

# Create your views here.

class cbv_html(TemplateView):
    template_name='cbv_html.html'


class cbv_context(TemplateView):
        template_name='cbv_context.html'

        def get_context_data(self, **kwargs):
            EDCO= super().get_context_data(**kwargs)
            EDCO['name']='Manasa'
            EDCO['age']=21
            return EDCO
