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


class ObpApiLoopbackJson(object):
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
        'connector_version': 'str',
        'git_commit': 'str',
        'duration_time': 'str'
    }

    attribute_map = {
        'connector_version': 'connector_version',
        'git_commit': 'git_commit',
        'duration_time': 'duration_time'
    }

    def __init__(self, connector_version=None, git_commit=None, duration_time=None, _configuration=None):  # noqa: E501
        """ObpApiLoopbackJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connector_version = None
        self._git_commit = None
        self._duration_time = None
        self.discriminator = None

        self.connector_version = connector_version
        self.git_commit = git_commit
        self.duration_time = duration_time

    @property
    def connector_version(self):
        """Gets the connector_version of this ObpApiLoopbackJson.  # noqa: E501


        :return: The connector_version of this ObpApiLoopbackJson.  # noqa: E501
        :rtype: str
        """
        return self._connector_version

    @connector_version.setter
    def connector_version(self, connector_version):
        """Sets the connector_version of this ObpApiLoopbackJson.


        :param connector_version: The connector_version of this ObpApiLoopbackJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connector_version is None:
            raise ValueError("Invalid value for `connector_version`, must not be `None`")  # noqa: E501

        self._connector_version = connector_version

    @property
    def git_commit(self):
        """Gets the git_commit of this ObpApiLoopbackJson.  # noqa: E501


        :return: The git_commit of this ObpApiLoopbackJson.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this ObpApiLoopbackJson.


        :param git_commit: The git_commit of this ObpApiLoopbackJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and git_commit is None:
            raise ValueError("Invalid value for `git_commit`, must not be `None`")  # noqa: E501

        self._git_commit = git_commit

    @property
    def duration_time(self):
        """Gets the duration_time of this ObpApiLoopbackJson.  # noqa: E501


        :return: The duration_time of this ObpApiLoopbackJson.  # noqa: E501
        :rtype: str
        """
        return self._duration_time

    @duration_time.setter
    def duration_time(self, duration_time):
        """Sets the duration_time of this ObpApiLoopbackJson.


        :param duration_time: The duration_time of this ObpApiLoopbackJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and duration_time is None:
            raise ValueError("Invalid value for `duration_time`, must not be `None`")  # noqa: E501

        self._duration_time = duration_time

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
        if issubclass(ObpApiLoopbackJson, dict):
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
        if not isinstance(other, ObpApiLoopbackJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObpApiLoopbackJson):
            return True

        return self.to_dict() != other.to_dict()
