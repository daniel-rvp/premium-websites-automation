from django.db import models

from questionnaire.models import User

# Create your models here.
class Home(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    hero_title = models.TextField()
    hero_subtitutle = models.TextField()
    hero_image = models.TextField()
    intro_title = models.TextField()
    intro_subtitle = models.TextField()
    intro_image = models.TextField()
    amenities_gallery_title = models.TextField()
    amenities_gallery_subtitle = models.TextField()
    activities_subtitle = models.TextField()
    activities_image = models.TextField()
    amenities_subtitle = models.TextField()
    rules_subtitle = models.TextField()
    rules_image = models.TextField()
    rule_check_in_out_time = models.TextField()
    rule_quiet_time = models.TextField()
    rule_campfire = models.TextField()
    rule_pets = models.TextField()
    rule_wifi = models.TextField()
    cta_title = models.TextField()
    cta_subtitle = models.TextField()
    attractions_subtitle = models.TextField


class HomeHeroAmenity(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    title = models.TextField()


class HomeGalleryAmenity(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    title = models.TextField()
    image_url = models.TextField()
    image_alt = models.TextField()


class HomeActivity(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    title = models.TextField()
    icon = models.TextField()


class HomeAmenity(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image_url = models.TextField()
    image_alt = models.TextField()


class HomeAttraction(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image_url = models.TextField()
    image_alt = models.TextField()
    distance = models.TextField()