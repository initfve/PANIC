#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        PanicViewDS.py
#
#  Project :     Panic View Device Server
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      srubio$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["PanicViewDS", "PanicViewDSClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(PanicViewDS.additionnal_import) ENABLED START -----#
import traceback as tb
import fandango as fd, fandango.tango as ft
import panic, panic.view
#----- PROTECTED REGION END -----#	//	PanicViewDS.additionnal_import

# Device States Description
# No states for this device


class PanicViewDS (PyTango.Device_4Impl):
    """Device Server to export panic.AlarmView objects to remote clients"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(PanicViewDS.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PanicViewDS.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        PanicViewDS.init_device(self)
        #----- PROTECTED REGION ID(PanicViewDS.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(PanicViewDS.delete_device) ENABLED START -----#
        self.view.disconnect()
        #----- PROTECTED REGION END -----#	//	PanicViewDS.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_Scope_read = ""
        self.attr_LastUpdate_read = 0.0
        self.attr_AlarmList_read = [""]
        self.attr_Filters_read = [""]
        self.attr_Summary_read = [""]
        #----- PROTECTED REGION ID(PanicViewDS.init_device) ENABLED START -----#
        self.view = panic.view.AlarmView(scope=self.Scope,
                                         filters=self.Filters,
                                         refresh=self.Refresh,
                                         events=self.UseEvents,
                                         )
        #----- PROTECTED REGION END -----#	//	PanicViewDS.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(PanicViewDS.always_executed_hook) ENABLED START -----#
        now = fd.now()
        if not self.view.last_event_time:
            self.set_state(PyTango.DevState.INIT)
        elif now - self.view.last_event_time > 60.:
            self.set_state(PyTango.DevState.UNKNOWN)
        else:
            self.set_state(PyTango.DevState.ON)  
        self.set_status('AlarmView(%s) updated at %s'
                        %(self.Scope,fd.time2str(self.view.last_event_time)))
        #----- PROTECTED REGION END -----#	//	PanicViewDS.always_executed_hook

    # -------------------------------------------------------------------------
    #    PanicViewDS read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_Scope(self, attr):
        self.debug_stream("In read_Scope()")
        #----- PROTECTED REGION ID(PanicViewDS.Scope_read) ENABLED START -----#
        self.attr_Scope_read = self.Scope[:]
        attr.set_value(self.attr_Scope_read)
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.Scope_read
        
    def read_LastUpdate(self, attr):
        self.debug_stream("In read_LastUpdate()")
        #----- PROTECTED REGION ID(PanicViewDS.LastUpdate_read) ENABLED START -----#
        self.attr_LastUpdate_read = self.view.last_event_time
        attr.set_value(self.attr_LastUpdate_read)
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.LastUpdate_read
        
    def read_AlarmList(self, attr):
        self.debug_stream("In read_AlarmList()")
        #----- PROTECTED REGION ID(PanicViewDS.AlarmList_read) ENABLED START -----#
        self.attr_AlarmList_read = self.view.sort(as_text=True)
        attr.set_value(self.attr_AlarmList_read)
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.AlarmList_read
        
    def read_Filters(self, attr):
        self.debug_stream("In read_Filters()")
        #----- PROTECTED REGION ID(PanicViewDS.Filters_read) ENABLED START -----#
        self.attr_Filters_read = self.Filters[:]
        attr.set_value(self.attr_Filters_read)
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.Filters_read
        
    def read_Summary(self, attr):
        self.debug_stream("In read_Summary()")
        #----- PROTECTED REGION ID(PanicViewDS.Summary_read) ENABLED START -----#
        self.attr_Summary_read = self.view.sort(as_text=True)
        attr.set_value(self.attr_Summary_read)
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.Summary_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(PanicViewDS.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.read_attr_hardware


    # -------------------------------------------------------------------------
    #    PanicViewDS command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(PanicViewDS.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PanicViewDS.programmer_methods

class PanicViewDSClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(PanicViewDS.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	PanicViewDS.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'Scope':
            [PyTango.DevString, 
            "Regexp filter to select PyAlarm/PanicDS devices",
            ["*"] ],
        'Filters':
            [PyTango.DevVarStringArray, 
             '',
            [] ],
        'UseEvents':
            [PyTango.DevString, 
             '',
            [] ],
        'Refresh':
            [PyTango.DevDouble, 
             '',
            [3.0]],
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'Scope':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ]],
        'LastUpdate':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ]],
        'AlarmList':
            [[PyTango.DevString,
            PyTango.SPECTRUM,
            PyTango.READ, 8192]],
        'Filters':
            [[PyTango.DevString,
            PyTango.SPECTRUM,
            PyTango.READ, 512]],
        'Summary':
            [[PyTango.DevString,
            PyTango.SPECTRUM,
            PyTango.READ, 8192]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(PanicViewDSClass, PanicViewDS, 'PanicViewDS')
        #----- PROTECTED REGION ID(PanicViewDS.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	PanicViewDS.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
