# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LabelRequest(Model):
    """LabelRequest.

    All required parameters must be populated in order to send to Azure.

    :param begin: Required. begin of a detection time range
    :type begin: datetime
    :param end: Required. end of a detection time range
    :type end: datetime
    :param type: Required. Possible values include: 'changePoint', 'anomaly'
    :type type: str or
     ~azure.cognitiveservices.anomalydetector.models.LabelType
    :param value: Required. Possible values include: 'true', 'false'
    :type value: str or
     ~azure.cognitiveservices.anomalydetector.models.LabelValue
    """

    _validation = {
        'begin': {'required': True},
        'end': {'required': True},
        'type': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'begin': {'key': 'begin', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'LabelType'},
        'value': {'key': 'value', 'type': 'LabelValue'},
    }

    def __init__(self, **kwargs):
        super(LabelRequest, self).__init__(**kwargs)
        self.begin = kwargs.get('begin', None)
        self.end = kwargs.get('end', None)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)
