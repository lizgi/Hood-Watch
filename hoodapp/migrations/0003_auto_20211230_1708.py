# Generated by Django 3.2.9 on 2021-12-30 14:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0002_auto_20211222_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='neighborhood',
            name='occupants_count',
        ),
        migrations.RemoveField(
            model_name='neighborhood',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='healthcenter_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='hood_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='police_hotline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='hoodapp.profile'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='location',
            field=models.CharField(max_length=60),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hoodapp.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hoodapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(null=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hoodapp.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='hoodapp.profile')),
            ],
        ),
    ]
