""" Cisco_IOS_XR_ip_mobileip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-mobileip package operational data.

This module contains definitions
for the following management objects\:
  pmipv6\: Proxy Mobile IPv6

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Pmipv6Addr(Enum):
    """
    Pmipv6Addr

    Address Types

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPV4 Address

    .. data:: ipv6 = 2

    	IPV6 Address

    .. data:: pmipv6_addr_ipv4_ipv6 = 3

    	Both IPV4 and IPV6 Address

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    pmipv6_addr_ipv4_ipv6 = Enum.YLeaf(3, "pmipv6-addr-ipv4-ipv6")


class Pmipv6Encap(Enum):
    """
    Pmipv6Encap

    ENCAP Types

    .. data:: none = 0

    	None

    .. data:: ipv6 = 1

    	IPV6 Tunnel

    .. data:: ipv6_ipv4 = 2

    	IPV6 in IPV4 Tunnel

    .. data:: ipv6_udp = 3

    	IPV6 in IPV4 UDP Tunnel

    .. data:: gre_ipv4 = 4

    	GRE IPV4 Tunnel

    .. data:: gre_ipv6 = 5

    	GRE IPV6 Tunnel

    .. data:: gre = 6

    	GRE Tunnel

    .. data:: mgre_ipv4 = 7

    	MGRE IPV4 Tunnel

    .. data:: mgre_ipv6 = 8

    	MGRE IPV6 Tunnel

    .. data:: mip_udp = 9

    	MIP UDP Tunnel

    .. data:: mip_mudp = 10

    	MIP MUDP Tunnel

    .. data:: max = 11

    	MAX Encap Type

    """

    none = Enum.YLeaf(0, "none")

    ipv6 = Enum.YLeaf(1, "ipv6")

    ipv6_ipv4 = Enum.YLeaf(2, "ipv6-ipv4")

    ipv6_udp = Enum.YLeaf(3, "ipv6-udp")

    gre_ipv4 = Enum.YLeaf(4, "gre-ipv4")

    gre_ipv6 = Enum.YLeaf(5, "gre-ipv6")

    gre = Enum.YLeaf(6, "gre")

    mgre_ipv4 = Enum.YLeaf(7, "mgre-ipv4")

    mgre_ipv6 = Enum.YLeaf(8, "mgre-ipv6")

    mip_udp = Enum.YLeaf(9, "mip-udp")

    mip_mudp = Enum.YLeaf(10, "mip-mudp")

    max = Enum.YLeaf(11, "max")


class Pmipv6Role(Enum):
    """
    Pmipv6Role

    PMIPV6 Role Types

    .. data:: wlan = 0

    	WLAN

    .. data:: gpp = 1

    	3GPP

    .. data:: lte = 2

    	LTE

    .. data:: wi_max = 3

    	WiMAX

    .. data:: gma = 4

    	3GMA

    .. data:: rmax = 5

    	MAX Role

    """

    wlan = Enum.YLeaf(0, "wlan")

    gpp = Enum.YLeaf(1, "gpp")

    lte = Enum.YLeaf(2, "lte")

    wi_max = Enum.YLeaf(3, "wi-max")

    gma = Enum.YLeaf(4, "gma")

    rmax = Enum.YLeaf(5, "rmax")



