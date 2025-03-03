# Generated by Django 4.2.4 on 2023-10-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='copper_username',
            field=models.CharField(blank=True, null=True, verbose_name='Nombre de usuario en Coppermind'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='universe',
            field=models.ManyToManyField(blank=True, related_name='user_universe', to='login_app.universe', verbose_name='Universo'),
        ),
    ]
