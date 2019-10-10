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


class UpdateDataLakeAnalyticsAccountParameters(Model):
    """The parameters that can be used to update an existing Data Lake Analytics
    account.

    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param data_lake_store_accounts: The list of Data Lake Store accounts
     associated with this account.
    :type data_lake_store_accounts:
     list[~azure.mgmt.datalake.analytics.account.models.UpdateDataLakeStoreWithAccountParameters]
    :param storage_accounts: The list of Azure Blob storage accounts
     associated with this account.
    :type storage_accounts:
     list[~azure.mgmt.datalake.analytics.account.models.UpdateStorageAccountWithAccountParameters]
    :param compute_policies: The list of compute policies associated with this
     account.
    :type compute_policies:
     list[~azure.mgmt.datalake.analytics.account.models.UpdateComputePolicyWithAccountParameters]
    :param firewall_rules: The list of firewall rules associated with this
     account.
    :type firewall_rules:
     list[~azure.mgmt.datalake.analytics.account.models.UpdateFirewallRuleWithAccountParameters]
    :param firewall_state: The current state of the IP address firewall for
     this account. Disabling the firewall does not remove existing rules, they
     will just be ignored until the firewall is re-enabled. Possible values
     include: 'Enabled', 'Disabled'
    :type firewall_state: str or
     ~azure.mgmt.datalake.analytics.account.models.FirewallState
    :param firewall_allow_azure_ips: The current state of allowing or
     disallowing IPs originating within Azure through the firewall. If the
     firewall is disabled, this is not enforced. Possible values include:
     'Enabled', 'Disabled'
    :type firewall_allow_azure_ips: str or
     ~azure.mgmt.datalake.analytics.account.models.FirewallAllowAzureIpsState
    :param new_tier: The commitment tier to use for next month. Possible
     values include: 'Consumption', 'Commitment_100AUHours',
     'Commitment_500AUHours', 'Commitment_1000AUHours',
     'Commitment_5000AUHours', 'Commitment_10000AUHours',
     'Commitment_50000AUHours', 'Commitment_100000AUHours',
     'Commitment_500000AUHours'
    :type new_tier: str or
     ~azure.mgmt.datalake.analytics.account.models.TierType
    :param max_job_count: The maximum supported jobs running under the account
     at the same time.
    :type max_job_count: int
    :param max_degree_of_parallelism: The maximum supported degree of
     parallelism for this account.
    :type max_degree_of_parallelism: int
    :param max_degree_of_parallelism_per_job: The maximum supported degree of
     parallelism per job for this account.
    :type max_degree_of_parallelism_per_job: int
    :param min_priority_per_job: The minimum supported priority per job for
     this account.
    :type min_priority_per_job: int
    :param query_store_retention: The number of days that job metadata is
     retained.
    :type query_store_retention: int
    """

    _validation = {
        'max_job_count': {'minimum': 1},
        'max_degree_of_parallelism': {'minimum': 1},
        'max_degree_of_parallelism_per_job': {'minimum': 1},
        'min_priority_per_job': {'minimum': 1},
        'query_store_retention': {'maximum': 180, 'minimum': 1},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'data_lake_store_accounts': {'key': 'properties.dataLakeStoreAccounts', 'type': '[UpdateDataLakeStoreWithAccountParameters]'},
        'storage_accounts': {'key': 'properties.storageAccounts', 'type': '[UpdateStorageAccountWithAccountParameters]'},
        'compute_policies': {'key': 'properties.computePolicies', 'type': '[UpdateComputePolicyWithAccountParameters]'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[UpdateFirewallRuleWithAccountParameters]'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_allow_azure_ips': {'key': 'properties.firewallAllowAzureIps', 'type': 'FirewallAllowAzureIpsState'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
        'max_job_count': {'key': 'properties.maxJobCount', 'type': 'int'},
        'max_degree_of_parallelism': {'key': 'properties.maxDegreeOfParallelism', 'type': 'int'},
        'max_degree_of_parallelism_per_job': {'key': 'properties.maxDegreeOfParallelismPerJob', 'type': 'int'},
        'min_priority_per_job': {'key': 'properties.minPriorityPerJob', 'type': 'int'},
        'query_store_retention': {'key': 'properties.queryStoreRetention', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(UpdateDataLakeAnalyticsAccountParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.data_lake_store_accounts = kwargs.get('data_lake_store_accounts', None)
        self.storage_accounts = kwargs.get('storage_accounts', None)
        self.compute_policies = kwargs.get('compute_policies', None)
        self.firewall_rules = kwargs.get('firewall_rules', None)
        self.firewall_state = kwargs.get('firewall_state', None)
        self.firewall_allow_azure_ips = kwargs.get('firewall_allow_azure_ips', None)
        self.new_tier = kwargs.get('new_tier', None)
        self.max_job_count = kwargs.get('max_job_count', None)
        self.max_degree_of_parallelism = kwargs.get('max_degree_of_parallelism', None)
        self.max_degree_of_parallelism_per_job = kwargs.get('max_degree_of_parallelism_per_job', None)
        self.min_priority_per_job = kwargs.get('min_priority_per_job', None)
        self.query_store_retention = kwargs.get('query_store_retention', None)