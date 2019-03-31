from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .models import * 
from .forms import ContactoForm, BarberoForm


class BarberoCreateView(generic.CreateView):
	model = Barbero	
	template_name = 'barberos/registrar-barbero.html'
	form_class = BarberoForm
	success_url = reverse_lazy('barberos:barberos')


class BarberoList(generic.ListView):
	model = Barbero
	context_object_name = "barberos"
	template_name = "barberos/listar_barberos.html"


class BarberoDetail(generic.DetailView):
	model = Barbero
	template_name = 'barberos/detalle_barbero.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		barbero = Barbero.objects.get(pk=self.object.pk)
		context['barbero'] = barbero
		context['contactos'] = Contacto.objects.filter(barbero=barbero)
		context['cuentas'] = Cuenta.objects.filter(barbero=barbero)
		return context

def crear_contacto(request, id_barbero):
	form = ContactoForm(request.POST or None)
	barbero = Barbero.objects.get(pk=id_barbero)
	context = {'form': form, 'barbero':barbero}
	
	if request.method == 'POST':
		if form.is_valid():
			numero = request.POST.get('numero')
			contacto = Contacto.objects.create(numero=numero, barbero=barbero)
			return HttpResponseRedirect(reverse_lazy('barberos:barberos'))
	else:
		form = ContactoForm()

	return render(request, 'barberos/contacto_form.html', context)


class ContactoUpdate(generic.UpdateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'barberos/contacto_form.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:barberos')


class ContactoDelete(generic.DeleteView):
	model = Contacto
	template_name = 'barberos/eliminar_contacto.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:barberos')	