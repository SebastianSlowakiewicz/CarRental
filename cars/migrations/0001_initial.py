# Generated by Django 5.1.6 on 2025-03-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('engine_type', models.CharField(choices=[('benzyna', 'Benzynowy'), ('diesel', 'Diesel'), ('elektryk', 'Elektryczny'), ('hybryda', 'Hybrydowy')], max_length=50)),
                ('gearbox_type', models.CharField(choices=[('manual', 'manualna'), ('automat', 'automatyczna')], max_length=50)),
                ('engine_power', models.PositiveSmallIntegerField()),
                ('engine_capacity', models.PositiveSmallIntegerField()),
                ('seats_count', models.PositiveSmallIntegerField()),
                ('doors_count', models.PositiveSmallIntegerField()),
                ('trunk_capacity', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('body_type', models.CharField(choices=[('hatchback', 'hatchback'), ('sedan', 'sedan'), ('combi', 'combi'), ('suv', 'SUV')], max_length=50)),
                ('category', models.CharField(choices=[('a', 'małe i mini'), ('b', 'miejskie'), ('c', 'kompaktowe'), ('d', 'rodzinne'), ('e', 'limuzyny'), ('f', 'luksusowe'), ('g', 'sportowe'), ('k', 'kabriolety'), ('i', 'terenowe'), ('m', 'van')], max_length=50)),
                ('fuel_usage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mileage_limit', models.PositiveIntegerField()),
                ('value', models.PositiveBigIntegerField()),
                ('availability', models.BooleanField()),
                ('insurance_expiry_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('equipment', models.ManyToManyField(to='cars.equipment')),
            ],
        ),
    ]
