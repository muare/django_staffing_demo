# Generated by Django 3.1.7 on 2021-10-05 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('efforts', '0003_auto_20211002_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effort',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='efforts', to='efforts.employee', verbose_name='员工'),
        ),
        migrations.AlterField(
            model_name='effort',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='efforts', to='efforts.project', verbose_name='项目'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='efforts.employee', verbose_name='上级'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='efforts.team', verbose_name='团队名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='efforts.customer', verbose_name='客户'),
        ),
        migrations.AlterField(
            model_name='project',
            name='product',
            field=models.ManyToManyField(related_name='projects', to='efforts.Product', verbose_name='产品'),
        ),
        migrations.AlterField(
            model_name='team',
            name='parent_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_teams', to='efforts.team', verbose_name='上级团队'),
        ),
    ]
