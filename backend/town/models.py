from django.db import models


# Create your models here.
class Town(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    area = models.ForeignKey("user.Area", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="town/", null=True)
    area_welfare = models.FloatField(default=0, null=True)
    town_welfare = models.FloatField(default=0, null=True)
    town_culture = models.FloatField(default=0, null=True)
    town_facility = models.FloatField(default=0, null=True)
    town_citizen = models.FloatField(default=0, null=True)
    advantage = models.TextField(null=True)
    disadvantage = models.TextField(null=True)
    star = models.FloatField(default=0, null=True)
    update_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "Town"

    def __str__(self):
        return self.name


class Town_Review(models.Model):
    id = models.AutoField(primary_key=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    content = models.TextField(null=True)
    area_welfare = models.FloatField(null=True)
    town_welfare = models.FloatField(null=True)
    town_culture = models.FloatField(null=True)
    town_facility = models.FloatField(null=True)
    town_citizen = models.FloatField(null=True)
    advantage = models.TextField(null=True)
    disadvantage = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Town_Review"
