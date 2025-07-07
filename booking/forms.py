from django import forms
from booking.models import Booking


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control mb-2'

    class Meta:
        model = Booking
        fields = ('name', 'email', 'date_in', 'date_out', 'phone')
        labels = {
            'name': 'ПІБ', 'email': 'Почта', 'phone': 'Мобільний телефон', 'date_in': 'Дата заїзду', 'date_out': 'Дата виїзду',
        }
        widgets = {
           'date_in': forms.DateTimeInput(attrs={'type': "datetime-local"}),
           'date_out': forms.DateTimeInput(attrs={'type': "datetime-local"}),
        }