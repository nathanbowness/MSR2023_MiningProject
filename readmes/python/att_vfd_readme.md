  
 
 
 
# VFd Overview 
Much in the way that a guest operating system requires a 
hypervisor to provide accessibility to the underlying real 
operating system and hardware, as well as to ensure policies 
are enforced, there is a similar need for a _NIC hypervisor_ 
when virtual functions (VFs) are directly available through 
SR-IOV[1]. While a bit more lightweight than a hypervisor, 
VFd can be thought of as the NIC hypervisor inasmuch as it 
provides the policy enforcement through both configuration 
and real-time validation of guest[2] requests. 
 
![cannot display: 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/overview.png 
]( 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/overview.png 
)   
Figure 1: General relationship of NIC, VFs, "guests" and VFd 
 
Figure 1 illustrates the relationship between the NIC (PF), 
the configured VFs, the guests, and VFd. VFd acts as the 
policy implementor by configuring each VF to stipulate which 
VLAN(s) a VF will receive traffic from, and be allowed to 
send traffic to. In addition, VFd will configure the PF and 
VFs to: 
 
 
* Strip and insert the outer VLAN tag. 
* Enable NIC bridging allowing guest to guest communication. 
* Allow unknown unicast traffic to be sent to one or more 
guests. 
* Allow broadcast and multicast traffic to be 
received/transmitted by a guest. 
* Enforce MAC and/or VLAN spoofing (drop spoofed packets). 
* Configure multiple MAC addresses for the VF. 
* Enable and configure DCB quality of service. 
 
 
 
 
In addition to the NIC configurations listed above, VFd 
provides the means to access the packet and byte counters 
allowing for them to be available to the user; something that 
is not possible when using a kernel driver to manage the VFs. 
Statistics, both at the PF and VF level include: 
 
 
* Packet counts for inbound (Rx) and outbound (Tx) 
* Byte counts, Tx and Rx 
* Error packet count 
* Count of spoofed packets 
 
 
 
 
 
 
## The Guests 
While the illustration shows only one VF allocated to each 
guest, it is possible to allocate multiple VFs, from 
different PFs, to a single guest. Of the various guests shown 
in figure 1, two are illustrations of how guest operating 
systems, virtual machines[3], can have one, or more, VF 
allocated as an SR-IOV device. Bare metal applications (e.g. 
DPDK applications) are also able to make use of the VFs 
offered up by the NIC and generally use the NIC's kernel VF 
interface/driver to do so. 
 
 
## Inside of a VM 
When a guest operating system is created, and one or more VFs 
is attached to it, the VF appears as a virtual network 
interface and standard kernel drivers can be used to treat 
the interface as an ordinary ethernet device, configurable 
with well known tools like <code>ifconfig</code> and 
<code>ip,</code> or a DPDK driver may be used to allow DPDK 
applications to run in the virtual machine. 
 
 
## What VFd Is Not 
While VFd is implemented as a DPDK application, primarily to 
easily access the network devices, VFd is **not** a packet 
processor, and does **not** insert itself into the path of 
any packet. 
 
 
# Necessity 
A valid, and often asked, question is _why exactly is VFd 
needed?_ It would seem that if the hardware offers all of the 
sophistication that they do, that the kernel drivers would 
supply the means to configure the hardware such that all of 
the features could be used. However, at least at the present 
time, this isn't the case, and there are several 
configuration options which unfortunately cannot be achieved 
through the kernel drivers. In order to take full advantage 
of the hardware, an independent configuration tool, VFd, is 
required. 
 
 
 
