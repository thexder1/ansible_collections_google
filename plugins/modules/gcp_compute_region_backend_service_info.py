#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_region_backend_service_info
description:
- Gather info for GCP RegionBackendService
short_description: Gather info for GCP RegionBackendService
version_added: '2.10'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
  region:
    description:
    - A reference to the region where the regional backend service resides.
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: get info on a region backend service
  gcp_compute_region_backend_service_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    backends:
      description:
      - The set of backends that serve this RegionBackendService.
      returned: success
      type: complex
      contains:
        balancingMode:
          description:
          - Specifies the balancing mode for this backend. Defaults to CONNECTION.
          returned: success
          type: str
        capacityScaler:
          description:
          - A multiplier applied to the group's maximum servicing capacity (based
            on UTILIZATION, RATE or CONNECTION).
          - "~>**NOTE**: This field cannot be set for INTERNAL region backend services
            (default loadBalancingScheme), but is required for non-INTERNAL backend
            service. The total capacity_scaler for all backends must be non-zero."
          - A setting of 0 means the group is completely drained, offering 0% of its
            available Capacity. Valid range is [0.0,1.0].
          returned: success
          type: str
        description:
          description:
          - An optional description of this resource.
          - Provide this property when you create the resource.
          returned: success
          type: str
        group:
          description:
          - The fully-qualified URL of an Instance Group or Network Endpoint Group
            resource. In case of instance group this defines the list of instances
            that serve traffic. Member virtual machine instances from each instance
            group must live in the same zone as the instance group itself. No two
            backends in a backend service are allowed to use same Instance Group resource.
          - For Network Endpoint Groups this defines list of endpoints. All endpoints
            of Network Endpoint Group must be hosted on instances located in the same
            zone as the Network Endpoint Group.
          - Backend services cannot mix Instance Group and Network Endpoint Group
            backends.
          - When the `load_balancing_scheme` is INTERNAL, only instance groups are
            supported.
          - Note that you must specify an Instance Group or Network Endpoint Group
            resource using the fully-qualified URL, rather than a partial URL.
          returned: success
          type: str
        maxConnections:
          description:
          - The max number of simultaneous connections for the group. Can be used
            with either CONNECTION or UTILIZATION balancing modes.
          - Cannot be set for INTERNAL backend services.
          - For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance
            or maxConnectionsPerEndpoint, as appropriate for group type, must be set.
          returned: success
          type: int
        maxConnectionsPerInstance:
          description:
          - The max number of simultaneous connections that a single backend instance
            can handle. Cannot be set for INTERNAL backend services.
          - This is used to calculate the capacity of the group.
          - Can be used in either CONNECTION or UTILIZATION balancing modes.
          - For CONNECTION mode, either maxConnections or maxConnectionsPerInstance
            must be set.
          returned: success
          type: int
        maxConnectionsPerEndpoint:
          description:
          - The max number of simultaneous connections that a single backend network
            endpoint can handle. Cannot be set for INTERNAL backend services.
          - This is used to calculate the capacity of the group. Can be used in either
            CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either
            maxConnections or maxConnectionsPerEndpoint must be set.
          returned: success
          type: int
        maxRate:
          description:
          - The max requests per second (RPS) of the group. Cannot be set for INTERNAL
            backend services.
          - Can be used with either RATE or UTILIZATION balancing modes, but required
            if RATE mode. Either maxRate or one of maxRatePerInstance or maxRatePerEndpoint,
            as appropriate for group type, must be set.
          returned: success
          type: int
        maxRatePerInstance:
          description:
          - The max requests per second (RPS) that a single backend instance can handle.
            This is used to calculate the capacity of the group. Can be used in either
            balancing mode. For RATE mode, either maxRate or maxRatePerInstance must
            be set. Cannot be set for INTERNAL backend services.
          returned: success
          type: str
        maxRatePerEndpoint:
          description:
          - The max requests per second (RPS) that a single backend network endpoint
            can handle. This is used to calculate the capacity of the group. Can be
            used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint
            must be set. Cannot be set for INTERNAL backend services.
          returned: success
          type: str
        maxUtilization:
          description:
          - Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization
            target for the group. Valid range is [0.0, 1.0].
          - Cannot be set for INTERNAL backend services.
          returned: success
          type: str
    connectionDraining:
      description:
      - Settings for connection draining .
      returned: success
      type: complex
      contains:
        drainingTimeoutSec:
          description:
          - Time for which instance will be drained (not accept new connections, but
            still work to finish started).
          returned: success
          type: int
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource.
      returned: success
      type: str
    fingerprint:
      description:
      - Fingerprint of this resource. A hash of the contents stored in this object.
        This field is used in optimistic locking.
      returned: success
      type: str
    healthChecks:
      description:
      - The set of URLs to HealthCheck resources for health checking this RegionBackendService.
        Currently at most one health check can be specified, and a health check is
        required.
      returned: success
      type: list
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    loadBalancingScheme:
      description:
      - Indicates what kind of load balancing this regional backend service will be
        used for. A backend service created for one type of load balancing cannot
        be used with the other(s). Must be `INTERNAL` or `INTERNAL_MANAGED`. Defaults
        to `INTERNAL`.
      returned: success
      type: str
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    protocol:
      description:
      - The protocol this RegionBackendService uses to communicate with backends.
      - 'Possible values are HTTP, HTTPS, HTTP2, SSL, TCP, and UDP. The default is
        HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and
        may result in errors if used with the GA API.'
      returned: success
      type: str
    sessionAffinity:
      description:
      - Type of session affinity to use. The default is NONE. Session affinity is
        not applicable if the protocol is UDP.
      returned: success
      type: str
    timeoutSec:
      description:
      - How many seconds to wait for the backend before considering it a failed request.
        Default is 30 seconds. Valid range is [1, 86400].
      returned: success
      type: int
    region:
      description:
      - A reference to the region where the regional backend service resides.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
