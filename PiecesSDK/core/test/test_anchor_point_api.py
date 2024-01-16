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

from openapi_client.api.anchor_point_api import AnchorPointApi  # noqa: E501


class TestAnchorPointApi(unittest.TestCase):
    """AnchorPointApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnchorPointApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_anchor_point_scores_increment(self) -> None:
        """Test case for anchor_point_scores_increment

        '/anchor_point/{anchor_point}/scores/increment' [POST]  # noqa: E501
        """
        pass

    def test_anchor_point_specific_anchor_point_snapshot(self) -> None:
        """Test case for anchor_point_specific_anchor_point_snapshot

        /anchor_point/{anchor_point} [GET]  # noqa: E501
        """
        pass

    def test_anchor_point_update(self) -> None:
        """Test case for anchor_point_update

        /anchor_point/update [POST]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()