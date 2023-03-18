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


class KycCheckJSON(object):
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
        'customer_id': 'str',
        'customer_number': 'str',
        'bank_id': 'str',
        'id': 'str',
        'how': 'str',
        '_date': 'date',
        'satisfied': 'bool',
        'staff_user_id': 'str',
        'staff_name': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'customer_number': 'customer_number',
        'bank_id': 'bank_id',
        'id': 'id',
        'how': 'how',
        '_date': 'date',
        'satisfied': 'satisfied',
        'staff_user_id': 'staff_user_id',
        'staff_name': 'staff_name',
        'comments': 'comments'
    }

    def __init__(self, customer_id=None, customer_number=None, bank_id=None, id=None, how=None, _date=None, satisfied=None, staff_user_id=None, staff_name=None, comments=None, _configuration=None):  # noqa: E501
        """KycCheckJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer_id = None
        self._customer_number = None
        self._bank_id = None
        self._id = None
        self._how = None
        self.__date = None
        self._satisfied = None
        self._staff_user_id = None
        self._staff_name = None
        self._comments = None
        self.discriminator = None

        self.customer_id = customer_id
        self.customer_number = customer_number
        self.bank_id = bank_id
        self.id = id
        self.how = how
        self._date = _date
        self.satisfied = satisfied
        self.staff_user_id = staff_user_id
        self.staff_name = staff_name
        self.comments = comments

    @property
    def customer_id(self):
        """Gets the customer_id of this KycCheckJSON.  # noqa: E501


        :return: The customer_id of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this KycCheckJSON.


        :param customer_id: The customer_id of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def customer_number(self):
        """Gets the customer_number of this KycCheckJSON.  # noqa: E501


        :return: The customer_number of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this KycCheckJSON.


        :param customer_number: The customer_number of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def bank_id(self):
        """Gets the bank_id of this KycCheckJSON.  # noqa: E501


        :return: The bank_id of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this KycCheckJSON.


        :param bank_id: The bank_id of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def id(self):
        """Gets the id of this KycCheckJSON.  # noqa: E501


        :return: The id of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KycCheckJSON.


        :param id: The id of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def how(self):
        """Gets the how of this KycCheckJSON.  # noqa: E501


        :return: The how of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._how

    @how.setter
    def how(self, how):
        """Sets the how of this KycCheckJSON.


        :param how: The how of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and how is None:
            raise ValueError("Invalid value for `how`, must not be `None`")  # noqa: E501

        self._how = how

    @property
    def _date(self):
        """Gets the _date of this KycCheckJSON.  # noqa: E501


        :return: The _date of this KycCheckJSON.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this KycCheckJSON.


        :param _date: The _date of this KycCheckJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def satisfied(self):
        """Gets the satisfied of this KycCheckJSON.  # noqa: E501


        :return: The satisfied of this KycCheckJSON.  # noqa: E501
        :rtype: bool
        """
        return self._satisfied

    @satisfied.setter
    def satisfied(self, satisfied):
        """Sets the satisfied of this KycCheckJSON.


        :param satisfied: The satisfied of this KycCheckJSON.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and satisfied is None:
            raise ValueError("Invalid value for `satisfied`, must not be `None`")  # noqa: E501

        self._satisfied = satisfied

    @property
    def staff_user_id(self):
        """Gets the staff_user_id of this KycCheckJSON.  # noqa: E501


        :return: The staff_user_id of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._staff_user_id

    @staff_user_id.setter
    def staff_user_id(self, staff_user_id):
        """Sets the staff_user_id of this KycCheckJSON.


        :param staff_user_id: The staff_user_id of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_user_id is None:
            raise ValueError("Invalid value for `staff_user_id`, must not be `None`")  # noqa: E501

        self._staff_user_id = staff_user_id

    @property
    def staff_name(self):
        """Gets the staff_name of this KycCheckJSON.  # noqa: E501


        :return: The staff_name of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._staff_name

    @staff_name.setter
    def staff_name(self, staff_name):
        """Sets the staff_name of this KycCheckJSON.


        :param staff_name: The staff_name of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_name is None:
            raise ValueError("Invalid value for `staff_name`, must not be `None`")  # noqa: E501

        self._staff_name = staff_name

    @property
    def comments(self):
        """Gets the comments of this KycCheckJSON.  # noqa: E501


        :return: The comments of this KycCheckJSON.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this KycCheckJSON.


        :param comments: The comments of this KycCheckJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")  # noqa: E501

        self._comments = comments

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
        if issubclass(KycCheckJSON, dict):
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
        if not isinstance(other, KycCheckJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KycCheckJSON):
            return True

        return self.to_dict() != other.to_dict()
