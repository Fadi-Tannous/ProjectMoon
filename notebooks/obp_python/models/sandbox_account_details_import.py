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


class SandboxAccountDetailsImport(object):
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
        'new_balance': 'str',
        'description': 'str',
        'completed': 'str',
        'type': 'str',
        'value': 'str',
        'posted': 'str'
    }

    attribute_map = {
        'new_balance': 'new_balance',
        'description': 'description',
        'completed': 'completed',
        'type': 'type',
        'value': 'value',
        'posted': 'posted'
    }

    def __init__(self, new_balance=None, description=None, completed=None, type=None, value=None, posted=None, _configuration=None):  # noqa: E501
        """SandboxAccountDetailsImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_balance = None
        self._description = None
        self._completed = None
        self._type = None
        self._value = None
        self._posted = None
        self.discriminator = None

        self.new_balance = new_balance
        self.description = description
        self.completed = completed
        self.type = type
        self.value = value
        self.posted = posted

    @property
    def new_balance(self):
        """Gets the new_balance of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The new_balance of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._new_balance

    @new_balance.setter
    def new_balance(self, new_balance):
        """Sets the new_balance of this SandboxAccountDetailsImport.


        :param new_balance: The new_balance of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and new_balance is None:
            raise ValueError("Invalid value for `new_balance`, must not be `None`")  # noqa: E501

        self._new_balance = new_balance

    @property
    def description(self):
        """Gets the description of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The description of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SandboxAccountDetailsImport.


        :param description: The description of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def completed(self):
        """Gets the completed of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The completed of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this SandboxAccountDetailsImport.


        :param completed: The completed of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and completed is None:
            raise ValueError("Invalid value for `completed`, must not be `None`")  # noqa: E501

        self._completed = completed

    @property
    def type(self):
        """Gets the type of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The type of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SandboxAccountDetailsImport.


        :param type: The type of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The value of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SandboxAccountDetailsImport.


        :param value: The value of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def posted(self):
        """Gets the posted of this SandboxAccountDetailsImport.  # noqa: E501


        :return: The posted of this SandboxAccountDetailsImport.  # noqa: E501
        :rtype: str
        """
        return self._posted

    @posted.setter
    def posted(self, posted):
        """Sets the posted of this SandboxAccountDetailsImport.


        :param posted: The posted of this SandboxAccountDetailsImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and posted is None:
            raise ValueError("Invalid value for `posted`, must not be `None`")  # noqa: E501

        self._posted = posted

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
        if issubclass(SandboxAccountDetailsImport, dict):
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
        if not isinstance(other, SandboxAccountDetailsImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxAccountDetailsImport):
            return True

        return self.to_dict() != other.to_dict()