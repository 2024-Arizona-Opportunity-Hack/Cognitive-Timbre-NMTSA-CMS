from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, MultipleChooserPanel, InlinePanel, PageChooserPanel
from wagtail.fields import RichTextField
from wagtail.models import ParentalKey, Orderable, Page
from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail.snippets.models import register_snippet
import GDriveManager.gdrive_sharing as gdrive

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.file_id})"


class FileChooserViewSet(ChooserViewSet):
    model = File

    icon = "file"
    choose_one_text = "Choose a file"
    choose_another_text = "Choose another file"
    edit_item_text = "Edit this file"

    def get_object_list(self):
        # Refresh the files before returning the queryset
        print("Refreshing files")
        gdrive.refresh_files()

        queryset = File.objects.all()

        return queryset

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
            'g_drive_page_files', label="GDrive File", chooser_field_name="file"
        ),
        InlinePanel('g_drive_groups', label="GDrive Groups"),
    ]


class GDriveGroup(Orderable):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(GDrivePage, on_delete=models.CASCADE, related_name='g_drive_groups')
    group = models.ForeignKey(
        'auth.Group',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel('group'),
    ]


class GDrivePageFile(Orderable):
    id = models.AutoField(primary_key=True)
    page = ParentalKey(GDrivePage, on_delete=models.CASCADE, related_name='g_drive_page_files')
    file = models.ForeignKey(
        'GDriveManager.File', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('file'),
    ]