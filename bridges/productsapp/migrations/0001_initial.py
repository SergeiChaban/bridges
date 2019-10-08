

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название материала')),
                ('slug', models.SlugField(max_length=500, unique=True, verbose_name='слаг')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),

                ('description', models.TextField(blank=True, verbose_name='описание материала')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='категория материала')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория материала',
                'verbose_name_plural': 'Категории материалов',
            },
        ),
        migrations.CreateModel(
            name='MeasureTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28, unique=True, verbose_name='единица измерения')),
                ('shortcut', models.CharField(max_length=10, unique=True, verbose_name='ед.изм.')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='TechnicalSolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название материала')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='слаг')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),

                ('description', models.TextField(blank=True, verbose_name='описание материала')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('material_content', models.ManyToManyField(to='productsapp.Material')),
            ],
            options={
                'verbose_name': 'Техническое решение',
                'verbose_name_plural': 'Технические решения',
            },
        ),
        migrations.CreateModel(
            name='TechnicalSolutionsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_desc', models.CharField(blank=True, max_length=128, verbose_name='alt фотографии')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Фотография')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('material', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='productsapp.TechnicalSolutions')),
            ],
            options={
                'verbose_name': 'Фотография технического решения',
                'verbose_name_plural': 'Фотографии технических решений',
            },
        ),
        migrations.CreateModel(
            name='MaterialImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_desc', models.CharField(blank=True, max_length=128, verbose_name='alt фотографии')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Фотография')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('material', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='productsapp.Material')),
            ],
            options={
                'verbose_name': 'Фотография материаллов',
                'verbose_name_plural': 'Фотографии материаллов',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.MaterialCategory', verbose_name='категория материала'),
        ),
        migrations.AddField(
            model_name='material',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.MeasureTypes', verbose_name='Единица измерения'),
        ),
    ]
