from datetime import timedelta, datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from booking.models import Booking


class BookingCreate(CreateView):
    model = Booking
    fields = ['name', 'date_from', 'date_to']
    success_url = reverse_lazy('booking_list')


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['name', 'date_from', 'date_to']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('booking_list')


class BookingDelete(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking_list')


class BookingListView(View):
    template_name = 'list.html'

    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, self.template_name, {'bookings': bookings})


class BookingApiView(View):
    def get(self, request):
        events = []

        try:
            start = request.GET.get("start").split("T")[0]
            start_date = datetime.strptime(start, "%Y-%m-%d")

            end = request.GET.get("end").split("T")[0]
            end_date = datetime.strptime(end, "%Y-%m-%d")

            bookings = Booking.objects.filter(Q(date_from__range=(start_date, end_date)) | Q(date_to__range=(start_date, end_date)))
        except Exception as ex:
            bookings = Booking.objects.all()

        for booking in bookings:
            events.append(dict(
                id=booking.id,
                title=booking.name,
                start=booking.date_from.strftime("%Y-%m-%d"),
                end=(booking.date_to + timedelta(days=1)).strftime("%Y-%m-%d"),
                url=reverse('booking_update', kwargs={'pk': booking.pk})
            ))
        return JsonResponse(events, safe=False)
