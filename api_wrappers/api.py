import logging
from urllib.parse import urljoin
from requests import Session

from .resource import Resource


logger = logging.getLogger(__name__)


class Api:

    resources = {
        'self': '',
        'latest': 'latest',
        'fluctuation': 'fluctuation',
    }
    resource_class = Resource

    def __init__(self, base_url, verify=None, auth=None):
        self.session = Session()
        self.base_url = base_url

        if verify is not None:
            self.session.verify = verify

    def __getitem__(self, item):
        if item in self.resources:
            resource_uri = self.resources[item]
            logger.debug(
                'Resource %r found in resources dict: %r',
                item,
                resource_uri
            )
        else:
            resource_uri = item
            logger.debug(
                'Resource %r not found in resources dict, using as URL part',
                item
            )
        url = urljoin(self.base_url, resource_uri)
        return self.resource_class(base_url=url, session=self.session,)
