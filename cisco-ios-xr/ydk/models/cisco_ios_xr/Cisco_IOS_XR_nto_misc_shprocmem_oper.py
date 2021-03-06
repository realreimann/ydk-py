""" Cisco_IOS_XR_nto_misc_shprocmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR nto\-misc\-shprocmem package operational data.

This module contains definitions
for the following management objects\:
  processes\-memory\: Process statistics

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ProcessesMemory(Entity):
    """
    Process statistics
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes>`
    
    

    """

    _prefix = 'nto-misc-shprocmem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ProcessesMemory, self).__init__()
        self._top_entity = None

        self.yang_name = "processes-memory"
        self.yang_parent_name = "Cisco-IOS-XR-nto-misc-shprocmem-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", ProcessesMemory.Nodes)}
        self._child_list_classes = {}

        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory"


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'nto-misc-shprocmem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ProcessesMemory.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "processes-memory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", ProcessesMemory.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessesMemory.Nodes, [], name, value)


        class Node(Entity):
            """
            Node ID
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: job_ids
            
            	List of jobs
            	**type**\:  :py:class:`JobIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node.JobIds>`
            
            

            """

            _prefix = 'nto-misc-shprocmem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ProcessesMemory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"job-ids" : ("job_ids", ProcessesMemory.Nodes.Node.JobIds)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.job_ids = ProcessesMemory.Nodes.Node.JobIds()
                self.job_ids.parent = self
                self._children_name_map["job_ids"] = "job-ids"
                self._children_yang_names.add("job-ids")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ProcessesMemory.Nodes.Node, ['node_name'], name, value)


            class JobIds(Entity):
                """
                List of jobs
                
                .. attribute:: job_id
                
                	Job Id
                	**type**\: list of  		 :py:class:`JobId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node.JobIds.JobId>`
                
                

                """

                _prefix = 'nto-misc-shprocmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ProcessesMemory.Nodes.Node.JobIds, self).__init__()

                    self.yang_name = "job-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"job-id" : ("job_id", ProcessesMemory.Nodes.Node.JobIds.JobId)}

                    self.job_id = YList(self)
                    self._segment_path = lambda: "job-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcessesMemory.Nodes.Node.JobIds, [], name, value)


                class JobId(Entity):
                    """
                    Job Id
                    
                    .. attribute:: job_id  <key>
                    
                    	Job Id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_seg_size
                    
                    	Text Segment Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_seg_size
                    
                    	Data Segment Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stack_seg_size
                    
                    	Stack Segment Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: malloc_size
                    
                    	Malloced Memory Size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'nto-misc-shprocmem-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ProcessesMemory.Nodes.Node.JobIds.JobId, self).__init__()

                        self.yang_name = "job-id"
                        self.yang_parent_name = "job-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.job_id = YLeaf(YType.int32, "job-id")

                        self.name = YLeaf(YType.str, "name")

                        self.jid = YLeaf(YType.uint32, "jid")

                        self.text_seg_size = YLeaf(YType.uint32, "text-seg-size")

                        self.data_seg_size = YLeaf(YType.uint32, "data-seg-size")

                        self.stack_seg_size = YLeaf(YType.uint32, "stack-seg-size")

                        self.malloc_size = YLeaf(YType.uint32, "malloc-size")
                        self._segment_path = lambda: "job-id" + "[job-id='" + self.job_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ProcessesMemory.Nodes.Node.JobIds.JobId, ['job_id', 'name', 'jid', 'text_seg_size', 'data_seg_size', 'stack_seg_size', 'malloc_size'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessesMemory()
        return self._top_entity

