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


class SocialMediaJSON(object):
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
        'date_activated': 'date',
        'customer_number': 'str',
        'date_added': 'date',
        'type': 'str',
        'handle': 'str'
    }

    attribute_map = {
        'date_activated': 'date_activated',
        'customer_number': 'customer_number',
        'date_added': 'date_added',
        'type': 'type',
        'handle': 'handle'
    }

    def __init__(self, date_activated=None, customer_number=None, date_added=None, type=None, handle=None, _configuration=None):  # noqa: E501
        """SocialMediaJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_activated = None
        self._customer_number = None
        self._date_added = None
        self._type = None
        self._handle = None
        self.discriminator = None

        self.date_activated = date_activated
        self.customer_number = customer_number
        self.date_added = date_added
        self.type = type
        self.handle = handle

    @property
    def date_activated(self):
        """Gets the date_activated of this SocialMediaJSON.  # noqa: E501


        :return: The date_activated of this SocialMediaJSON.  # noqa: E501
        :rtype: date
        """
        return self._date_activated

    @date_activated.setter
    def date_activated(self, date_activated):
        """Sets the date_activated of this SocialMediaJSON.


        :param date_activated: The date_activated of this SocialMediaJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_activated is None:
            raise ValueError("Invalid value for `date_activated`, must not be `None`")  # noqa: E501

        self._date_activated = date_activated

    @property
    def customer_number(self):
        """Gets the customer_number of this SocialMediaJSON.  # noqa: E501


        :return: The customer_number of this SocialMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this SocialMediaJSON.


        :param customer_number: The customer_number of this SocialMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def date_added(self):
        """Gets the date_added of this SocialMediaJSON.  # noqa: E501


        :return: The date_added of this SocialMediaJSON.  # noqa: E501
        :rtype: date
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this SocialMediaJSON.


        :param date_added: The date_added of this SocialMediaJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_added is None:
            raise ValueError("Invalid value for `date_added`, must not be `None`")  # noqa: E501

        self._date_added = date_added

    @property
    def type(self):
        """Gets the type of this SocialMediaJSON.  # noqa: E501


        :return: The type of this SocialMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SocialMediaJSON.


        :param type: The type of this SocialMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def handle(self):
        """Gets the handle of this SocialMediaJSON.  # noqa: E501


        :return: The handle of this SocialMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this SocialMediaJSON.


        :param handle: The handle of this SocialMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

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
        if issubclass(SocialMediaJSON, dict):
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
        if not isinstance(other, SocialMediaJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SocialMediaJSON):
            return True

        return self.to_dict() != other.to_dict()