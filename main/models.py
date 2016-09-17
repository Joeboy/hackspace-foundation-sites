from __future__ import unicode_literals

from django.db import models


class Alias(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    type = models.IntegerField()

    class Meta:
        db_table = 'aliases'


class Card(models.Model):
    uid = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey('User')
    added_date = models.DateTimeField()
    active = models.BooleanField()

    class Meta:
        db_table = 'cards'


class Interest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('InterestCategory', db_column='category')
    suggested = models.BooleanField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'interests'


class InterestCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'interests_categories'


class Learning(models.Model):
    learning_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'learnings'


class Location(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'locations'


class PasswordReset(models.Model):
    key = models.TextField(primary_key=True)
    user = models.ForeignKey('User')
    expires = models.DateTimeField()

    class Meta:
        db_table = 'password_resets'


class Permission(models.Model):
    perm_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'perms'


class ProjectStates(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'project_states'


class Project(models.Model):
    user = models.ForeignKey('User')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    state = models.ForeignKey(ProjectStates)
    location = models.ForeignKey(Location)
    location_name = models.CharField(db_column='location', max_length=255, blank=True, null=True)
    updated_date = models.DateTimeField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    contact = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'projects'


class ProjectLog(models.Model):
    timestamp = models.IntegerField()
    project = models.ForeignKey(Project)
    user = models.ForeignKey('User', blank=True, null=True)
    details = models.CharField(max_length=255)

    class Meta:
        db_table = 'projects_logs'


class Subscription(models.Model):
    user = models.ForeignKey('User')
    transaction = models.ForeignKey('Transaction')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'subscriptions'


class Transaction(models.Model):
    fit_id = models.TextField(unique=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey('User')
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'transactions'


class UserPermission(models.Model):
    perm = models.ForeignKey(Permission)
    user = models.ForeignKey('User')

    class Meta:
        db_table = 'userperms'


class User(models.Model):
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    subscribed = models.BooleanField(default=False)
    bankhash = models.TextField(blank=True, null=True)
    creationdate = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hackney = models.BooleanField(default=False)
    subscription_period = models.IntegerField(default=0)
    nickname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    irc_nick = models.CharField(unique=True, max_length=255, blank=True, null=True)
    gladosfile = models.CharField(max_length=255, blank=True, null=True)
    terminated = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    has_profile = models.BooleanField(default=False)
    disabled_profile = models.BooleanField(default=False)
    doorbot_timestamp = models.DateTimeField(blank=True, null=True)
    emergency_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_phone = models.CharField(max_length=40, blank=True, null=True)
    ldapuser = models.CharField(unique=True, max_length=32, blank=True, null=True)
    ldapnthash = models.CharField(max_length=32, blank=True, null=True)
    ldapsshahash = models.CharField(max_length=38, blank=True, null=True)
    ldapshell = models.CharField(max_length=32, blank=True, null=True)
    ldapemail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'users'


class UserAlias(models.Model):
    user = models.ForeignKey(User)
    alias = models.ForeignKey(Alias)
    username = models.CharField(max_length=255)

    class Meta:
        db_table = 'users_aliases'
        unique_together = (('user', 'alias'),)


class UserInterest(models.Model):
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)

    class Meta:
        db_table = 'users_interests'
        unique_together = (('user', 'interest'),)


class UserLearning(models.Model):
    user = models.ForeignKey(User)
    learning = models.ForeignKey(Learning)

    class Meta:
        db_table = 'users_learnings'
        unique_together = (('user', 'learning'),)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    allow_email = models.BooleanField()
    allow_doorbot = models.BooleanField()
    photo = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'users_profiles'
