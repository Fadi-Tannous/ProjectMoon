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


class IbanDetailsJsonV400(object):
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
        'bank_routings': 'list[BankRoutingJsonV121]',
        'city': 'str',
        'postcode': 'str',
        'branch': 'str',
        'country': 'str',
        'attributes': 'list[AttributeJsonV400]',
        'bank': 'str',
        'address': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'bank_routings': 'bank_routings',
        'city': 'city',
        'postcode': 'postcode',
        'branch': 'branch',
        'country': 'country',
        'attributes': 'attributes',
        'bank': 'bank',
        'address': 'address',
        'phone': 'phone'
    }

    def __init__(self, bank_routings=None, city=None, postcode=None, branch=None, country=None, attributes=None, bank=None, address=None, phone=None, _configuration=None):  # noqa: E501
        """IbanDetailsJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bank_routings = None
        self._city = None
        self._postcode = None
        self._branch = None
        self._country = None
        self._attributes = None
        self._bank = None
        self._address = None
        self._phone = None
        self.discriminator = None

        self.bank_routings = bank_routings
        self.city = city
        self.postcode = postcode
        self.branch = branch
        self.country = country
        self.attributes = attributes
        self.bank = bank
        self.address = address
        self.phone = phone

    @property
    def bank_routings(self):
        """Gets the bank_routings of this IbanDetailsJsonV400.  # noqa: E501


        :return: The bank_routings of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: list[BankRoutingJsonV121]
        """
        return self._bank_routings

    @bank_routings.setter
    def bank_routings(self, bank_routings):
        """Sets the bank_routings of this IbanDetailsJsonV400.


        :param bank_routings: The bank_routings of this IbanDetailsJsonV400.  # noqa: E501
        :type: list[BankRoutingJsonV121]
        """
        if self._configuration.client_side_validation and bank_routings is None:
            raise ValueError("Invalid value for `bank_routings`, must not be `None`")  # noqa: E501

        self._bank_routings = bank_routings

    @property
    def city(self):
        """Gets the city of this IbanDetailsJsonV400.  # noqa: E501


        :return: The city of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this IbanDetailsJsonV400.


        :param city: The city of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def postcode(self):
        """Gets the postcode of this IbanDetailsJsonV400.  # noqa: E501


        :return: The postcode of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this IbanDetailsJsonV400.


        :param postcode: The postcode of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")  # noqa: E501

        self._postcode = postcode

    @property
    def branch(self):
        """Gets the branch of this IbanDetailsJsonV400.  # noqa: E501


        :return: The branch of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this IbanDetailsJsonV400.


        :param branch: The branch of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and branch is None:
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch

    @property
    def country(self):
        """Gets the country of this IbanDetailsJsonV400.  # noqa: E501


        :return: The country of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IbanDetailsJsonV400.


        :param country: The country of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def attributes(self):
        """Gets the attributes of this IbanDetailsJsonV400.  # noqa: E501


        :return: The attributes of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: list[AttributeJsonV400]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this IbanDetailsJsonV400.


        :param attributes: The attributes of this IbanDetailsJsonV400.  # noqa: E501
        :type: list[AttributeJsonV400]
        """
        if self._configuration.client_side_validation and attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def bank(self):
        """Gets the bank of this IbanDetailsJsonV400.  # noqa: E501


        :return: The bank of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this IbanDetailsJsonV400.


        :param bank: The bank of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank is None:
            raise ValueError("Invalid value for `bank`, must not be `None`")  # noqa: E501

        self._bank = bank

    @property
    def address(self):
        """Gets the address of this IbanDetailsJsonV400.  # noqa: E501


        :return: The address of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IbanDetailsJsonV400.


        :param address: The address of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def phone(self):
        """Gets the phone of this IbanDetailsJsonV400.  # noqa: E501


        :return: The phone of this IbanDetailsJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this IbanDetailsJsonV400.


        :param phone: The phone of this IbanDetailsJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

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
        if issubclass(IbanDetailsJsonV400, dict):
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
        if not isinstance(other, IbanDetailsJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IbanDetailsJsonV400):
            return True

        return self.to_dict() != other.to_dict()
