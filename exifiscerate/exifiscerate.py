import logging
import itertools
from exif import Image
from pelican import signals
from pelican.generators import (
    ArticlesGenerator,
    PagesGenerator
)
from pelican.settings import DEFAULT_CONFIG


logger = logging.getLogger(__name__)


def initialized(pelican):
    '''Initialize context settings:
        * allow for new exif tag values
        * specify exif tags to strip
        * specify exif tags to save
    '''
    pass


def strip_exif(generator, content, image):
    pass


def handle_image(generator, content):
    image = content.metadata.get('image', None)

    if image:
        if image.startswith('{photo}'):
            pass


def find_images(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in itertools.chain(generator.articles,
                                           generator.translations,
                                           generator.drafts):
                handle_image(generator, article)

        if isinstance(generator, PagesGenerator):
            for page in itertools.chain(generator.pages,
                                        generator.translations,
                                        generator.drafts):
                handle_image(generator, page)


def register():
    signals.initialized.connect(initialized)
    try:
        signals.all_generators_finalized.connect(find_images)
    except Exception as e:
        logger.exception('Plugin failed to execute: {}'.format(e))
