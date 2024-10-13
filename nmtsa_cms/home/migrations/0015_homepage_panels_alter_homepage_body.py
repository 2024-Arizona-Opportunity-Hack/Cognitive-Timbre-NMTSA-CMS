# Generated by Django 4.2.16 on 2024-10-13 06:10

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_merge_20241013_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='panels',
            field=wagtail.fields.StreamField([('qualified_charitable', 6)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'max_length': 255, 'required': True}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 2: ('wagtail.blocks.RichTextBlock', (), {'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'max_length': 50, 'required': True}), 4: ('wagtail.blocks.PageChooserBlock', (), {'required': False}), 5: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter a hex color code (e.g., #FFFFFF for white)', 'max_length': 7, 'required': False}), 6: ('wagtail.blocks.StructBlock', [[('title', 0), ('image', 1), ('description', 2), ('cta_text', 3), ('cta_link', 4), ('background_color', 5)]], {})}, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]