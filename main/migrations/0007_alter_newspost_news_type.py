# Generated by Django 4.1.7 on 2023-03-31 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_newspost_body_alter_person_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='news_type',
            field=models.CharField(choices=[('primary', 'Video'), ('secondary', 'Foto'), ('triary', 'Qonunchilik')], max_length=255),
        ),
    ]
