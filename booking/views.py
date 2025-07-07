from django.shortcuts import redirect, render, get_object_or_404

from booking.models import Room, Booking
from booking.forms import BookingForm
# Create your views here.
def main_page(request):
    rooms = Room.objects.all()

    context = {
        "data": "Привіт з джанго!",
        "room_list": rooms
    }

    return render(request, "booking/room_list.html", context)


def booking_page(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = BookingForm()

    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect('main')

    context = {
        "room": room,
        "form": form,
    }

    return render(request, 'booking/booking_page.html', context)



