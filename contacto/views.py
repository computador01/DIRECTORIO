from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf
from django.urls import reverse_lazy


from .models import Contacto

from django.views.generic import (
ListView,
DetailView,
UpdateView,
DeleteView,
CreateView,
View
)

# Create your views here.

class listar(ListView):
    template_name = 'listar.html'
    paginate_by = 4
    ordering = 'Nombre'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Contacto.objects.filter(
            Nombre__icontains=palabra_clave
        )
        return lista
    
    
class ListContactosPdf(View):
    
    def get(self, request, *args, **kwargs):
        contactos = Contacto.objects.all()
        data = {
            'contactos': contactos,
            'cantidad': contactos.count()
        }
        pdf = render_to_pdf('lista.html', data)
        return HttpResponse(pdf, content_type='application/pdf') 
    
    
class ContactoDetailView(DetailView):
    model = Contacto
    template_name = 'detail.html'
    
    def get_context_data(self, **kwargs): 
        context = super(ContactoDetailView, self).get_context_data(**kwargs)
        context['Nombre'] = 'Contacto del mes'
        return context
    
    
class listar_all(ListView):
    template_name = 'listar_all.html'
    paginate_by = 4
    ordering = 'Nombre'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Contacto.objects.filter(
            Nombre__icontains=palabra_clave
        )
        return lista
    
    
class ContactoUpdateView(UpdateView):
    template_name = 'update.html'
    model = Contacto
    fields = [
        'Nombre',
        'Apellidos',
        'Telefono',
        'Profesion',
        'Ciudad',   
    ]
    success_url = reverse_lazy('listar_all')
    
    
class ContactoDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Contacto
    success_url = reverse_lazy('listar_all')


class ContactoCreateView(CreateView):
    template_name = 'add.html'
    model = Contacto
    fields = [
        'image',
        'Nombre',
        'Apellidos',
        'Telefono',
        'Profesion',
        'Ciudad',   
    ]
    success_url = reverse_lazy('listar_all')
    
    
    

    
    
    


    

    
    

