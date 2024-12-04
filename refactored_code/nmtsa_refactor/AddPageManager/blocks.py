from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock  # For embedding documents


class TextBlock(blocks.RichTextBlock):
    class Meta:
        label = "Text Block"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        label = "Image Block"


class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, max_length=50)
    button_url = blocks.URLBlock(required=True)

    class Meta:
        label = "Button Block"


# Change the 'VideoBlock' to 'EmbedBlock' for embedding videos
class EmbedBlock(blocks.StructBlock):
    embed_url = blocks.URLBlock(help_text="Embed URL for the video or content")
    embed_title = blocks.CharBlock(required=False, help_text="Optional title for the embed")

    class Meta:
        label = "Embed Block"


# BlogPostBlock for individual blog posts
class BlogPostBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=250, help_text="Title of the blog post")
    intro = blocks.TextBlock(help_text="Short introduction or summary of the blog post")
    date = blocks.DateBlock(help_text="Publication date")
    link = blocks.URLBlock(help_text="Link to the full blog post")

    class Meta:
        label = "Blog Post"


# BlogPostsBlock for multiple blog posts
class BlogPostsBlock(blocks.StructBlock):
    blog_posts = blocks.ListBlock(BlogPostBlock())

    class Meta:
        label = "Blog Posts"


# VideoPostsBlock for multiple video entries
class VideoPostsBlock(blocks.StructBlock):
    videos = blocks.ListBlock(EmbedBlock())  # Change from VideoBlock to EmbedBlock

    class Meta:
        label = "Video Posts"


# FileBlock for individual file entry
class FileBlock(blocks.StructBlock):
    file = DocumentChooserBlock()  # Corrected here to use DocumentChooserBlock
    description = blocks.CharBlock(max_length=250, required=False, help_text="Short description of the file")

    class Meta:
        label = "File Entry"


# FilesBlock for multiple files
class FilesBlock(blocks.StructBlock):
    files = blocks.ListBlock(FileBlock())

    class Meta:
        label = "Files List"


class ContentBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(form_classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    embed = EmbedBlock()  # Changed video block to embed block
    document = DocumentChooserBlock()

    # Added support for embed in nested content
    nested_content = blocks.StreamBlock([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),  # Embeds can now be included in nested content
        ('document', DocumentChooserBlock())
    ], max_num=10)

    class Meta:
        max_num = None
        label = "Content Block"