## Real-time Authorisation 
In addition to managing the configurations of all VFs, VFd 
also provides real-time policy enforcement when a guest makes 
a request to configure it's interface. The following are 
examples of guest actions which require the approval of VFd 
before the requested changes are actually applied o the VF: 
 
 
* Add or modify VLAN ID(s) 
* Change default MAC address 
* Add/delete alternate (white list) MAC addresses 
* Set the MTU value 
 
 
VFd will authorise (ACK) any request provided that the change 
is within the policy as defined to VFd via the PF and VF 
configuration files. For example, if a guests requests to 
add/modify a VLAN ID, it will be permitted only if the 
requested ID has been defined in the VF's configuration file. 
MTU changes are limited by the overall maximum MTU defined 
for each device in the main VFd configuration file. Looking 
from a policy assurance point of view, VFd provides a service 
that would otherwise not be available even if all NIC 
features could be exercised through the kernel driver 
interface as the drivers provide no mechanism to call out to 
an independent authority to make these kinds of decisions. 
 
 
 
# VF Configuration Features 
The following sections provide a high level explanation of 
NIC features which may be managed using VFd. The purpose here 
is to outline what can be done; for information on how to 
actually implement these, please refer to the _VFd User's 
Guide._ 
 
 
## Anti-Spoofing 
_Spoofing_ is used in reference to a machine on a network 
pretending to be another machine, usually by using the other 
machine's MAC address, or using an unauthorised VLAN ID in 
packets, or possibly both. VFd forces _anti-spoofing_ 
settings to be enabled for VLAN IDs[4] under the assumption 
that a guest assigned to a VLAN must always send packets with 
the assigned ID, but may send with any source MAC address. 
 
 
## VLAN Considerations 
The list of _approved_ VLAN IDs that are given in a VF's 
configuration file limit the packets that the NIC will 
forward to the VF. Only packets containing one of the VLAN 
IDs in the list are allowed to pass. VFd does not permit a VF 
to see all packets regardless of VLAN ID, nor does it permit 
untagged packets from being written onto a VF's queue. 
 
![cannot display: 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/vlan_strip.png 
]( 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/vlan_strip.png 
)   
Figure 2: On transmit, insert VLAN tag into untagged packet 
(top to middle), and into a single tagged packet (middle to 
bottom). On receipt, the reverse. 
 
 
 
### Stripping and Inserting VLAN Tags 
The VLAN ID, or tag, may be automatically removed, stripped, 
as a packet is received, and automatically inserted prior to 
transmission; both of these actions are performed by the NIC 
and thus are as efficient as is possible. Whether or not one 
or multiple VLAN IDs are configured for a VF, the stripping 
of the tag is straight forward: the tag is removed from the 
packet before the packet is presented to the VF. For the case 
where a VF receives packets with a single VLAN tag, the 
process of insertion is also straight forward: the NIC 
inserts the tag into the packet before transmission. When a 
VF is permitted send and receive packets using one of several 
VLAN IDs, the insertion of the correct ID is the 
responsibility of the sending process, and cannot be added to 
the packet by the NIC. 
 
 
### Q in Q Stripping 
Packets arriving with multiple embedded VLAN IDs (figure 2, 
bottom), also known as Q in Q, are subject to the same 
stripping practice as described above. Only the first, or _ 
outer_ tag, is removed from a received packet, and only the 
outer tag will be inserted on transmit. Using the 
illustration as an example, the middle packet would be 
delivered to the guest after stripping, and the bottom packet 
would be transmitted. It is the responsibility of the guest 
software (kernel driver, or DPDK application) to properly 
distinguish packets, if necessary, based on the VLAN ID which 
remains in the packet. 
 
 
## MAC Addresses 
By default the NIC generates a random MAC address for each VF 
that is created. This random address is known as the _default 
MAC,_ and is visible to the guest (e.g. it is what would be 
displayed in the output of an <code>ifconfig</code> command). 
If it is necessary, the default MAC address can be supplied 
in a VF's configuration file which will replace the random 
address generated by the NIC. 
 
 
### Guest Generated MAC Addresses 
It is sometimes desirable for a guest to generate the default 
MAC, and possibly other _white-list_ MAC addresses. VFd will 
approve these guest requests provided that: 
 
