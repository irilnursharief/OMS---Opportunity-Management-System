# Generated by Django 4.2.5 on 2025-07-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='capabilites/')),
            ],
            options={
                'verbose_name_plural': 'Capabilites',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('newsletter_opt_in', models.BooleanField(default=False)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_title', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_company', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_logo', models.ImageField(blank=True, null=True, upload_to='testimonials/logos/')),
            ],
            options={
                'ordering': ['customer_name'],
            },
        ),
    ]
