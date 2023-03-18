# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2022. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from obp_python.configuration import Configuration


class ConsentRequestResponseJsonPayloadAccountAccess(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_routing': 'ConsentRequestResponseJsonPayloadAccountRouting',
        'view_id': 'str'
    }

    attribute_map = {
        'account_routing': 'account_routing',
        'view_id': 'view_id'
    }

    def __init__(self, account_routing=None, view_id=None, _configuration=None):  # noqa: E501
        """ConsentRequestResponseJsonPayloadAccountAccess - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_routing = None
        self._view_id = None
        self.discriminator = None

        self.account_routing = account_routing
        self.view_id = view_id

    @property
    def account_routing(self):
        """Gets the account_routing of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501


        :return: The account_routing of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501
        :rtype: ConsentRequestResponseJsonPayloadAccountRouting
        """
        return self._account_routing

    @account_routing.setter
    def account_routing(self, account_routing):
        """Sets the account_routing of this ConsentRequestResponseJsonPayloadAccountAccess.


        :param account_routing: The account_routing of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501
        :type: ConsentRequestResponseJsonPayloadAccountRouting
        """
        if self._configuration.client_side_validation and account_routing is None:
            raise ValueError("Invalid value for `account_routing`, must not be `None`")  # noqa: E501

        self._account_routing = account_routing

    @property
    def view_id(self):
        """Gets the view_id of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501


        :return: The view_id of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this ConsentRequestResponseJsonPayloadAccountAccess.


        :param view_id: The view_id of this ConsentRequestResponseJsonPayloadAccountAccess.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and view_id is None:
            raise ValueError("Invalid value for `view_id`, must not be `None`")  # noqa: E501

        self._view_id = view_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConsentRequestResponseJsonPayloadAccountAccess, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConsentRequestResponseJsonPayloadAccountAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentRequestResponseJsonPayloadAccountAccess):
            return True

        return self.to_dict() != other.to_dict()
