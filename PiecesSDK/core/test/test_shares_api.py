# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.shares_api import SharesApi  # noqa: E501


class TestSharesApi(unittest.TestCase):
    """SharesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SharesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_shares_create_new_share(self) -> None:
        """Test case for shares_create_new_share

        /shares/create [POST]  # noqa: E501
        """
        pass

    def test_shares_delete_share(self) -> None:
        """Test case for shares_delete_share

        /shares/{share}/delete [POST]  # noqa: E501
        """
        pass

    def test_shares_snapshot(self) -> None:
        """Test case for shares_snapshot

        /shares [GET]  # noqa: E501
        """
        pass

    def test_shares_specific_share_snapshot(self) -> None:
        """Test case for shares_specific_share_snapshot

        /shares/{share} [GET]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()