from django.contrib import admin
from . models import Department,Doctors,Booking,Contact

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=("id",'p_name','p_phone','doc_name','booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)
class contactAdmin(admin.ModelAdmin):
    list_display=("id",'p_name','p_email','p_message','contact_on')
admin.site.register(Contact)