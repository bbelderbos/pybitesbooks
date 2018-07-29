# Generated by Django 2.0.7 on 2018-07-29 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0008_auto_20180729_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BookNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='inserted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='inserted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='booknote',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AddField(
            model_name='booknote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
