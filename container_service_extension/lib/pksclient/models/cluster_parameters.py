# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterParameters(object):
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
        'kubernetes_master_host': 'str',
        'kubernetes_master_port': 'int',
        'worker_haproxy_ip_addresses': 'str',
        'kubernetes_worker_instances': 'int',
        'authorization_mode': 'str',
        'kubernetes_setting_plan_details': 'KubernetesSettings',
        'kubernetes_setting_cluster_details': 'KubernetesSettings',
        'nsxt_network_profile': 'str',
        'nsxt_network_details': 'str',
        'compute_profile': 'str',
        'k8s_customization_parameters': 'KubernetesCustomizationParameters',
        'custom_ca_certs': 'list[CustomCaCert]',
        'cluster_tags': 'list[ClusterTag]'
    }

    attribute_map = {
        'kubernetes_master_host': 'kubernetes_master_host',
        'kubernetes_master_port': 'kubernetes_master_port',
        'worker_haproxy_ip_addresses': 'worker_haproxy_ip_addresses',
        'kubernetes_worker_instances': 'kubernetes_worker_instances',
        'authorization_mode': 'authorization_mode',
        'kubernetes_setting_plan_details': 'kubernetes_setting_plan_details',
        'kubernetes_setting_cluster_details': 'kubernetes_setting_cluster_details',
        'nsxt_network_profile': 'nsxt_network_profile',
        'nsxt_network_details': 'nsxt_network_details',
        'compute_profile': 'compute_profile',
        'k8s_customization_parameters': 'k8s_customization_parameters',
        'custom_ca_certs': 'custom_ca_certs',
        'cluster_tags': 'cluster_tags'
    }

    def __init__(self, kubernetes_master_host=None, kubernetes_master_port=8443, worker_haproxy_ip_addresses=None, kubernetes_worker_instances=None, authorization_mode=None, kubernetes_setting_plan_details=None, kubernetes_setting_cluster_details=None, nsxt_network_profile=None, nsxt_network_details=None, compute_profile=None, k8s_customization_parameters=None, custom_ca_certs=None, cluster_tags=None):  # noqa: E501
        """ClusterParameters - a model defined in Swagger"""  # noqa: E501

        self._kubernetes_master_host = None
        self._kubernetes_master_port = None
        self._worker_haproxy_ip_addresses = None
        self._kubernetes_worker_instances = None
        self._authorization_mode = None
        self._kubernetes_setting_plan_details = None
        self._kubernetes_setting_cluster_details = None
        self._nsxt_network_profile = None
        self._nsxt_network_details = None
        self._compute_profile = None
        self._k8s_customization_parameters = None
        self._custom_ca_certs = None
        self._cluster_tags = None
        self.discriminator = None

        self.kubernetes_master_host = kubernetes_master_host
        if kubernetes_master_port is not None:
            self.kubernetes_master_port = kubernetes_master_port
        if worker_haproxy_ip_addresses is not None:
            self.worker_haproxy_ip_addresses = worker_haproxy_ip_addresses
        if kubernetes_worker_instances is not None:
            self.kubernetes_worker_instances = kubernetes_worker_instances
        if authorization_mode is not None:
            self.authorization_mode = authorization_mode
        if kubernetes_setting_plan_details is not None:
            self.kubernetes_setting_plan_details = kubernetes_setting_plan_details
        if kubernetes_setting_cluster_details is not None:
            self.kubernetes_setting_cluster_details = kubernetes_setting_cluster_details
        if nsxt_network_profile is not None:
            self.nsxt_network_profile = nsxt_network_profile
        if nsxt_network_details is not None:
            self.nsxt_network_details = nsxt_network_details
        if compute_profile is not None:
            self.compute_profile = compute_profile
        if k8s_customization_parameters is not None:
            self.k8s_customization_parameters = k8s_customization_parameters
        if custom_ca_certs is not None:
            self.custom_ca_certs = custom_ca_certs
        if cluster_tags is not None:
            self.cluster_tags = cluster_tags

    @property
    def kubernetes_master_host(self):
        """Gets the kubernetes_master_host of this ClusterParameters.  # noqa: E501


        :return: The kubernetes_master_host of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_master_host

    @kubernetes_master_host.setter
    def kubernetes_master_host(self, kubernetes_master_host):
        """Sets the kubernetes_master_host of this ClusterParameters.


        :param kubernetes_master_host: The kubernetes_master_host of this ClusterParameters.  # noqa: E501
        :type: str
        """
        if kubernetes_master_host is None:
            raise ValueError("Invalid value for `kubernetes_master_host`, must not be `None`")  # noqa: E501
        if kubernetes_master_host is not None and len(kubernetes_master_host) > 64:
            raise ValueError("Invalid value for `kubernetes_master_host`, length must be less than or equal to `64`")  # noqa: E501

        self._kubernetes_master_host = kubernetes_master_host

    @property
    def kubernetes_master_port(self):
        """Gets the kubernetes_master_port of this ClusterParameters.  # noqa: E501


        :return: The kubernetes_master_port of this ClusterParameters.  # noqa: E501
        :rtype: int
        """
        return self._kubernetes_master_port

    @kubernetes_master_port.setter
    def kubernetes_master_port(self, kubernetes_master_port):
        """Sets the kubernetes_master_port of this ClusterParameters.


        :param kubernetes_master_port: The kubernetes_master_port of this ClusterParameters.  # noqa: E501
        :type: int
        """

        self._kubernetes_master_port = kubernetes_master_port

    @property
    def worker_haproxy_ip_addresses(self):
        """Gets the worker_haproxy_ip_addresses of this ClusterParameters.  # noqa: E501


        :return: The worker_haproxy_ip_addresses of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._worker_haproxy_ip_addresses

    @worker_haproxy_ip_addresses.setter
    def worker_haproxy_ip_addresses(self, worker_haproxy_ip_addresses):
        """Sets the worker_haproxy_ip_addresses of this ClusterParameters.


        :param worker_haproxy_ip_addresses: The worker_haproxy_ip_addresses of this ClusterParameters.  # noqa: E501
        :type: str
        """

        self._worker_haproxy_ip_addresses = worker_haproxy_ip_addresses

    @property
    def kubernetes_worker_instances(self):
        """Gets the kubernetes_worker_instances of this ClusterParameters.  # noqa: E501


        :return: The kubernetes_worker_instances of this ClusterParameters.  # noqa: E501
        :rtype: int
        """
        return self._kubernetes_worker_instances

    @kubernetes_worker_instances.setter
    def kubernetes_worker_instances(self, kubernetes_worker_instances):
        """Sets the kubernetes_worker_instances of this ClusterParameters.


        :param kubernetes_worker_instances: The kubernetes_worker_instances of this ClusterParameters.  # noqa: E501
        :type: int
        """
        if kubernetes_worker_instances is not None and kubernetes_worker_instances < 1:  # noqa: E501
            raise ValueError("Invalid value for `kubernetes_worker_instances`, must be a value greater than or equal to `1`")  # noqa: E501

        self._kubernetes_worker_instances = kubernetes_worker_instances

    @property
    def authorization_mode(self):
        """Gets the authorization_mode of this ClusterParameters.  # noqa: E501


        :return: The authorization_mode of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, authorization_mode):
        """Sets the authorization_mode of this ClusterParameters.


        :param authorization_mode: The authorization_mode of this ClusterParameters.  # noqa: E501
        :type: str
        """

        self._authorization_mode = authorization_mode

    @property
    def kubernetes_setting_plan_details(self):
        """Gets the kubernetes_setting_plan_details of this ClusterParameters.  # noqa: E501


        :return: The kubernetes_setting_plan_details of this ClusterParameters.  # noqa: E501
        :rtype: KubernetesSettings
        """
        return self._kubernetes_setting_plan_details

    @kubernetes_setting_plan_details.setter
    def kubernetes_setting_plan_details(self, kubernetes_setting_plan_details):
        """Sets the kubernetes_setting_plan_details of this ClusterParameters.


        :param kubernetes_setting_plan_details: The kubernetes_setting_plan_details of this ClusterParameters.  # noqa: E501
        :type: KubernetesSettings
        """

        self._kubernetes_setting_plan_details = kubernetes_setting_plan_details

    @property
    def kubernetes_setting_cluster_details(self):
        """Gets the kubernetes_setting_cluster_details of this ClusterParameters.  # noqa: E501


        :return: The kubernetes_setting_cluster_details of this ClusterParameters.  # noqa: E501
        :rtype: KubernetesSettings
        """
        return self._kubernetes_setting_cluster_details

    @kubernetes_setting_cluster_details.setter
    def kubernetes_setting_cluster_details(self, kubernetes_setting_cluster_details):
        """Sets the kubernetes_setting_cluster_details of this ClusterParameters.


        :param kubernetes_setting_cluster_details: The kubernetes_setting_cluster_details of this ClusterParameters.  # noqa: E501
        :type: KubernetesSettings
        """

        self._kubernetes_setting_cluster_details = kubernetes_setting_cluster_details

    @property
    def nsxt_network_profile(self):
        """Gets the nsxt_network_profile of this ClusterParameters.  # noqa: E501


        :return: The nsxt_network_profile of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._nsxt_network_profile

    @nsxt_network_profile.setter
    def nsxt_network_profile(self, nsxt_network_profile):
        """Sets the nsxt_network_profile of this ClusterParameters.


        :param nsxt_network_profile: The nsxt_network_profile of this ClusterParameters.  # noqa: E501
        :type: str
        """

        self._nsxt_network_profile = nsxt_network_profile

    @property
    def nsxt_network_details(self):
        """Gets the nsxt_network_details of this ClusterParameters.  # noqa: E501


        :return: The nsxt_network_details of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._nsxt_network_details

    @nsxt_network_details.setter
    def nsxt_network_details(self, nsxt_network_details):
        """Sets the nsxt_network_details of this ClusterParameters.


        :param nsxt_network_details: The nsxt_network_details of this ClusterParameters.  # noqa: E501
        :type: str
        """

        self._nsxt_network_details = nsxt_network_details

    @property
    def compute_profile(self):
        """Gets the compute_profile of this ClusterParameters.  # noqa: E501


        :return: The compute_profile of this ClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._compute_profile

    @compute_profile.setter
    def compute_profile(self, compute_profile):
        """Sets the compute_profile of this ClusterParameters.


        :param compute_profile: The compute_profile of this ClusterParameters.  # noqa: E501
        :type: str
        """

        self._compute_profile = compute_profile

    @property
    def k8s_customization_parameters(self):
        """Gets the k8s_customization_parameters of this ClusterParameters.  # noqa: E501


        :return: The k8s_customization_parameters of this ClusterParameters.  # noqa: E501
        :rtype: KubernetesCustomizationParameters
        """
        return self._k8s_customization_parameters

    @k8s_customization_parameters.setter
    def k8s_customization_parameters(self, k8s_customization_parameters):
        """Sets the k8s_customization_parameters of this ClusterParameters.


        :param k8s_customization_parameters: The k8s_customization_parameters of this ClusterParameters.  # noqa: E501
        :type: KubernetesCustomizationParameters
        """

        self._k8s_customization_parameters = k8s_customization_parameters

    @property
    def custom_ca_certs(self):
        """Gets the custom_ca_certs of this ClusterParameters.  # noqa: E501


        :return: The custom_ca_certs of this ClusterParameters.  # noqa: E501
        :rtype: list[CustomCaCert]
        """
        return self._custom_ca_certs

    @custom_ca_certs.setter
    def custom_ca_certs(self, custom_ca_certs):
        """Sets the custom_ca_certs of this ClusterParameters.


        :param custom_ca_certs: The custom_ca_certs of this ClusterParameters.  # noqa: E501
        :type: list[CustomCaCert]
        """

        self._custom_ca_certs = custom_ca_certs

    @property
    def cluster_tags(self):
        """Gets the cluster_tags of this ClusterParameters.  # noqa: E501


        :return: The cluster_tags of this ClusterParameters.  # noqa: E501
        :rtype: list[ClusterTag]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        """Sets the cluster_tags of this ClusterParameters.


        :param cluster_tags: The cluster_tags of this ClusterParameters.  # noqa: E501
        :type: list[ClusterTag]
        """

        self._cluster_tags = cluster_tags

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
        if issubclass(ClusterParameters, dict):
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
        if not isinstance(other, ClusterParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other