from home.models import file_chooser_viewset

FileChooserBlock = file_chooser_viewset.get_block_class(
    name="FileChooserBlock", module_path="nmtsa_cms.blocks"
)