from django.shortcuts import render
from django.views import generic


class IndexView(generic.View):
	def get(self, request):
		return render(request, "web/index.html")
