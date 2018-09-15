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
from swagger_client.api.position_template__deprecated_api import PositionTemplateDeprecatedApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPositionTemplateDeprecatedApi(unittest.TestCase):
    """PositionTemplateDeprecatedApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.position_template__deprecated_api.PositionTemplateDeprecatedApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_createpositiontemplate(self):
        """Test case for createpositiontemplate

        Create a new position template  # noqa: E501
        """
        pass

    def test_delete_position_template(self):
        """Test case for delete_position_template

        Delete a specific position template instance  # noqa: E501
        """
        pass

    def test_get_applicant_fields(self):
        """Test case for get_applicant_fields

        List multiple applicant custom fields of a specific position template  # noqa: E501
        """
        pass

    def test_getpositiontemplate(self):
        """Test case for getpositiontemplate

        Return a specific position template instance.  # noqa: E501
        """
        pass

    def test_getpositiontemplates(self):
        """Test case for getpositiontemplates

        List multiple positions template resources.  # noqa: E501
        """
        pass

    def test_importpositiontemplate(self):
        """Test case for importpositiontemplate

        Import a new position template  # noqa: E501
        """
        pass

    def test_updatepositiontemplate(self):
        """Test case for updatepositiontemplate

        Update a specific position template instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
