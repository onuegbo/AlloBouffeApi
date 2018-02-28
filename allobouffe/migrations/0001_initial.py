# Generated by Django 2.0.2 on 2018-02-26 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='nourritures/')),
                ('name', models.CharField(max_length=128)),
                ('delivery_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurants/')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('addresse', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('telephone', models.IntegerField(default=0)),
                ('is_hidden', models.BooleanField(default=False)),
                ('created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'restaurant',
                'ordering': ['created'],
                'verbose_name_plural': 'restaurants',
                'db_table': 'restaurant',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='allobouffe.Restaurant'),
        ),
    ]