# Generated by Django 3.1.2 on 2020-11-02 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partner_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='address',
            field=models.CharField(max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='contact',
            field=models.CharField(max_length=50, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(verbose_name='상세 소개'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=50, verbose_name='업체 이름'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.partner')),
            ],
        ),
    ]
