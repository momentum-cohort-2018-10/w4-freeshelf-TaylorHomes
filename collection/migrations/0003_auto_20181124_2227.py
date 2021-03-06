# Generated by Django 2.1.3 on 2018-11-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20181121_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='css',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='javascript',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='templates/'),
        ),
        migrations.AddField(
            model_name='book',
            name='python',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
