from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from .blocks import TextBlock, ImageBlock, ButtonBlock, EmbedBlock, BlogPostsBlock, VideoPostsBlock, FilesBlock, ContentBlock

# Create your models here.
class AddPage(Page):  # Changed from ServicesPage to AddPage
    intro = models.CharField(max_length=250, blank=True, help_text="Short intro text")

    body = StreamField([
        ('text', TextBlock()),
        ('image', ImageBlock()),
        ('button', ButtonBlock()),
        ('embed', EmbedBlock()),
        ('blog_posts', BlogPostsBlock()),
        ('video_posts', VideoPostsBlock()),
        ('files', FilesBlock()),
        ('content', ContentBlock()),  # This is where ContentBlock can be added up to 10 times
    ], null=True, blank=True, max_num=10)  # Limit to 10 ContentBlock entries


    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        return context
