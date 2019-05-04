"""ternevej URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from booking.views import BookingApiView, BookingListView, BookingCreate, BookingUpdate, BookingDelete

urlpatterns = [
    path('', BookingListView.as_view(), name="booking_list"),
    path('booking/', BookingCreate.as_view(), name="booking_create"),
    path('booking/<pk>/', BookingUpdate.as_view(), name="booking_update"),
    path('booking/delete/<pk>/', BookingDelete.as_view(), name="booking_delete"),
    path('api/booking/', BookingApiView.as_view(), name="booking_api"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
