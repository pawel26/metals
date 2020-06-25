"""
Tests for API resource wrapper
"""
from datetime import date, datetime
import pickle
import pytz
from six.moves.urllib.parse import urljoin

from api_wrappers.resource import Resource


class ResourceTestCase:
    """
    Test resource wrapper
    """
    base_url = 'http://httpbin.org'

    def test_pickling_resource_object(self):
        """
        Check if simple resource object can be pickled and unpickled
        """
        resource = Resource(self.base_url)
        pickled_resource = pickle.dumps(resource)
        unpickled_resource = pickle.loads(pickled_resource)

        assert resource.url == unpickled_resource.url

    def test_get(self):
        """
        Check if GET requests are possible
        """
        url = urljoin(self.base_url, '/get')
        response = Resource(url).get()

        assert 200 == response.status_code
        assert url ==response.json()['url']

    def test_post(self):
        """
        Check, if POST is possible
        """
        url = urljoin(self.base_url, '/post')
        response = Resource(url).post(data={})

        assert 200 == response.status_code
        assert url == response.json()['url']

    def test_default_serialization(self):
        """
        Check if deserialized data is serialized properly with default format
        """
        resource = Resource('http://httpbin.org/post')
        data = {'a': 'b', 'c': ['d', 'e']}
        response = resource.post(data)

        self.assertLess(response.status_code, 300)

        response_data = response.json()

        # Check content type header:
        self.assertEqual(
            'application/json',
            response_data['headers']['Content-Type'],
        )
        # Check JSON payload:
        self.assertEqual(data, response_data['json'])

    def test_adding_query_params(self):
        """
        Check, if existing resource can be modified by extending query params
        """
        resource = Resource('http://httpbin.org/get')
        resource = resource.add_query_params(a=123, b='cde')

        # Check, if URL contains proper strings:
        self.assertIn('a=123', resource.url.split('?', 1)[1])
        self.assertIn('b=cde', resource.url.split('?', 1)[1])

        # Check, if query string is passed to the server properly:
        response_data = resource.get().json()
        self.assertEqual('123', response_data['args']['a'])
        self.assertEqual('cde', response_data['args']['b'])

    def test_date_and_time_serialization(self):
        """
        Check, if dates & times are serialized according to ISO-8601 standard
        """
        data = {
            'date': date(1985, 3, 2),
            'datetime': datetime(1985, 3, 2, 2, 30, 0, 0),
            'datetime_aware': datetime(
                1985, 3, 2, 2, 30, 0, 0, tzinfo=pytz.UTC,
            ),
        }
        resource = Resource('http://httpbin.org/post')
        response = resource.post(data)

        dates = response.json()['json']

        self.assertEqual(dates['date'], '1985-03-02')
        self.assertEqual(dates['datetime'], '1985-03-02T02:30:00')
        self.assertEqual(dates['datetime_aware'], '1985-03-02T02:30:00Z')
