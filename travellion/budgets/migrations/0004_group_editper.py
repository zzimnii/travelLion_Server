# Generated by Django 4.0.4 on 2023-11-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0003_group_invite_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='editPer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
