# Generated by Django 3.2.3 on 2021-06-02 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=30)),
                ('etage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('ville', models.CharField(max_length=30)),
                ('poste', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('salaire', models.DecimalField(decimal_places=2, max_digits=12)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employes.departement')),
            ],
        ),
    ]
