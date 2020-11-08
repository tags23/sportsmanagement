from django.db import models


class User(models.Model):
    # FYI, a separate id field does not have to be defined, models interface does it on its own:
    # https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fields

    name = models.CharField(max_length=200, blank=False, null=True)
    surname = models.CharField(max_length=200, blank=False, null=True)
    phone = models.CharField(max_length=10, blank=False, null=True)
    qualification = models.CharField(max_length=100)
    username = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    user_type = models.CharField(max_length=100, blank=False, null=True)
    password = models.CharField(max_length=100, blank=False, null=True)
    created_at = models.DateTimeField(blank=False, null=True)
    updated_at = models.DateTimeField(blank=False, null=True)
    deleted_at = models.DateTimeField(blank=False, null=True)
    remember_token = models.CharField(max_length=100, blank=False, null=True)  # a boolean, maybe?


class Competition(models.Model):
    address = models.CharField(max_length=200, blank=False, null=True)
    date = models.DateField(blank=False, null=True)
    time = models.TimeField(blank=False, null=True)
    sport = models.CharField(max_length=100, blank=False, null=True)
    comp_format = models.CharField(max_length=100, blank=False, null=True)
    comp_name = models.CharField(max_length=200, blank=False, null=True)
    no_of_participants = models.IntegerField()


class CompType(models.Model):  # type...?
    # v_id = models.CharField(max_length=200, blank=False, null=True)
    comp_id = models.ForeignKey(to=Competition, blank=False, null=True, on_delete=models.SET_NULL)  # is set null valid?
    created_at = models.DateTimeField(blank=False, null=True)
    updated_at = models.DateTimeField(blank=False, null=True)


class Participant(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    surname = models.CharField(max_length=200, blank=False, null=True)
    phone = models.CharField(max_length=10, blank=False, null=True)
    gender = models.CharField(max_length=1, blank=False, null=True)
    status = models.CharField(max_length=200, blank=False, null=True)


class Result(models.Model):
    # Sacensību versijas ID
    comp_type_id = models.ForeignKey(to=CompType, blank=False, null=True, on_delete=models.SET_NULL)
    p1_result = models.IntegerField(blank=False, null=True)
    p2_result = models.IntegerField(blank=False, null=True)
    p1 = models.ForeignKey(to=Participant, on_delete=models.SET_NULL, blank=False, null=True, related_name='p1')
    p2 = models.ForeignKey(to=Participant, on_delete=models.SET_NULL, blank=False, null=True, related_name='p2')
    notes = models.TextField()


class PasswordResets(models.Model):
    user = models.ForeignKey(to=User, blank=False, null=True, on_delete=models.SET_NULL)
    password_token = models.CharField(max_length=200, blank=False, null=True)
    created_at = models.DateTimeField(blank=False, null=True)


class OrgUser(models.Model):
    user_id = models.ForeignKey(to=User, blank=False, null=True, on_delete=models.SET_NULL)
    comp_id = models.ForeignKey(to=Competition, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(blank=False, null=True)
