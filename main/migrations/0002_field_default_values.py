# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    # The PHP signup form complains if fields are not null and don't have
    # defaults. Django models don't do default db values. Hence this bodge.

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "alter table users alter column hackney set default false;"
        ),
        migrations.RunSQL(
            "alter table users alter column subscribed set default false;"
        ),
        migrations.RunSQL(
            "alter table users alter column subscription_period set default 0;"
        ),
        migrations.RunSQL(
            "alter table users alter column terminated set default false;"
        ),
        migrations.RunSQL(
            "alter table users alter column admin set default false;"
        ),
        migrations.RunSQL(
            "alter table users alter column has_profile set default false;"
        ),
        migrations.RunSQL(
            "alter table users alter column disabled_profile set default false;"
        ),
    ]
