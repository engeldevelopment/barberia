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
		context['contactos'] = barbero.contacto_set.all()
		context['cuentas'] = barbero.cuenta_set.all()
		return context


def crear_contacto(request, id_barbero):
	barbero = Barbero.objects.get(pk=id_barbero)
	
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			numero = request.POST.get('numero')
			contacto = Contacto.objects.create(numero=numero, barbero=barbero)
			return HttpResponseRedirect(reverse_lazy('barberos:barberos'))

	form = ContactoForm(request.GET)

	return render(request, 'barberos/contacto_form.html', {'form': form})


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