from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class BarberoBasicMixin(LoginRequiredMixin,
						PermissionRequiredMixin):
	pass