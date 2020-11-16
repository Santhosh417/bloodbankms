from django.db import models
from users.models import Staff, Donor, Recipient
from django.urls import reverse

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.DO_NOTHING, related_name='appointment_donor', blank=False)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='appointment_staff')

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('inventory:appointment_detail', args=[str(self.id)])

class BloodInventory(models.Model):
    blood_bag_num = models.AutoField(primary_key=True)
    blood_type = models.CharField(max_length=5)
    date_of_donation = models.DateField(blank=False)
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING, related_name='blood_appointment', blank=False)
    recipient = models.ForeignKey(Recipient, on_delete=models.DO_NOTHING, related_name='blood_recipient', blank=True, null=True )
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='blood_staff')

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.blood_type

    def get_absolute_url(self):
        return reverse('inventory:inventory_detail', args=[str(self.blood_bag_num)])


