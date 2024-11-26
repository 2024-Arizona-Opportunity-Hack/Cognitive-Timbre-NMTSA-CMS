# Generated by Django 4.2.16 on 2024-11-26 00:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('home', '0023_remove_file_url_file_file_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.CharField(blank=True, help_text='Short intro text', max_length=250)),
                ('body', wagtail.fields.StreamField([('text', 0), ('image', 3), ('button', 6), ('embed', 9), ('blog_posts', 16), ('video_posts', 18), ('files', 23), ('content', 28)], blank=True, block_lookup={0: ('home.blocks.TextBlock', (), {}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 2: ('wagtail.blocks.CharBlock', (), {'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 1), ('caption', 2)]], {}), 4: ('wagtail.blocks.CharBlock', (), {'max_length': 50, 'required': True}), 5: ('wagtail.blocks.URLBlock', (), {'required': True}), 6: ('wagtail.blocks.StructBlock', [[('button_text', 4), ('button_url', 5)]], {}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Embed URL for the video or content'}), 8: ('wagtail.blocks.CharBlock', (), {'help_text': 'Optional title for the embed', 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('embed_url', 7), ('embed_title', 8)]], {}), 10: ('wagtail.blocks.CharBlock', (), {'help_text': 'Title of the blog post', 'max_length': 250}), 11: ('wagtail.blocks.TextBlock', (), {'help_text': 'Short introduction or summary of the blog post'}), 12: ('wagtail.blocks.DateBlock', (), {'help_text': 'Publication date'}), 13: ('wagtail.blocks.URLBlock', (), {'help_text': 'Link to the full blog post'}), 14: ('wagtail.blocks.StructBlock', [[('title', 10), ('intro', 11), ('date', 12), ('link', 13)]], {}), 15: ('wagtail.blocks.ListBlock', (14,), {}), 16: ('wagtail.blocks.StructBlock', [[('blog_posts', 15)]], {}), 17: ('wagtail.blocks.ListBlock', (9,), {}), 18: ('wagtail.blocks.StructBlock', [[('videos', 17)]], {}), 19: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 20: ('wagtail.blocks.CharBlock', (), {'help_text': 'Short description of the file', 'max_length': 250, 'required': False}), 21: ('wagtail.blocks.StructBlock', [[('file', 19), ('description', 20)]], {}), 22: ('wagtail.blocks.ListBlock', (21,), {}), 23: ('wagtail.blocks.StructBlock', [[('files', 22)]], {}), 24: ('wagtail.blocks.CharBlock', (), {'form_classname': 'full title'}), 25: ('wagtail.blocks.RichTextBlock', (), {}), 26: ('wagtail.blocks.CharBlock', (), {}), 27: ('wagtail.blocks.StreamBlock', [[('heading', 26), ('paragraph', 25), ('image', 1), ('embed', 9), ('document', 19)]], {'max_num': 10}), 28: ('wagtail.blocks.StreamBlock', [[('heading', 24), ('paragraph', 25), ('image', 1), ('embed', 9), ('document', 19), ('nested_content', 27)]], {})}, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NavigationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('external_url', models.URLField(blank=True, verbose_name='External link')),
                ('css_class', models.CharField(blank=True, help_text='CSS class for this menu item', max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Navigation Item',
                'verbose_name_plural': 'Navigation Items',
                'ordering': ['order'],
            },
        ),
    ]