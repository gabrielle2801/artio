from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtailvideos.blocks import VideoChooserBlock


class ContentPage(Page):
    body = StreamField([
        ('video', VideoChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]