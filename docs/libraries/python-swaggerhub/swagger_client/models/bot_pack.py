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

class BotPack(object):
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
        'name': 'str',
        'description': 'str',
        'icon': 'str',
        'banner': 'str',
        'bots': 'list[str]',
        'id': 'str',
        'created_at': 'datetime',
        'owner': 'BaseUser',
        'resolved_bots': 'list[PackBot]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'icon': 'icon',
        'banner': 'banner',
        'bots': 'bots',
        'id': 'id',
        'created_at': 'created_at',
        'owner': 'owner',
        'resolved_bots': 'resolved_bots'
    }

    def __init__(self, name=None, description=None, icon=None, banner=None, bots=None, id=None, created_at=None, owner=None, resolved_bots=None):  # noqa: E501
        """BotPack - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._icon = None
        self._banner = None
        self._bots = None
        self._id = None
        self._created_at = None
        self._owner = None
        self._resolved_bots = None
        self.discriminator = None
        self.name = name
        self.description = description
        if icon is not None:
            self.icon = icon
        if banner is not None:
            self.banner = banner
        self.bots = bots
        self.id = id
        self.created_at = created_at
        self.owner = owner
        self.resolved_bots = resolved_bots

    @property
    def name(self):
        """Gets the name of this BotPack.  # noqa: E501


        :return: The name of this BotPack.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BotPack.


        :param name: The name of this BotPack.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this BotPack.  # noqa: E501


        :return: The description of this BotPack.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BotPack.


        :param description: The description of this BotPack.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this BotPack.  # noqa: E501


        :return: The icon of this BotPack.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this BotPack.


        :param icon: The icon of this BotPack.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def banner(self):
        """Gets the banner of this BotPack.  # noqa: E501


        :return: The banner of this BotPack.  # noqa: E501
        :rtype: str
        """
        return self._banner

    @banner.setter
    def banner(self, banner):
        """Sets the banner of this BotPack.


        :param banner: The banner of this BotPack.  # noqa: E501
        :type: str
        """

        self._banner = banner

    @property
    def bots(self):
        """Gets the bots of this BotPack.  # noqa: E501


        :return: The bots of this BotPack.  # noqa: E501
        :rtype: list[str]
        """
        return self._bots

    @bots.setter
    def bots(self, bots):
        """Sets the bots of this BotPack.


        :param bots: The bots of this BotPack.  # noqa: E501
        :type: list[str]
        """
        if bots is None:
            raise ValueError("Invalid value for `bots`, must not be `None`")  # noqa: E501

        self._bots = bots

    @property
    def id(self):
        """Gets the id of this BotPack.  # noqa: E501


        :return: The id of this BotPack.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BotPack.


        :param id: The id of this BotPack.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this BotPack.  # noqa: E501


        :return: The created_at of this BotPack.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BotPack.


        :param created_at: The created_at of this BotPack.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def owner(self):
        """Gets the owner of this BotPack.  # noqa: E501


        :return: The owner of this BotPack.  # noqa: E501
        :rtype: BaseUser
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BotPack.


        :param owner: The owner of this BotPack.  # noqa: E501
        :type: BaseUser
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def resolved_bots(self):
        """Gets the resolved_bots of this BotPack.  # noqa: E501


        :return: The resolved_bots of this BotPack.  # noqa: E501
        :rtype: list[PackBot]
        """
        return self._resolved_bots

    @resolved_bots.setter
    def resolved_bots(self, resolved_bots):
        """Sets the resolved_bots of this BotPack.


        :param resolved_bots: The resolved_bots of this BotPack.  # noqa: E501
        :type: list[PackBot]
        """
        if resolved_bots is None:
            raise ValueError("Invalid value for `resolved_bots`, must not be `None`")  # noqa: E501

        self._resolved_bots = resolved_bots

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
        if issubclass(BotPack, dict):
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
        if not isinstance(other, BotPack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other