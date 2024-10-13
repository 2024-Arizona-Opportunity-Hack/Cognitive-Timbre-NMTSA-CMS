# content_panels.py

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class QualifiedCharitableBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=False)
    description = blocks.RichTextBlock(required=True)
    cta_text = blocks.CharBlock(required=True, max_length=50)
    cta_link = blocks.PageChooserBlock(required=False)

    class Meta:
        icon = 'edit'
        label = 'Qualified Charitable Organization Tax Credit'

class CorporateSponsorsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=False)
    description = blocks.RichTextBlock(required=True)
    items = blocks.ListBlock(blocks.CharBlock())
    cta_text = blocks.CharBlock(required=True, max_length=50)
    cta_link = blocks.PageChooserBlock(required=False)

    class Meta:
        icon = 'edit'
        label = 'Corporate Sponsors'