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


class DynamicEntityFooBar(object):
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
        'bank_id': 'str',
        'foo_bar': 'DynamicEntityDefinition',
        'dynamic_entity_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'bank_id': 'bankId',
        'foo_bar': 'FooBar',
        'dynamic_entity_id': 'dynamicEntityId',
        'user_id': 'userId'
    }

    def __init__(self, bank_id=None, foo_bar=None, dynamic_entity_id=None, user_id=None, _configuration=None):  # noqa: E501
        """DynamicEntityFooBar - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bank_id = None
        self._foo_bar = None
        self._dynamic_entity_id = None
        self._user_id = None
        self.discriminator = None

        if bank_id is not None:
            self.bank_id = bank_id
        self.foo_bar = foo_bar
        if dynamic_entity_id is not None:
            self.dynamic_entity_id = dynamic_entity_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def bank_id(self):
        """Gets the bank_id of this DynamicEntityFooBar.  # noqa: E501


        :return: The bank_id of this DynamicEntityFooBar.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this DynamicEntityFooBar.


        :param bank_id: The bank_id of this DynamicEntityFooBar.  # noqa: E501
        :type: str
        """

        self._bank_id = bank_id

    @property
    def foo_bar(self):
        """Gets the foo_bar of this DynamicEntityFooBar.  # noqa: E501


        :return: The foo_bar of this DynamicEntityFooBar.  # noqa: E501
        :rtype: DynamicEntityDefinition
        """
        return self._foo_bar

    @foo_bar.setter
    def foo_bar(self, foo_bar):
        """Sets the foo_bar of this DynamicEntityFooBar.


        :param foo_bar: The foo_bar of this DynamicEntityFooBar.  # noqa: E501
        :type: DynamicEntityDefinition
        """
        if self._configuration.client_side_validation and foo_bar is None:
            raise ValueError("Invalid value for `foo_bar`, must not be `None`")  # noqa: E501

        self._foo_bar = foo_bar

    @property
    def dynamic_entity_id(self):
        """Gets the dynamic_entity_id of this DynamicEntityFooBar.  # noqa: E501


        :return: The dynamic_entity_id of this DynamicEntityFooBar.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_entity_id

    @dynamic_entity_id.setter
    def dynamic_entity_id(self, dynamic_entity_id):
        """Sets the dynamic_entity_id of this DynamicEntityFooBar.


        :param dynamic_entity_id: The dynamic_entity_id of this DynamicEntityFooBar.  # noqa: E501
        :type: str
        """

        self._dynamic_entity_id = dynamic_entity_id

    @property
    def user_id(self):
        """Gets the user_id of this DynamicEntityFooBar.  # noqa: E501


        :return: The user_id of this DynamicEntityFooBar.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DynamicEntityFooBar.


        :param user_id: The user_id of this DynamicEntityFooBar.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(DynamicEntityFooBar, dict):
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
        if not isinstance(other, DynamicEntityFooBar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicEntityFooBar):
            return True

        return self.to_dict() != other.to_dict()
