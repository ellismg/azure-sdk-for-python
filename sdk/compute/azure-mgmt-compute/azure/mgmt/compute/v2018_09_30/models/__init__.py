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

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import CreationData
    from ._models_py3 import Disk
    from ._models_py3 import DiskSku
    from ._models_py3 import DiskUpdate
    from ._models_py3 import EncryptionSettingsCollection
    from ._models_py3 import EncryptionSettingsElement
    from ._models_py3 import GrantAccessData
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import Resource
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotSku
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
except (SyntaxError, ImportError):
    from ._models import AccessUri
    from ._models import CreationData
    from ._models import Disk
    from ._models import DiskSku
    from ._models import DiskUpdate
    from ._models import EncryptionSettingsCollection
    from ._models import EncryptionSettingsElement
    from ._models import GrantAccessData
    from ._models import ImageDiskReference
    from ._models import KeyVaultAndKeyReference
    from ._models import KeyVaultAndSecretReference
    from ._models import Resource
    from ._models import Snapshot
    from ._models import SnapshotSku
    from ._models import SnapshotUpdate
    from ._models import SourceVault
from ._paged_models import DiskPaged
from ._paged_models import SnapshotPaged
from ._compute_management_client_enums import (
    DiskStorageAccountTypes,
    OperatingSystemTypes,
    HyperVGeneration,
    DiskCreateOption,
    DiskState,
    SnapshotStorageAccountTypes,
    AccessLevel,
)

__all__ = [
    'AccessUri',
    'CreationData',
    'Disk',
    'DiskSku',
    'DiskUpdate',
    'EncryptionSettingsCollection',
    'EncryptionSettingsElement',
    'GrantAccessData',
    'ImageDiskReference',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'Resource',
    'Snapshot',
    'SnapshotSku',
    'SnapshotUpdate',
    'SourceVault',
    'DiskPaged',
    'SnapshotPaged',
    'DiskStorageAccountTypes',
    'OperatingSystemTypes',
    'HyperVGeneration',
    'DiskCreateOption',
    'DiskState',
    'SnapshotStorageAccountTypes',
    'AccessLevel',
]
