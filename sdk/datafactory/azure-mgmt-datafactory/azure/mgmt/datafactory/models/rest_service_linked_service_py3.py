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

from .linked_service_py3 import LinkedService


class RestServiceLinkedService(LinkedService):
    """Rest Service linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     linked service.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param url: Required. The base URL of the REST service.
    :type url: object
    :param enable_server_certificate_validation: Whether to validate server
     side SSL certificate when connecting to the endpoint.The default value is
     true. Type: boolean (or Expression with resultType boolean).
    :type enable_server_certificate_validation: object
    :param authentication_type: Required. Type of authentication used to
     connect to the REST service. Possible values include: 'Anonymous',
     'Basic', 'AadServicePrincipal', 'ManagedServiceIdentity'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.RestServiceAuthenticationType
    :param user_name: The user name used in Basic authentication type.
    :type user_name: object
    :param password: The password used in Basic authentication type.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param service_principal_id: The application's client ID used in
     AadServicePrincipal authentication type.
    :type service_principal_id: object
    :param service_principal_key: The application's key used in
     AadServicePrincipal authentication type.
    :type service_principal_key: ~azure.mgmt.datafactory.models.SecretBase
    :param tenant: The tenant information (domain name or tenant ID) used in
     AadServicePrincipal authentication type under which your application
     resides.
    :type tenant: object
    :param aad_resource_id: The resource you are requesting authorization to
     use.
    :type aad_resource_id: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'url': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'object'},
        'enable_server_certificate_validation': {'key': 'typeProperties.enableServerCertificateValidation', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'service_principal_id': {'key': 'typeProperties.servicePrincipalId', 'type': 'object'},
        'service_principal_key': {'key': 'typeProperties.servicePrincipalKey', 'type': 'SecretBase'},
        'tenant': {'key': 'typeProperties.tenant', 'type': 'object'},
        'aad_resource_id': {'key': 'typeProperties.aadResourceId', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, *, url, authentication_type, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, enable_server_certificate_validation=None, user_name=None, password=None, service_principal_id=None, service_principal_key=None, tenant=None, aad_resource_id=None, encrypted_credential=None, **kwargs) -> None:
        super(RestServiceLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.url = url
        self.enable_server_certificate_validation = enable_server_certificate_validation
        self.authentication_type = authentication_type
        self.user_name = user_name
        self.password = password
        self.service_principal_id = service_principal_id
        self.service_principal_key = service_principal_key
        self.tenant = tenant
        self.aad_resource_id = aad_resource_id
        self.encrypted_credential = encrypted_credential
        self.type = 'RestService'
