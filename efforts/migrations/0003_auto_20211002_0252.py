# Generated by Django 3.1.7 on 2021-10-02 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0002_auto_20211002_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='efforts.employee', verbose_name='上级'),
        ),
    ]