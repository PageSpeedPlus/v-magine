# Copyright 2014 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import wmi


class HostUtilsV2(object):
    def __init__(self, host='.'):
        self._wmi_cimv2_namespace = "//./root/cimv2"

    @property
    def _conn_cimv2(self):
        self._wmi_conn_cimv2 = wmi.WMI(moniker=self._wmi_cimv2_namespace)
        return self._wmi_conn_cimv2

    def get_host_available_memory_mb(self):
        c = self._conn_cimv2
        d = c.Win32_PerfRawData_BalancerStats_HyperVDynamicMemoryBalancer()
        return d[0].AvailableMemory
