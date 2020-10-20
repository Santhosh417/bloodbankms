from django.db import models
from users.models import Staff, Donor, Recipient

class BloodInventory(models.Model):
    blood_bag_num = models.AutoField(primary_key=True)
    blood_type = models.CharField(max_length=5)
    date_of_donation = models.DateField(blank=True, null=True)
    donor = models.ForeignKey(Donor, on_delete=models.DO_NOTHING, related_name='blood_donor')
    recipient = models.ForeignKey(Recipient, on_delete=models.DO_NOTHING, related_name='blood_recipient', blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, related_name='blood_staff')
    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

    def __str__(self):
        return self.blood_type
