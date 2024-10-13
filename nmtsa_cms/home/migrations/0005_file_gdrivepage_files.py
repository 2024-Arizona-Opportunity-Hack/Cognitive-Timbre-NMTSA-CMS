# Generated by Django 4.2.16 on 2024-10-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_gdrivepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('file', 'File'), ('folder', 'Folder')], default='file', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='gdrivepage',
            name='files',
            field=models.ManyToManyField(blank=True, help_text='Select files to be associated with this page', related_name='gdrive_pages', to='home.file'),
        ),
    ]