# coding: utf-8

"""
    Fates List

                 Current API: v2 beta 3             Default API: v2             API URL: https://api.fateslist.xyz             API Docs: https://apidocs.fateslist.xyz             Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen           # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Troubleshoot(object):
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
        'req_user_agent': 'str',
        'pid': 'int',
        'cf_ip': 'str',
        'user': 'BaseUser'
    }

    attribute_map = {
        'req_user_agent': 'req_user_agent',
        'pid': 'pid',
        'cf_ip': 'cf_ip',
        'user': 'user'
    }

    def __init__(self, req_user_agent=None, pid=None, cf_ip=None, user=None):  # noqa: E501
        """Troubleshoot - a model defined in Swagger"""  # noqa: E501
        self._req_user_agent = None
        self._pid = None
        self._cf_ip = None
        self._user = None
        self.discriminator = None
        if req_user_agent is not None:
            self.req_user_agent = req_user_agent
        self.pid = pid
        if cf_ip is not None:
            self.cf_ip = cf_ip
        if user is not None:
            self.user = user

    @property
    def req_user_agent(self):
        """Gets the req_user_agent of this Troubleshoot.  # noqa: E501


        :return: The req_user_agent of this Troubleshoot.  # noqa: E501
        :rtype: str
        """
        return self._req_user_agent

    @req_user_agent.setter
    def req_user_agent(self, req_user_agent):
        """Sets the req_user_agent of this Troubleshoot.


        :param req_user_agent: The req_user_agent of this Troubleshoot.  # noqa: E501
        :type: str
        """

        self._req_user_agent = req_user_agent

    @property
    def pid(self):
        """Gets the pid of this Troubleshoot.  # noqa: E501


        :return: The pid of this Troubleshoot.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this Troubleshoot.


        :param pid: The pid of this Troubleshoot.  # noqa: E501
        :type: int
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")  # noqa: E501

        self._pid = pid

    @property
    def cf_ip(self):
        """Gets the cf_ip of this Troubleshoot.  # noqa: E501


        :return: The cf_ip of this Troubleshoot.  # noqa: E501
        :rtype: str
        """
        return self._cf_ip

    @cf_ip.setter
    def cf_ip(self, cf_ip):
        """Sets the cf_ip of this Troubleshoot.


        :param cf_ip: The cf_ip of this Troubleshoot.  # noqa: E501
        :type: str
        """

        self._cf_ip = cf_ip

    @property
    def user(self):
        """Gets the user of this Troubleshoot.  # noqa: E501


        :return: The user of this Troubleshoot.  # noqa: E501
        :rtype: BaseUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Troubleshoot.


        :param user: The user of this Troubleshoot.  # noqa: E501
        :type: BaseUser
        """

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
        if issubclass(Troubleshoot, dict):
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
        if not isinstance(other, Troubleshoot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other