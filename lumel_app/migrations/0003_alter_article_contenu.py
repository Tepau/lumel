# Generated by Django 5.0.4 on 2024-05-29 16:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumel_app', '0002_remove_article_test_field2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor.fields.RichTextField(),
        ),
    ]