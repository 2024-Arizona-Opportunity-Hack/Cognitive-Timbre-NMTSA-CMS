from django.db import models

from wagtail.models import Page, ParentalKey, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, MultipleChooserPanel
from django.conf import settings
from django.core.exceptions import ValidationError
from django import forms

class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel('body'),
    ]
    
class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
class FileChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "home.File"

    icon = "file"
    choose_one_text = "Choose a file"
    choose_another_text = "Choose another file"
    edit_item_text = "Edit this file"
    # form_fields = ["name", "url"]  # fields to show in the "Create" tab

file_chooser_viewset = FileChooserViewSet("file_chooser")
    
class GDrivePage(Page):
    # add the Hero section of HomePage:
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)
    
    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel('body'),
        MultipleChooserPanel(
            'g_drive_page_files', label="GDrive files", chooser_field_name="file"
        ),
    ]
            
class GDrivePageFile(Orderable):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(GDrivePage, on_delete=models.CASCADE, related_name='g_drive_page_files')
    file = models.ForeignKey(
        'home.File', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('file'),
    ]