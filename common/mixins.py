from django.http import HttpResponse
from django.urls import reverse


class LoginRedirect:

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous():
            return HttpResponse(reverse())
        return super().dispatch(request, *args, **kwargs)