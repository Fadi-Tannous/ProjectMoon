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


class AccountApplicationResponseJson(object):
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
        'date_of_application': 'date',
        'account_application_id': 'str',
        'product_code': 'str',
        'status': 'str',
        'customer': 'CustomerJsonV310',
        'user': 'ResourceUserJSON'
    }

    attribute_map = {
        'date_of_application': 'date_of_application',
        'account_application_id': 'account_application_id',
        'product_code': 'product_code',
        'status': 'status',
        'customer': 'customer',
        'user': 'user'
    }

    def __init__(self, date_of_application=None, account_application_id=None, product_code=None, status=None, customer=None, user=None, _configuration=None):  # noqa: E501
        """AccountApplicationResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_of_application = None
        self._account_application_id = None
        self._product_code = None
        self._status = None
        self._customer = None
        self._user = None
        self.discriminator = None

        self.date_of_application = date_of_application
        self.account_application_id = account_application_id
        self.product_code = product_code
        self.status = status
        self.customer = customer
        self.user = user

    @property
    def date_of_application(self):
        """Gets the date_of_application of this AccountApplicationResponseJson.  # noqa: E501


        :return: The date_of_application of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: date
        """
        return self._date_of_application

    @date_of_application.setter
    def date_of_application(self, date_of_application):
        """Sets the date_of_application of this AccountApplicationResponseJson.


        :param date_of_application: The date_of_application of this AccountApplicationResponseJson.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_of_application is None:
            raise ValueError("Invalid value for `date_of_application`, must not be `None`")  # noqa: E501

        self._date_of_application = date_of_application

    @property
    def account_application_id(self):
        """Gets the account_application_id of this AccountApplicationResponseJson.  # noqa: E501


        :return: The account_application_id of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._account_application_id

    @account_application_id.setter
    def account_application_id(self, account_application_id):
        """Sets the account_application_id of this AccountApplicationResponseJson.


        :param account_application_id: The account_application_id of this AccountApplicationResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_application_id is None:
            raise ValueError("Invalid value for `account_application_id`, must not be `None`")  # noqa: E501

        self._account_application_id = account_application_id

    @property
    def product_code(self):
        """Gets the product_code of this AccountApplicationResponseJson.  # noqa: E501


        :return: The product_code of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this AccountApplicationResponseJson.


        :param product_code: The product_code of this AccountApplicationResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def status(self):
        """Gets the status of this AccountApplicationResponseJson.  # noqa: E501


        :return: The status of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountApplicationResponseJson.


        :param status: The status of this AccountApplicationResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def customer(self):
        """Gets the customer of this AccountApplicationResponseJson.  # noqa: E501


        :return: The customer of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: CustomerJsonV310
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this AccountApplicationResponseJson.


        :param customer: The customer of this AccountApplicationResponseJson.  # noqa: E501
        :type: CustomerJsonV310
        """
        if self._configuration.client_side_validation and customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def user(self):
        """Gets the user of this AccountApplicationResponseJson.  # noqa: E501


        :return: The user of this AccountApplicationResponseJson.  # noqa: E501
        :rtype: ResourceUserJSON
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccountApplicationResponseJson.


        :param user: The user of this AccountApplicationResponseJson.  # noqa: E501
        :type: ResourceUserJSON
        """
        if self._configuration.client_side_validation and user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(AccountApplicationResponseJson, dict):
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
        if not isinstance(other, AccountApplicationResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountApplicationResponseJson):
            return True

        return self.to_dict() != other.to_dict()
