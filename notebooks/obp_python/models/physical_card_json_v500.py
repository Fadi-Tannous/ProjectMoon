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


class PhysicalCardJsonV500(object):
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
        'allows': 'list[str]',
        'cvv': 'str',
        'expires_date': 'date',
        'networks': 'list[str]',
        'customer_id': 'str',
        'issue_number': 'str',
        'replacement': 'ReplacementJSON',
        'enabled': 'bool',
        'collected': 'date',
        'brand': 'str',
        'card_number': 'str',
        'technology': 'str',
        'cancelled': 'bool',
        'bank_id': 'str',
        'card_id': 'str',
        'pin_reset': 'list[PinResetJSON]',
        'serial_number': 'str',
        'account': 'AccountJSON',
        'valid_from_date': 'date',
        'name_on_card': 'str',
        'posted': 'date',
        'card_type': 'str',
        'on_hot_list': 'bool'
    }

    attribute_map = {
        'allows': 'allows',
        'cvv': 'cvv',
        'expires_date': 'expires_date',
        'networks': 'networks',
        'customer_id': 'customer_id',
        'issue_number': 'issue_number',
        'replacement': 'replacement',
        'enabled': 'enabled',
        'collected': 'collected',
        'brand': 'brand',
        'card_number': 'card_number',
        'technology': 'technology',
        'cancelled': 'cancelled',
        'bank_id': 'bank_id',
        'card_id': 'card_id',
        'pin_reset': 'pin_reset',
        'serial_number': 'serial_number',
        'account': 'account',
        'valid_from_date': 'valid_from_date',
        'name_on_card': 'name_on_card',
        'posted': 'posted',
        'card_type': 'card_type',
        'on_hot_list': 'on_hot_list'
    }

    def __init__(self, allows=None, cvv=None, expires_date=None, networks=None, customer_id=None, issue_number=None, replacement=None, enabled=None, collected=None, brand=None, card_number=None, technology=None, cancelled=None, bank_id=None, card_id=None, pin_reset=None, serial_number=None, account=None, valid_from_date=None, name_on_card=None, posted=None, card_type=None, on_hot_list=None, _configuration=None):  # noqa: E501
        """PhysicalCardJsonV500 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allows = None
        self._cvv = None
        self._expires_date = None
        self._networks = None
        self._customer_id = None
        self._issue_number = None
        self._replacement = None
        self._enabled = None
        self._collected = None
        self._brand = None
        self._card_number = None
        self._technology = None
        self._cancelled = None
        self._bank_id = None
        self._card_id = None
        self._pin_reset = None
        self._serial_number = None
        self._account = None
        self._valid_from_date = None
        self._name_on_card = None
        self._posted = None
        self._card_type = None
        self._on_hot_list = None
        self.discriminator = None

        self.allows = allows
        self.cvv = cvv
        self.expires_date = expires_date
        self.networks = networks
        self.customer_id = customer_id
        self.issue_number = issue_number
        self.replacement = replacement
        self.enabled = enabled
        self.collected = collected
        self.brand = brand
        self.card_number = card_number
        self.technology = technology
        self.cancelled = cancelled
        self.bank_id = bank_id
        self.card_id = card_id
        self.pin_reset = pin_reset
        self.serial_number = serial_number
        self.account = account
        self.valid_from_date = valid_from_date
        self.name_on_card = name_on_card
        self.posted = posted
        self.card_type = card_type
        self.on_hot_list = on_hot_list

    @property
    def allows(self):
        """Gets the allows of this PhysicalCardJsonV500.  # noqa: E501


        :return: The allows of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: list[str]
        """
        return self._allows

    @allows.setter
    def allows(self, allows):
        """Sets the allows of this PhysicalCardJsonV500.


        :param allows: The allows of this PhysicalCardJsonV500.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and allows is None:
            raise ValueError("Invalid value for `allows`, must not be `None`")  # noqa: E501

        self._allows = allows

    @property
    def cvv(self):
        """Gets the cvv of this PhysicalCardJsonV500.  # noqa: E501


        :return: The cvv of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this PhysicalCardJsonV500.


        :param cvv: The cvv of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cvv is None:
            raise ValueError("Invalid value for `cvv`, must not be `None`")  # noqa: E501

        self._cvv = cvv

    @property
    def expires_date(self):
        """Gets the expires_date of this PhysicalCardJsonV500.  # noqa: E501


        :return: The expires_date of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._expires_date

    @expires_date.setter
    def expires_date(self, expires_date):
        """Sets the expires_date of this PhysicalCardJsonV500.


        :param expires_date: The expires_date of this PhysicalCardJsonV500.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and expires_date is None:
            raise ValueError("Invalid value for `expires_date`, must not be `None`")  # noqa: E501

        self._expires_date = expires_date

    @property
    def networks(self):
        """Gets the networks of this PhysicalCardJsonV500.  # noqa: E501


        :return: The networks of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: list[str]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this PhysicalCardJsonV500.


        :param networks: The networks of this PhysicalCardJsonV500.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and networks is None:
            raise ValueError("Invalid value for `networks`, must not be `None`")  # noqa: E501

        self._networks = networks

    @property
    def customer_id(self):
        """Gets the customer_id of this PhysicalCardJsonV500.  # noqa: E501


        :return: The customer_id of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this PhysicalCardJsonV500.


        :param customer_id: The customer_id of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def issue_number(self):
        """Gets the issue_number of this PhysicalCardJsonV500.  # noqa: E501


        :return: The issue_number of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """Sets the issue_number of this PhysicalCardJsonV500.


        :param issue_number: The issue_number of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and issue_number is None:
            raise ValueError("Invalid value for `issue_number`, must not be `None`")  # noqa: E501

        self._issue_number = issue_number

    @property
    def replacement(self):
        """Gets the replacement of this PhysicalCardJsonV500.  # noqa: E501


        :return: The replacement of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: ReplacementJSON
        """
        return self._replacement

    @replacement.setter
    def replacement(self, replacement):
        """Sets the replacement of this PhysicalCardJsonV500.


        :param replacement: The replacement of this PhysicalCardJsonV500.  # noqa: E501
        :type: ReplacementJSON
        """
        if self._configuration.client_side_validation and replacement is None:
            raise ValueError("Invalid value for `replacement`, must not be `None`")  # noqa: E501

        self._replacement = replacement

    @property
    def enabled(self):
        """Gets the enabled of this PhysicalCardJsonV500.  # noqa: E501


        :return: The enabled of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PhysicalCardJsonV500.


        :param enabled: The enabled of this PhysicalCardJsonV500.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def collected(self):
        """Gets the collected of this PhysicalCardJsonV500.  # noqa: E501


        :return: The collected of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._collected

    @collected.setter
    def collected(self, collected):
        """Sets the collected of this PhysicalCardJsonV500.


        :param collected: The collected of this PhysicalCardJsonV500.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and collected is None:
            raise ValueError("Invalid value for `collected`, must not be `None`")  # noqa: E501

        self._collected = collected

    @property
    def brand(self):
        """Gets the brand of this PhysicalCardJsonV500.  # noqa: E501


        :return: The brand of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PhysicalCardJsonV500.


        :param brand: The brand of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def card_number(self):
        """Gets the card_number of this PhysicalCardJsonV500.  # noqa: E501


        :return: The card_number of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this PhysicalCardJsonV500.


        :param card_number: The card_number of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def technology(self):
        """Gets the technology of this PhysicalCardJsonV500.  # noqa: E501


        :return: The technology of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this PhysicalCardJsonV500.


        :param technology: The technology of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and technology is None:
            raise ValueError("Invalid value for `technology`, must not be `None`")  # noqa: E501

        self._technology = technology

    @property
    def cancelled(self):
        """Gets the cancelled of this PhysicalCardJsonV500.  # noqa: E501


        :return: The cancelled of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this PhysicalCardJsonV500.


        :param cancelled: The cancelled of this PhysicalCardJsonV500.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and cancelled is None:
            raise ValueError("Invalid value for `cancelled`, must not be `None`")  # noqa: E501

        self._cancelled = cancelled

    @property
    def bank_id(self):
        """Gets the bank_id of this PhysicalCardJsonV500.  # noqa: E501


        :return: The bank_id of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this PhysicalCardJsonV500.


        :param bank_id: The bank_id of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def card_id(self):
        """Gets the card_id of this PhysicalCardJsonV500.  # noqa: E501


        :return: The card_id of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this PhysicalCardJsonV500.


        :param card_id: The card_id of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and card_id is None:
            raise ValueError("Invalid value for `card_id`, must not be `None`")  # noqa: E501

        self._card_id = card_id

    @property
    def pin_reset(self):
        """Gets the pin_reset of this PhysicalCardJsonV500.  # noqa: E501


        :return: The pin_reset of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: list[PinResetJSON]
        """
        return self._pin_reset

    @pin_reset.setter
    def pin_reset(self, pin_reset):
        """Sets the pin_reset of this PhysicalCardJsonV500.


        :param pin_reset: The pin_reset of this PhysicalCardJsonV500.  # noqa: E501
        :type: list[PinResetJSON]
        """
        if self._configuration.client_side_validation and pin_reset is None:
            raise ValueError("Invalid value for `pin_reset`, must not be `None`")  # noqa: E501

        self._pin_reset = pin_reset

    @property
    def serial_number(self):
        """Gets the serial_number of this PhysicalCardJsonV500.  # noqa: E501


        :return: The serial_number of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this PhysicalCardJsonV500.


        :param serial_number: The serial_number of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def account(self):
        """Gets the account of this PhysicalCardJsonV500.  # noqa: E501


        :return: The account of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: AccountJSON
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this PhysicalCardJsonV500.


        :param account: The account of this PhysicalCardJsonV500.  # noqa: E501
        :type: AccountJSON
        """
        if self._configuration.client_side_validation and account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def valid_from_date(self):
        """Gets the valid_from_date of this PhysicalCardJsonV500.  # noqa: E501


        :return: The valid_from_date of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._valid_from_date

    @valid_from_date.setter
    def valid_from_date(self, valid_from_date):
        """Sets the valid_from_date of this PhysicalCardJsonV500.


        :param valid_from_date: The valid_from_date of this PhysicalCardJsonV500.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and valid_from_date is None:
            raise ValueError("Invalid value for `valid_from_date`, must not be `None`")  # noqa: E501

        self._valid_from_date = valid_from_date

    @property
    def name_on_card(self):
        """Gets the name_on_card of this PhysicalCardJsonV500.  # noqa: E501


        :return: The name_on_card of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """Sets the name_on_card of this PhysicalCardJsonV500.


        :param name_on_card: The name_on_card of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_on_card is None:
            raise ValueError("Invalid value for `name_on_card`, must not be `None`")  # noqa: E501

        self._name_on_card = name_on_card

    @property
    def posted(self):
        """Gets the posted of this PhysicalCardJsonV500.  # noqa: E501


        :return: The posted of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._posted

    @posted.setter
    def posted(self, posted):
        """Sets the posted of this PhysicalCardJsonV500.


        :param posted: The posted of this PhysicalCardJsonV500.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and posted is None:
            raise ValueError("Invalid value for `posted`, must not be `None`")  # noqa: E501

        self._posted = posted

    @property
    def card_type(self):
        """Gets the card_type of this PhysicalCardJsonV500.  # noqa: E501


        :return: The card_type of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this PhysicalCardJsonV500.


        :param card_type: The card_type of this PhysicalCardJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and card_type is None:
            raise ValueError("Invalid value for `card_type`, must not be `None`")  # noqa: E501

        self._card_type = card_type

    @property
    def on_hot_list(self):
        """Gets the on_hot_list of this PhysicalCardJsonV500.  # noqa: E501


        :return: The on_hot_list of this PhysicalCardJsonV500.  # noqa: E501
        :rtype: bool
        """
        return self._on_hot_list

    @on_hot_list.setter
    def on_hot_list(self, on_hot_list):
        """Sets the on_hot_list of this PhysicalCardJsonV500.


        :param on_hot_list: The on_hot_list of this PhysicalCardJsonV500.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and on_hot_list is None:
            raise ValueError("Invalid value for `on_hot_list`, must not be `None`")  # noqa: E501

        self._on_hot_list = on_hot_list

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
        if issubclass(PhysicalCardJsonV500, dict):
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
        if not isinstance(other, PhysicalCardJsonV500):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalCardJsonV500):
            return True

        return self.to_dict() != other.to_dict()
