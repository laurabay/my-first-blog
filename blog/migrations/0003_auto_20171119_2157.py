# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171119_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='paginas',
            new_name='fecha_publicacion',
        ),
    ]
