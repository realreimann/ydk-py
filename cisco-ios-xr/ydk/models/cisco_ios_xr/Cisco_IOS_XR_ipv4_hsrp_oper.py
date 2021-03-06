""" Cisco_IOS_XR_ipv4_hsrp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package operational data.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HsrpBAf(Enum):
    """
    HsrpBAf

    Hsrp b af

    .. data:: ipv4 = 0

    	IPv4 Address Family

    .. data:: ipv6 = 1

    	IPv6 Address Family

    .. data:: count = 2

    	The number of supported address families

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")

    count = Enum.YLeaf(2, "count")


class HsrpBfdSessionState(Enum):
    """
    HsrpBfdSessionState

    Hsrp bfd session state

    .. data:: bfd_state_none = 0

    	None

    .. data:: bfd_state_inactive = 1

    	Inactive

    .. data:: bfd_state_up = 2

    	Up

    .. data:: bfd_state_down = 3

    	Down

    """

    bfd_state_none = Enum.YLeaf(0, "bfd-state-none")

    bfd_state_inactive = Enum.YLeaf(1, "bfd-state-inactive")

    bfd_state_up = Enum.YLeaf(2, "bfd-state-up")

    bfd_state_down = Enum.YLeaf(3, "bfd-state-down")


class HsrpStateChangeReason(Enum):
    """
    HsrpStateChangeReason

    Hsrp state change reason

    .. data:: state_change_bfd_down = 0

    	BFD session down

    .. data:: state_change_vip_learnt = 1

    	Virtual IP learnt

    .. data:: state_change_interface_ip = 2

    	Interface IP update

    .. data:: state_change_delay_timer = 3

    	Delay timer expired

    .. data:: state_change_startup = 4

    	Ready on startup

    .. data:: state_change_shutdown = 5

    	HSRP shut down

    .. data:: state_change_interface_up = 6

    	Interface Up update

    .. data:: state_change_interface_down = 7

    	Interface Down update

    .. data:: state_change_active_timer = 8

    	Active timer expired

    .. data:: state_change_standby_timer = 9

    	Standby timer expired

    .. data:: state_change_resign = 10

    	Resign received

    .. data:: state_change_coup = 11

    	Coup received

    .. data:: state_change_higher_priority_speak = 12

    	Higher priority speak received

    .. data:: state_change_higher_priority_standby = 13

    	Higher priority standby received

    .. data:: state_change_lower_priority_standby = 14

    	Lower priority standby received

    .. data:: state_change_higher_priority_active = 15

    	Higher priority active received

    .. data:: state_change_lower_priority_active = 16

    	Lower priority active received

    .. data:: state_change_virtual_ip_configured = 17

    	Virtual IP configured

    .. data:: state_change_virtual_ip_lost = 18

    	Virtual IP lost

    .. data:: state_change_recovered_from_checkpoint = 19

    	Recovered from checkpoint

    .. data:: state_change_mac_update = 20

    	MAC address update

    .. data:: state_change_admin = 21

    	Forwarder Admin state change

    .. data:: state_change_parent = 22

    	MGO parent change

    .. data:: state_change_chkpt_update = 23

    	Checkpoint update from Primary HSRP instance

    .. data:: state_change_issu_resync = 24

    	Resync following ISSU primary event

    .. data:: state_change_reset_to_learn = 25

    	Reset to learn parameters

    .. data:: state_change_max = 26

    	Maximum reason in enumeration

    """

    state_change_bfd_down = Enum.YLeaf(0, "state-change-bfd-down")

    state_change_vip_learnt = Enum.YLeaf(1, "state-change-vip-learnt")

    state_change_interface_ip = Enum.YLeaf(2, "state-change-interface-ip")

    state_change_delay_timer = Enum.YLeaf(3, "state-change-delay-timer")

    state_change_startup = Enum.YLeaf(4, "state-change-startup")

    state_change_shutdown = Enum.YLeaf(5, "state-change-shutdown")

    state_change_interface_up = Enum.YLeaf(6, "state-change-interface-up")

    state_change_interface_down = Enum.YLeaf(7, "state-change-interface-down")

    state_change_active_timer = Enum.YLeaf(8, "state-change-active-timer")

    state_change_standby_timer = Enum.YLeaf(9, "state-change-standby-timer")

    state_change_resign = Enum.YLeaf(10, "state-change-resign")

    state_change_coup = Enum.YLeaf(11, "state-change-coup")

    state_change_higher_priority_speak = Enum.YLeaf(12, "state-change-higher-priority-speak")

    state_change_higher_priority_standby = Enum.YLeaf(13, "state-change-higher-priority-standby")

    state_change_lower_priority_standby = Enum.YLeaf(14, "state-change-lower-priority-standby")

    state_change_higher_priority_active = Enum.YLeaf(15, "state-change-higher-priority-active")

    state_change_lower_priority_active = Enum.YLeaf(16, "state-change-lower-priority-active")

    state_change_virtual_ip_configured = Enum.YLeaf(17, "state-change-virtual-ip-configured")

    state_change_virtual_ip_lost = Enum.YLeaf(18, "state-change-virtual-ip-lost")

    state_change_recovered_from_checkpoint = Enum.YLeaf(19, "state-change-recovered-from-checkpoint")

    state_change_mac_update = Enum.YLeaf(20, "state-change-mac-update")

    state_change_admin = Enum.YLeaf(21, "state-change-admin")

    state_change_parent = Enum.YLeaf(22, "state-change-parent")

    state_change_chkpt_update = Enum.YLeaf(23, "state-change-chkpt-update")

    state_change_issu_resync = Enum.YLeaf(24, "state-change-issu-resync")

    state_change_reset_to_learn = Enum.YLeaf(25, "state-change-reset-to-learn")

    state_change_max = Enum.YLeaf(26, "state-change-max")


class HsrpVmacState(Enum):
    """
    HsrpVmacState

    Hsrp vmac state

    .. data:: stored = 0

    	VMAC stored locally

    .. data:: reserved = 1

    	VMAC reserved in mac table

    .. data:: active = 2

    	VMAC active in mac table

    .. data:: reserving = 3

    	VMAC not yet reserved in mac table

    """

    stored = Enum.YLeaf(0, "stored")

    reserved = Enum.YLeaf(1, "reserved")

    active = Enum.YLeaf(2, "active")

    reserving = Enum.YLeaf(3, "reserving")


class StandbyGrpState(Enum):
    """
    StandbyGrpState

    Standby grp state

    .. data:: state_initial = 1

    	Initial

    .. data:: state_learn = 2

    	Learn

    .. data:: state_listen = 3

    	Listen

    .. data:: state_speak = 4

    	Speak

    .. data:: state_standby = 5

    	Standby

    .. data:: state_active = 6

    	Active

    """

    state_initial = Enum.YLeaf(1, "state-initial")

    state_learn = Enum.YLeaf(2, "state-learn")

    state_listen = Enum.YLeaf(3, "state-listen")

    state_speak = Enum.YLeaf(4, "state-speak")

    state_standby = Enum.YLeaf(5, "state-standby")

    state_active = Enum.YLeaf(6, "state-active")



