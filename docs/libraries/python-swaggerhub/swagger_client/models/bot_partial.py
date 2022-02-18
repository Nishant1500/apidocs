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

class BotPartial(object):
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
        'guild_count': 'int',
        'banner': 'str',
        'state': 'BotState',
        'nsfw': 'bool',
        'votes': 'int',
        'user': 'BaseUser'
    }

    attribute_map = {
        'description': 'description',
        'guild_count': 'guild_count',
        'banner': 'banner',
        'state': 'state',
        'nsfw': 'nsfw',
        'votes': 'votes',
        'user': 'user'
    }

    def __init__(self, description=None, guild_count=None, banner=None, state=None, nsfw=None, votes=None, user=None):  # noqa: E501
        """BotPartial - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._guild_count = None
        self._banner = None
        self._state = None
        self._nsfw = None
        self._votes = None
        self._user = None
        self.discriminator = None
        self.description = description
        self.guild_count = guild_count
        if banner is not None:
            self.banner = banner
        self.state = state
        self.nsfw = nsfw
        self.votes = votes
        self.user = user

    @property
    def description(self):
        """Gets the description of this BotPartial.  # noqa: E501


        :return: The description of this BotPartial.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BotPartial.


        :param description: The description of this BotPartial.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def guild_count(self):
        """Gets the guild_count of this BotPartial.  # noqa: E501


        :return: The guild_count of this BotPartial.  # noqa: E501
        :rtype: int
        """
        return self._guild_count

    @guild_count.setter
    def guild_count(self, guild_count):
        """Sets the guild_count of this BotPartial.


        :param guild_count: The guild_count of this BotPartial.  # noqa: E501
        :type: int
        """
        if guild_count is None:
            raise ValueError("Invalid value for `guild_count`, must not be `None`")  # noqa: E501

        self._guild_count = guild_count

    @property
    def banner(self):
        """Gets the banner of this BotPartial.  # noqa: E501


        :return: The banner of this BotPartial.  # noqa: E501
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """Sets the banner of this BotPartial.


        :param banner: The banner of this BotPartial.  # noqa: E501
        :type: str
        """

        self._banner = banner

    @property
    def state(self):
        """Gets the state of this BotPartial.  # noqa: E501


        :return: The state of this BotPartial.  # noqa: E501
        :rtype: BotState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BotPartial.


        :param state: The state of this BotPartial.  # noqa: E501
        :type: BotState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def nsfw(self):
        """Gets the nsfw of this BotPartial.  # noqa: E501


        :return: The nsfw of this BotPartial.  # noqa: E501
        :rtype: bool
        """
        return self._nsfw

    @nsfw.setter
    def nsfw(self, nsfw):
        """Sets the nsfw of this BotPartial.


        :param nsfw: The nsfw of this BotPartial.  # noqa: E501
        :type: bool
        """
        if nsfw is None:
            raise ValueError("Invalid value for `nsfw`, must not be `None`")  # noqa: E501

        self._nsfw = nsfw

    @property
    def votes(self):
        """Gets the votes of this BotPartial.  # noqa: E501


        :return: The votes of this BotPartial.  # noqa: E501
        :rtype: int
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this BotPartial.


        :param votes: The votes of this BotPartial.  # noqa: E501
        :type: int
        """
        if votes is None:
            raise ValueError("Invalid value for `votes`, must not be `None`")  # noqa: E501

        self._votes = votes

    @property
    def user(self):
        """Gets the user of this BotPartial.  # noqa: E501


        :return: The user of this BotPartial.  # noqa: E501
        :rtype: BaseUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BotPartial.


        :param user: The user of this BotPartial.  # noqa: E501
        :type: BaseUser
        """
        if user is None:
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
        if issubclass(BotPartial, dict):
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
        if not isinstance(other, BotPartial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other