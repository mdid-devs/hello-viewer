from django.conf import settings as settings
import logging

log = logging.getLogger('rooibos')


def get_presentation_data(presentation, user):
    items = presentation.items.filter(hidden=False)
    data = []

    for item in items:
        fvs = item.get_fieldvalues(owner=user)
        slide = {'title': item.title,
                 'img_src': item.record.get_image_url(),
                 'thmb': item.record.get_thumbnail_url(),
                 'thmb_sq': item.record.get_square_thumbnail_url(),
                 'order': item.order}

        for value in fvs:
            slide[value.resolved_label] = value.value

        slide['metadata'] = [
            dict(label=value.resolved_label, value=value.value) for value in fvs
        ]

        if settings.DEBUG:
            log.debug('===========data===============')
            log.debug(data)

        data.append(slide)

    return data
