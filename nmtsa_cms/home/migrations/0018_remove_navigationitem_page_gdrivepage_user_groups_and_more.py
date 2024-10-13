# Generated by Django 4.2.16 on 2024-10-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0017_merge_20241013_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigationitem',
            name='page',
        ),
        migrations.AddField(
            model_name='gdrivepage',
            name='user_groups',
            field=models.ManyToManyField(blank=True, help_text='Select user groups that can access this page', related_name='gdrive_pages', to='auth.group'),
        ),
        migrations.DeleteModel(
            name='AddPage',
        ),
        migrations.DeleteModel(
            name='NavigationItem',
        ),
    ]