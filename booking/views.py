from django.shortcuts import render
from django.views import View

from booking.forms import BookingForm


class BookingView(View):
    template_name = 'booking.html'

    def get(self, request):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})
