from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .models import Barbero, Contacto 
from .forms import ContactoForm, BarberoForm, UserForm


class BarberoCreateView(PermissionRequiredMixin,
						LoginRequiredMixin, 
						generic.CreateView):
	model = Barbero	
	template_name = 'barberos/form.html'
	form_class = BarberoForm
	second_form_class = UserForm
	permission_required = ('barberos.add_barbero',)
	success_url = reverse_lazy('barberos:index')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		if not 'barber_form' in context:
			context['barber_form'] = self.form_class
		
		if not 'user_form' in context:
			context['user_form'] = self.second_form_class

		return context

	def post(self, request):
		barber_form = self.form_class(request.POST)
		user_form = self.second_form_class(request.POST)	

		if barber_form.is_valid() and user_form.is_valid():
			usuario = user_form.save()
			barbero = barber_form.save(commit=False)
			barbero.usuario = usuario
			barbero.save()
			return HttpResponseRedirect(self.success_url)

		return render(request, 
					self.template_name, 
					{'user_form': user_form, 'barber_form': barber_form })	


class BarberoCambiarStatus(LoginRequiredMixin, 
							generic.View):

	def post(self, request, pk):
		barbero = get_object_or_404(Barbero, pk=pk)
		barbero.cambiar_status()
		return JsonResponse({'status': barbero.activo, 'pk': pk}, status=200)


class BarberoList(generic.ListView):
	model = Barbero
	context_object_name = "barberos"
	template_name = "barberos/listar.html"


class BarberoDetail(generic.DetailView):
	model = Barbero
	template_name = 'barberos/detalle.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		barbero = Barbero.objects.get(pk=self.object.pk)
		context['barbero'] = barbero
		context['contactos'] = barbero.contacto_set.all()
		context['cuentas'] = barbero.cuenta_set.all()
		return context


class BarberoDeleteView(generic.DeleteView):
	model = Barbero
	template_name = 'barberos/delete.html'
	context_object_name = 'barbero'
	success_url = reverse_lazy('barberos:index')

	def post(self, request, pk):
		barbero = Barbero.objects.get(pk=pk)
		usuario = User.objects.get(username=barbero.usuario)
		usuario.delete()
		barbero.delete()
		return HttpResponseRedirect(self.success_url)		


class ContactoCreateView(generic.CreateView):
	model = Contacto
	template_name = 'barberos/contacto_form.html'
	form_class = ContactoForm

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		if not 'form' in context:
			context['form'] = self.form_class

		return context

	def post(self, request, id_barbero):
		barbero = get_object_or_404(
				Barbero, 
				pk=id_barbero
			)

		form = self.form_class(request.POST)

		if form.is_valid():
			numero = request.POST.get('numero')
			contacto = Contacto.objects.create(numero=numero, barbero=barbero)
			return redirect(barbero)

		return render(request, self.template_name, {'form': form})	



class ContactoUpdate(generic.UpdateView):
	model = Contacto
	form_class = ContactoForm
	template_name = 'barberos/contacto_form.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:index')

	def post(self, request, pk):
		self.object = self.get_object

		form  = self.form_class(request.POST)
		if form.is_valid():
			contacto = get_object_or_404(Contacto, pk=pk)
			contacto.numero = request.POST.get('numero')
			contacto.save()
			return redirect(contacto.barbero)

		return self.form_invalid(self, form)


class ContactoDelete(generic.DeleteView):
	model = Contacto
	template_name = 'barberos/eliminar_contacto.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:index')	