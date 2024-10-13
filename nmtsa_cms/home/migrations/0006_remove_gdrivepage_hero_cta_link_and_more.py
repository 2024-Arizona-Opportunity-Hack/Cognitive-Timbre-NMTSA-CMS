# Generated by Django 4.2.16 on 2024-10-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('home', '0005_file_gdrivepage_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gdrivepage',
            name='hero_cta_link',
        ),
        migrations.AddField(
            model_name='gdrivepage',
            name='hero_cta_links',
            field=models.ManyToManyField(blank=True, help_text='Choose pages to link to for the Call to Action', related_name='gdrive_pages_hero_cta_links', to='wagtailcore.page', verbose_name='Hero CTA links'),
        ),
    ]