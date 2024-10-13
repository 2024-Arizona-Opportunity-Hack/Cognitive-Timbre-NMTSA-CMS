from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.documents.models import Document
from wagtail.search import index  # For search indexing
from wagtail.images.blocks import ImageChooserBlock  # For using images in StreamField
from wagtail import blocks  # Import blocks for StreamField usage
from .components.ContentPanelBlock import QualifiedCharitableBlock, CorporateSponsorsBlock


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]


class TherapyPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    testimonials = StreamField([
        ('testimonial', blocks.RichTextBlock()),  # Use blocks.RichTextBlock() for StreamField
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('testimonials'),
    ]


class PostPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]


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
    
    def get_context(self, request):
        context = super().get_context(request)
        services_page = ServicesPage.objects.live().first()

        if services_page:
            print(f"DEBUG: Found ServicesPage: {services_page.title}")
        else:
            print("DEBUG: No ServicesPage found")

        context['services_page'] = services_page
        return context


class ServicesPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    blog_section = models.CharField(
        max_length=250, blank=True, help_text="Blog section intro text"
    )
    resources_section = models.CharField(
        max_length=250, blank=True, help_text="Resources section intro text"
    )
    therapy_section = models.CharField(
        max_length=250, blank=True, help_text="Therapy section intro text"
    )

    service_name = models.CharField(max_length=250)
    service_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        MultiFieldPanel(
            [
                FieldPanel("blog_section"),
                FieldPanel("resources_section"),
                FieldPanel("therapy_section"),
            ],
            heading="Service Sections"
        ),
        FieldPanel('service_name'),
        FieldPanel('service_description'),
        FieldPanel('body')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blogposts'] = BlogPage.objects.live().order_by('-date')[:5]
        context['therapy_posts'] = TherapyPage.objects.live().order_by('-date')[:5]
        context['document_list'] = Document.objects.all()
        context['other_posts'] = PostPage.objects.live().order_by('-date')[:5]
        return context
