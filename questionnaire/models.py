import requests

from django.contrib.auth.models import AbstractUser

from django.db import models

from rest_framework.authtoken.models import Token

from ._questions import QUESTIONS

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="client_set", # Unique related_name for Client's groups
        related_query_name="client",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="client_permissions_set", # Unique related_name for Client's user_permissions
        related_query_name="client_permission",
    )

    def get_my_token(self):
        return Token.objects.get_or_create(user=self)

    my_token = property(get_my_token)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new_instance = self.pk is None

        super().save(*args, **kwargs)

        if is_new_instance:
            self.domain = f"{self.name}.surge.sh"

            self.set_password(self.password)
            super().save(update_fields=['domain', 'password'])

            Token.objects.get_or_create(user=self)

            new_questionnaire = PremiumWebsiteForm(camp=self)
            new_questionnaire.save()

            for id, question in QUESTIONS.items():
                new_q_and_a = QandA(
                    type=id,
                    question=question,
                    questionnaire=new_questionnaire
                )
                new_q_and_a.save()

            print(self.my_token)

            response = requests.post(
                url='https://bmlrxdnnxhawrhncbvoz.supabase.co/rest/v1/clients',
                headers={
                    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtbHJ4ZG5ueGhhd3JobmNidm96Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTU1Mjc4NSwiZXhwIjoyMDY1MTI4Nzg1fQ.nxB9n8R4OjPaAdCYc8CooJYfx5OVLxcs_Xs3ZKW295I',
                    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtbHJ4ZG5ueGhhd3JobmNidm96Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTU1Mjc4NSwiZXhwIjoyMDY1MTI4Nzg1fQ.nxB9n8R4OjPaAdCYc8CooJYfx5OVLxcs_Xs3ZKW295I'
                },
                data={
                    'name': self.name,
                    'phone': self.phone,
                    'address': self.address,
                    'state': self.state,
                    'domain': self.domain,
                    'token': self.my_token[0].key
                }
            )

            return self


class PremiumWebsiteForm(models.Model):
    camp = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.camp.name


class QandA(models.Model):
    type = models.CharField(max_length=2, null=True)
    question = models.TextField()
    answer = models.TextField()
    checked = models.BooleanField(default=False)
    questionnaire = models.ForeignKey(PremiumWebsiteForm, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question #{self.type} for {self.questionnaire}'