class Pmipv6(Entity):
    """
    Proxy Mobile IPv6
    
    .. attribute:: lma
    
    	None
    	**type**\:  :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma>`
    
    

    """

    _prefix = 'ip-mobileip-oper'
    _revision = '2016-03-10'

    def __init__(self):
        super(Pmipv6, self).__init__()
        self._top_entity = None

        self.yang_name = "pmipv6"
        self.yang_parent_name = "Cisco-IOS-XR-ip-mobileip-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"lma" : ("lma", Pmipv6.Lma)}
        self._child_list_classes = {}

        self.lma = Pmipv6.Lma()
        self.lma.parent = self
        self._children_name_map["lma"] = "lma"
        self._children_yang_names.add("lma")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6"


    class Lma(Entity):
        """
        None
        
        .. attribute:: statistics
        
        	None
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics>`
        
        .. attribute:: bindings
        
        	Table of Binding
        	**type**\:  :py:class:`Bindings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings>`
        
        .. attribute:: heartbeats
        
        	Table of Heartbeat
        	**type**\:  :py:class:`Heartbeats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Heartbeats>`
        
        .. attribute:: config_variables
        
        	Global Configuration Variables
        	**type**\:  :py:class:`ConfigVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables>`
        
        

        """

        _prefix = 'ip-mobileip-oper'
        _revision = '2016-03-10'

        def __init__(self):
            super(Pmipv6.Lma, self).__init__()

            self.yang_name = "lma"
            self.yang_parent_name = "pmipv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"statistics" : ("statistics", Pmipv6.Lma.Statistics), "bindings" : ("bindings", Pmipv6.Lma.Bindings), "heartbeats" : ("heartbeats", Pmipv6.Lma.Heartbeats), "config-variables" : ("config_variables", Pmipv6.Lma.ConfigVariables)}
            self._child_list_classes = {}

            self.statistics = Pmipv6.Lma.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

            self.bindings = Pmipv6.Lma.Bindings()
            self.bindings.parent = self
            self._children_name_map["bindings"] = "bindings"
            self._children_yang_names.add("bindings")

            self.heartbeats = Pmipv6.Lma.Heartbeats()
            self.heartbeats.parent = self
            self._children_name_map["heartbeats"] = "heartbeats"
            self._children_yang_names.add("heartbeats")

            self.config_variables = Pmipv6.Lma.ConfigVariables()
            self.config_variables.parent = self
            self._children_name_map["config_variables"] = "config-variables"
            self._children_yang_names.add("config-variables")
            self._segment_path = lambda: "lma"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/%s" % self._segment_path()


        class Statistics(Entity):
            """
            None
            
            .. attribute:: customer_statistics
            
            	Table of CustomerStatistics
            	**type**\:  :py:class:`CustomerStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics>`
            
            .. attribute:: license
            
            	LMA License Statistics
            	**type**\:  :py:class:`License <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.License>`
            
            .. attribute:: global_
            
            	Global Statistics
            	**type**\:  :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_>`
            
            .. attribute:: mag_statistics
            
            	Table of MAGStatistics
            	**type**\:  :py:class:`MagStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "lma"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"customer-statistics" : ("customer_statistics", Pmipv6.Lma.Statistics.CustomerStatistics), "license" : ("license", Pmipv6.Lma.Statistics.License), "global" : ("global_", Pmipv6.Lma.Statistics.Global_), "mag-statistics" : ("mag_statistics", Pmipv6.Lma.Statistics.MagStatistics)}
                self._child_list_classes = {}

                self.customer_statistics = Pmipv6.Lma.Statistics.CustomerStatistics()
                self.customer_statistics.parent = self
                self._children_name_map["customer_statistics"] = "customer-statistics"
                self._children_yang_names.add("customer-statistics")

                self.license = Pmipv6.Lma.Statistics.License()
                self.license.parent = self
                self._children_name_map["license"] = "license"
                self._children_yang_names.add("license")

                self.global_ = Pmipv6.Lma.Statistics.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.mag_statistics = Pmipv6.Lma.Statistics.MagStatistics()
                self.mag_statistics.parent = self
                self._children_name_map["mag_statistics"] = "mag-statistics"
                self._children_yang_names.add("mag-statistics")
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self._segment_path()


            class CustomerStatistics(Entity):
                """
                Table of CustomerStatistics
                
                .. attribute:: customer_statistic
                
                	Customer statistics
                	**type**\: list of  		 :py:class:`CustomerStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.CustomerStatistics, self).__init__()

                    self.yang_name = "customer-statistics"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"customer-statistic" : ("customer_statistic", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic)}

                    self.customer_statistic = YList(self)
                    self._segment_path = lambda: "customer-statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics, [], name, value)


                class CustomerStatistic(Entity):
                    """
                    Customer statistics
                    
                    .. attribute:: customer_name  <key>
                    
                    	Customer Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: protocol_statistics
                    
                    	LMA Protocol Statistics
                    	**type**\:  :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics>`
                    
                    .. attribute:: accounting_statistics
                    
                    	LMA Accounting Statistics
                    	**type**\:  :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics>`
                    
                    .. attribute:: lma_identifier
                    
                    	LMA Identifier
                    	**type**\: str
                    
                    .. attribute:: bce_count
                    
                    	Count of Bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: handoff_count
                    
                    	Count of Handoffs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_mnp_count
                    
                    	Count of IPv4 Mobile Node Prefixes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6_mnp_count
                    
                    	Count of IPv6 Mobile Node Prefixes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic, self).__init__()

                        self.yang_name = "customer-statistic"
                        self.yang_parent_name = "customer-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"protocol-statistics" : ("protocol_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics), "accounting-statistics" : ("accounting_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics)}
                        self._child_list_classes = {}

                        self.customer_name = YLeaf(YType.str, "customer-name")

                        self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                        self.bce_count = YLeaf(YType.uint32, "bce-count")

                        self.handoff_count = YLeaf(YType.uint32, "handoff-count")

                        self.ipv4_mnp_count = YLeaf(YType.uint32, "ipv4-mnp-count")

                        self.ipv6_mnp_count = YLeaf(YType.uint32, "ipv6-mnp-count")

                        self.protocol_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics()
                        self.protocol_statistics.parent = self
                        self._children_name_map["protocol_statistics"] = "protocol-statistics"
                        self._children_yang_names.add("protocol-statistics")

                        self.accounting_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics()
                        self.accounting_statistics.parent = self
                        self._children_name_map["accounting_statistics"] = "accounting-statistics"
                        self._children_yang_names.add("accounting-statistics")
                        self._segment_path = lambda: "customer-statistic" + "[customer-name='" + self.customer_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/customer-statistics/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic, ['customer_name', 'lma_identifier', 'bce_count', 'handoff_count', 'ipv4_mnp_count', 'ipv6_mnp_count'], name, value)


                    class ProtocolStatistics(Entity):
                        """
                        LMA Protocol Statistics
                        
                        .. attribute:: pbu_receive_statistics
                        
                        	PBU Receive Statistics
                        	**type**\:  :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics>`
                        
                        .. attribute:: pba_send_statistics
                        
                        	PBA Send Statistics
                        	**type**\:  :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics>`
                        
                        .. attribute:: pbri_send_statistics
                        
                        	PBRI Send Statistics
                        	**type**\:  :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics>`
                        
                        .. attribute:: pbri_receive_statistics
                        
                        	PBRI Receive Statistics
                        	**type**\:  :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics>`
                        
                        .. attribute:: pbra_send_statistics
                        
                        	PBRA Send Statistics
                        	**type**\:  :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics>`
                        
                        .. attribute:: pbra_receive_statistics
                        
                        	PBRA Receive Statistics
                        	**type**\:  :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics, self).__init__()

                            self.yang_name = "protocol-statistics"
                            self.yang_parent_name = "customer-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"pbu-receive-statistics" : ("pbu_receive_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics), "pba-send-statistics" : ("pba_send_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics), "pbri-send-statistics" : ("pbri_send_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics), "pbri-receive-statistics" : ("pbri_receive_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics), "pbra-send-statistics" : ("pbra_send_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics), "pbra-receive-statistics" : ("pbra_receive_statistics", Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics)}
                            self._child_list_classes = {}

                            self.pbu_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics()
                            self.pbu_receive_statistics.parent = self
                            self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                            self._children_yang_names.add("pbu-receive-statistics")

                            self.pba_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics()
                            self.pba_send_statistics.parent = self
                            self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                            self._children_yang_names.add("pba-send-statistics")

                            self.pbri_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics()
                            self.pbri_send_statistics.parent = self
                            self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                            self._children_yang_names.add("pbri-send-statistics")

                            self.pbri_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics()
                            self.pbri_receive_statistics.parent = self
                            self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                            self._children_yang_names.add("pbri-receive-statistics")

                            self.pbra_send_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics()
                            self.pbra_send_statistics.parent = self
                            self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                            self._children_yang_names.add("pbra-send-statistics")

                            self.pbra_receive_statistics = Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics()
                            self.pbra_receive_statistics.parent = self
                            self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                            self._children_yang_names.add("pbra-receive-statistics")
                            self._segment_path = lambda: "protocol-statistics"


                        class PbuReceiveStatistics(Entity):
                            """
                            PBU Receive Statistics
                            
                            .. attribute:: pbu_count
                            
                            	Count of PBUs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbu_drop_count
                            
                            	Count of PBUs Dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                                self.yang_name = "pbu-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                                self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")
                                self._segment_path = lambda: "pbu-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbuReceiveStatistics, ['pbu_count', 'pbu_drop_count'], name, value)


                        class PbaSendStatistics(Entity):
                            """
                            PBA Send Statistics
                            
                            .. attribute:: pba_count
                            
                            	Count of PBAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pba_drop_count
                            
                            	Count of PBAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accepted_count
                            
                            	Count of Status Code \- Binding Update accepted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_count
                            
                            	Count of Status Code \- Last BA status code sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_failure_count
                            
                            	Count of Status Code \- Reason unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_failure_count
                            
                            	Count of Status Code \- Administratively prohibited
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resource_failure_count
                            
                            	Count of Status Code \- Insufficient resources
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_reg_failure_count
                            
                            	Count of Status Code \- Home registration not supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_subnet_failure_count
                            
                            	Count of Status Code \- Not home subnet
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_sequence_failure_count
                            
                            	Count of Status Code \- Sequence number out of window
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reg_type_failure_count
                            
                            	Count of Status Code \- Registration type change
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_failure_count
                            
                            	Count of Status Code \- Auth Fail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_reg_not_enabled_count
                            
                            	Count of Status Code \- Proxy Registration not enabled
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: not_lma_for_this_mn_count
                            
                            	Count of Status Code \- Not LMA for this Mobile Node
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_proxy_reg_count
                            
                            	Count of Status Code \- MAG not auth.for proxyreg
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_hnp_count
                            
                            	Count of Status Code \- Not authorized for HNP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_mismatch_count
                            
                            	Count of Status Code \- Invalid timestamp value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_lower_than_previous_accepted_count
                            
                            	Count of Status Code \- Timestamp lower than previous accepted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hnp_opt_count
                            
                            	Count of Status Code \- Missing Home Network Prefix option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_hnps_do_not_match_bce_hnps_count
                            
                            	Count of Status Code \- Recevied HNPs do not match with BCE
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_mn_id_opt_count
                            
                            	Count of Status Code \- Missing MN identifier option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hi_opt_count
                            
                            	Count of Status Code \- Missing Handoff Indicator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_access_tech_type_opt_count
                            
                            	Count of Status Code \- Missing ATT option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv4 mobility
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_hoa_count
                            
                            	Count of Status Code \- Not authorized for IPv4 HoA
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv6_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv6 mobility
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple_ipv4_ho_a_not_supported_count
                            
                            	Count of Status Code \- Multiple IPv4 HoA not supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gre_key_opt_required_count
                            
                            	Count of Status Code \- GRE Key option is required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics, self).__init__()

                                self.yang_name = "pba-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pba_count = YLeaf(YType.uint64, "pba-count")

                                self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                                self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                                self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                                self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                                self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                                self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                                self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                                self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                                self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                                self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                                self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                                self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                                self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                                self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                                self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                                self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                                self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                                self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                                self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                                self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                                self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                                self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                                self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                                self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                                self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                                self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                                self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")
                                self._segment_path = lambda: "pba-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbaSendStatistics, ['pba_count', 'pba_drop_count', 'accepted_count', 'unknown_count', 'unspecified_failure_count', 'admin_failure_count', 'resource_failure_count', 'home_reg_failure_count', 'home_subnet_failure_count', 'bad_sequence_failure_count', 'reg_type_failure_count', 'authen_failure_count', 'proxy_reg_not_enabled_count', 'not_lma_for_this_mn_count', 'no_author_for_proxy_reg_count', 'no_author_for_hnp_count', 'timestamp_mismatch_count', 'timestamp_lower_than_previous_accepted_count', 'missing_hnp_opt_count', 'received_hnps_do_not_match_bce_hnps_count', 'missing_mn_id_opt_count', 'missing_hi_opt_count', 'missing_access_tech_type_opt_count', 'no_author_for_ipv4_mobility_count', 'no_author_for_ipv4_hoa_count', 'no_author_for_ipv6_mobility_count', 'multiple_ipv4_ho_a_not_supported_count', 'gre_key_opt_required_count'], name, value)


                        class PbriSendStatistics(Entity):
                            """
                            PBRI Send Statistics
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics, self).__init__()

                                self.yang_name = "pbri-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                                self._segment_path = lambda: "pbri-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriSendStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                        class PbriReceiveStatistics(Entity):
                            """
                            PBRI Receive Statistics
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                                self.yang_name = "pbri-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                                self._segment_path = lambda: "pbri-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbriReceiveStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                        class PbraSendStatistics(Entity):
                            """
                            PBRA Send Statistics
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics, self).__init__()

                                self.yang_name = "pbra-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                                self._segment_path = lambda: "pbra-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraSendStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


                        class PbraReceiveStatistics(Entity):
                            """
                            PBRA Receive Statistics
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                                self.yang_name = "pbra-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                                self._segment_path = lambda: "pbra-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.ProtocolStatistics.PbraReceiveStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


                    class AccountingStatistics(Entity):
                        """
                        LMA Accounting Statistics
                        
                        .. attribute:: accounting_start_sent_count
                        
                        	Count of Accounting Start Records Sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: accounting_update_sent_count
                        
                        	Count of Accounting Update Records Sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: accounting_stop_sent_count
                        
                        	Count of Accounting Stop Records Sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics, self).__init__()

                            self.yang_name = "accounting-statistics"
                            self.yang_parent_name = "customer-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.accounting_start_sent_count = YLeaf(YType.uint64, "accounting-start-sent-count")

                            self.accounting_update_sent_count = YLeaf(YType.uint64, "accounting-update-sent-count")

                            self.accounting_stop_sent_count = YLeaf(YType.uint64, "accounting-stop-sent-count")
                            self._segment_path = lambda: "accounting-statistics"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.CustomerStatistics.CustomerStatistic.AccountingStatistics, ['accounting_start_sent_count', 'accounting_update_sent_count', 'accounting_stop_sent_count'], name, value)


            class License(Entity):
                """
                LMA License Statistics
                
                .. attribute:: lma_identifier
                
                	LMA Identifier
                	**type**\: str
                
                .. attribute:: bce_count
                
                	Instantaneous Count of Bindings
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_bce_count
                
                	Peak Count of Bindings
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_bce_count_reset_timestamp
                
                	Timestamp when the Peak Count of Bindings was reset
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.License, self).__init__()

                    self.yang_name = "license"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                    self.bce_count = YLeaf(YType.uint32, "bce-count")

                    self.peak_bce_count = YLeaf(YType.uint32, "peak-bce-count")

                    self.peak_bce_count_reset_timestamp = YLeaf(YType.uint32, "peak-bce-count-reset-timestamp")
                    self._segment_path = lambda: "license"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Statistics.License, ['lma_identifier', 'bce_count', 'peak_bce_count', 'peak_bce_count_reset_timestamp'], name, value)


            class Global_(Entity):
                """
                Global Statistics
                
                .. attribute:: packet_statistics
                
                	Packet Statistics
                	**type**\:  :py:class:`PacketStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.PacketStatistics>`
                
                .. attribute:: protocol_statistics
                
                	LMA Protocol Statistics
                	**type**\:  :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics>`
                
                .. attribute:: accounting_statistics
                
                	LMA Accounting Statistics
                	**type**\:  :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.AccountingStatistics>`
                
                .. attribute:: lma_identifier
                
                	LMA Identifier
                	**type**\: str
                
                .. attribute:: bce_count
                
                	Count of Bindings
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: handoff_count
                
                	Count of Handoffs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: single_tenant_count
                
                	Count of Single Tenants
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: multi_tenant_count
                
                	Count of Multi Tenants
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"packet-statistics" : ("packet_statistics", Pmipv6.Lma.Statistics.Global_.PacketStatistics), "protocol-statistics" : ("protocol_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics), "accounting-statistics" : ("accounting_statistics", Pmipv6.Lma.Statistics.Global_.AccountingStatistics)}
                    self._child_list_classes = {}

                    self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                    self.bce_count = YLeaf(YType.uint32, "bce-count")

                    self.handoff_count = YLeaf(YType.uint32, "handoff-count")

                    self.single_tenant_count = YLeaf(YType.uint32, "single-tenant-count")

                    self.multi_tenant_count = YLeaf(YType.uint32, "multi-tenant-count")

                    self.packet_statistics = Pmipv6.Lma.Statistics.Global_.PacketStatistics()
                    self.packet_statistics.parent = self
                    self._children_name_map["packet_statistics"] = "packet-statistics"
                    self._children_yang_names.add("packet-statistics")

                    self.protocol_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics()
                    self.protocol_statistics.parent = self
                    self._children_name_map["protocol_statistics"] = "protocol-statistics"
                    self._children_yang_names.add("protocol-statistics")

                    self.accounting_statistics = Pmipv6.Lma.Statistics.Global_.AccountingStatistics()
                    self.accounting_statistics.parent = self
                    self._children_name_map["accounting_statistics"] = "accounting-statistics"
                    self._children_yang_names.add("accounting-statistics")
                    self._segment_path = lambda: "global"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Statistics.Global_, ['lma_identifier', 'bce_count', 'handoff_count', 'single_tenant_count', 'multi_tenant_count'], name, value)


                class PacketStatistics(Entity):
                    """
                    Packet Statistics
                    
                    .. attribute:: checksum_errors
                    
                    	Checksumm errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: send_drops
                    
                    	Drop count of sent packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: receive_drops
                    
                    	Drop count of received packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_received
                    
                    	Count of received packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Count of sent packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: send_drops_ipv6
                    
                    	Drop count of IPv6 sent packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: receive_drops_ipv6
                    
                    	Drop count of IPv6 received packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_received_ipv6
                    
                    	Count of IPv6 received packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent_ipv6
                    
                    	Count of IPv6 sent packets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.PacketStatistics, self).__init__()

                        self.yang_name = "packet-statistics"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.checksum_errors = YLeaf(YType.uint64, "checksum-errors")

                        self.send_drops = YLeaf(YType.uint64, "send-drops")

                        self.receive_drops = YLeaf(YType.uint64, "receive-drops")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.send_drops_ipv6 = YLeaf(YType.uint64, "send-drops-ipv6")

                        self.receive_drops_ipv6 = YLeaf(YType.uint64, "receive-drops-ipv6")

                        self.packets_received_ipv6 = YLeaf(YType.uint64, "packets-received-ipv6")

                        self.packets_sent_ipv6 = YLeaf(YType.uint64, "packets-sent-ipv6")
                        self._segment_path = lambda: "packet-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Statistics.Global_.PacketStatistics, ['checksum_errors', 'send_drops', 'receive_drops', 'packets_received', 'packets_sent', 'send_drops_ipv6', 'receive_drops_ipv6', 'packets_received_ipv6', 'packets_sent_ipv6'], name, value)


                class ProtocolStatistics(Entity):
                    """
                    LMA Protocol Statistics
                    
                    .. attribute:: pbu_receive_statistics
                    
                    	PBU Receive Statistics
                    	**type**\:  :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics>`
                    
                    .. attribute:: pba_send_statistics
                    
                    	PBA Send Statistics
                    	**type**\:  :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics>`
                    
                    .. attribute:: pbri_send_statistics
                    
                    	PBRI Send Statistics
                    	**type**\:  :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics>`
                    
                    .. attribute:: pbri_receive_statistics
                    
                    	PBRI Receive Statistics
                    	**type**\:  :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics>`
                    
                    .. attribute:: pbra_send_statistics
                    
                    	PBRA Send Statistics
                    	**type**\:  :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics>`
                    
                    .. attribute:: pbra_receive_statistics
                    
                    	PBRA Receive Statistics
                    	**type**\:  :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics, self).__init__()

                        self.yang_name = "protocol-statistics"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"pbu-receive-statistics" : ("pbu_receive_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics), "pba-send-statistics" : ("pba_send_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics), "pbri-send-statistics" : ("pbri_send_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics), "pbri-receive-statistics" : ("pbri_receive_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics), "pbra-send-statistics" : ("pbra_send_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics), "pbra-receive-statistics" : ("pbra_receive_statistics", Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics)}
                        self._child_list_classes = {}

                        self.pbu_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics()
                        self.pbu_receive_statistics.parent = self
                        self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                        self._children_yang_names.add("pbu-receive-statistics")

                        self.pba_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics()
                        self.pba_send_statistics.parent = self
                        self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                        self._children_yang_names.add("pba-send-statistics")

                        self.pbri_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics()
                        self.pbri_send_statistics.parent = self
                        self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                        self._children_yang_names.add("pbri-send-statistics")

                        self.pbri_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics()
                        self.pbri_receive_statistics.parent = self
                        self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                        self._children_yang_names.add("pbri-receive-statistics")

                        self.pbra_send_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics()
                        self.pbra_send_statistics.parent = self
                        self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                        self._children_yang_names.add("pbra-send-statistics")

                        self.pbra_receive_statistics = Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics()
                        self.pbra_receive_statistics.parent = self
                        self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                        self._children_yang_names.add("pbra-receive-statistics")
                        self._segment_path = lambda: "protocol-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self._segment_path()


                    class PbuReceiveStatistics(Entity):
                        """
                        PBU Receive Statistics
                        
                        .. attribute:: pbu_count
                        
                        	Count of PBUs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbu_drop_count
                        
                        	Count of PBUs Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                            self.yang_name = "pbu-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                            self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")
                            self._segment_path = lambda: "pbu-receive-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbuReceiveStatistics, ['pbu_count', 'pbu_drop_count'], name, value)


                    class PbaSendStatistics(Entity):
                        """
                        PBA Send Statistics
                        
                        .. attribute:: pba_count
                        
                        	Count of PBAs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pba_drop_count
                        
                        	Count of PBAs dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accepted_count
                        
                        	Count of Status Code \- Binding Update accepted
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_count
                        
                        	Count of Status Code \- Last BA status code sent
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_failure_count
                        
                        	Count of Status Code \- Reason unspecified
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_failure_count
                        
                        	Count of Status Code \- Administratively prohibited
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resource_failure_count
                        
                        	Count of Status Code \- Insufficient resources
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: home_reg_failure_count
                        
                        	Count of Status Code \- Home registration not supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: home_subnet_failure_count
                        
                        	Count of Status Code \- Not home subnet
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: bad_sequence_failure_count
                        
                        	Count of Status Code \- Sequence number out of window
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: reg_type_failure_count
                        
                        	Count of Status Code \- Registration type change
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: authen_failure_count
                        
                        	Count of Status Code \- Auth Fail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: proxy_reg_not_enabled_count
                        
                        	Count of Status Code \- Proxy Registration not enabled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: not_lma_for_this_mn_count
                        
                        	Count of Status Code \- Not LMA for this Mobile Node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_proxy_reg_count
                        
                        	Count of Status Code \- MAG not auth.for proxyreg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_hnp_count
                        
                        	Count of Status Code \- Not authorized for HNP
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_mismatch_count
                        
                        	Count of Status Code \- Invalid timestamp value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timestamp_lower_than_previous_accepted_count
                        
                        	Count of Status Code \- Timestamp lower than previous accepted
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_hnp_opt_count
                        
                        	Count of Status Code \- Missing Home Network Prefix option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_hnps_do_not_match_bce_hnps_count
                        
                        	Count of Status Code \- Recevied HNPs do not match with BCE
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_mn_id_opt_count
                        
                        	Count of Status Code \- Missing MN identifier option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_hi_opt_count
                        
                        	Count of Status Code \- Missing Handoff Indicator
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: missing_access_tech_type_opt_count
                        
                        	Count of Status Code \- Missing ATT option
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv4_mobility_count
                        
                        	Count of Status Code \- Not authorized for IPv4 mobility
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv4_hoa_count
                        
                        	Count of Status Code \- Not authorized for IPv4 HoA
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_ipv6_mobility_count
                        
                        	Count of Status Code \- Not authorized for IPv6 mobility
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multiple_ipv4_ho_a_not_supported_count
                        
                        	Count of Status Code \- Multiple IPv4 HoA not supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: gre_key_opt_required_count
                        
                        	Count of Status Code \- GRE Key option is required
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics, self).__init__()

                            self.yang_name = "pba-send-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pba_count = YLeaf(YType.uint64, "pba-count")

                            self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                            self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                            self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                            self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                            self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                            self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                            self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                            self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                            self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                            self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                            self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                            self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                            self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                            self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                            self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                            self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                            self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                            self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                            self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                            self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                            self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                            self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                            self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                            self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                            self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                            self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                            self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")
                            self._segment_path = lambda: "pba-send-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbaSendStatistics, ['pba_count', 'pba_drop_count', 'accepted_count', 'unknown_count', 'unspecified_failure_count', 'admin_failure_count', 'resource_failure_count', 'home_reg_failure_count', 'home_subnet_failure_count', 'bad_sequence_failure_count', 'reg_type_failure_count', 'authen_failure_count', 'proxy_reg_not_enabled_count', 'not_lma_for_this_mn_count', 'no_author_for_proxy_reg_count', 'no_author_for_hnp_count', 'timestamp_mismatch_count', 'timestamp_lower_than_previous_accepted_count', 'missing_hnp_opt_count', 'received_hnps_do_not_match_bce_hnps_count', 'missing_mn_id_opt_count', 'missing_hi_opt_count', 'missing_access_tech_type_opt_count', 'no_author_for_ipv4_mobility_count', 'no_author_for_ipv4_hoa_count', 'no_author_for_ipv6_mobility_count', 'multiple_ipv4_ho_a_not_supported_count', 'gre_key_opt_required_count'], name, value)


                    class PbriSendStatistics(Entity):
                        """
                        PBRI Send Statistics
                        
                        .. attribute:: pbri_count
                        
                        	Count of PBRIs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbri_drop_count
                        
                        	Count of PBRIs dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_count
                        
                        	Count of Revoc Trigger \- Unspecified
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_reason_count
                        
                        	Count of Revoc Trigger \- Administrative Reason
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_same_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_different_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_unknown_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Unknown
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: user_session_termination_count
                        
                        	Count of Revoc Trigger \- User Init Session Terminatation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_session_termination_count
                        
                        	Count of Revoc Trigger \- Access Network Session Termination
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: out_of_sync_bce_state_count
                        
                        	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: per_peer_policy_count
                        
                        	Count of Revoc Trigger \- Per\-Peer Policy
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoking_mn_local_policy_count
                        
                        	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics, self).__init__()

                            self.yang_name = "pbri-send-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                            self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                            self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                            self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                            self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                            self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                            self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                            self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                            self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                            self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                            self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                            self._segment_path = lambda: "pbri-send-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriSendStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                    class PbriReceiveStatistics(Entity):
                        """
                        PBRI Receive Statistics
                        
                        .. attribute:: pbri_count
                        
                        	Count of PBRIs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbri_drop_count
                        
                        	Count of PBRIs dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unspecified_count
                        
                        	Count of Revoc Trigger \- Unspecified
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: admin_reason_count
                        
                        	Count of Revoc Trigger \- Administrative Reason
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_same_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_different_att_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mag_handover_unknown_count
                        
                        	Count of Revoc Trigger \- Inter MAG Handover Unknown
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: user_session_termination_count
                        
                        	Count of Revoc Trigger \- User Init Session Terminatation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: network_session_termination_count
                        
                        	Count of Revoc Trigger \- Access Network Session Termination
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: out_of_sync_bce_state_count
                        
                        	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: per_peer_policy_count
                        
                        	Count of Revoc Trigger \- Per\-Peer Policy
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoking_mn_local_policy_count
                        
                        	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                            self.yang_name = "pbri-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                            self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                            self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                            self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                            self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                            self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                            self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                            self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                            self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                            self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                            self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                            self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                            self._segment_path = lambda: "pbri-receive-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbriReceiveStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                    class PbraSendStatistics(Entity):
                        """
                        PBRA Send Statistics
                        
                        .. attribute:: pbra_count
                        
                        	Count of PBRAs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbra_drop_count
                        
                        	Count of PBRAs dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: success_count
                        
                        	Count of Revoc Status \- Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: partial_success_count
                        
                        	Count of Revoc Status \- Partial Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_binding_count
                        
                        	Count of Revoc Status \- Binding Does Not Exist
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hoa_required_count
                        
                        	Count of Revoc Status \- IPv4 Home Address Option Required
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_global_revoc_count
                        
                        	Count of Revoc Status \- Global Revocation NOT Authorized
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_identity_required_count
                        
                        	Count of Revoc Status \- Revoked Mobile Node Identity Required
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_attached_count
                        
                        	Count of Revoc Status \- Revocation Failed \- MN is Attached
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_revoc_trigger_count
                        
                        	Count of Revoc Status \- Revocation Trigger NOT supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoc_function_not_supported_count
                        
                        	Count of Revoc Status \- Revocation Function NOT Supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbr_not_supported_count
                        
                        	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics, self).__init__()

                            self.yang_name = "pbra-send-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                            self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                            self.success_count = YLeaf(YType.uint32, "success-count")

                            self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                            self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                            self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                            self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                            self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                            self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                            self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                            self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                            self._segment_path = lambda: "pbra-send-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraSendStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


                    class PbraReceiveStatistics(Entity):
                        """
                        PBRA Receive Statistics
                        
                        .. attribute:: pbra_count
                        
                        	Count of PBRAs
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pbra_drop_count
                        
                        	Count of PBRAs dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: success_count
                        
                        	Count of Revoc Status \- Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: partial_success_count
                        
                        	Count of Revoc Status \- Partial Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_binding_count
                        
                        	Count of Revoc Status \- Binding Does Not Exist
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hoa_required_count
                        
                        	Count of Revoc Status \- IPv4 Home Address Option Required
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_author_for_global_revoc_count
                        
                        	Count of Revoc Status \- Global Revocation NOT Authorized
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_identity_required_count
                        
                        	Count of Revoc Status \- Revoked Mobile Node Identity Required
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mn_attached_count
                        
                        	Count of Revoc Status \- Revocation Failed \- MN is Attached
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unknown_revoc_trigger_count
                        
                        	Count of Revoc Status \- Revocation Trigger NOT supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: revoc_function_not_supported_count
                        
                        	Count of Revoc Status \- Revocation Function NOT Supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: pbr_not_supported_count
                        
                        	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                            self.yang_name = "pbra-receive-statistics"
                            self.yang_parent_name = "protocol-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                            self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                            self.success_count = YLeaf(YType.uint32, "success-count")

                            self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                            self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                            self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                            self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                            self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                            self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                            self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                            self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                            self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                            self._segment_path = lambda: "pbra-receive-statistics"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/protocol-statistics/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.Statistics.Global_.ProtocolStatistics.PbraReceiveStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


                class AccountingStatistics(Entity):
                    """
                    LMA Accounting Statistics
                    
                    .. attribute:: accounting_start_sent_count
                    
                    	Count of Accounting Start Records Sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: accounting_update_sent_count
                    
                    	Count of Accounting Update Records Sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: accounting_stop_sent_count
                    
                    	Count of Accounting Stop Records Sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.Global_.AccountingStatistics, self).__init__()

                        self.yang_name = "accounting-statistics"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accounting_start_sent_count = YLeaf(YType.uint64, "accounting-start-sent-count")

                        self.accounting_update_sent_count = YLeaf(YType.uint64, "accounting-update-sent-count")

                        self.accounting_stop_sent_count = YLeaf(YType.uint64, "accounting-stop-sent-count")
                        self._segment_path = lambda: "accounting-statistics"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/global/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Statistics.Global_.AccountingStatistics, ['accounting_start_sent_count', 'accounting_update_sent_count', 'accounting_stop_sent_count'], name, value)


            class MagStatistics(Entity):
                """
                Table of MAGStatistics
                
                .. attribute:: mag_statistic
                
                	Peer MAG statistics
                	**type**\: list of  		 :py:class:`MagStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Statistics.MagStatistics, self).__init__()

                    self.yang_name = "mag-statistics"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"mag-statistic" : ("mag_statistic", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic)}

                    self.mag_statistic = YList(self)
                    self._segment_path = lambda: "mag-statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics, [], name, value)


                class MagStatistic(Entity):
                    """
                    Peer MAG statistics
                    
                    .. attribute:: mag_name  <key>
                    
                    	Peer MAG Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: protocol_statistics
                    
                    	LMA Protocol Statistics
                    	**type**\:  :py:class:`ProtocolStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics>`
                    
                    .. attribute:: lma_identifier
                    
                    	LMA Identifier
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic, self).__init__()

                        self.yang_name = "mag-statistic"
                        self.yang_parent_name = "mag-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"protocol-statistics" : ("protocol_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics)}
                        self._child_list_classes = {}

                        self.mag_name = YLeaf(YType.str, "mag-name")

                        self.lma_identifier = YLeaf(YType.str, "lma-identifier")

                        self.protocol_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics()
                        self.protocol_statistics.parent = self
                        self._children_name_map["protocol_statistics"] = "protocol-statistics"
                        self._children_yang_names.add("protocol-statistics")
                        self._segment_path = lambda: "mag-statistic" + "[mag-name='" + self.mag_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/statistics/mag-statistics/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic, ['mag_name', 'lma_identifier'], name, value)


                    class ProtocolStatistics(Entity):
                        """
                        LMA Protocol Statistics
                        
                        .. attribute:: pbu_receive_statistics
                        
                        	PBU Receive Statistics
                        	**type**\:  :py:class:`PbuReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics>`
                        
                        .. attribute:: pba_send_statistics
                        
                        	PBA Send Statistics
                        	**type**\:  :py:class:`PbaSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics>`
                        
                        .. attribute:: pbri_send_statistics
                        
                        	PBRI Send Statistics
                        	**type**\:  :py:class:`PbriSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics>`
                        
                        .. attribute:: pbri_receive_statistics
                        
                        	PBRI Receive Statistics
                        	**type**\:  :py:class:`PbriReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics>`
                        
                        .. attribute:: pbra_send_statistics
                        
                        	PBRA Send Statistics
                        	**type**\:  :py:class:`PbraSendStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics>`
                        
                        .. attribute:: pbra_receive_statistics
                        
                        	PBRA Receive Statistics
                        	**type**\:  :py:class:`PbraReceiveStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics, self).__init__()

                            self.yang_name = "protocol-statistics"
                            self.yang_parent_name = "mag-statistic"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"pbu-receive-statistics" : ("pbu_receive_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics), "pba-send-statistics" : ("pba_send_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics), "pbri-send-statistics" : ("pbri_send_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics), "pbri-receive-statistics" : ("pbri_receive_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics), "pbra-send-statistics" : ("pbra_send_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics), "pbra-receive-statistics" : ("pbra_receive_statistics", Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics)}
                            self._child_list_classes = {}

                            self.pbu_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics()
                            self.pbu_receive_statistics.parent = self
                            self._children_name_map["pbu_receive_statistics"] = "pbu-receive-statistics"
                            self._children_yang_names.add("pbu-receive-statistics")

                            self.pba_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics()
                            self.pba_send_statistics.parent = self
                            self._children_name_map["pba_send_statistics"] = "pba-send-statistics"
                            self._children_yang_names.add("pba-send-statistics")

                            self.pbri_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics()
                            self.pbri_send_statistics.parent = self
                            self._children_name_map["pbri_send_statistics"] = "pbri-send-statistics"
                            self._children_yang_names.add("pbri-send-statistics")

                            self.pbri_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics()
                            self.pbri_receive_statistics.parent = self
                            self._children_name_map["pbri_receive_statistics"] = "pbri-receive-statistics"
                            self._children_yang_names.add("pbri-receive-statistics")

                            self.pbra_send_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics()
                            self.pbra_send_statistics.parent = self
                            self._children_name_map["pbra_send_statistics"] = "pbra-send-statistics"
                            self._children_yang_names.add("pbra-send-statistics")

                            self.pbra_receive_statistics = Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics()
                            self.pbra_receive_statistics.parent = self
                            self._children_name_map["pbra_receive_statistics"] = "pbra-receive-statistics"
                            self._children_yang_names.add("pbra-receive-statistics")
                            self._segment_path = lambda: "protocol-statistics"


                        class PbuReceiveStatistics(Entity):
                            """
                            PBU Receive Statistics
                            
                            .. attribute:: pbu_count
                            
                            	Count of PBUs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbu_drop_count
                            
                            	Count of PBUs Dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics, self).__init__()

                                self.yang_name = "pbu-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbu_count = YLeaf(YType.uint64, "pbu-count")

                                self.pbu_drop_count = YLeaf(YType.uint32, "pbu-drop-count")
                                self._segment_path = lambda: "pbu-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbuReceiveStatistics, ['pbu_count', 'pbu_drop_count'], name, value)


                        class PbaSendStatistics(Entity):
                            """
                            PBA Send Statistics
                            
                            .. attribute:: pba_count
                            
                            	Count of PBAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pba_drop_count
                            
                            	Count of PBAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accepted_count
                            
                            	Count of Status Code \- Binding Update accepted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_count
                            
                            	Count of Status Code \- Last BA status code sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_failure_count
                            
                            	Count of Status Code \- Reason unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_failure_count
                            
                            	Count of Status Code \- Administratively prohibited
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resource_failure_count
                            
                            	Count of Status Code \- Insufficient resources
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_reg_failure_count
                            
                            	Count of Status Code \- Home registration not supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: home_subnet_failure_count
                            
                            	Count of Status Code \- Not home subnet
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bad_sequence_failure_count
                            
                            	Count of Status Code \- Sequence number out of window
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: reg_type_failure_count
                            
                            	Count of Status Code \- Registration type change
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: authen_failure_count
                            
                            	Count of Status Code \- Auth Fail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: proxy_reg_not_enabled_count
                            
                            	Count of Status Code \- Proxy Registration not enabled
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: not_lma_for_this_mn_count
                            
                            	Count of Status Code \- Not LMA for this Mobile Node
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_proxy_reg_count
                            
                            	Count of Status Code \- MAG not auth.for proxyreg
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_hnp_count
                            
                            	Count of Status Code \- Not authorized for HNP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_mismatch_count
                            
                            	Count of Status Code \- Invalid timestamp value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: timestamp_lower_than_previous_accepted_count
                            
                            	Count of Status Code \- Timestamp lower than previous accepted
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hnp_opt_count
                            
                            	Count of Status Code \- Missing Home Network Prefix option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_hnps_do_not_match_bce_hnps_count
                            
                            	Count of Status Code \- Recevied HNPs do not match with BCE
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_mn_id_opt_count
                            
                            	Count of Status Code \- Missing MN identifier option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_hi_opt_count
                            
                            	Count of Status Code \- Missing Handoff Indicator
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: missing_access_tech_type_opt_count
                            
                            	Count of Status Code \- Missing ATT option
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv4 mobility
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv4_hoa_count
                            
                            	Count of Status Code \- Not authorized for IPv4 HoA
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_ipv6_mobility_count
                            
                            	Count of Status Code \- Not authorized for IPv6 mobility
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple_ipv4_ho_a_not_supported_count
                            
                            	Count of Status Code \- Multiple IPv4 HoA not supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: gre_key_opt_required_count
                            
                            	Count of Status Code \- GRE Key option is required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics, self).__init__()

                                self.yang_name = "pba-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pba_count = YLeaf(YType.uint64, "pba-count")

                                self.pba_drop_count = YLeaf(YType.uint32, "pba-drop-count")

                                self.accepted_count = YLeaf(YType.uint32, "accepted-count")

                                self.unknown_count = YLeaf(YType.uint32, "unknown-count")

                                self.unspecified_failure_count = YLeaf(YType.uint32, "unspecified-failure-count")

                                self.admin_failure_count = YLeaf(YType.uint32, "admin-failure-count")

                                self.resource_failure_count = YLeaf(YType.uint32, "resource-failure-count")

                                self.home_reg_failure_count = YLeaf(YType.uint32, "home-reg-failure-count")

                                self.home_subnet_failure_count = YLeaf(YType.uint32, "home-subnet-failure-count")

                                self.bad_sequence_failure_count = YLeaf(YType.uint32, "bad-sequence-failure-count")

                                self.reg_type_failure_count = YLeaf(YType.uint32, "reg-type-failure-count")

                                self.authen_failure_count = YLeaf(YType.uint32, "authen-failure-count")

                                self.proxy_reg_not_enabled_count = YLeaf(YType.uint32, "proxy-reg-not-enabled-count")

                                self.not_lma_for_this_mn_count = YLeaf(YType.uint32, "not-lma-for-this-mn-count")

                                self.no_author_for_proxy_reg_count = YLeaf(YType.uint32, "no-author-for-proxy-reg-count")

                                self.no_author_for_hnp_count = YLeaf(YType.uint32, "no-author-for-hnp-count")

                                self.timestamp_mismatch_count = YLeaf(YType.uint32, "timestamp-mismatch-count")

                                self.timestamp_lower_than_previous_accepted_count = YLeaf(YType.uint32, "timestamp-lower-than-previous-accepted-count")

                                self.missing_hnp_opt_count = YLeaf(YType.uint32, "missing-hnp-opt-count")

                                self.received_hnps_do_not_match_bce_hnps_count = YLeaf(YType.uint32, "received-hnps-do-not-match-bce-hnps-count")

                                self.missing_mn_id_opt_count = YLeaf(YType.uint32, "missing-mn-id-opt-count")

                                self.missing_hi_opt_count = YLeaf(YType.uint32, "missing-hi-opt-count")

                                self.missing_access_tech_type_opt_count = YLeaf(YType.uint32, "missing-access-tech-type-opt-count")

                                self.no_author_for_ipv4_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv4-mobility-count")

                                self.no_author_for_ipv4_hoa_count = YLeaf(YType.uint32, "no-author-for-ipv4-hoa-count")

                                self.no_author_for_ipv6_mobility_count = YLeaf(YType.uint32, "no-author-for-ipv6-mobility-count")

                                self.multiple_ipv4_ho_a_not_supported_count = YLeaf(YType.uint32, "multiple-ipv4-ho-a-not-supported-count")

                                self.gre_key_opt_required_count = YLeaf(YType.uint32, "gre-key-opt-required-count")
                                self._segment_path = lambda: "pba-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbaSendStatistics, ['pba_count', 'pba_drop_count', 'accepted_count', 'unknown_count', 'unspecified_failure_count', 'admin_failure_count', 'resource_failure_count', 'home_reg_failure_count', 'home_subnet_failure_count', 'bad_sequence_failure_count', 'reg_type_failure_count', 'authen_failure_count', 'proxy_reg_not_enabled_count', 'not_lma_for_this_mn_count', 'no_author_for_proxy_reg_count', 'no_author_for_hnp_count', 'timestamp_mismatch_count', 'timestamp_lower_than_previous_accepted_count', 'missing_hnp_opt_count', 'received_hnps_do_not_match_bce_hnps_count', 'missing_mn_id_opt_count', 'missing_hi_opt_count', 'missing_access_tech_type_opt_count', 'no_author_for_ipv4_mobility_count', 'no_author_for_ipv4_hoa_count', 'no_author_for_ipv6_mobility_count', 'multiple_ipv4_ho_a_not_supported_count', 'gre_key_opt_required_count'], name, value)


                        class PbriSendStatistics(Entity):
                            """
                            PBRI Send Statistics
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics, self).__init__()

                                self.yang_name = "pbri-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                                self._segment_path = lambda: "pbri-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriSendStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                        class PbriReceiveStatistics(Entity):
                            """
                            PBRI Receive Statistics
                            
                            .. attribute:: pbri_count
                            
                            	Count of PBRIs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbri_drop_count
                            
                            	Count of PBRIs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unspecified_count
                            
                            	Count of Revoc Trigger \- Unspecified
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: admin_reason_count
                            
                            	Count of Revoc Trigger \- Administrative Reason
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_same_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Same ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_different_att_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Different ATT
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mag_handover_unknown_count
                            
                            	Count of Revoc Trigger \- Inter MAG Handover Unknown
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: user_session_termination_count
                            
                            	Count of Revoc Trigger \- User Init Session Terminatation
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: network_session_termination_count
                            
                            	Count of Revoc Trigger \- Access Network Session Termination
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_of_sync_bce_state_count
                            
                            	Count of Revoc Trigger \- Possible Out\-of\-Sync BCE State
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: per_peer_policy_count
                            
                            	Count of Revoc Trigger \- Per\-Peer Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoking_mn_local_policy_count
                            
                            	Count of Revoc Trigger \- Revoking Mobility Node Local Policy
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics, self).__init__()

                                self.yang_name = "pbri-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbri_count = YLeaf(YType.uint64, "pbri-count")

                                self.pbri_drop_count = YLeaf(YType.uint32, "pbri-drop-count")

                                self.unspecified_count = YLeaf(YType.uint32, "unspecified-count")

                                self.admin_reason_count = YLeaf(YType.uint32, "admin-reason-count")

                                self.mag_handover_same_att_count = YLeaf(YType.uint32, "mag-handover-same-att-count")

                                self.mag_handover_different_att_count = YLeaf(YType.uint32, "mag-handover-different-att-count")

                                self.mag_handover_unknown_count = YLeaf(YType.uint32, "mag-handover-unknown-count")

                                self.user_session_termination_count = YLeaf(YType.uint32, "user-session-termination-count")

                                self.network_session_termination_count = YLeaf(YType.uint32, "network-session-termination-count")

                                self.out_of_sync_bce_state_count = YLeaf(YType.uint32, "out-of-sync-bce-state-count")

                                self.per_peer_policy_count = YLeaf(YType.uint32, "per-peer-policy-count")

                                self.revoking_mn_local_policy_count = YLeaf(YType.uint32, "revoking-mn-local-policy-count")
                                self._segment_path = lambda: "pbri-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbriReceiveStatistics, ['pbri_count', 'pbri_drop_count', 'unspecified_count', 'admin_reason_count', 'mag_handover_same_att_count', 'mag_handover_different_att_count', 'mag_handover_unknown_count', 'user_session_termination_count', 'network_session_termination_count', 'out_of_sync_bce_state_count', 'per_peer_policy_count', 'revoking_mn_local_policy_count'], name, value)


                        class PbraSendStatistics(Entity):
                            """
                            PBRA Send Statistics
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics, self).__init__()

                                self.yang_name = "pbra-send-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                                self._segment_path = lambda: "pbra-send-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraSendStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


                        class PbraReceiveStatistics(Entity):
                            """
                            PBRA Receive Statistics
                            
                            .. attribute:: pbra_count
                            
                            	Count of PBRAs
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pbra_drop_count
                            
                            	Count of PBRAs dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: success_count
                            
                            	Count of Revoc Status \- Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: partial_success_count
                            
                            	Count of Revoc Status \- Partial Success
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_binding_count
                            
                            	Count of Revoc Status \- Binding Does Not Exist
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: hoa_required_count
                            
                            	Count of Revoc Status \- IPv4 Home Address Option Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: no_author_for_global_revoc_count
                            
                            	Count of Revoc Status \- Global Revocation NOT Authorized
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_identity_required_count
                            
                            	Count of Revoc Status \- Revoked Mobile Node Identity Required
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mn_attached_count
                            
                            	Count of Revoc Status \- Revocation Failed \- MN is Attached
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unknown_revoc_trigger_count
                            
                            	Count of Revoc Status \- Revocation Trigger NOT supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: revoc_function_not_supported_count
                            
                            	Count of Revoc Status \- Revocation Function NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pbr_not_supported_count
                            
                            	Count of Revoc Status \- Proxy Binding Revocation NOT Supported
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-mobileip-oper'
                            _revision = '2016-03-10'

                            def __init__(self):
                                super(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics, self).__init__()

                                self.yang_name = "pbra-receive-statistics"
                                self.yang_parent_name = "protocol-statistics"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pbra_count = YLeaf(YType.uint64, "pbra-count")

                                self.pbra_drop_count = YLeaf(YType.uint32, "pbra-drop-count")

                                self.success_count = YLeaf(YType.uint32, "success-count")

                                self.partial_success_count = YLeaf(YType.uint32, "partial-success-count")

                                self.no_binding_count = YLeaf(YType.uint32, "no-binding-count")

                                self.hoa_required_count = YLeaf(YType.uint32, "hoa-required-count")

                                self.no_author_for_global_revoc_count = YLeaf(YType.uint32, "no-author-for-global-revoc-count")

                                self.mn_identity_required_count = YLeaf(YType.uint32, "mn-identity-required-count")

                                self.mn_attached_count = YLeaf(YType.uint32, "mn-attached-count")

                                self.unknown_revoc_trigger_count = YLeaf(YType.uint32, "unknown-revoc-trigger-count")

                                self.revoc_function_not_supported_count = YLeaf(YType.uint32, "revoc-function-not-supported-count")

                                self.pbr_not_supported_count = YLeaf(YType.uint32, "pbr-not-supported-count")
                                self._segment_path = lambda: "pbra-receive-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pmipv6.Lma.Statistics.MagStatistics.MagStatistic.ProtocolStatistics.PbraReceiveStatistics, ['pbra_count', 'pbra_drop_count', 'success_count', 'partial_success_count', 'no_binding_count', 'hoa_required_count', 'no_author_for_global_revoc_count', 'mn_identity_required_count', 'mn_attached_count', 'unknown_revoc_trigger_count', 'revoc_function_not_supported_count', 'pbr_not_supported_count'], name, value)


        class Bindings(Entity):
            """
            Table of Binding
            
            .. attribute:: binding
            
            	Binding Parameters
            	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Bindings, self).__init__()

                self.yang_name = "bindings"
                self.yang_parent_name = "lma"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"binding" : ("binding", Pmipv6.Lma.Bindings.Binding)}

                self.binding = YList(self)
                self._segment_path = lambda: "bindings"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pmipv6.Lma.Bindings, [], name, value)


            class Binding(Entity):
                """
                Binding Parameters
                
                .. attribute:: mag_name
                
                	Peer MAG ID
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: nai_string
                
                	NAI String
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: imsi_string
                
                	IMSI String
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: customer_name
                
                	Customer String
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: mnnai
                
                	Mobile Node Identifier
                	**type**\: str
                
                .. attribute:: customer_name_xr
                
                	Customer name
                	**type**\: str
                
                .. attribute:: llid
                
                	Link Layer Identifier
                	**type**\: str
                
                .. attribute:: peer_id
                
                	Peer Identifier
                	**type**\: str
                
                .. attribute:: phyintf
                
                	Access Interface
                	**type**\: str
                
                .. attribute:: tunnel
                
                	Tunnel Interface
                	**type**\: str
                
                .. attribute:: state
                
                	State Name
                	**type**\: str
                
                .. attribute:: apn
                
                	Access Point Network
                	**type**\: str
                
                .. attribute:: att
                
                	MN ATT
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: hoa
                
                	MN HOA
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: dflt
                
                	MN Default Router
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lifetime
                
                	Life Time of Binding
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: liferem
                
                	Life Time Remaining
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: refresh
                
                	Refresh Time of Binding
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: refresh_rem
                
                	Refresh Time Remaining
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_len
                
                	Prefix Length
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_hnps
                
                	HNP count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_coa
                
                	COA count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_dmnp_v4
                
                	IPv4 DMNP count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: num_dmnp_v6
                
                	IPv6 DMNP count
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: hnps
                
                	MN Home Network Prefixes
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ignore_home_address
                
                	Ignore HoA/HNP
                	**type**\: bool
                
                .. attribute:: up_stream_grekey
                
                	Upstream GRE Key
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_stream_grekey
                
                	DownStream GRE Key
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrfid
                
                	VRF ID of Access Interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: coa
                
                	COA entries
                	**type**\: list of  		 :py:class:`Coa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.Coa>`
                
                .. attribute:: dmnp_v4
                
                	IPv4 DMNP prefixes
                	**type**\: list of  		 :py:class:`DmnpV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.DmnpV4>`
                
                .. attribute:: dmnp_v6
                
                	IPv6 DMNP prefixes
                	**type**\: list of  		 :py:class:`DmnpV6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Bindings.Binding.DmnpV6>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Bindings.Binding, self).__init__()

                    self.yang_name = "binding"
                    self.yang_parent_name = "bindings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"coa" : ("coa", Pmipv6.Lma.Bindings.Binding.Coa), "dmnp-v4" : ("dmnp_v4", Pmipv6.Lma.Bindings.Binding.DmnpV4), "dmnp-v6" : ("dmnp_v6", Pmipv6.Lma.Bindings.Binding.DmnpV6)}

                    self.mag_name = YLeaf(YType.str, "mag-name")

                    self.nai_string = YLeaf(YType.str, "nai-string")

                    self.imsi_string = YLeaf(YType.str, "imsi-string")

                    self.customer_name = YLeaf(YType.str, "customer-name")

                    self.mnnai = YLeaf(YType.str, "mnnai")

                    self.customer_name_xr = YLeaf(YType.str, "customer-name-xr")

                    self.llid = YLeaf(YType.str, "llid")

                    self.peer_id = YLeaf(YType.str, "peer-id")

                    self.phyintf = YLeaf(YType.str, "phyintf")

                    self.tunnel = YLeaf(YType.str, "tunnel")

                    self.state = YLeaf(YType.str, "state")

                    self.apn = YLeaf(YType.str, "apn")

                    self.att = YLeaf(YType.uint16, "att")

                    self.hoa = YLeaf(YType.str, "hoa")

                    self.dflt = YLeaf(YType.str, "dflt")

                    self.lifetime = YLeaf(YType.uint32, "lifetime")

                    self.liferem = YLeaf(YType.uint32, "liferem")

                    self.refresh = YLeaf(YType.uint32, "refresh")

                    self.refresh_rem = YLeaf(YType.uint32, "refresh-rem")

                    self.prefix_len = YLeaf(YType.uint8, "prefix-len")

                    self.num_hnps = YLeaf(YType.uint8, "num-hnps")

                    self.num_coa = YLeaf(YType.uint8, "num-coa")

                    self.num_dmnp_v4 = YLeaf(YType.uint8, "num-dmnp-v4")

                    self.num_dmnp_v6 = YLeaf(YType.uint8, "num-dmnp-v6")

                    self.hnps = YLeaf(YType.str, "hnps")

                    self.ignore_home_address = YLeaf(YType.boolean, "ignore-home-address")

                    self.up_stream_grekey = YLeaf(YType.uint32, "up-stream-grekey")

                    self.down_stream_grekey = YLeaf(YType.uint32, "down-stream-grekey")

                    self.vrfid = YLeaf(YType.uint32, "vrfid")

                    self.coa = YList(self)
                    self.dmnp_v4 = YList(self)
                    self.dmnp_v6 = YList(self)
                    self._segment_path = lambda: "binding"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Bindings.Binding, ['mag_name', 'nai_string', 'imsi_string', 'customer_name', 'mnnai', 'customer_name_xr', 'llid', 'peer_id', 'phyintf', 'tunnel', 'state', 'apn', 'att', 'hoa', 'dflt', 'lifetime', 'liferem', 'refresh', 'refresh_rem', 'prefix_len', 'num_hnps', 'num_coa', 'num_dmnp_v4', 'num_dmnp_v6', 'hnps', 'ignore_home_address', 'up_stream_grekey', 'down_stream_grekey', 'vrfid'], name, value)


                class Coa(Entity):
                    """
                    COA entries
                    
                    .. attribute:: llid
                    
                    	Link Layer Identifier
                    	**type**\: str
                    
                    .. attribute:: peer_name
                    
                    	Peer Name
                    	**type**\: str
                    
                    .. attribute:: tunnel
                    
                    	Tunnel Interface
                    	**type**\: str
                    
                    .. attribute:: e_label
                    
                    	Egress Label
                    	**type**\: str
                    
                    .. attribute:: color
                    
                    	Label Color
                    	**type**\: str
                    
                    .. attribute:: roa_min_tf
                    
                    	Roaming Intf
                    	**type**\: str
                    
                    .. attribute:: pstate
                    
                    	COA STATE
                    	**type**\: str
                    
                    .. attribute:: msisdn
                    
                    	MSISDN
                    	**type**\: str
                    
                    .. attribute:: imsi
                    
                    	IMSI or IMSI NAI
                    	**type**\: str
                    
                    .. attribute:: cdma_nai
                    
                    	CDMA NAI
                    	**type**\: str
                    
                    .. attribute:: pgw_apn
                    
                    	Subscriber APN on PWG
                    	**type**\: str
                    
                    .. attribute:: pgw_trans_vrf
                    
                    	Subscriber Transport VRF on PGW
                    	**type**\: str
                    
                    .. attribute:: att
                    
                    	MN ATT
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: lifetime
                    
                    	Life Time of coa
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lifetime_remaining
                    
                    	Life Time remain of coa
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: refresh
                    
                    	refresh Time of coa
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: refresh_rem
                    
                    	refresh Time remain of coa
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dnkey
                    
                    	down key for coa tunnel
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: upkey
                    
                    	up key for coa tunnel
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coa_v4
                    
                    	IPv4 CoA
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: coa_v6
                    
                    	IPv6 CoA
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.Coa, self).__init__()

                        self.yang_name = "coa"
                        self.yang_parent_name = "binding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.llid = YLeaf(YType.str, "llid")

                        self.peer_name = YLeaf(YType.str, "peer-name")

                        self.tunnel = YLeaf(YType.str, "tunnel")

                        self.e_label = YLeaf(YType.str, "e-label")

                        self.color = YLeaf(YType.str, "color")

                        self.roa_min_tf = YLeaf(YType.str, "roa-min-tf")

                        self.pstate = YLeaf(YType.str, "pstate")

                        self.msisdn = YLeaf(YType.str, "msisdn")

                        self.imsi = YLeaf(YType.str, "imsi")

                        self.cdma_nai = YLeaf(YType.str, "cdma-nai")

                        self.pgw_apn = YLeaf(YType.str, "pgw-apn")

                        self.pgw_trans_vrf = YLeaf(YType.str, "pgw-trans-vrf")

                        self.att = YLeaf(YType.uint16, "att")

                        self.lifetime = YLeaf(YType.uint32, "lifetime")

                        self.lifetime_remaining = YLeaf(YType.uint32, "lifetime-remaining")

                        self.refresh = YLeaf(YType.uint32, "refresh")

                        self.refresh_rem = YLeaf(YType.uint32, "refresh-rem")

                        self.dnkey = YLeaf(YType.uint32, "dnkey")

                        self.upkey = YLeaf(YType.uint32, "upkey")

                        self.coa_v4 = YLeaf(YType.str, "coa-v4")

                        self.coa_v6 = YLeaf(YType.str, "coa-v6")
                        self._segment_path = lambda: "coa"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Bindings.Binding.Coa, ['llid', 'peer_name', 'tunnel', 'e_label', 'color', 'roa_min_tf', 'pstate', 'msisdn', 'imsi', 'cdma_nai', 'pgw_apn', 'pgw_trans_vrf', 'att', 'lifetime', 'lifetime_remaining', 'refresh', 'refresh_rem', 'dnkey', 'upkey', 'coa_v4', 'coa_v6'], name, value)


                class DmnpV4(Entity):
                    """
                    IPv4 DMNP prefixes
                    
                    .. attribute:: pfxlen
                    
                    	IPv4 prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: prefix
                    
                    	IPv4 prefix
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.DmnpV4, self).__init__()

                        self.yang_name = "dmnp-v4"
                        self.yang_parent_name = "binding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pfxlen = YLeaf(YType.uint8, "pfxlen")

                        self.prefix = YLeaf(YType.str, "prefix")
                        self._segment_path = lambda: "dmnp-v4"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Bindings.Binding.DmnpV4, ['pfxlen', 'prefix'], name, value)


                class DmnpV6(Entity):
                    """
                    IPv6 DMNP prefixes
                    
                    .. attribute:: pfxlen
                    
                    	IPv6 prefix length
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: prefix
                    
                    	IPv6 prefix
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.Bindings.Binding.DmnpV6, self).__init__()

                        self.yang_name = "dmnp-v6"
                        self.yang_parent_name = "binding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pfxlen = YLeaf(YType.uint8, "pfxlen")

                        self.prefix = YLeaf(YType.str, "prefix")
                        self._segment_path = lambda: "dmnp-v6"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/bindings/binding/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.Bindings.Binding.DmnpV6, ['pfxlen', 'prefix'], name, value)


        class Heartbeats(Entity):
            """
            Table of Heartbeat
            
            .. attribute:: heartbeat
            
            	Heartbeat information
            	**type**\: list of  		 :py:class:`Heartbeat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.Heartbeats.Heartbeat>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.Heartbeats, self).__init__()

                self.yang_name = "heartbeats"
                self.yang_parent_name = "lma"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"heartbeat" : ("heartbeat", Pmipv6.Lma.Heartbeats.Heartbeat)}

                self.heartbeat = YList(self)
                self._segment_path = lambda: "heartbeats"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pmipv6.Lma.Heartbeats, [], name, value)


            class Heartbeat(Entity):
                """
                Heartbeat information
                
                .. attribute:: peer_addr  <key>
                
                	IPv4 or IPv6 address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: vrf
                
                	VRF Name
                	**type**\: str
                
                .. attribute:: customer_name
                
                	Customer Name
                	**type**\: str
                
                .. attribute:: source_port
                
                	Source Port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_port
                
                	Destination Port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: source_ipv4_address
                
                	Source IPv4 Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv4_address
                
                	Destination IPv4 Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: source_ipv6_address
                
                	Source IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Destination IPv6 Address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: status
                
                	Path Status
                	**type**\: bool
                
                .. attribute:: ipv6_path
                
                	IPv6 Path
                	**type**\: bool
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.Heartbeats.Heartbeat, self).__init__()

                    self.yang_name = "heartbeat"
                    self.yang_parent_name = "heartbeats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.peer_addr = YLeaf(YType.str, "peer-addr")

                    self.vrf = YLeaf(YType.str, "vrf")

                    self.customer_name = YLeaf(YType.str, "customer-name")

                    self.source_port = YLeaf(YType.uint32, "source-port")

                    self.destination_port = YLeaf(YType.uint32, "destination-port")

                    self.source_ipv4_address = YLeaf(YType.str, "source-ipv4-address")

                    self.destination_ipv4_address = YLeaf(YType.str, "destination-ipv4-address")

                    self.source_ipv6_address = YLeaf(YType.str, "source-ipv6-address")

                    self.destination_ipv6_address = YLeaf(YType.str, "destination-ipv6-address")

                    self.status = YLeaf(YType.boolean, "status")

                    self.ipv6_path = YLeaf(YType.boolean, "ipv6-path")
                    self._segment_path = lambda: "heartbeat" + "[peer-addr='" + self.peer_addr.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/heartbeats/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.Heartbeats.Heartbeat, ['peer_addr', 'vrf', 'customer_name', 'source_port', 'destination_port', 'source_ipv4_address', 'destination_ipv4_address', 'source_ipv6_address', 'destination_ipv6_address', 'status', 'ipv6_path'], name, value)


        class ConfigVariables(Entity):
            """
            Global Configuration Variables
            
            .. attribute:: customer_variables
            
            	Table of CustomerVariables
            	**type**\:  :py:class:`CustomerVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables>`
            
            .. attribute:: global_variables
            
            	Global Configuration Variables
            	**type**\:  :py:class:`GlobalVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables>`
            
            

            """

            _prefix = 'ip-mobileip-oper'
            _revision = '2016-03-10'

            def __init__(self):
                super(Pmipv6.Lma.ConfigVariables, self).__init__()

                self.yang_name = "config-variables"
                self.yang_parent_name = "lma"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"customer-variables" : ("customer_variables", Pmipv6.Lma.ConfigVariables.CustomerVariables), "global-variables" : ("global_variables", Pmipv6.Lma.ConfigVariables.GlobalVariables)}
                self._child_list_classes = {}

                self.customer_variables = Pmipv6.Lma.ConfigVariables.CustomerVariables()
                self.customer_variables.parent = self
                self._children_name_map["customer_variables"] = "customer-variables"
                self._children_yang_names.add("customer-variables")

                self.global_variables = Pmipv6.Lma.ConfigVariables.GlobalVariables()
                self.global_variables.parent = self
                self._children_name_map["global_variables"] = "global-variables"
                self._children_yang_names.add("global-variables")
                self._segment_path = lambda: "config-variables"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/%s" % self._segment_path()


            class CustomerVariables(Entity):
                """
                Table of CustomerVariables
                
                .. attribute:: customer_variable
                
                	Customer name string
                	**type**\: list of  		 :py:class:`CustomerVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.ConfigVariables.CustomerVariables, self).__init__()

                    self.yang_name = "customer-variables"
                    self.yang_parent_name = "config-variables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"customer-variable" : ("customer_variable", Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable)}

                    self.customer_variable = YList(self)
                    self._segment_path = lambda: "customer-variables"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.ConfigVariables.CustomerVariables, [], name, value)


                class CustomerVariable(Entity):
                    """
                    Customer name string
                    
                    .. attribute:: customer_name  <key>
                    
                    	Customer name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: mll_service
                    
                    	MLL service parameters
                    	**type**\:  :py:class:`MllService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService>`
                    
                    .. attribute:: cust_name
                    
                    	Customer Name
                    	**type**\: str
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable, self).__init__()

                        self.yang_name = "customer-variable"
                        self.yang_parent_name = "customer-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"mll-service" : ("mll_service", Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService)}
                        self._child_list_classes = {}

                        self.customer_name = YLeaf(YType.str, "customer-name")

                        self.cust_name = YLeaf(YType.str, "cust-name")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.mll_service = Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService()
                        self.mll_service.parent = self
                        self._children_name_map["mll_service"] = "mll-service"
                        self._children_yang_names.add("mll-service")
                        self._segment_path = lambda: "customer-variable" + "[customer-name='" + self.customer_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/customer-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable, ['customer_name', 'cust_name', 'vrf_name', 'auth_option'], name, value)


                    class MllService(Entity):
                        """
                        MLL service parameters
                        
                        .. attribute:: ignore_hoa
                        
                        	Ignore Home Address
                        	**type**\: bool
                        
                        .. attribute:: mnp_ipv4_lmn_max
                        
                        	Max IPv4 prefixes per LMN
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mnp_ipv6_lmn_max
                        
                        	Max IPv6 prefixes per LMN
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mnp_lmn_max
                        
                        	Max prefixes per LMN
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mnp_ipv4_cust_max
                        
                        	Max IPv4 prefixes per Customer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv6_cust_max
                        
                        	Max IPv6 prefixes per Customer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_cust_max
                        
                        	Max prefixes per Customer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv4_cust_cur
                        
                        	Current IPv4 prefixes per Customer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mnp_ipv6_cust_cur
                        
                        	Current IPv6 prefixes per Customer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService, self).__init__()

                            self.yang_name = "mll-service"
                            self.yang_parent_name = "customer-variable"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ignore_hoa = YLeaf(YType.boolean, "ignore-hoa")

                            self.mnp_ipv4_lmn_max = YLeaf(YType.uint16, "mnp-ipv4-lmn-max")

                            self.mnp_ipv6_lmn_max = YLeaf(YType.uint16, "mnp-ipv6-lmn-max")

                            self.mnp_lmn_max = YLeaf(YType.uint16, "mnp-lmn-max")

                            self.mnp_ipv4_cust_max = YLeaf(YType.uint32, "mnp-ipv4-cust-max")

                            self.mnp_ipv6_cust_max = YLeaf(YType.uint32, "mnp-ipv6-cust-max")

                            self.mnp_cust_max = YLeaf(YType.uint32, "mnp-cust-max")

                            self.mnp_ipv4_cust_cur = YLeaf(YType.uint32, "mnp-ipv4-cust-cur")

                            self.mnp_ipv6_cust_cur = YLeaf(YType.uint32, "mnp-ipv6-cust-cur")
                            self._segment_path = lambda: "mll-service"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.ConfigVariables.CustomerVariables.CustomerVariable.MllService, ['ignore_hoa', 'mnp_ipv4_lmn_max', 'mnp_ipv6_lmn_max', 'mnp_lmn_max', 'mnp_ipv4_cust_max', 'mnp_ipv6_cust_max', 'mnp_cust_max', 'mnp_ipv4_cust_cur', 'mnp_ipv6_cust_cur'], name, value)


            class GlobalVariables(Entity):
                """
                Global Configuration Variables
                
                .. attribute:: parameters
                
                	Domain Parameters
                	**type**\:  :py:class:`Parameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters>`
                
                .. attribute:: mll_service
                
                	MLL service parameters
                	**type**\:  :py:class:`MllService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService>`
                
                .. attribute:: domain
                
                	Domain Name
                	**type**\: str
                
                .. attribute:: selfid
                
                	Self ID
                	**type**\: str
                
                .. attribute:: apn_name
                
                	APN Name
                	**type**\: str
                
                .. attribute:: role
                
                	Role Type
                	**type**\:  :py:class:`Pmipv6Role <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Role>`
                
                .. attribute:: count
                
                	Number of Networks/Intf
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peers
                
                	Number of Peers
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: customers
                
                	Number of Customers
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_network
                
                	Number of Networks
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discover_mn
                
                	Discover MN Detachment
                	**type**\: bool
                
                .. attribute:: local_routing
                
                	Local Routing
                	**type**\: bool
                
                .. attribute:: aaa_accounting
                
                	AAA Accounting
                	**type**\: bool
                
                .. attribute:: default_mn
                
                	Default MN Enabled
                	**type**\: bool
                
                .. attribute:: apn
                
                	APN Present
                	**type**\: bool
                
                .. attribute:: learn_mag
                
                	Learn MAG
                	**type**\: bool
                
                .. attribute:: session_mgr
                
                	Session Manager
                	**type**\: bool
                
                .. attribute:: service
                
                	Service
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: profile
                
                	Default MN Profile Name
                	**type**\: str
                
                .. attribute:: ddp
                
                	Discover Detach Period
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ddt
                
                	Discover Detach Timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ddr
                
                	Discover Detach Retries
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: intf
                
                	MAG Access List
                	**type**\: list of  		 :py:class:`Intf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf>`
                
                .. attribute:: peer
                
                	Peer Parameters
                	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer>`
                
                .. attribute:: network
                
                	LMA Network Parameters
                	**type**\: list of  		 :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Network>`
                
                .. attribute:: cust
                
                	Customer parameters
                	**type**\: list of  		 :py:class:`Cust <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust>`
                
                

                """

                _prefix = 'ip-mobileip-oper'
                _revision = '2016-03-10'

                def __init__(self):
                    super(Pmipv6.Lma.ConfigVariables.GlobalVariables, self).__init__()

                    self.yang_name = "global-variables"
                    self.yang_parent_name = "config-variables"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"parameters" : ("parameters", Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters), "mll-service" : ("mll_service", Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService)}
                    self._child_list_classes = {"intf" : ("intf", Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf), "peer" : ("peer", Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer), "network" : ("network", Pmipv6.Lma.ConfigVariables.GlobalVariables.Network), "cust" : ("cust", Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust)}

                    self.domain = YLeaf(YType.str, "domain")

                    self.selfid = YLeaf(YType.str, "selfid")

                    self.apn_name = YLeaf(YType.str, "apn-name")

                    self.role = YLeaf(YType.enumeration, "role")

                    self.count = YLeaf(YType.uint32, "count")

                    self.peers = YLeaf(YType.uint32, "peers")

                    self.customers = YLeaf(YType.uint32, "customers")

                    self.num_network = YLeaf(YType.uint32, "num-network")

                    self.discover_mn = YLeaf(YType.boolean, "discover-mn")

                    self.local_routing = YLeaf(YType.boolean, "local-routing")

                    self.aaa_accounting = YLeaf(YType.boolean, "aaa-accounting")

                    self.default_mn = YLeaf(YType.boolean, "default-mn")

                    self.apn = YLeaf(YType.boolean, "apn")

                    self.learn_mag = YLeaf(YType.boolean, "learn-mag")

                    self.session_mgr = YLeaf(YType.boolean, "session-mgr")

                    self.service = YLeaf(YType.uint8, "service")

                    self.profile = YLeaf(YType.str, "profile")

                    self.ddp = YLeaf(YType.uint32, "ddp")

                    self.ddt = YLeaf(YType.uint32, "ddt")

                    self.ddr = YLeaf(YType.uint8, "ddr")

                    self.parameters = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters()
                    self.parameters.parent = self
                    self._children_name_map["parameters"] = "parameters"
                    self._children_yang_names.add("parameters")

                    self.mll_service = Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService()
                    self.mll_service.parent = self
                    self._children_name_map["mll_service"] = "mll-service"
                    self._children_yang_names.add("mll-service")

                    self.intf = YList(self)
                    self.peer = YList(self)
                    self.network = YList(self)
                    self.cust = YList(self)
                    self._segment_path = lambda: "global-variables"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables, ['domain', 'selfid', 'apn_name', 'role', 'count', 'peers', 'customers', 'num_network', 'discover_mn', 'local_routing', 'aaa_accounting', 'default_mn', 'apn', 'learn_mag', 'session_mgr', 'service', 'profile', 'ddp', 'ddt', 'ddr'], name, value)


                class Parameters(Entity):
                    """
                    Domain Parameters
                    
                    .. attribute:: self_id
                    
                    	Self Identifier
                    	**type**\:  :py:class:`SelfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId>`
                    
                    .. attribute:: timestamp
                    
                    	Timestamp method in use
                    	**type**\: bool
                    
                    .. attribute:: window
                    
                    	Timestamp Validity Window
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\: bool
                    
                    .. attribute:: reg_time
                    
                    	BCE Registration Lifetime
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ref_time
                    
                    	BCE Refresh Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: retx
                    
                    	Refresh Retransmit Init
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: ret_max
                    
                    	Refresh Retransmit Max
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bri_init
                    
                    	BRI Init Delay time
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bri_retries
                    
                    	BRI Max Retries
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bri_max
                    
                    	BRI Max Delay time
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_bindings
                    
                    	Allowed Max. Bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hnp
                    
                    	Allowed HNPs per MN Intf
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: encap
                    
                    	Encapsulation Type
                    	**type**\:  :py:class:`Pmipv6Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Encap>`
                    
                    .. attribute:: delete_time
                    
                    	BCE Delete Hold Timer
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: create_time
                    
                    	BCE Create Wait Timer
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: up_grekey
                    
                    	Upstream GRE Key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: down_grekey
                    
                    	Downstream GRE Key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters, self).__init__()

                        self.yang_name = "parameters"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"self-id" : ("self_id", Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId)}
                        self._child_list_classes = {}

                        self.timestamp = YLeaf(YType.boolean, "timestamp")

                        self.window = YLeaf(YType.uint64, "window")

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.reg_time = YLeaf(YType.uint32, "reg-time")

                        self.ref_time = YLeaf(YType.uint32, "ref-time")

                        self.retx = YLeaf(YType.uint16, "retx")

                        self.ret_max = YLeaf(YType.uint16, "ret-max")

                        self.bri_init = YLeaf(YType.uint16, "bri-init")

                        self.bri_retries = YLeaf(YType.uint16, "bri-retries")

                        self.bri_max = YLeaf(YType.uint16, "bri-max")

                        self.max_bindings = YLeaf(YType.uint32, "max-bindings")

                        self.hnp = YLeaf(YType.uint8, "hnp")

                        self.encap = YLeaf(YType.enumeration, "encap")

                        self.delete_time = YLeaf(YType.uint16, "delete-time")

                        self.create_time = YLeaf(YType.uint16, "create-time")

                        self.up_grekey = YLeaf(YType.uint32, "up-grekey")

                        self.down_grekey = YLeaf(YType.uint32, "down-grekey")

                        self.self_id = Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId()
                        self.self_id.parent = self
                        self._children_name_map["self_id"] = "self-id"
                        self._children_yang_names.add("self-id")
                        self._segment_path = lambda: "parameters"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters, ['timestamp', 'window', 'auth_option', 'reg_time', 'ref_time', 'retx', 'ret_max', 'bri_init', 'bri_retries', 'bri_max', 'max_bindings', 'hnp', 'encap', 'delete_time', 'create_time', 'up_grekey', 'down_grekey'], name, value)


                    class SelfId(Entity):
                        """
                        Self Identifier
                        
                        .. attribute:: entity_
                        
                        	Identifier of PMIP Node
                        	**type**\: str
                        
                        .. attribute:: addr_type
                        
                        	IPV4 or IPV6 or Both
                        	**type**\:  :py:class:`Pmipv6Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Addr>`
                        
                        .. attribute:: address
                        
                        	IPV6 address of LMA/MAG
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv4_address
                        
                        	IPV4 addrress of LMA/MAG
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-mobileip-oper'
                        _revision = '2016-03-10'

                        def __init__(self):
                            super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId, self).__init__()

                            self.yang_name = "self-id"
                            self.yang_parent_name = "parameters"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.entity_ = YLeaf(YType.str, "entity")

                            self.addr_type = YLeaf(YType.enumeration, "addr-type")

                            self.address = YLeaf(YType.str, "address")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")
                            self._segment_path = lambda: "self-id"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/parameters/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Parameters.SelfId, ['entity_', 'addr_type', 'address', 'ipv4_address'], name, value)


                class MllService(Entity):
                    """
                    MLL service parameters
                    
                    .. attribute:: ignore_hoa
                    
                    	Ignore Home Address
                    	**type**\: bool
                    
                    .. attribute:: mnp_ipv4_lmn_max
                    
                    	Max IPv4 prefixes per LMN
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mnp_ipv6_lmn_max
                    
                    	Max IPv6 prefixes per LMN
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mnp_lmn_max
                    
                    	Max prefixes per LMN
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mnp_ipv4_cust_max
                    
                    	Max IPv4 prefixes per Customer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv6_cust_max
                    
                    	Max IPv6 prefixes per Customer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_cust_max
                    
                    	Max prefixes per Customer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv4_cust_cur
                    
                    	Current IPv4 prefixes per Customer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mnp_ipv6_cust_cur
                    
                    	Current IPv6 prefixes per Customer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService, self).__init__()

                        self.yang_name = "mll-service"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ignore_hoa = YLeaf(YType.boolean, "ignore-hoa")

                        self.mnp_ipv4_lmn_max = YLeaf(YType.uint16, "mnp-ipv4-lmn-max")

                        self.mnp_ipv6_lmn_max = YLeaf(YType.uint16, "mnp-ipv6-lmn-max")

                        self.mnp_lmn_max = YLeaf(YType.uint16, "mnp-lmn-max")

                        self.mnp_ipv4_cust_max = YLeaf(YType.uint32, "mnp-ipv4-cust-max")

                        self.mnp_ipv6_cust_max = YLeaf(YType.uint32, "mnp-ipv6-cust-max")

                        self.mnp_cust_max = YLeaf(YType.uint32, "mnp-cust-max")

                        self.mnp_ipv4_cust_cur = YLeaf(YType.uint32, "mnp-ipv4-cust-cur")

                        self.mnp_ipv6_cust_cur = YLeaf(YType.uint32, "mnp-ipv6-cust-cur")
                        self._segment_path = lambda: "mll-service"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.MllService, ['ignore_hoa', 'mnp_ipv4_lmn_max', 'mnp_ipv6_lmn_max', 'mnp_lmn_max', 'mnp_ipv4_cust_max', 'mnp_ipv6_cust_max', 'mnp_cust_max', 'mnp_ipv4_cust_cur', 'mnp_ipv6_cust_cur'], name, value)


                class Intf(Entity):
                    """
                    MAG Access List
                    
                    .. attribute:: apn
                    
                    	APN Present
                    	**type**\: bool
                    
                    .. attribute:: interface
                    
                    	Access Interface Name
                    	**type**\: str
                    
                    .. attribute:: apn_name
                    
                    	APN Name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf, self).__init__()

                        self.yang_name = "intf"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.apn = YLeaf(YType.boolean, "apn")

                        self.interface = YLeaf(YType.str, "interface")

                        self.apn_name = YLeaf(YType.str, "apn-name")
                        self._segment_path = lambda: "intf"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Intf, ['apn', 'interface', 'apn_name'], name, value)


                class Peer(Entity):
                    """
                    Peer Parameters
                    
                    .. attribute:: peer
                    
                    	Peer Name
                    	**type**\: str
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Peer static tunnel intf
                    	**type**\: str
                    
                    .. attribute:: encap
                    
                    	Encapsulation Type
                    	**type**\:  :py:class:`Pmipv6Encap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_oper.Pmipv6Encap>`
                    
                    .. attribute:: auth
                    
                    	Authentication Option
                    	**type**\: bool
                    
                    .. attribute:: vrf
                    
                    	VRF Present
                    	**type**\: bool
                    
                    .. attribute:: statictunnel
                    
                    	Static tunnel Present
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.peer = YLeaf(YType.str, "peer")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.encap = YLeaf(YType.enumeration, "encap")

                        self.auth = YLeaf(YType.boolean, "auth")

                        self.vrf = YLeaf(YType.boolean, "vrf")

                        self.statictunnel = YLeaf(YType.boolean, "statictunnel")
                        self._segment_path = lambda: "peer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Peer, ['peer', 'vrf_name', 'interface', 'encap', 'auth', 'vrf', 'statictunnel'], name, value)


                class Network(Entity):
                    """
                    LMA Network Parameters
                    
                    .. attribute:: v4pool
                    
                    	IPV4 pool Present
                    	**type**\: bool
                    
                    .. attribute:: v6pool
                    
                    	IPV6 pool Present
                    	**type**\: bool
                    
                    .. attribute:: network
                    
                    	Network Name
                    	**type**\: str
                    
                    .. attribute:: ipv4
                    
                    	IPv4 Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: v4pfx_len
                    
                    	v4 prefix len
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: v6pfx_len
                    
                    	v6 prefix len
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: mrnet
                    
                    	num of mrnet
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Network, self).__init__()

                        self.yang_name = "network"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.v4pool = YLeaf(YType.boolean, "v4pool")

                        self.v6pool = YLeaf(YType.boolean, "v6pool")

                        self.network = YLeaf(YType.str, "network")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")

                        self.v4pfx_len = YLeaf(YType.uint8, "v4pfx-len")

                        self.v6pfx_len = YLeaf(YType.uint8, "v6pfx-len")

                        self.mrnet = YLeaf(YType.uint8, "mrnet")
                        self._segment_path = lambda: "network"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Network, ['v4pool', 'v6pool', 'network', 'ipv4', 'ipv6', 'v4pfx_len', 'v6pfx_len', 'mrnet'], name, value)


                class Cust(Entity):
                    """
                    Customer parameters
                    
                    .. attribute:: cust
                    
                    	Customer Present
                    	**type**\: bool
                    
                    .. attribute:: vrf
                    
                    	Customer VRF Present
                    	**type**\: bool
                    
                    .. attribute:: t_vrf
                    
                    	Transport VRF Present
                    	**type**\: bool
                    
                    .. attribute:: auth_option
                    
                    	Authentication Option
                    	**type**\: bool
                    
                    .. attribute:: heart_beat
                    
                    	HeartBeat Option
                    	**type**\: bool
                    
                    .. attribute:: reg_time
                    
                    	BCE Registration Lifetime
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cust_name
                    
                    	CUSTOMER Name
                    	**type**\: str
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: t_vrf_name
                    
                    	Transport VRF Name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ip-mobileip-oper'
                    _revision = '2016-03-10'

                    def __init__(self):
                        super(Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust, self).__init__()

                        self.yang_name = "cust"
                        self.yang_parent_name = "global-variables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.cust = YLeaf(YType.boolean, "cust")

                        self.vrf = YLeaf(YType.boolean, "vrf")

                        self.t_vrf = YLeaf(YType.boolean, "t-vrf")

                        self.auth_option = YLeaf(YType.boolean, "auth-option")

                        self.heart_beat = YLeaf(YType.boolean, "heart-beat")

                        self.reg_time = YLeaf(YType.uint32, "reg-time")

                        self.cust_name = YLeaf(YType.str, "cust-name")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.t_vrf_name = YLeaf(YType.str, "t-vrf-name")
                        self._segment_path = lambda: "cust"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-mobileip-oper:pmipv6/lma/config-variables/global-variables/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pmipv6.Lma.ConfigVariables.GlobalVariables.Cust, ['cust', 'vrf', 't_vrf', 'auth_option', 'heart_beat', 'reg_time', 'cust_name', 'vrf_name', 't_vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Pmipv6()
        return self._top_entity

