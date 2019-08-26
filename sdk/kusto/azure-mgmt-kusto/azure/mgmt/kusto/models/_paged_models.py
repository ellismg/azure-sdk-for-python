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

from msrest.paging import Paged


class ClusterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Cluster <azure.mgmt.kusto.models.Cluster>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Cluster]'}
    }

    def __init__(self, *args, **kwargs):

        super(ClusterPaged, self).__init__(*args, **kwargs)
class SkuDescriptionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SkuDescription <azure.mgmt.kusto.models.SkuDescription>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SkuDescription]'}
    }

    def __init__(self, *args, **kwargs):

        super(SkuDescriptionPaged, self).__init__(*args, **kwargs)
class AzureResourceSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AzureResourceSku <azure.mgmt.kusto.models.AzureResourceSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AzureResourceSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(AzureResourceSkuPaged, self).__init__(*args, **kwargs)
class DatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Database <azure.mgmt.kusto.models.Database>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Database]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabasePaged, self).__init__(*args, **kwargs)
class DatabasePrincipalPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabasePrincipal <azure.mgmt.kusto.models.DatabasePrincipal>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabasePrincipal]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabasePrincipalPaged, self).__init__(*args, **kwargs)
class DataConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataConnection <azure.mgmt.kusto.models.DataConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataConnectionPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.kusto.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
