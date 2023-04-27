# nyontek OIDs SNMP

lagu lama via shell dengan *snmpwalk*

default (tanpa options)
---
```shell
# snmpwalk -v2c  -c public1  192.168.110.2  
SNMPv2-MIB::sysDescr.0 = STRING: Ruijie Indoor AP710 (802.11a/n/ac and 802.11b/g/n) By Ruijie Networks.
SNMPv2-MIB::sysObjectID.0 = OID: SNMPv2-SMI::enterprises.4881.1.3.1.1.198
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (898735927) 104 days, 0:29:19.27
SNMPv2-MIB::sysContact.0 = STRING: 
SNMPv2-MIB::sysName.0 = STRING: Ruijie
SNMPv2-MIB::sysLocation.0 = STRING: amil_27_2 
SNMPv2-MIB::sysServices.0 = INTEGER: 7
IF-MIB::ifNumber.0 = INTEGER: 7
IF-MIB::ifIndex.1 = INTEGER: 1
IF-MIB::ifIndex.2 = INTEGER: 2
IF-MIB::ifIndex.3 = INTEGER: 3
IF-MIB::ifIndex.4 = INTEGER: 4
IF-MIB::ifIndex.5 = INTEGER: 5
IF-MIB::ifIndex.6 = INTEGER: 6
IF-MIB::ifIndex.4096 = INTEGER: 4096
IF-MIB::ifDescr.1 = STRING: GigabitEthernet 0/1
IF-MIB::ifDescr.2 = STRING: Dot11radio 1/0
```

print full OIDs on output  ( -Of )
---
```shell
# snmpwalk -v2c  -c public1 -Of  192.168.110.2  
.iso.org.dod.internet.mgmt.mib-2.system.sysDescr.0 = STRING: Ruijie Indoor AP710 (802.11a/n/ac and 802.11b/g/n) By Ruijie Networks.
.iso.org.dod.internet.mgmt.mib-2.system.sysObjectID.0 = OID: .iso.org.dod.internet.private.enterprises.4881.1.3.1.1.198
.iso.org.dod.internet.mgmt.mib-2.system.sysUpTime.sysUpTimeInstance = Timeticks: (898755338) 104 days, 0:32:33.38
.iso.org.dod.internet.mgmt.mib-2.system.sysContact.0 = STRING: 
.iso.org.dod.internet.mgmt.mib-2.system.sysName.0 = STRING: Ruijie
.iso.org.dod.internet.mgmt.mib-2.system.sysLocation.0 = STRING: amil_27_2 
.iso.org.dod.internet.mgmt.mib-2.system.sysServices.0 = INTEGER: 7
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifNumber.0 = INTEGER: 7
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.1 = INTEGER: 1
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.2 = INTEGER: 2
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.3 = INTEGER: 3
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.4 = INTEGER: 4
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.5 = INTEGER: 5
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.6 = INTEGER: 6
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifIndex.4096 = INTEGER: 4096
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.1 = STRING: GigabitEthernet 0/1
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.2 = STRING: Dot11radio 1/0
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.3 = STRING: Dot11radio 2/0
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.4 = STRING: Dot11radio 1/0.1
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.5 = STRING: Dot11radio 2/0.1
.iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr.6 = STRING: BVI 1
```

print OIDs numerically ( -On )
---
```shell
# snmpwalk -v2c  -c public1 -On  192.168.110.2  
.1.3.6.1.2.1.1.1.0 = STRING: Ruijie Indoor AP710 (802.11a/n/ac and 802.11b/g/n) By Ruijie Networks.
.1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.4881.1.3.1.1.198
.1.3.6.1.2.1.1.3.0 = Timeticks: (898765666) 104 days, 0:34:16.66
.1.3.6.1.2.1.1.4.0 = STRING: 
.1.3.6.1.2.1.1.5.0 = STRING: Ruijie
.1.3.6.1.2.1.1.6.0 = STRING: amil_27_2 
.1.3.6.1.2.1.1.7.0 = INTEGER: 7
.1.3.6.1.2.1.2.1.0 = INTEGER: 7
.1.3.6.1.2.1.2.2.1.1.1 = INTEGER: 1
.1.3.6.1.2.1.2.2.1.1.2 = INTEGER: 2
.1.3.6.1.2.1.2.2.1.1.3 = INTEGER: 3
.1.3.6.1.2.1.2.2.1.1.4 = INTEGER: 4
.1.3.6.1.2.1.2.2.1.1.5 = INTEGER: 5
.1.3.6.1.2.1.2.2.1.1.6 = INTEGER: 6
.1.3.6.1.2.1.2.2.1.1.4096 = INTEGER: 4096
.1.3.6.1.2.1.2.2.1.2.1 = STRING: GigabitEthernet 0/1
.1.3.6.1.2.1.2.2.1.2.2 = STRING: Dot11radio 1/0
.1.3.6.1.2.1.2.2.1.2.3 = STRING: Dot11radio 2/0
.1.3.6.1.2.1.2.2.1.2.4 = STRING: Dot11radio 1/0.1
.1.3.6.1.2.1.2.2.1.2.5 = STRING: Dot11radio 2/0.1
.1.3.6.1.2.1.2.2.1.2.6 = STRING: BVI 1
.1.3.6.1.2.1.2.2.1.2.4096 = STRING: Null 0
.1.3.6.1.2.1.2.2.1.3.1 = INTEGER: ethernetCsmacd(6)
.1.3.6.1.2.1.2.2.1.3.2 = INTEGER: ethernetCsmacd(6)
.1.3.6.1.2.1.2.2.1.3.3 = INTEGER: ethernetCsmacd(6)
.1.3.6.1.2.1.2.2.1.3.4 = INTEGER: ethernetCsmacd(6)

```
