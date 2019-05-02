from django.forms import ModelForm

from booking.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date_from', 'date_to']
