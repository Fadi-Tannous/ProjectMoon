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


class UpdateViewJSON(object):
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
        'description': 'str',
        'is_public': 'bool',
        'hide_metadata_if_alias_used': 'bool',
        'which_alias_to_use': 'str',
        'is_firehose': 'bool',
        'metadata_view': 'str',
        'allowed_actions': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'is_public': 'is_public',
        'hide_metadata_if_alias_used': 'hide_metadata_if_alias_used',
        'which_alias_to_use': 'which_alias_to_use',
        'is_firehose': 'is_firehose',
        'metadata_view': 'metadata_view',
        'allowed_actions': 'allowed_actions'
    }

    def __init__(self, description=None, is_public=None, hide_metadata_if_alias_used=None, which_alias_to_use=None, is_firehose=None, metadata_view=None, allowed_actions=None, _configuration=None):  # noqa: E501
        """UpdateViewJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._is_public = None
        self._hide_metadata_if_alias_used = None
        self._which_alias_to_use = None
        self._is_firehose = None
        self._metadata_view = None
        self._allowed_actions = None
        self.discriminator = None

        self.description = description
        self.is_public = is_public
        self.hide_metadata_if_alias_used = hide_metadata_if_alias_used
        self.which_alias_to_use = which_alias_to_use
        if is_firehose is not None:
            self.is_firehose = is_firehose
        self.metadata_view = metadata_view
        self.allowed_actions = allowed_actions

    @property
    def description(self):
        """Gets the description of this UpdateViewJSON.  # noqa: E501


        :return: The description of this UpdateViewJSON.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateViewJSON.


        :param description: The description of this UpdateViewJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def is_public(self):
        """Gets the is_public of this UpdateViewJSON.  # noqa: E501


        :return: The is_public of this UpdateViewJSON.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this UpdateViewJSON.


        :param is_public: The is_public of this UpdateViewJSON.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def hide_metadata_if_alias_used(self):
        """Gets the hide_metadata_if_alias_used of this UpdateViewJSON.  # noqa: E501


        :return: The hide_metadata_if_alias_used of this UpdateViewJSON.  # noqa: E501
        :rtype: bool
        """
        return self._hide_metadata_if_alias_used

    @hide_metadata_if_alias_used.setter
    def hide_metadata_if_alias_used(self, hide_metadata_if_alias_used):
        """Sets the hide_metadata_if_alias_used of this UpdateViewJSON.


        :param hide_metadata_if_alias_used: The hide_metadata_if_alias_used of this UpdateViewJSON.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and hide_metadata_if_alias_used is None:
            raise ValueError("Invalid value for `hide_metadata_if_alias_used`, must not be `None`")  # noqa: E501

        self._hide_metadata_if_alias_used = hide_metadata_if_alias_used

    @property
    def which_alias_to_use(self):
        """Gets the which_alias_to_use of this UpdateViewJSON.  # noqa: E501


        :return: The which_alias_to_use of this UpdateViewJSON.  # noqa: E501
        :rtype: str
        """
        return self._which_alias_to_use

    @which_alias_to_use.setter
    def which_alias_to_use(self, which_alias_to_use):
        """Sets the which_alias_to_use of this UpdateViewJSON.


        :param which_alias_to_use: The which_alias_to_use of this UpdateViewJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and which_alias_to_use is None:
            raise ValueError("Invalid value for `which_alias_to_use`, must not be `None`")  # noqa: E501

        self._which_alias_to_use = which_alias_to_use

    @property
    def is_firehose(self):
        """Gets the is_firehose of this UpdateViewJSON.  # noqa: E501


        :return: The is_firehose of this UpdateViewJSON.  # noqa: E501
        :rtype: bool
        """
        return self._is_firehose

    @is_firehose.setter
    def is_firehose(self, is_firehose):
        """Sets the is_firehose of this UpdateViewJSON.


        :param is_firehose: The is_firehose of this UpdateViewJSON.  # noqa: E501
        :type: bool
        """

        self._is_firehose = is_firehose

    @property
    def metadata_view(self):
        """Gets the metadata_view of this UpdateViewJSON.  # noqa: E501


        :return: The metadata_view of this UpdateViewJSON.  # noqa: E501
        :rtype: str
        """
        return self._metadata_view

    @metadata_view.setter
    def metadata_view(self, metadata_view):
        """Sets the metadata_view of this UpdateViewJSON.


        :param metadata_view: The metadata_view of this UpdateViewJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and metadata_view is None:
            raise ValueError("Invalid value for `metadata_view`, must not be `None`")  # noqa: E501

        self._metadata_view = metadata_view

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this UpdateViewJSON.  # noqa: E501


        :return: The allowed_actions of this UpdateViewJSON.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this UpdateViewJSON.


        :param allowed_actions: The allowed_actions of this UpdateViewJSON.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and allowed_actions is None:
            raise ValueError("Invalid value for `allowed_actions`, must not be `None`")  # noqa: E501

        self._allowed_actions = allowed_actions

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
        if issubclass(UpdateViewJSON, dict):
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
        if not isinstance(other, UpdateViewJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateViewJSON):
            return True

        return self.to_dict() != other.to_dict()