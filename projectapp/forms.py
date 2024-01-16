from django  import forms
from .models import Booking,Contact
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
        widgets={
            'booking_date':
                DateInput()
        }
        labels={
               
        'p_name':'patient name:',
        'p_phone': 'phone number:',
        'p_email':'patient email:',
        'doc_name':'doctor name:',
        'booking_date':"booking date:",
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
       
        
        labels={
            'p_name':'patient name',
            'p_email':'patient email',
            'p_phone':'phone number',
            'p_message':'text message'
        }        