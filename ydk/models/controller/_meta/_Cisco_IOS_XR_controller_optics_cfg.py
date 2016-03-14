


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Threshold_Enum' : _MetaInfoEnum('Threshold_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg',
        {
            'low':'LOW',
            'high':'HIGH',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsLoopback_Enum' : _MetaInfoEnum('OpticsLoopback_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg',
        {
            'none':'NONE',
            'internal':'INTERNAL',
            'line':'LINE',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierGrid_Enum' : _MetaInfoEnum('OpticsDwdmCarrierGrid_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg',
        {
            '50g-hz-grid':'Y_50G_HZ_GRID',
            '100mhz-grid':'Y_100MHZ_GRID',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
    'OpticsDwdmCarrierParam_Enum' : _MetaInfoEnum('OpticsDwdmCarrierParam_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_cfg',
        {
            'itu-ch':'ITU_CH',
            'wavelength':'WAVELENGTH',
            'frequency':'FREQUENCY',
        }, 'Cisco-IOS-XR-controller-optics-cfg', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-cfg']),
}