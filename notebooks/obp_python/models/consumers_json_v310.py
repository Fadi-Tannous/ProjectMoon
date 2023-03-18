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


class ConsumersJsonV310(object):
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
        'consumers': 'list[ConsumerJsonV310]'
    }

    attribute_map = {
        'consumers': 'consumers'
    }

    def __init__(self, consumers=None, _configuration=None):  # noqa: E501
        """ConsumersJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consumers = None
        self.discriminator = None

        self.consumers = consumers

    @property
    def consumers(self):
        """Gets the consumers of this ConsumersJsonV310.  # noqa: E501


        :return: The consumers of this ConsumersJsonV310.  # noqa: E501
        :rtype: list[ConsumerJsonV310]
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        """Sets the consumers of this ConsumersJsonV310.


        :param consumers: The consumers of this ConsumersJsonV310.  # noqa: E501
        :type: list[ConsumerJsonV310]
        """
        if self._configuration.client_side_validation and consumers is None:
            raise ValueError("Invalid value for `consumers`, must not be `None`")  # noqa: E501

        self._consumers = consumers

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
        if issubclass(ConsumersJsonV310, dict):
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
        if not isinstance(other, ConsumersJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsumersJsonV310):
            return True

        return self.to_dict() != other.to_dict()
