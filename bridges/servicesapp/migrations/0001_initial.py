

from django.db import migrations, models
import django.db.models.deletion
import servicesapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='категория услуги')),
                ('slug', models.SlugField(blank=True, max_length=154, unique=True, verbose_name='слаг')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория услуги',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название услуги')),
                ('slug', models.SlugField(max_length=154, unique=True, verbose_name='слаг')),
                ('image', models.ImageField(blank=True, upload_to=servicesapp.models.image_folder)),
                ('description', models.TextField(blank=True, verbose_name='описание услуги')),
                ('is_active', models.BooleanField(default=True, verbose_name='показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicesapp.ServiceCategory')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
