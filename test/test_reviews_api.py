# coding: utf-8

"""
    Kenoby

    Issues or Questions? <a href=\"mailto:devs@kenoby.com\" target=\"_blank\">Send us an e-mail</a>.<br>                      For better experience <a href=\"http://api.kenoby.com/swagger.json\" target=\"_blank\">Download our swagger.json</a>                      and use it on <a href=\"https://www.getpostman.com/\" target=\"_blank\">Postman</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.reviews_api import ReviewsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReviewsApi(unittest.TestCase):
    """ReviewsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.reviews_api.ReviewsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createreviews(self):
        """Test case for createreviews

        Create a new reviews  # noqa: E501
        """
        pass

    def test_deletereviews(self):
        """Test case for deletereviews

        Delete a specific review instance.  # noqa: E501
        """
        pass

    def test_getreviews(self):
        """Test case for getreviews

        Return a specific review instance.  # noqa: E501
        """
        pass

    def test_getreviewss(self):
        """Test case for getreviewss

        List multiple reviews resources.  # noqa: E501
        """
        pass

    def test_updatereviews(self):
        """Test case for updatereviews

        Update a specific review instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