* The address is not in use by another VF on the same PF. 
* The number of addresses currently allocated on the VF is 
not at maximum 
* THe number of addresses currently allocated on the PF is 
not at maximum. 
 
 
 
 
Guest allocated MAC addresses remain in place until the VF 
configuration is deleted. When the configuration is deleted 
any guest allocated addresses are replaced by a single, 
randomly generated, default address. 
 
 
## Broadcast, Unknown Unicast, Multicast Traffic 
VFd allows each VF to be configured to cause the NIC to allow 
or reject each of these types of traffic. The configuration 
of a VF provides for three independent settings allowing each 
to be managed separately. All packets falling within each 
traffic type are subject to VLAN filtering; it is not 
possible for a VF to see **all** *-cast traffic. 
 
 
# PF Configuration Features 
There are several configuration options that VFd provides 
which apply to all VFs on a given NIC, or to all PFs on the 
NIC, and thus are supplied in the main VFd configuration 
file. These configuration options are described in the 
following sections. 
 
 
## Loopback 
By default the NIC bridge is disabled which forces a packet 
to be transmitted to the switch, and then back, should two 
guests using VFs on the same PF need to communicate. Enabling 
the loopback option for a VF will enable the NIC bridge and 
allow packets to be exchanged between VFs on the PF without 
having to travel onto the real network. 
 
 
## Flow Control 
While evidence suggests that using flow control can 
significantly impact performance (max throughput), VFd does 
allow flow control on the NIC to be enabled. 
 
 
## Quality of Service 
VFd is able to configure all PFs to enable Datacenter 
Bridging (DCB) quality of service. This defines a set of 
traffic classes and allows the assignment of bandwidth shares 
(percentages) for each VF with respect to each traffic class. 
 
 
## MTU Limit 
The overall maximum MTU limit can be set on each PF. When 
set, an attempt by a guest to increase the MTU value over 
this limit will be rejected. 
 
 
# Traffic Mirroring 
Traffic mirroring is a specialised form of loopback. VFd 
provides for real-time mirror configuration, independent of 
VF configuration files, allowing for inbound[5], outbound, or 
all of a VF's traffic to be duplicated and passed to another 
VF on the same PF. 
 
 
![cannot display: 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/mirror_in.png 
]( 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/mirror_in.png 
)   
Figure 3: Inbound mirroring showting traffic also being 
delivered to Guest B. 
 
![cannot display: 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/mirror_out.png 
]( 
https://raw.githubusercontent.com/wiki/att/vfd/images/overview/mirror_out.png 
)   
Figure 4: Outbound mirroring showing all Tx traffic from 
Guest A delivered to Guest B. 
 
 
 
Mirroring traffic locally has benefits with respect to 
debugging connectivity issues as well as application issues. 
However, there are potential impacts, some serious, to the 
overall throughput of the NIC when traffic is mirrored over 
the NIC bridge. For instance, a badly behaved application 
used as the receiver for mirrored traffic has the potential 
to block all traffic to the source VF. 
 
 
# Notes 
 
_____________________________________________________________
 
[1] A basic primer on SR-IOV can be found via the following 
URL: 
www.intel.com/content/dam/doc/application-note/pci-sig-sr-iov-primer-sr-iov-technology-paper.pdf 
 
 
 
 
[2] For the purposes of this document, we use the term _ 
guest_ to mean either a guest operating system or any 
application which has been given direct access to an SR-IOV 
device. 
 
 
 
 
[3] To avoid confusion, we tend not to use the acronym VM 
when refering to a guest operating system (virtual machine) 
as some vendors refer to the virtual functions on the NIC 
as VMs which could lead to confusion. 
 
 
 
 
[4] For some NICs in order to enable VLAN anti-spoofing, 
MAC anti-spoofing must also be enabled. 
 
 
 
 
[5] The directional notation of mirrored traffic is 
relative to the guest, and not to the NIC or switch. Thus _ 
inbound_ means traffic received; inbound to the guest. 
 
 
*** 
 
 
 
 
 
 
_____________________________________________________________
 
  
**Source:** vfd/doc/overview/overview.xfm   
**Original:** 19 February 2018   
**Revised:** 2 March 2018   
**Formatter:** tfm V2.2/0a266 
 
