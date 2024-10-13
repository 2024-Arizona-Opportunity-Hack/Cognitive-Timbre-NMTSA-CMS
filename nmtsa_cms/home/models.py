from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.fields import RichTextField
from .blocks import TextBlock, ImageBlock, ButtonBlock, EmbedBlock, BlogPostsBlock, VideoPostsBlock, FilesBlock, ContentBlock  # Import your custom blocks
from .components.ContentPanelBlock import QualifiedCharitableBlock
class HomePage(Page):
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
        max_length=255,
        help_text="Write an introduction for the site"
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

    panels = StreamField([
        ('qualified_charitable', QualifiedCharitableBlock()),
    ], null=True, blank=True)

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
        FieldPanel('panels'),
    ]
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


from wagtail.snippets.models import register_snippet

@register_snippet
class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    external_url = models.URLField("External link", blank=True)
    css_class = models.CharField(max_length=100, blank=True, help_text="CSS class for this menu item")
    order = models.IntegerField(default=0)

    panels = [
        FieldPanel('title'),
        PageChooserPanel('page'),
        FieldPanel('external_url'),
        FieldPanel('css_class'),
        FieldPanel('order'),
    ]

    def __str__(self):
        return self.title

    @property
    def link(self):
        if self.page:
            return self.page.url
        elif self.external_url:
            return self.external_url
        return '#'

    class Meta:
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"
        ordering = ['order']