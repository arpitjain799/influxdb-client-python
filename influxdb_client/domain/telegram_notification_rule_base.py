# coding: utf-8

"""
Influx OSS API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.notification_rule_discriminator import NotificationRuleDiscriminator


class TelegramNotificationRuleBase(NotificationRuleDiscriminator):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'message_template': 'str',
        'parse_mode': 'str',
        'disable_web_page_preview': 'bool',
        'latest_completed': 'datetime',
        'last_run_status': 'str',
        'last_run_error': 'str',
        'id': 'str',
        'endpoint_id': 'str',
        'org_id': 'str',
        'task_id': 'str',
        'owner_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'TaskStatusType',
        'name': 'str',
        'sleep_until': 'str',
        'every': 'str',
        'offset': 'str',
        'runbook_link': 'str',
        'limit_every': 'int',
        'limit': 'int',
        'tag_rules': 'list[TagRule]',
        'description': 'str',
        'status_rules': 'list[StatusRule]',
        'labels': 'list[Label]',
        'links': 'NotificationRuleBaseLinks'
    }

    attribute_map = {
        'type': 'type',
        'message_template': 'messageTemplate',
        'parse_mode': 'parseMode',
        'disable_web_page_preview': 'disableWebPagePreview',
        'latest_completed': 'latestCompleted',
        'last_run_status': 'lastRunStatus',
        'last_run_error': 'lastRunError',
        'id': 'id',
        'endpoint_id': 'endpointID',
        'org_id': 'orgID',
        'task_id': 'taskID',
        'owner_id': 'ownerID',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'status': 'status',
        'name': 'name',
        'sleep_until': 'sleepUntil',
        'every': 'every',
        'offset': 'offset',
        'runbook_link': 'runbookLink',
        'limit_every': 'limitEvery',
        'limit': 'limit',
        'tag_rules': 'tagRules',
        'description': 'description',
        'status_rules': 'statusRules',
        'labels': 'labels',
        'links': 'links'
    }

    def __init__(self, type=None, message_template=None, parse_mode=None, disable_web_page_preview=None, latest_completed=None, last_run_status=None, last_run_error=None, id=None, endpoint_id=None, org_id=None, task_id=None, owner_id=None, created_at=None, updated_at=None, status=None, name=None, sleep_until=None, every=None, offset=None, runbook_link=None, limit_every=None, limit=None, tag_rules=None, description=None, status_rules=None, labels=None, links=None):  # noqa: E501,D401,D403
        """TelegramNotificationRuleBase - a model defined in OpenAPI."""  # noqa: E501
        NotificationRuleDiscriminator.__init__(self, latest_completed=latest_completed, last_run_status=last_run_status, last_run_error=last_run_error, id=id, endpoint_id=endpoint_id, org_id=org_id, task_id=task_id, owner_id=owner_id, created_at=created_at, updated_at=updated_at, status=status, name=name, sleep_until=sleep_until, every=every, offset=offset, runbook_link=runbook_link, limit_every=limit_every, limit=limit, tag_rules=tag_rules, description=description, status_rules=status_rules, labels=labels, links=links)  # noqa: E501

        self._type = None
        self._message_template = None
        self._parse_mode = None
        self._disable_web_page_preview = None
        self.discriminator = None

        self.type = type
        self.message_template = message_template
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if disable_web_page_preview is not None:
            self.disable_web_page_preview = disable_web_page_preview

    @property
    def type(self):
        """Get the type of this TelegramNotificationRuleBase.

        The discriminator between other types of notification rules is "telegram".

        :return: The type of this TelegramNotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._type

    @type.setter
    def type(self, type):
        """Set the type of this TelegramNotificationRuleBase.

        The discriminator between other types of notification rules is "telegram".

        :param type: The type of this TelegramNotificationRuleBase.
        :type: str
        """  # noqa: E501
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def message_template(self):
        """Get the message_template of this TelegramNotificationRuleBase.

        The message template as a flux interpolated string.

        :return: The message_template of this TelegramNotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._message_template

    @message_template.setter
    def message_template(self, message_template):
        """Set the message_template of this TelegramNotificationRuleBase.

        The message template as a flux interpolated string.

        :param message_template: The message_template of this TelegramNotificationRuleBase.
        :type: str
        """  # noqa: E501
        if message_template is None:
            raise ValueError("Invalid value for `message_template`, must not be `None`")  # noqa: E501
        self._message_template = message_template

    @property
    def parse_mode(self):
        """Get the parse_mode of this TelegramNotificationRuleBase.

        Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options . Defaults to "MarkdownV2" .

        :return: The parse_mode of this TelegramNotificationRuleBase.
        :rtype: str
        """  # noqa: E501
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, parse_mode):
        """Set the parse_mode of this TelegramNotificationRuleBase.

        Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options . Defaults to "MarkdownV2" .

        :param parse_mode: The parse_mode of this TelegramNotificationRuleBase.
        :type: str
        """  # noqa: E501
        self._parse_mode = parse_mode

    @property
    def disable_web_page_preview(self):
        """Get the disable_web_page_preview of this TelegramNotificationRuleBase.

        Disables preview of web links in the sent messages when "true". Defaults to "false" .

        :return: The disable_web_page_preview of this TelegramNotificationRuleBase.
        :rtype: bool
        """  # noqa: E501
        return self._disable_web_page_preview

    @disable_web_page_preview.setter
    def disable_web_page_preview(self, disable_web_page_preview):
        """Set the disable_web_page_preview of this TelegramNotificationRuleBase.

        Disables preview of web links in the sent messages when "true". Defaults to "false" .

        :param disable_web_page_preview: The disable_web_page_preview of this TelegramNotificationRuleBase.
        :type: bool
        """  # noqa: E501
        self._disable_web_page_preview = disable_web_page_preview

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, TelegramNotificationRuleBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other