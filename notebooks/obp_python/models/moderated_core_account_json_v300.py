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


class ModeratedCoreAccountJsonV300(object):
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
        'number': 'str',
        'account_attributes': 'list[AccountAttributeResponseJson]',
        'account_routings': 'list[AccountRoutingJsonV121]',
        'label': 'str',
        'owners': 'list[UserJSONV121]',
        'balance': 'AmountOfMoneyJsonV121',
        'bank_id': 'str',
        'id': 'str',
        'type': 'str',
        'account_rules': 'list[AccountRuleJsonV300]'
    }

    attribute_map = {
        'number': 'number',
        'account_attributes': 'account_attributes',
        'account_routings': 'account_routings',
        'label': 'label',
        'owners': 'owners',
        'balance': 'balance',
        'bank_id': 'bank_id',
        'id': 'id',
        'type': 'type',
        'account_rules': 'account_rules'
    }

    def __init__(self, number=None, account_attributes=None, account_routings=None, label=None, owners=None, balance=None, bank_id=None, id=None, type=None, account_rules=None, _configuration=None):  # noqa: E501
        """ModeratedCoreAccountJsonV300 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number = None
        self._account_attributes = None
        self._account_routings = None
        self._label = None
        self._owners = None
        self._balance = None
        self._bank_id = None
        self._id = None
        self._type = None
        self._account_rules = None
        self.discriminator = None

        self.number = number
        if account_attributes is not None:
            self.account_attributes = account_attributes
        self.account_routings = account_routings
        self.label = label
        self.owners = owners
        self.balance = balance
        self.bank_id = bank_id
        self.id = id
        self.type = type
        self.account_rules = account_rules

    @property
    def number(self):
        """Gets the number of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The number of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ModeratedCoreAccountJsonV300.


        :param number: The number of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def account_attributes(self):
        """Gets the account_attributes of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The account_attributes of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: list[AccountAttributeResponseJson]
        """
        return self._account_attributes

    @account_attributes.setter
    def account_attributes(self, account_attributes):
        """Sets the account_attributes of this ModeratedCoreAccountJsonV300.


        :param account_attributes: The account_attributes of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: list[AccountAttributeResponseJson]
        """

        self._account_attributes = account_attributes

    @property
    def account_routings(self):
        """Gets the account_routings of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The account_routings of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: list[AccountRoutingJsonV121]
        """
        return self._account_routings

    @account_routings.setter
    def account_routings(self, account_routings):
        """Sets the account_routings of this ModeratedCoreAccountJsonV300.


        :param account_routings: The account_routings of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: list[AccountRoutingJsonV121]
        """
        if self._configuration.client_side_validation and account_routings is None:
            raise ValueError("Invalid value for `account_routings`, must not be `None`")  # noqa: E501

        self._account_routings = account_routings

    @property
    def label(self):
        """Gets the label of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The label of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModeratedCoreAccountJsonV300.


        :param label: The label of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def owners(self):
        """Gets the owners of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The owners of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: list[UserJSONV121]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this ModeratedCoreAccountJsonV300.


        :param owners: The owners of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: list[UserJSONV121]
        """
        if self._configuration.client_side_validation and owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def balance(self):
        """Gets the balance of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The balance of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ModeratedCoreAccountJsonV300.


        :param balance: The balance of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def bank_id(self):
        """Gets the bank_id of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The bank_id of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this ModeratedCoreAccountJsonV300.


        :param bank_id: The bank_id of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def id(self):
        """Gets the id of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The id of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModeratedCoreAccountJsonV300.


        :param id: The id of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The type of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModeratedCoreAccountJsonV300.


        :param type: The type of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def account_rules(self):
        """Gets the account_rules of this ModeratedCoreAccountJsonV300.  # noqa: E501


        :return: The account_rules of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :rtype: list[AccountRuleJsonV300]
        """
        return self._account_rules

    @account_rules.setter
    def account_rules(self, account_rules):
        """Sets the account_rules of this ModeratedCoreAccountJsonV300.


        :param account_rules: The account_rules of this ModeratedCoreAccountJsonV300.  # noqa: E501
        :type: list[AccountRuleJsonV300]
        """
        if self._configuration.client_side_validation and account_rules is None:
            raise ValueError("Invalid value for `account_rules`, must not be `None`")  # noqa: E501

        self._account_rules = account_rules

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
        if issubclass(ModeratedCoreAccountJsonV300, dict):
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
        if not isinstance(other, ModeratedCoreAccountJsonV300):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModeratedCoreAccountJsonV300):
            return True

        return self.to_dict() != other.to_dict()
