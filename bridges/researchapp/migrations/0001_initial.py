

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productsapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

            ],
            options={

            },
        ),
        migrations.CreateModel(
            name='SubjectOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='предмет исследования')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Предмет исследование',
                'verbose_name_plural': 'Предметы исследований',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),

            ],
            options={
                'verbose_name': 'Документ и исследование',
                'verbose_name_plural': 'Документы и исследования',
            },
        ),
    ]
