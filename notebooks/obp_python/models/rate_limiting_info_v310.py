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


class RateLimitingInfoV310(object):
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
        'enabled': 'bool',
        'technology': 'str',
        'service_available': 'bool',
        'is_active': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'technology': 'technology',
        'service_available': 'service_available',
        'is_active': 'is_active'
    }

    def __init__(self, enabled=None, technology=None, service_available=None, is_active=None, _configuration=None):  # noqa: E501
        """RateLimitingInfoV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._technology = None
        self._service_available = None
        self._is_active = None
        self.discriminator = None

        self.enabled = enabled
        self.technology = technology
        self.service_available = service_available
        self.is_active = is_active

    @property
    def enabled(self):
        """Gets the enabled of this RateLimitingInfoV310.  # noqa: E501


        :return: The enabled of this RateLimitingInfoV310.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this RateLimitingInfoV310.


        :param enabled: The enabled of this RateLimitingInfoV310.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def technology(self):
        """Gets the technology of this RateLimitingInfoV310.  # noqa: E501


        :return: The technology of this RateLimitingInfoV310.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this RateLimitingInfoV310.


        :param technology: The technology of this RateLimitingInfoV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and technology is None:
            raise ValueError("Invalid value for `technology`, must not be `None`")  # noqa: E501

        self._technology = technology

    @property
    def service_available(self):
        """Gets the service_available of this RateLimitingInfoV310.  # noqa: E501


        :return: The service_available of this RateLimitingInfoV310.  # noqa: E501
        :rtype: bool
        """
        return self._service_available

    @service_available.setter
    def service_available(self, service_available):
        """Sets the service_available of this RateLimitingInfoV310.


        :param service_available: The service_available of this RateLimitingInfoV310.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and service_available is None:
            raise ValueError("Invalid value for `service_available`, must not be `None`")  # noqa: E501

        self._service_available = service_available

    @property
    def is_active(self):
        """Gets the is_active of this RateLimitingInfoV310.  # noqa: E501


        :return: The is_active of this RateLimitingInfoV310.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this RateLimitingInfoV310.


        :param is_active: The is_active of this RateLimitingInfoV310.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

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
        if issubclass(RateLimitingInfoV310, dict):
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
        if not isinstance(other, RateLimitingInfoV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RateLimitingInfoV310):
            return True

        return self.to_dict() != other.to_dict()
