# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-25 21:54
from __future__ import unicode_literals

from django.db import migrations
import datetime

def update_old_rounds(apps, schema_editor):
    # Get models
    RoundPage = apps.get_model('home.RoundPage')
    rounds = RoundPage.objects.all()
    for r in rounds:
        r.tax_form_deadline = r.internstarts + datetime.timedelta(days=12)
        r.initial_payment_date = r.initialfeedback + datetime.timedelta(days=30)
        r.midpoint_payment_date = r.midfeedback + datetime.timedelta(days=30)
        r.final_payment_date = r.finalfeedback + datetime.timedelta(days=30)
        r.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0172_auto_20191125_2153'),
    ]

    operations = [
        migrations.RunPython(update_old_rounds),
    ]