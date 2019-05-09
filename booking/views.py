import random
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

        colors = [
            "#e6194B",
            "#3cb44b",
            "#ffe119",
            "#4363d8",
            "#f58231",
            "#911eb4",
            "#42d4f4",
            "#f032e6",
            "#bfef45",
            "#fabebe",
            "#469990",
            "#e6beff",
            "#9A6324",
            "#fffac8",
            "#800000",
            "#aaffc3",
            "#808000",
            "#ffd8b1",
            "#000075",
            "#a9a9a9",
            "#ffffff",
            "#000000"
        ]

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
                url=reverse('booking_update', kwargs={'pk': booking.pk}),
                color=random.choice(colors)
            ))
        return JsonResponse(events, safe=False)
