# Generated by Django 3.2.3 on 2021-06-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employes', to='employes.departement'),
        ),
    ]