class Hsrp(Entity):
    """
    HSRP operational data
    
    .. attribute:: ipv4
    
    	IPv4 HSRP information
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4>`
    
    .. attribute:: mgo_sessions
    
    	HSRP MGO session table
    	**type**\:  :py:class:`MgoSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions>`
    
    .. attribute:: ipv6
    
    	IPv6 HSRP information
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6>`
    
    .. attribute:: bfd_sessions
    
    	The table of HSRP BFD Sessions
    	**type**\:  :py:class:`BfdSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions>`
    
    .. attribute:: summary
    
    	HSRP summary statistics
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Summary>`
    
    

    """

    _prefix = 'ipv4-hsrp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Hsrp, self).__init__()
        self._top_entity = None

        self.yang_name = "hsrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-hsrp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ipv4" : ("ipv4", Hsrp.Ipv4), "mgo-sessions" : ("mgo_sessions", Hsrp.MgoSessions), "ipv6" : ("ipv6", Hsrp.Ipv6), "bfd-sessions" : ("bfd_sessions", Hsrp.BfdSessions), "summary" : ("summary", Hsrp.Summary)}
        self._child_list_classes = {}

        self.ipv4 = Hsrp.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._children_yang_names.add("ipv4")

        self.mgo_sessions = Hsrp.MgoSessions()
        self.mgo_sessions.parent = self
        self._children_name_map["mgo_sessions"] = "mgo-sessions"
        self._children_yang_names.add("mgo-sessions")

        self.ipv6 = Hsrp.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._children_yang_names.add("ipv6")

        self.bfd_sessions = Hsrp.BfdSessions()
        self.bfd_sessions.parent = self
        self._children_name_map["bfd_sessions"] = "bfd-sessions"
        self._children_yang_names.add("bfd-sessions")

        self.summary = Hsrp.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp"


    class Ipv4(Entity):
        """
        IPv4 HSRP information
        
        .. attribute:: groups
        
        	The HSRP standby group table
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups>`
        
        .. attribute:: tracked_interfaces
        
        	The HSRP tracked interfaces table
        	**type**\:  :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.TrackedInterfaces>`
        
        .. attribute:: interfaces
        
        	The HSRP interface information table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"groups" : ("groups", Hsrp.Ipv4.Groups), "tracked-interfaces" : ("tracked_interfaces", Hsrp.Ipv4.TrackedInterfaces), "interfaces" : ("interfaces", Hsrp.Ipv4.Interfaces)}
            self._child_list_classes = {}

            self.groups = Hsrp.Ipv4.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")

            self.tracked_interfaces = Hsrp.Ipv4.TrackedInterfaces()
            self.tracked_interfaces.parent = self
            self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
            self._children_yang_names.add("tracked-interfaces")

            self.interfaces = Hsrp.Ipv4.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self._segment_path()


        class Groups(Entity):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"group" : ("group", Hsrp.Ipv4.Groups.Group)}

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv4.Groups, [], name, value)


            class Group(Entity):
                """
                An HSRP standby group
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:  :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.ResignSentTime>`
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:  :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.ResignReceivedTime>`
                
                .. attribute:: coup_sent_time
                
                	Time last coup was sent
                	**type**\:  :py:class:`CoupSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.CoupSentTime>`
                
                .. attribute:: coup_received_time
                
                	Time last coup was received
                	**type**\:  :py:class:`CoupReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.CoupReceivedTime>`
                
                .. attribute:: statistics
                
                	HSRP Group statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.Statistics>`
                
                .. attribute:: authentication_string
                
                	Authentication string
                	**type**\: str
                
                	**length:** 0..9
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
                
                .. attribute:: version
                
                	HSRP Protocol Version
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\: bool
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: preempt_delay
                
                	Preempt delay time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: preempt_timer_secs
                
                	Preempt time remaining in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hello_time
                
                	Hellotime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hold_time
                
                	Holdtime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hello_time
                
                	Learned hellotime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hold_time
                
                	Learned holdtime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: virtual_ip_address
                
                	Configured Virtual IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ip_address
                
                	Active router's IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ipv6_address
                
                	Active router's IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_mac_address
                
                	Active router's interface MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: standby_ip_address
                
                	Standby router's IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_ipv6_address
                
                	Standby router's IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_mac_address
                
                	Standby router's interface MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: hsrp_router_state
                
                	HSRP router state
                	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                
                .. attribute:: interface_name_xr
                
                	Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: router_priority
                
                	Priority of the router
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: active_priority
                
                	Priority of the Active router
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: active_timer_flag
                
                	Active timer running flag
                	**type**\: bool
                
                .. attribute:: active_timer_secs
                
                	Active timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: active_timer_msecs
                
                	Active timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: standby_timer_flag
                
                	Standby timer running flag
                	**type**\: bool
                
                .. attribute:: standby_timer_secs
                
                	Standby timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: standby_timer_msecs
                
                	Standby timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_flag
                
                	Hello timer running flag
                	**type**\: bool
                
                .. attribute:: hello_timer_secs
                
                	Hello timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hello_timer_msecs
                
                	Hello timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\: bool
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: current_state_timer_secs
                
                	Time in current state secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_count
                
                	Number of tracked interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked interfaces up
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: preempt_enabled
                
                	Preempt enabled
                	**type**\: bool
                
                .. attribute:: use_configured_timers
                
                	Use configured timers
                	**type**\: bool
                
                .. attribute:: use_configured_virtual_ip
                
                	Use configured virtual IP
                	**type**\: bool
                
                .. attribute:: use_bia_configured
                
                	Use burnt in MAC address configured
                	**type**\: bool
                
                .. attribute:: configured_timers
                
                	Non\-default timers are configured
                	**type**\: bool
                
                .. attribute:: configured_mac_address
                
                	MAC address configured
                	**type**\: bool
                
                .. attribute:: redirects_disabled
                
                	HSRP redirects disabled
                	**type**\: bool
                
                .. attribute:: bfd_enabled
                
                	HSRP BFD fast failover
                	**type**\: bool
                
                .. attribute:: bfd_interface
                
                	BFD Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: bfd_peer_ip_address
                
                	BFD Peer IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_peer_ipv6_address
                
                	BFD Peer IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:  :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:  :py:class:`HsrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacState>`
                
                .. attribute:: secondary_address
                
                	Secondary virtual IP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: global_address
                
                	Global virtual IPv6 addresses
                	**type**\: list of  		 :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.GlobalAddress>`
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of  		 :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.StateChangeHistory>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"resign-sent-time" : ("resign_sent_time", Hsrp.Ipv4.Groups.Group.ResignSentTime), "resign-received-time" : ("resign_received_time", Hsrp.Ipv4.Groups.Group.ResignReceivedTime), "coup-sent-time" : ("coup_sent_time", Hsrp.Ipv4.Groups.Group.CoupSentTime), "coup-received-time" : ("coup_received_time", Hsrp.Ipv4.Groups.Group.CoupReceivedTime), "statistics" : ("statistics", Hsrp.Ipv4.Groups.Group.Statistics)}
                    self._child_list_classes = {"global-address" : ("global_address", Hsrp.Ipv4.Groups.Group.GlobalAddress), "state-change-history" : ("state_change_history", Hsrp.Ipv4.Groups.Group.StateChangeHistory)}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.version = YLeaf(YType.uint8, "version")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.preempt_delay = YLeaf(YType.uint32, "preempt-delay")

                    self.preempt_timer_secs = YLeaf(YType.uint32, "preempt-timer-secs")

                    self.hello_time = YLeaf(YType.uint32, "hello-time")

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.learned_hello_time = YLeaf(YType.uint32, "learned-hello-time")

                    self.learned_hold_time = YLeaf(YType.uint32, "learned-hold-time")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.virtual_ip_address = YLeaf(YType.str, "virtual-ip-address")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.active_ip_address = YLeaf(YType.str, "active-ip-address")

                    self.active_ipv6_address = YLeaf(YType.str, "active-ipv6-address")

                    self.active_mac_address = YLeaf(YType.str, "active-mac-address")

                    self.standby_ip_address = YLeaf(YType.str, "standby-ip-address")

                    self.standby_ipv6_address = YLeaf(YType.str, "standby-ipv6-address")

                    self.standby_mac_address = YLeaf(YType.str, "standby-mac-address")

                    self.hsrp_router_state = YLeaf(YType.enumeration, "hsrp-router-state")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.interface = YLeaf(YType.str, "interface")

                    self.router_priority = YLeaf(YType.uint8, "router-priority")

                    self.active_priority = YLeaf(YType.uint8, "active-priority")

                    self.active_timer_flag = YLeaf(YType.boolean, "active-timer-flag")

                    self.active_timer_secs = YLeaf(YType.uint32, "active-timer-secs")

                    self.active_timer_msecs = YLeaf(YType.uint32, "active-timer-msecs")

                    self.standby_timer_flag = YLeaf(YType.boolean, "standby-timer-flag")

                    self.standby_timer_secs = YLeaf(YType.uint32, "standby-timer-secs")

                    self.standby_timer_msecs = YLeaf(YType.uint32, "standby-timer-msecs")

                    self.hello_timer_flag = YLeaf(YType.boolean, "hello-timer-flag")

                    self.hello_timer_secs = YLeaf(YType.uint32, "hello-timer-secs")

                    self.hello_timer_msecs = YLeaf(YType.uint32, "hello-timer-msecs")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.current_state_timer_secs = YLeaf(YType.uint32, "current-state-timer-secs")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.preempt_enabled = YLeaf(YType.boolean, "preempt-enabled")

                    self.use_configured_timers = YLeaf(YType.boolean, "use-configured-timers")

                    self.use_configured_virtual_ip = YLeaf(YType.boolean, "use-configured-virtual-ip")

                    self.use_bia_configured = YLeaf(YType.boolean, "use-bia-configured")

                    self.configured_timers = YLeaf(YType.boolean, "configured-timers")

                    self.configured_mac_address = YLeaf(YType.boolean, "configured-mac-address")

                    self.redirects_disabled = YLeaf(YType.boolean, "redirects-disabled")

                    self.bfd_enabled = YLeaf(YType.boolean, "bfd-enabled")

                    self.bfd_interface = YLeaf(YType.str, "bfd-interface")

                    self.bfd_peer_ip_address = YLeaf(YType.str, "bfd-peer-ip-address")

                    self.bfd_peer_ipv6_address = YLeaf(YType.str, "bfd-peer-ipv6-address")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.secondary_address = YLeafList(YType.str, "secondary-address")

                    self.resign_sent_time = Hsrp.Ipv4.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.resign_received_time = Hsrp.Ipv4.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.coup_sent_time = Hsrp.Ipv4.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self._children_name_map["coup_sent_time"] = "coup-sent-time"
                    self._children_yang_names.add("coup-sent-time")

                    self.coup_received_time = Hsrp.Ipv4.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self._children_name_map["coup_received_time"] = "coup-received-time"
                    self._children_yang_names.add("coup-received-time")

                    self.statistics = Hsrp.Ipv4.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.global_address = YList(self)
                    self.state_change_history = YList(self)
                    self._segment_path = lambda: "group" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv4.Groups.Group, ['interface_name', 'group_number', 'authentication_string', 'virtual_mac_address', 'hsrp_group_number', 'address_family', 'version', 'session_name', 'slaves', 'is_slave', 'followed_session_name', 'configured_priority', 'preempt_delay', 'preempt_timer_secs', 'hello_time', 'hold_time', 'learned_hello_time', 'learned_hold_time', 'min_delay_time', 'reload_delay_time', 'virtual_ip_address', 'virtual_linklocal_ipv6_address', 'active_ip_address', 'active_ipv6_address', 'active_mac_address', 'standby_ip_address', 'standby_ipv6_address', 'standby_mac_address', 'hsrp_router_state', 'interface_name_xr', 'interface', 'router_priority', 'active_priority', 'active_timer_flag', 'active_timer_secs', 'active_timer_msecs', 'standby_timer_flag', 'standby_timer_secs', 'standby_timer_msecs', 'hello_timer_flag', 'hello_timer_secs', 'hello_timer_msecs', 'delay_timer_flag', 'delay_timer_secs', 'delay_timer_msecs', 'current_state_timer_secs', 'state_change_count', 'tracked_interface_count', 'tracked_interface_up_count', 'preempt_enabled', 'use_configured_timers', 'use_configured_virtual_ip', 'use_bia_configured', 'configured_timers', 'configured_mac_address', 'redirects_disabled', 'bfd_enabled', 'bfd_interface', 'bfd_peer_ip_address', 'bfd_peer_ipv6_address', 'bfd_session_state', 'bfd_interval', 'bfd_multiplier', 'virtual_mac_address_state', 'secondary_address'], name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "resign-sent-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.ResignSentTime, ['seconds', 'nanoseconds'], name, value)


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "resign-received-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.ResignReceivedTime, ['seconds', 'nanoseconds'], name, value)


                class CoupSentTime(Entity):
                    """
                    Time last coup was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.CoupSentTime, self).__init__()

                        self.yang_name = "coup-sent-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "coup-sent-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.CoupSentTime, ['seconds', 'nanoseconds'], name, value)


                class CoupReceivedTime(Entity):
                    """
                    Time last coup was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.CoupReceivedTime, self).__init__()

                        self.yang_name = "coup-received-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "coup-received-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.CoupReceivedTime, ['seconds', 'nanoseconds'], name, value)


                class Statistics(Entity):
                    """
                    HSRP Group statistics
                    
                    .. attribute:: active_transitions
                    
                    	Number of transitions to Active State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_transitions
                    
                    	Number of transitions to Standby State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speak_transitions
                    
                    	Number of transitions to Speak State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: listen_transitions
                    
                    	Number of transitions to Listen State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: learn_transitions
                    
                    	Number of transitions to Learn State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_transitions
                    
                    	Number of transitions to Init State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_sent
                    
                    	Number of Hello Packets sent (NB\: Bundles only)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_sent
                    
                    	Number of Resign Packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_sent
                    
                    	Number of Coup Packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_received
                    
                    	Number of Hello Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_received
                    
                    	Number of Resign Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_received
                    
                    	Number of Coup Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_fail_received
                    
                    	Number of Packets received that failed authentication
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer_received
                    
                    	Number of packets received with invalid Hello Time value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mismatch_virtual_ip_address_received
                    
                    	Number of packets received with mismatching virtual IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_transitions = YLeaf(YType.uint32, "active-transitions")

                        self.standby_transitions = YLeaf(YType.uint32, "standby-transitions")

                        self.speak_transitions = YLeaf(YType.uint32, "speak-transitions")

                        self.listen_transitions = YLeaf(YType.uint32, "listen-transitions")

                        self.learn_transitions = YLeaf(YType.uint32, "learn-transitions")

                        self.init_transitions = YLeaf(YType.uint32, "init-transitions")

                        self.hello_packets_sent = YLeaf(YType.uint32, "hello-packets-sent")

                        self.resign_packets_sent = YLeaf(YType.uint32, "resign-packets-sent")

                        self.coup_packets_sent = YLeaf(YType.uint32, "coup-packets-sent")

                        self.hello_packets_received = YLeaf(YType.uint32, "hello-packets-received")

                        self.resign_packets_received = YLeaf(YType.uint32, "resign-packets-received")

                        self.coup_packets_received = YLeaf(YType.uint32, "coup-packets-received")

                        self.auth_fail_received = YLeaf(YType.uint32, "auth-fail-received")

                        self.invalid_timer_received = YLeaf(YType.uint32, "invalid-timer-received")

                        self.mismatch_virtual_ip_address_received = YLeaf(YType.uint32, "mismatch-virtual-ip-address-received")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.Statistics, ['active_transitions', 'standby_transitions', 'speak_transitions', 'listen_transitions', 'learn_transitions', 'init_transitions', 'hello_packets_sent', 'resign_packets_sent', 'coup_packets_sent', 'hello_packets_received', 'resign_packets_received', 'coup_packets_received', 'auth_fail_received', 'invalid_timer_received', 'mismatch_virtual_ip_address_received'], name, value)


                class GlobalAddress(Entity):
                    """
                    Global virtual IPv6 addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.GlobalAddress, self).__init__()

                        self.yang_name = "global-address"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                        self._segment_path = lambda: "global-address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.GlobalAddress, ['ipv6_address'], name, value)


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:  :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:  :py:class:`HsrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReason>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Groups.Group.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"time" : ("time", Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time)}
                        self._child_list_classes = {}

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._children_yang_names.add("time")
                        self._segment_path = lambda: "state-change-history"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Groups.Group.StateChangeHistory, ['old_state', 'new_state', 'reason'], name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.seconds = YLeaf(YType.uint32, "seconds")

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                            self._segment_path = lambda: "time"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time, ['seconds', 'nanoseconds'], name, value)


        class TrackedInterfaces(Entity):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of  		 :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.TrackedInterfaces, self).__init__()

                self.yang_name = "tracked-interfaces"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"tracked-interface" : ("tracked_interface", Hsrp.Ipv4.TrackedInterfaces.TrackedInterface)}

                self.tracked_interface = YList(self)
                self._segment_path = lambda: "tracked-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv4.TrackedInterfaces, [], name, value)


            class TrackedInterface(Entity):
                """
                An HSRP tracked interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The interface name of the interface being tracked
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_decrement
                
                	Priority weighting
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_up_flag
                
                	Interface up flag
                	**type**\: bool
                
                .. attribute:: tracked_interface_name_xr
                
                	Tracked Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: is_object
                
                	Tracked Object Flag
                	**type**\: bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.TrackedInterfaces.TrackedInterface, self).__init__()

                    self.yang_name = "tracked-interface"
                    self.yang_parent_name = "tracked-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.interface_up_flag = YLeaf(YType.boolean, "interface-up-flag")

                    self.tracked_interface_name_xr = YLeaf(YType.str, "tracked-interface-name-xr")

                    self.is_object = YLeaf(YType.boolean, "is-object")
                    self._segment_path = lambda: "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/tracked-interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv4.TrackedInterfaces.TrackedInterface, ['interface_name', 'group_number', 'tracked_interface_name', 'interface', 'hsrp_group_number', 'priority_decrement', 'interface_up_flag', 'tracked_interface_name_xr', 'is_object'], name, value)


        class Interfaces(Entity):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv4.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Hsrp.Ipv4.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv4.Interfaces, [], name, value)


            class Interface(Entity):
                """
                A HSRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: statistics
                
                	HSRP Interface Statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv4.Interfaces.Interface.Statistics>`
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: use_bia_flag
                
                	Use burnt in mac address flag
                	**type**\: bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv4.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"statistics" : ("statistics", Hsrp.Ipv4.Interfaces.Interface.Statistics)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.use_bia_flag = YLeaf(YType.boolean, "use-bia-flag")

                    self.statistics = Hsrp.Ipv4.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv4/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv4.Interfaces.Interface, ['interface_name', 'interface', 'use_bia_flag'], name, value)


                class Statistics(Entity):
                    """
                    HSRP Interface Statistics
                    
                    .. attribute:: advert_packets_sent
                    
                    	Number of advertisement packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: advert_packets_received
                    
                    	Number of advertisement packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: long_packets_received
                    
                    	Number of packets received that were too Long
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: short_packets_received
                    
                    	Number of packets received that were too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_received
                    
                    	Number of packets received with invalid version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_operation_code_received
                    
                    	Number of packets received with invalid operation code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_group_received
                    
                    	Number of packets received for an unknown group id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inoperational_group_received
                    
                    	Number of packets received for an inoperational group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conflict_source_ip_address_received
                    
                    	Number of packets received from a conflicting Source IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv4.Interfaces.Interface.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.advert_packets_sent = YLeaf(YType.uint32, "advert-packets-sent")

                        self.advert_packets_received = YLeaf(YType.uint32, "advert-packets-received")

                        self.long_packets_received = YLeaf(YType.uint32, "long-packets-received")

                        self.short_packets_received = YLeaf(YType.uint32, "short-packets-received")

                        self.invalid_version_received = YLeaf(YType.uint32, "invalid-version-received")

                        self.invalid_operation_code_received = YLeaf(YType.uint32, "invalid-operation-code-received")

                        self.unknown_group_received = YLeaf(YType.uint32, "unknown-group-received")

                        self.inoperational_group_received = YLeaf(YType.uint32, "inoperational-group-received")

                        self.conflict_source_ip_address_received = YLeaf(YType.uint32, "conflict-source-ip-address-received")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv4.Interfaces.Interface.Statistics, ['advert_packets_sent', 'advert_packets_received', 'long_packets_received', 'short_packets_received', 'invalid_version_received', 'invalid_operation_code_received', 'unknown_group_received', 'inoperational_group_received', 'conflict_source_ip_address_received'], name, value)


    class MgoSessions(Entity):
        """
        HSRP MGO session table
        
        .. attribute:: mgo_session
        
        	HSRP MGO session
        	**type**\: list of  		 :py:class:`MgoSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.MgoSessions, self).__init__()

            self.yang_name = "mgo-sessions"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mgo-session" : ("mgo_session", Hsrp.MgoSessions.MgoSession)}

            self.mgo_session = YList(self)
            self._segment_path = lambda: "mgo-sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.MgoSessions, [], name, value)


        class MgoSession(Entity):
            """
            HSRP MGO session
            
            .. attribute:: session_name  <key>
            
            	HSRP MGO session name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: primary_session_name
            
            	Session Name
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: primary_session_interface
            
            	Interface of primary session
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: primary_af_name
            
            	Address family of primary session
            	**type**\:  :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
            
            .. attribute:: primary_session_number
            
            	Group number of primary session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: primary_session_state
            
            	State of primary session
            	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
            
            .. attribute:: slave
            
            	List of slaves following this primary session
            	**type**\: list of  		 :py:class:`Slave <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.MgoSessions.MgoSession.Slave>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.MgoSessions.MgoSession, self).__init__()

                self.yang_name = "mgo-session"
                self.yang_parent_name = "mgo-sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"slave" : ("slave", Hsrp.MgoSessions.MgoSession.Slave)}

                self.session_name = YLeaf(YType.str, "session-name")

                self.primary_session_name = YLeaf(YType.str, "primary-session-name")

                self.primary_session_interface = YLeaf(YType.str, "primary-session-interface")

                self.primary_af_name = YLeaf(YType.enumeration, "primary-af-name")

                self.primary_session_number = YLeaf(YType.uint32, "primary-session-number")

                self.primary_session_state = YLeaf(YType.enumeration, "primary-session-state")

                self.slave = YList(self)
                self._segment_path = lambda: "mgo-session" + "[session-name='" + self.session_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/mgo-sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.MgoSessions.MgoSession, ['session_name', 'primary_session_name', 'primary_session_interface', 'primary_af_name', 'primary_session_number', 'primary_session_state'], name, value)


            class Slave(Entity):
                """
                List of slaves following this primary session
                
                .. attribute:: slave_group_interface
                
                	Interface of slave group
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: slave_group_number
                
                	Group number of slave group
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.MgoSessions.MgoSession.Slave, self).__init__()

                    self.yang_name = "slave"
                    self.yang_parent_name = "mgo-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.slave_group_interface = YLeaf(YType.str, "slave-group-interface")

                    self.slave_group_number = YLeaf(YType.uint32, "slave-group-number")
                    self._segment_path = lambda: "slave"

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.MgoSessions.MgoSession.Slave, ['slave_group_interface', 'slave_group_number'], name, value)


    class Ipv6(Entity):
        """
        IPv6 HSRP information
        
        .. attribute:: tracked_interfaces
        
        	The HSRP tracked interfaces table
        	**type**\:  :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.TrackedInterfaces>`
        
        .. attribute:: groups
        
        	The HSRP standby group table
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups>`
        
        .. attribute:: interfaces
        
        	The HSRP interface information table
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tracked-interfaces" : ("tracked_interfaces", Hsrp.Ipv6.TrackedInterfaces), "groups" : ("groups", Hsrp.Ipv6.Groups), "interfaces" : ("interfaces", Hsrp.Ipv6.Interfaces)}
            self._child_list_classes = {}

            self.tracked_interfaces = Hsrp.Ipv6.TrackedInterfaces()
            self.tracked_interfaces.parent = self
            self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
            self._children_yang_names.add("tracked-interfaces")

            self.groups = Hsrp.Ipv6.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")

            self.interfaces = Hsrp.Ipv6.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self._segment_path()


        class TrackedInterfaces(Entity):
            """
            The HSRP tracked interfaces table
            
            .. attribute:: tracked_interface
            
            	An HSRP tracked interface entry
            	**type**\: list of  		 :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.TrackedInterfaces.TrackedInterface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.TrackedInterfaces, self).__init__()

                self.yang_name = "tracked-interfaces"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"tracked-interface" : ("tracked_interface", Hsrp.Ipv6.TrackedInterfaces.TrackedInterface)}

                self.tracked_interface = YList(self)
                self._segment_path = lambda: "tracked-interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv6.TrackedInterfaces, [], name, value)


            class TrackedInterface(Entity):
                """
                An HSRP tracked interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name of the interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: tracked_interface_name  <key>
                
                	The interface name of the interface being tracked
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority_decrement
                
                	Priority weighting
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_up_flag
                
                	Interface up flag
                	**type**\: bool
                
                .. attribute:: tracked_interface_name_xr
                
                	Tracked Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: is_object
                
                	Tracked Object Flag
                	**type**\: bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.TrackedInterfaces.TrackedInterface, self).__init__()

                    self.yang_name = "tracked-interface"
                    self.yang_parent_name = "tracked-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.tracked_interface_name = YLeaf(YType.str, "tracked-interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                    self.interface_up_flag = YLeaf(YType.boolean, "interface-up-flag")

                    self.tracked_interface_name_xr = YLeaf(YType.str, "tracked-interface-name-xr")

                    self.is_object = YLeaf(YType.boolean, "is-object")
                    self._segment_path = lambda: "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']" + "[tracked-interface-name='" + self.tracked_interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/tracked-interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv6.TrackedInterfaces.TrackedInterface, ['interface_name', 'group_number', 'tracked_interface_name', 'interface', 'hsrp_group_number', 'priority_decrement', 'interface_up_flag', 'tracked_interface_name_xr', 'is_object'], name, value)


        class Groups(Entity):
            """
            The HSRP standby group table
            
            .. attribute:: group
            
            	An HSRP standby group
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"group" : ("group", Hsrp.Ipv6.Groups.Group)}

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv6.Groups, [], name, value)


            class Group(Entity):
                """
                An HSRP standby group
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: group_number  <key>
                
                	The HSRP group number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: resign_sent_time
                
                	Time last resign was sent
                	**type**\:  :py:class:`ResignSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.ResignSentTime>`
                
                .. attribute:: resign_received_time
                
                	Time last resign was received
                	**type**\:  :py:class:`ResignReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.ResignReceivedTime>`
                
                .. attribute:: coup_sent_time
                
                	Time last coup was sent
                	**type**\:  :py:class:`CoupSentTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.CoupSentTime>`
                
                .. attribute:: coup_received_time
                
                	Time last coup was received
                	**type**\:  :py:class:`CoupReceivedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.CoupReceivedTime>`
                
                .. attribute:: statistics
                
                	HSRP Group statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.Statistics>`
                
                .. attribute:: authentication_string
                
                	Authentication string
                	**type**\: str
                
                	**length:** 0..9
                
                .. attribute:: virtual_mac_address
                
                	Virtual mac address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
                
                .. attribute:: version
                
                	HSRP Protocol Version
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: session_name
                
                	Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: slaves
                
                	Number of slaves following state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_slave
                
                	Group is a slave group
                	**type**\: bool
                
                .. attribute:: followed_session_name
                
                	Followed Session Name
                	**type**\: str
                
                	**length:** 0..16
                
                .. attribute:: configured_priority
                
                	Configured priority
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: preempt_delay
                
                	Preempt delay time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: preempt_timer_secs
                
                	Preempt time remaining in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hello_time
                
                	Hellotime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hold_time
                
                	Holdtime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hello_time
                
                	Learned hellotime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: learned_hold_time
                
                	Learned holdtime in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: min_delay_time
                
                	Minimum delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: reload_delay_time
                
                	Reload delay time in msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: virtual_ip_address
                
                	Configured Virtual IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtual_linklocal_ipv6_address
                
                	Virtual linklocal IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ip_address
                
                	Active router's IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_ipv6_address
                
                	Active router's IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: active_mac_address
                
                	Active router's interface MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: standby_ip_address
                
                	Standby router's IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_ipv6_address
                
                	Standby router's IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: standby_mac_address
                
                	Standby router's interface MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: hsrp_router_state
                
                	HSRP router state
                	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                
                .. attribute:: interface_name_xr
                
                	Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: router_priority
                
                	Priority of the router
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: active_priority
                
                	Priority of the Active router
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: active_timer_flag
                
                	Active timer running flag
                	**type**\: bool
                
                .. attribute:: active_timer_secs
                
                	Active timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: active_timer_msecs
                
                	Active timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: standby_timer_flag
                
                	Standby timer running flag
                	**type**\: bool
                
                .. attribute:: standby_timer_secs
                
                	Standby timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: standby_timer_msecs
                
                	Standby timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: hello_timer_flag
                
                	Hello timer running flag
                	**type**\: bool
                
                .. attribute:: hello_timer_secs
                
                	Hello timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: hello_timer_msecs
                
                	Hello timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: delay_timer_flag
                
                	Delay timer running flag
                	**type**\: bool
                
                .. attribute:: delay_timer_secs
                
                	Delay timer running time secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: delay_timer_msecs
                
                	Delay timer running time msecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: current_state_timer_secs
                
                	Time in current state secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: state_change_count
                
                	Number of state changes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_count
                
                	Number of tracked interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tracked_interface_up_count
                
                	Number of tracked interfaces up
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: preempt_enabled
                
                	Preempt enabled
                	**type**\: bool
                
                .. attribute:: use_configured_timers
                
                	Use configured timers
                	**type**\: bool
                
                .. attribute:: use_configured_virtual_ip
                
                	Use configured virtual IP
                	**type**\: bool
                
                .. attribute:: use_bia_configured
                
                	Use burnt in MAC address configured
                	**type**\: bool
                
                .. attribute:: configured_timers
                
                	Non\-default timers are configured
                	**type**\: bool
                
                .. attribute:: configured_mac_address
                
                	MAC address configured
                	**type**\: bool
                
                .. attribute:: redirects_disabled
                
                	HSRP redirects disabled
                	**type**\: bool
                
                .. attribute:: bfd_enabled
                
                	HSRP BFD fast failover
                	**type**\: bool
                
                .. attribute:: bfd_interface
                
                	BFD Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: bfd_peer_ip_address
                
                	BFD Peer IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_peer_ipv6_address
                
                	BFD Peer IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bfd_session_state
                
                	BFD session state
                	**type**\:  :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
                
                .. attribute:: bfd_interval
                
                	BFD packet send interval
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bfd_multiplier
                
                	BFD multiplier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: virtual_mac_address_state
                
                	Virtual mac address state
                	**type**\:  :py:class:`HsrpVmacState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpVmacState>`
                
                .. attribute:: secondary_address
                
                	Secondary virtual IP addresses
                	**type**\: list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: global_address
                
                	Global virtual IPv6 addresses
                	**type**\: list of  		 :py:class:`GlobalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.GlobalAddress>`
                
                .. attribute:: state_change_history
                
                	State change history
                	**type**\: list of  		 :py:class:`StateChangeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.StateChangeHistory>`
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"resign-sent-time" : ("resign_sent_time", Hsrp.Ipv6.Groups.Group.ResignSentTime), "resign-received-time" : ("resign_received_time", Hsrp.Ipv6.Groups.Group.ResignReceivedTime), "coup-sent-time" : ("coup_sent_time", Hsrp.Ipv6.Groups.Group.CoupSentTime), "coup-received-time" : ("coup_received_time", Hsrp.Ipv6.Groups.Group.CoupReceivedTime), "statistics" : ("statistics", Hsrp.Ipv6.Groups.Group.Statistics)}
                    self._child_list_classes = {"global-address" : ("global_address", Hsrp.Ipv6.Groups.Group.GlobalAddress), "state-change-history" : ("state_change_history", Hsrp.Ipv6.Groups.Group.StateChangeHistory)}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.group_number = YLeaf(YType.int32, "group-number")

                    self.authentication_string = YLeaf(YType.str, "authentication-string")

                    self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")

                    self.address_family = YLeaf(YType.enumeration, "address-family")

                    self.version = YLeaf(YType.uint8, "version")

                    self.session_name = YLeaf(YType.str, "session-name")

                    self.slaves = YLeaf(YType.uint32, "slaves")

                    self.is_slave = YLeaf(YType.boolean, "is-slave")

                    self.followed_session_name = YLeaf(YType.str, "followed-session-name")

                    self.configured_priority = YLeaf(YType.uint8, "configured-priority")

                    self.preempt_delay = YLeaf(YType.uint32, "preempt-delay")

                    self.preempt_timer_secs = YLeaf(YType.uint32, "preempt-timer-secs")

                    self.hello_time = YLeaf(YType.uint32, "hello-time")

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.learned_hello_time = YLeaf(YType.uint32, "learned-hello-time")

                    self.learned_hold_time = YLeaf(YType.uint32, "learned-hold-time")

                    self.min_delay_time = YLeaf(YType.uint32, "min-delay-time")

                    self.reload_delay_time = YLeaf(YType.uint32, "reload-delay-time")

                    self.virtual_ip_address = YLeaf(YType.str, "virtual-ip-address")

                    self.virtual_linklocal_ipv6_address = YLeaf(YType.str, "virtual-linklocal-ipv6-address")

                    self.active_ip_address = YLeaf(YType.str, "active-ip-address")

                    self.active_ipv6_address = YLeaf(YType.str, "active-ipv6-address")

                    self.active_mac_address = YLeaf(YType.str, "active-mac-address")

                    self.standby_ip_address = YLeaf(YType.str, "standby-ip-address")

                    self.standby_ipv6_address = YLeaf(YType.str, "standby-ipv6-address")

                    self.standby_mac_address = YLeaf(YType.str, "standby-mac-address")

                    self.hsrp_router_state = YLeaf(YType.enumeration, "hsrp-router-state")

                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                    self.interface = YLeaf(YType.str, "interface")

                    self.router_priority = YLeaf(YType.uint8, "router-priority")

                    self.active_priority = YLeaf(YType.uint8, "active-priority")

                    self.active_timer_flag = YLeaf(YType.boolean, "active-timer-flag")

                    self.active_timer_secs = YLeaf(YType.uint32, "active-timer-secs")

                    self.active_timer_msecs = YLeaf(YType.uint32, "active-timer-msecs")

                    self.standby_timer_flag = YLeaf(YType.boolean, "standby-timer-flag")

                    self.standby_timer_secs = YLeaf(YType.uint32, "standby-timer-secs")

                    self.standby_timer_msecs = YLeaf(YType.uint32, "standby-timer-msecs")

                    self.hello_timer_flag = YLeaf(YType.boolean, "hello-timer-flag")

                    self.hello_timer_secs = YLeaf(YType.uint32, "hello-timer-secs")

                    self.hello_timer_msecs = YLeaf(YType.uint32, "hello-timer-msecs")

                    self.delay_timer_flag = YLeaf(YType.boolean, "delay-timer-flag")

                    self.delay_timer_secs = YLeaf(YType.uint32, "delay-timer-secs")

                    self.delay_timer_msecs = YLeaf(YType.uint32, "delay-timer-msecs")

                    self.current_state_timer_secs = YLeaf(YType.uint32, "current-state-timer-secs")

                    self.state_change_count = YLeaf(YType.uint32, "state-change-count")

                    self.tracked_interface_count = YLeaf(YType.uint32, "tracked-interface-count")

                    self.tracked_interface_up_count = YLeaf(YType.uint32, "tracked-interface-up-count")

                    self.preempt_enabled = YLeaf(YType.boolean, "preempt-enabled")

                    self.use_configured_timers = YLeaf(YType.boolean, "use-configured-timers")

                    self.use_configured_virtual_ip = YLeaf(YType.boolean, "use-configured-virtual-ip")

                    self.use_bia_configured = YLeaf(YType.boolean, "use-bia-configured")

                    self.configured_timers = YLeaf(YType.boolean, "configured-timers")

                    self.configured_mac_address = YLeaf(YType.boolean, "configured-mac-address")

                    self.redirects_disabled = YLeaf(YType.boolean, "redirects-disabled")

                    self.bfd_enabled = YLeaf(YType.boolean, "bfd-enabled")

                    self.bfd_interface = YLeaf(YType.str, "bfd-interface")

                    self.bfd_peer_ip_address = YLeaf(YType.str, "bfd-peer-ip-address")

                    self.bfd_peer_ipv6_address = YLeaf(YType.str, "bfd-peer-ipv6-address")

                    self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                    self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                    self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                    self.virtual_mac_address_state = YLeaf(YType.enumeration, "virtual-mac-address-state")

                    self.secondary_address = YLeafList(YType.str, "secondary-address")

                    self.resign_sent_time = Hsrp.Ipv6.Groups.Group.ResignSentTime()
                    self.resign_sent_time.parent = self
                    self._children_name_map["resign_sent_time"] = "resign-sent-time"
                    self._children_yang_names.add("resign-sent-time")

                    self.resign_received_time = Hsrp.Ipv6.Groups.Group.ResignReceivedTime()
                    self.resign_received_time.parent = self
                    self._children_name_map["resign_received_time"] = "resign-received-time"
                    self._children_yang_names.add("resign-received-time")

                    self.coup_sent_time = Hsrp.Ipv6.Groups.Group.CoupSentTime()
                    self.coup_sent_time.parent = self
                    self._children_name_map["coup_sent_time"] = "coup-sent-time"
                    self._children_yang_names.add("coup-sent-time")

                    self.coup_received_time = Hsrp.Ipv6.Groups.Group.CoupReceivedTime()
                    self.coup_received_time.parent = self
                    self._children_name_map["coup_received_time"] = "coup-received-time"
                    self._children_yang_names.add("coup-received-time")

                    self.statistics = Hsrp.Ipv6.Groups.Group.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.global_address = YList(self)
                    self.state_change_history = YList(self)
                    self._segment_path = lambda: "group" + "[interface-name='" + self.interface_name.get() + "']" + "[group-number='" + self.group_number.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv6.Groups.Group, ['interface_name', 'group_number', 'authentication_string', 'virtual_mac_address', 'hsrp_group_number', 'address_family', 'version', 'session_name', 'slaves', 'is_slave', 'followed_session_name', 'configured_priority', 'preempt_delay', 'preempt_timer_secs', 'hello_time', 'hold_time', 'learned_hello_time', 'learned_hold_time', 'min_delay_time', 'reload_delay_time', 'virtual_ip_address', 'virtual_linklocal_ipv6_address', 'active_ip_address', 'active_ipv6_address', 'active_mac_address', 'standby_ip_address', 'standby_ipv6_address', 'standby_mac_address', 'hsrp_router_state', 'interface_name_xr', 'interface', 'router_priority', 'active_priority', 'active_timer_flag', 'active_timer_secs', 'active_timer_msecs', 'standby_timer_flag', 'standby_timer_secs', 'standby_timer_msecs', 'hello_timer_flag', 'hello_timer_secs', 'hello_timer_msecs', 'delay_timer_flag', 'delay_timer_secs', 'delay_timer_msecs', 'current_state_timer_secs', 'state_change_count', 'tracked_interface_count', 'tracked_interface_up_count', 'preempt_enabled', 'use_configured_timers', 'use_configured_virtual_ip', 'use_bia_configured', 'configured_timers', 'configured_mac_address', 'redirects_disabled', 'bfd_enabled', 'bfd_interface', 'bfd_peer_ip_address', 'bfd_peer_ipv6_address', 'bfd_session_state', 'bfd_interval', 'bfd_multiplier', 'virtual_mac_address_state', 'secondary_address'], name, value)


                class ResignSentTime(Entity):
                    """
                    Time last resign was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.ResignSentTime, self).__init__()

                        self.yang_name = "resign-sent-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "resign-sent-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.ResignSentTime, ['seconds', 'nanoseconds'], name, value)


                class ResignReceivedTime(Entity):
                    """
                    Time last resign was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.ResignReceivedTime, self).__init__()

                        self.yang_name = "resign-received-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "resign-received-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.ResignReceivedTime, ['seconds', 'nanoseconds'], name, value)


                class CoupSentTime(Entity):
                    """
                    Time last coup was sent
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.CoupSentTime, self).__init__()

                        self.yang_name = "coup-sent-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "coup-sent-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.CoupSentTime, ['seconds', 'nanoseconds'], name, value)


                class CoupReceivedTime(Entity):
                    """
                    Time last coup was received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.CoupReceivedTime, self).__init__()

                        self.yang_name = "coup-received-time"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "coup-received-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.CoupReceivedTime, ['seconds', 'nanoseconds'], name, value)


                class Statistics(Entity):
                    """
                    HSRP Group statistics
                    
                    .. attribute:: active_transitions
                    
                    	Number of transitions to Active State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_transitions
                    
                    	Number of transitions to Standby State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speak_transitions
                    
                    	Number of transitions to Speak State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: listen_transitions
                    
                    	Number of transitions to Listen State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: learn_transitions
                    
                    	Number of transitions to Learn State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_transitions
                    
                    	Number of transitions to Init State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_sent
                    
                    	Number of Hello Packets sent (NB\: Bundles only)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_sent
                    
                    	Number of Resign Packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_sent
                    
                    	Number of Coup Packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_packets_received
                    
                    	Number of Hello Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resign_packets_received
                    
                    	Number of Resign Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: coup_packets_received
                    
                    	Number of Coup Packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_fail_received
                    
                    	Number of Packets received that failed authentication
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer_received
                    
                    	Number of packets received with invalid Hello Time value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mismatch_virtual_ip_address_received
                    
                    	Number of packets received with mismatching virtual IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_transitions = YLeaf(YType.uint32, "active-transitions")

                        self.standby_transitions = YLeaf(YType.uint32, "standby-transitions")

                        self.speak_transitions = YLeaf(YType.uint32, "speak-transitions")

                        self.listen_transitions = YLeaf(YType.uint32, "listen-transitions")

                        self.learn_transitions = YLeaf(YType.uint32, "learn-transitions")

                        self.init_transitions = YLeaf(YType.uint32, "init-transitions")

                        self.hello_packets_sent = YLeaf(YType.uint32, "hello-packets-sent")

                        self.resign_packets_sent = YLeaf(YType.uint32, "resign-packets-sent")

                        self.coup_packets_sent = YLeaf(YType.uint32, "coup-packets-sent")

                        self.hello_packets_received = YLeaf(YType.uint32, "hello-packets-received")

                        self.resign_packets_received = YLeaf(YType.uint32, "resign-packets-received")

                        self.coup_packets_received = YLeaf(YType.uint32, "coup-packets-received")

                        self.auth_fail_received = YLeaf(YType.uint32, "auth-fail-received")

                        self.invalid_timer_received = YLeaf(YType.uint32, "invalid-timer-received")

                        self.mismatch_virtual_ip_address_received = YLeaf(YType.uint32, "mismatch-virtual-ip-address-received")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.Statistics, ['active_transitions', 'standby_transitions', 'speak_transitions', 'listen_transitions', 'learn_transitions', 'init_transitions', 'hello_packets_sent', 'resign_packets_sent', 'coup_packets_sent', 'hello_packets_received', 'resign_packets_received', 'coup_packets_received', 'auth_fail_received', 'invalid_timer_received', 'mismatch_virtual_ip_address_received'], name, value)


                class GlobalAddress(Entity):
                    """
                    Global virtual IPv6 addresses
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.GlobalAddress, self).__init__()

                        self.yang_name = "global-address"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                        self._segment_path = lambda: "global-address"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.GlobalAddress, ['ipv6_address'], name, value)


                class StateChangeHistory(Entity):
                    """
                    State change history
                    
                    .. attribute:: time
                    
                    	Time of state change
                    	**type**\:  :py:class:`Time <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time>`
                    
                    .. attribute:: old_state
                    
                    	Old State
                    	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: new_state
                    
                    	New State
                    	**type**\:  :py:class:`StandbyGrpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.StandbyGrpState>`
                    
                    .. attribute:: reason
                    
                    	Reason for state change
                    	**type**\:  :py:class:`HsrpStateChangeReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpStateChangeReason>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Groups.Group.StateChangeHistory, self).__init__()

                        self.yang_name = "state-change-history"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"time" : ("time", Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time)}
                        self._child_list_classes = {}

                        self.old_state = YLeaf(YType.enumeration, "old-state")

                        self.new_state = YLeaf(YType.enumeration, "new-state")

                        self.reason = YLeaf(YType.enumeration, "reason")

                        self.time = Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time()
                        self.time.parent = self
                        self._children_name_map["time"] = "time"
                        self._children_yang_names.add("time")
                        self._segment_path = lambda: "state-change-history"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Groups.Group.StateChangeHistory, ['old_state', 'new_state', 'reason'], name, value)


                    class Time(Entity):
                        """
                        Time of state change
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time, self).__init__()

                            self.yang_name = "time"
                            self.yang_parent_name = "state-change-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.seconds = YLeaf(YType.uint32, "seconds")

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                            self._segment_path = lambda: "time"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time, ['seconds', 'nanoseconds'], name, value)


        class Interfaces(Entity):
            """
            The HSRP interface information table
            
            .. attribute:: interface
            
            	A HSRP interface entry
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces.Interface>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Ipv6.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Hsrp.Ipv6.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Ipv6.Interfaces, [], name, value)


            class Interface(Entity):
                """
                A HSRP interface entry
                
                .. attribute:: interface_name  <key>
                
                	The interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: statistics
                
                	HSRP Interface Statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.Ipv6.Interfaces.Interface.Statistics>`
                
                .. attribute:: interface
                
                	IM Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: use_bia_flag
                
                	Use burnt in mac address flag
                	**type**\: bool
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Ipv6.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"statistics" : ("statistics", Hsrp.Ipv6.Interfaces.Interface.Statistics)}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.use_bia_flag = YLeaf(YType.boolean, "use-bia-flag")

                    self.statistics = Hsrp.Ipv6.Interfaces.Interface.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/ipv6/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Ipv6.Interfaces.Interface, ['interface_name', 'interface', 'use_bia_flag'], name, value)


                class Statistics(Entity):
                    """
                    HSRP Interface Statistics
                    
                    .. attribute:: advert_packets_sent
                    
                    	Number of advertisement packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: advert_packets_received
                    
                    	Number of advertisement packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: long_packets_received
                    
                    	Number of packets received that were too Long
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: short_packets_received
                    
                    	Number of packets received that were too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_version_received
                    
                    	Number of packets received with invalid version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_operation_code_received
                    
                    	Number of packets received with invalid operation code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_group_received
                    
                    	Number of packets received for an unknown group id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inoperational_group_received
                    
                    	Number of packets received for an inoperational group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conflict_source_ip_address_received
                    
                    	Number of packets received from a conflicting Source IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Ipv6.Interfaces.Interface.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.advert_packets_sent = YLeaf(YType.uint32, "advert-packets-sent")

                        self.advert_packets_received = YLeaf(YType.uint32, "advert-packets-received")

                        self.long_packets_received = YLeaf(YType.uint32, "long-packets-received")

                        self.short_packets_received = YLeaf(YType.uint32, "short-packets-received")

                        self.invalid_version_received = YLeaf(YType.uint32, "invalid-version-received")

                        self.invalid_operation_code_received = YLeaf(YType.uint32, "invalid-operation-code-received")

                        self.unknown_group_received = YLeaf(YType.uint32, "unknown-group-received")

                        self.inoperational_group_received = YLeaf(YType.uint32, "inoperational-group-received")

                        self.conflict_source_ip_address_received = YLeaf(YType.uint32, "conflict-source-ip-address-received")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Ipv6.Interfaces.Interface.Statistics, ['advert_packets_sent', 'advert_packets_received', 'long_packets_received', 'short_packets_received', 'invalid_version_received', 'invalid_operation_code_received', 'unknown_group_received', 'inoperational_group_received', 'conflict_source_ip_address_received'], name, value)


    class BfdSessions(Entity):
        """
        The table of HSRP BFD Sessions
        
        .. attribute:: bfd_session
        
        	An HSRP BFD Session
        	**type**\: list of  		 :py:class:`BfdSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions.BfdSession>`
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.BfdSessions, self).__init__()

            self.yang_name = "bfd-sessions"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"bfd-session" : ("bfd_session", Hsrp.BfdSessions.BfdSession)}

            self.bfd_session = YList(self)
            self._segment_path = lambda: "bfd-sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.BfdSessions, [], name, value)


        class BfdSession(Entity):
            """
            An HSRP BFD Session
            
            .. attribute:: interface_name  <key>
            
            	The interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: ip_address  <key>
            
            	Destination IP Address of BFD Session
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bfd_interface_name
            
            	BFD Interface Name
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: session_address_family
            
            	Session Address family
            	**type**\:  :py:class:`HsrpBAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBAf>`
            
            .. attribute:: destination_address
            
            	BFD destination address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: destination_ipv6_address
            
            	BFD IPv6 destination address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bfd_session_state
            
            	BFD session state
            	**type**\:  :py:class:`HsrpBfdSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.HsrpBfdSessionState>`
            
            .. attribute:: bfd_interval
            
            	BFD packet send interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: bfd_multiplier
            
            	BFD multiplier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: group
            
            	HSRP Groups tracking the BFD session
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper.Hsrp.BfdSessions.BfdSession.Group>`
            
            

            """

            _prefix = 'ipv4-hsrp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.BfdSessions.BfdSession, self).__init__()

                self.yang_name = "bfd-session"
                self.yang_parent_name = "bfd-sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"group" : ("group", Hsrp.BfdSessions.BfdSession.Group)}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.ip_address = YLeaf(YType.str, "ip-address")

                self.bfd_interface_name = YLeaf(YType.str, "bfd-interface-name")

                self.session_address_family = YLeaf(YType.enumeration, "session-address-family")

                self.destination_address = YLeaf(YType.str, "destination-address")

                self.destination_ipv6_address = YLeaf(YType.str, "destination-ipv6-address")

                self.bfd_session_state = YLeaf(YType.enumeration, "bfd-session-state")

                self.bfd_interval = YLeaf(YType.uint32, "bfd-interval")

                self.bfd_multiplier = YLeaf(YType.uint32, "bfd-multiplier")

                self.group = YList(self)
                self._segment_path = lambda: "bfd-session" + "[interface-name='" + self.interface_name.get() + "']" + "[ip-address='" + self.ip_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/bfd-sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.BfdSessions.BfdSession, ['interface_name', 'ip_address', 'bfd_interface_name', 'session_address_family', 'destination_address', 'destination_ipv6_address', 'bfd_session_state', 'bfd_interval', 'bfd_multiplier'], name, value)


            class Group(Entity):
                """
                HSRP Groups tracking the BFD session
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: hsrp_group_number
                
                	HSRP Group number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-hsrp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.BfdSessions.BfdSession.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "bfd-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.hsrp_group_number = YLeaf(YType.uint32, "hsrp-group-number")
                    self._segment_path = lambda: "group"

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.BfdSessions.BfdSession.Group, ['interface_name', 'hsrp_group_number'], name, value)


    class Summary(Entity):
        """
        HSRP summary statistics
        
        .. attribute:: ipv4_sessions_active
        
        	Number of IPv4 sessions in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_standby
        
        	Number of IPv4 sessions in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_speak
        
        	Number of IPv4 sessions in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_listen
        
        	Number of IPv4 sessions in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_learn
        
        	Number of IPv4 sessions in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_sessions_init
        
        	Number of IPv4 sessions in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_active
        
        	Number of IPv4 slaves in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_standby
        
        	Number of IPv4 slaves in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_speak
        
        	Number of IPv4 slaves in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_listen
        
        	Number of IPv4 slaves in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_learn
        
        	Number of IPv4 slaves in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_slaves_init
        
        	Number of IPv4 slaves in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_active_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_active_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_standby_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_standby_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_speak_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_speak_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_listen_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_listen_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_learn_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_learn_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_up
        
        	Number of UP IPv4 Virtual IP Addresses on groups in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv4 Virtual IP Addresses on groups in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_active
        
        	Number of IPv6 sessions in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_standby
        
        	Number of IPv6 sessions in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_speak
        
        	Number of IPv6 sessions in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_listen
        
        	Number of IPv6 sessions in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_learn
        
        	Number of IPv6 sessions in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_sessions_init
        
        	Number of IPv6 sessions in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_active
        
        	Number of IPv6 slaves in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_standby
        
        	Number of IPv6 slaves in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_speak
        
        	Number of IPv6 slaves in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_listen
        
        	Number of IPv6 slaves in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_learn
        
        	Number of IPv6 slaves in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_slaves_init
        
        	Number of IPv6 slaves in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_active_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_active_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in ACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_standby_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_standby_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in STANDBY state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_speak_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_speak_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in SPEAK state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_listen_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_listen_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in LISTEN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_learn_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_learn_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in LEARN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_up
        
        	Number of UP IPv6 Virtual IP Addresses on groups in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_virtual_ip_addresses_init_down
        
        	Number of DOWN IPv6 Virtual IP Addresses on groups in INIT state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_up
        
        	Number of HSRP interfaces with IPv4 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv4_state_down
        
        	Number of HSRP interfaces with IPv4 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_up
        
        	Number of tracked interfaces with IPv4 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv4_state_down
        
        	Number of tracked interfaces with IPv4 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_up
        
        	Number of tracked objects in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_objects_down
        
        	Number of tracked objects in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_up
        
        	Number of HSRP interfaces with IPv6 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interfaces_ipv6_state_down
        
        	Number of HSRP interfaces with IPv6 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_up
        
        	Number of tracked interfaces with IPv6 caps in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tracked_interfaces_ipv6_state_down
        
        	Number of tracked interfaces with IPv6 caps in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_up
        
        	Number of HSRP BFD sessions in UP state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_sessions_down
        
        	Number of HSRP BFD sessions in DOWN state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bfd_session_inactive
        
        	Number of HSRP BFD sessions in INACTIVE state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ipv4-hsrp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ipv4_sessions_active = YLeaf(YType.uint32, "ipv4-sessions-active")

            self.ipv4_sessions_standby = YLeaf(YType.uint32, "ipv4-sessions-standby")

            self.ipv4_sessions_speak = YLeaf(YType.uint32, "ipv4-sessions-speak")

            self.ipv4_sessions_listen = YLeaf(YType.uint32, "ipv4-sessions-listen")

            self.ipv4_sessions_learn = YLeaf(YType.uint32, "ipv4-sessions-learn")

            self.ipv4_sessions_init = YLeaf(YType.uint32, "ipv4-sessions-init")

            self.ipv4_slaves_active = YLeaf(YType.uint32, "ipv4-slaves-active")

            self.ipv4_slaves_standby = YLeaf(YType.uint32, "ipv4-slaves-standby")

            self.ipv4_slaves_speak = YLeaf(YType.uint32, "ipv4-slaves-speak")

            self.ipv4_slaves_listen = YLeaf(YType.uint32, "ipv4-slaves-listen")

            self.ipv4_slaves_learn = YLeaf(YType.uint32, "ipv4-slaves-learn")

            self.ipv4_slaves_init = YLeaf(YType.uint32, "ipv4-slaves-init")

            self.ipv4_virtual_ip_addresses_active_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-active-up")

            self.ipv4_virtual_ip_addresses_active_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-active-down")

            self.ipv4_virtual_ip_addresses_standby_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-standby-up")

            self.ipv4_virtual_ip_addresses_standby_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-standby-down")

            self.ipv4_virtual_ip_addresses_speak_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-speak-up")

            self.ipv4_virtual_ip_addresses_speak_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-speak-down")

            self.ipv4_virtual_ip_addresses_listen_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-listen-up")

            self.ipv4_virtual_ip_addresses_listen_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-listen-down")

            self.ipv4_virtual_ip_addresses_learn_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-learn-up")

            self.ipv4_virtual_ip_addresses_learn_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-learn-down")

            self.ipv4_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-up")

            self.ipv4_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv4-virtual-ip-addresses-init-down")

            self.ipv6_sessions_active = YLeaf(YType.uint32, "ipv6-sessions-active")

            self.ipv6_sessions_standby = YLeaf(YType.uint32, "ipv6-sessions-standby")

            self.ipv6_sessions_speak = YLeaf(YType.uint32, "ipv6-sessions-speak")

            self.ipv6_sessions_listen = YLeaf(YType.uint32, "ipv6-sessions-listen")

            self.ipv6_sessions_learn = YLeaf(YType.uint32, "ipv6-sessions-learn")

            self.ipv6_sessions_init = YLeaf(YType.uint32, "ipv6-sessions-init")

            self.ipv6_slaves_active = YLeaf(YType.uint32, "ipv6-slaves-active")

            self.ipv6_slaves_standby = YLeaf(YType.uint32, "ipv6-slaves-standby")

            self.ipv6_slaves_speak = YLeaf(YType.uint32, "ipv6-slaves-speak")

            self.ipv6_slaves_listen = YLeaf(YType.uint32, "ipv6-slaves-listen")

            self.ipv6_slaves_learn = YLeaf(YType.uint32, "ipv6-slaves-learn")

            self.ipv6_slaves_init = YLeaf(YType.uint32, "ipv6-slaves-init")

            self.ipv6_virtual_ip_addresses_active_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-active-up")

            self.ipv6_virtual_ip_addresses_active_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-active-down")

            self.ipv6_virtual_ip_addresses_standby_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-standby-up")

            self.ipv6_virtual_ip_addresses_standby_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-standby-down")

            self.ipv6_virtual_ip_addresses_speak_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-speak-up")

            self.ipv6_virtual_ip_addresses_speak_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-speak-down")

            self.ipv6_virtual_ip_addresses_listen_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-listen-up")

            self.ipv6_virtual_ip_addresses_listen_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-listen-down")

            self.ipv6_virtual_ip_addresses_learn_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-learn-up")

            self.ipv6_virtual_ip_addresses_learn_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-learn-down")

            self.ipv6_virtual_ip_addresses_init_up = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-up")

            self.ipv6_virtual_ip_addresses_init_down = YLeaf(YType.uint32, "ipv6-virtual-ip-addresses-init-down")

            self.interfaces_ipv4_state_up = YLeaf(YType.uint32, "interfaces-ipv4-state-up")

            self.interfaces_ipv4_state_down = YLeaf(YType.uint32, "interfaces-ipv4-state-down")

            self.tracked_interfaces_ipv4_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-up")

            self.tracked_interfaces_ipv4_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv4-state-down")

            self.tracked_objects_up = YLeaf(YType.uint32, "tracked-objects-up")

            self.tracked_objects_down = YLeaf(YType.uint32, "tracked-objects-down")

            self.interfaces_ipv6_state_up = YLeaf(YType.uint32, "interfaces-ipv6-state-up")

            self.interfaces_ipv6_state_down = YLeaf(YType.uint32, "interfaces-ipv6-state-down")

            self.tracked_interfaces_ipv6_state_up = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-up")

            self.tracked_interfaces_ipv6_state_down = YLeaf(YType.uint32, "tracked-interfaces-ipv6-state-down")

            self.bfd_sessions_up = YLeaf(YType.uint32, "bfd-sessions-up")

            self.bfd_sessions_down = YLeaf(YType.uint32, "bfd-sessions-down")

            self.bfd_session_inactive = YLeaf(YType.uint32, "bfd-session-inactive")
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-oper:hsrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.Summary, ['ipv4_sessions_active', 'ipv4_sessions_standby', 'ipv4_sessions_speak', 'ipv4_sessions_listen', 'ipv4_sessions_learn', 'ipv4_sessions_init', 'ipv4_slaves_active', 'ipv4_slaves_standby', 'ipv4_slaves_speak', 'ipv4_slaves_listen', 'ipv4_slaves_learn', 'ipv4_slaves_init', 'ipv4_virtual_ip_addresses_active_up', 'ipv4_virtual_ip_addresses_active_down', 'ipv4_virtual_ip_addresses_standby_up', 'ipv4_virtual_ip_addresses_standby_down', 'ipv4_virtual_ip_addresses_speak_up', 'ipv4_virtual_ip_addresses_speak_down', 'ipv4_virtual_ip_addresses_listen_up', 'ipv4_virtual_ip_addresses_listen_down', 'ipv4_virtual_ip_addresses_learn_up', 'ipv4_virtual_ip_addresses_learn_down', 'ipv4_virtual_ip_addresses_init_up', 'ipv4_virtual_ip_addresses_init_down', 'ipv6_sessions_active', 'ipv6_sessions_standby', 'ipv6_sessions_speak', 'ipv6_sessions_listen', 'ipv6_sessions_learn', 'ipv6_sessions_init', 'ipv6_slaves_active', 'ipv6_slaves_standby', 'ipv6_slaves_speak', 'ipv6_slaves_listen', 'ipv6_slaves_learn', 'ipv6_slaves_init', 'ipv6_virtual_ip_addresses_active_up', 'ipv6_virtual_ip_addresses_active_down', 'ipv6_virtual_ip_addresses_standby_up', 'ipv6_virtual_ip_addresses_standby_down', 'ipv6_virtual_ip_addresses_speak_up', 'ipv6_virtual_ip_addresses_speak_down', 'ipv6_virtual_ip_addresses_listen_up', 'ipv6_virtual_ip_addresses_listen_down', 'ipv6_virtual_ip_addresses_learn_up', 'ipv6_virtual_ip_addresses_learn_down', 'ipv6_virtual_ip_addresses_init_up', 'ipv6_virtual_ip_addresses_init_down', 'interfaces_ipv4_state_up', 'interfaces_ipv4_state_down', 'tracked_interfaces_ipv4_state_up', 'tracked_interfaces_ipv4_state_down', 'tracked_objects_up', 'tracked_objects_down', 'interfaces_ipv6_state_up', 'interfaces_ipv6_state_down', 'tracked_interfaces_ipv6_state_up', 'tracked_interfaces_ipv6_state_down', 'bfd_sessions_up', 'bfd_sessions_down', 'bfd_session_inactive'], name, value)

    def clone_ptr(self):
        self._top_entity = Hsrp()
        return self._top_entity

