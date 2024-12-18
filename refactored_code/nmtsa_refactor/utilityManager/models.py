from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
# Create your models here.

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