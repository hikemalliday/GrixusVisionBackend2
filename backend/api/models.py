from django.db import models

class CharInventory(models.Model):
    char_name = models.TextField(blank=True, null=True)
    char_guild = models.TextField(blank=True, null=True)
    item_name = models.TextField(blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True)
    item_location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'char_inventory'
