# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# Copyright 2019 Alex Afanasyev
#
# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from router_base import RoutingTableBase

class RoutingTable(RoutingTableBase):

    def lookup(self, ip):
        """Lookup entry in the routing table (longest prefix match)"""
        newEntry = None
        #for each row in the route table
        #    if the given address is a subnet of the prefix
        #        if the prefix length of the prefix is larger than the existing prefix length
        #        selected_entry = row

        #return selected_entry


        for entry in self.entries:
            if(int(entry.desk) & int(ip)):
                if((newEntry == None) or (int(newEntry.mask < int(self.entries[entry].mask)))):
                    newEntry = self.entries[entry]
          #      options.append(self.entries[entry])
        
        return newEntry

        
        # Hints:
        # - Iterate over entries
        # for entry in self.entries:
        #    ...
        #
        # - To get IP address as integer
        #   int(ip)
        #   int(entry.dest)
        #   int(entry.mask)
        #   int(entry.gw)
        
        ##########################
        ## TODO: IMPLEMENT THIS ##
        ##########################
        raise RuntimeError("NOT IMPLEMENTED YET")
