from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class QualifiedCharitableBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=False)
    description = blocks.RichTextBlock(required=True)
    cta_text = blocks.CharBlock(required=True, max_length=50)
    cta_link = blocks.PageChooserBlock(required=False)
    background_color = blocks.CharBlock(
        required=False,
        max_length=7,
        help_text="Enter a hex color code (e.g., #FFFFFF for white)"
    )

    class Meta:
        icon = 'edit'
        label = 'Qualified Charitable Organization Tax Credit'

