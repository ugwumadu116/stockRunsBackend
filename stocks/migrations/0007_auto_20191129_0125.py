# Generated by Django 2.2.7 on 2019-11-29 00:25

from django.db import migrations, models
import stocks.models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_mystockfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystockfile',
            name='file',
            field=models.FileField(storage=stocks.models.OverwriteStorage(), upload_to='C:\\Users\\ugwum\\Desktop\\DECAGON\\challenge\\PYTHON\\personalProjects\\stock_run_backend\\stockRunsBackend\\media', verbose_name='stockfilename'),
        ),
    ]
