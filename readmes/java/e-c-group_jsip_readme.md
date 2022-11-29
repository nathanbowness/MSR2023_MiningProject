
JAIN-SIP 1.2 Reference Implementation
--------------------------------------
NOTE: This is the official co.ecg.jain_sip 1.2 Reference Implementation.

CONTENTS
-------
See docs/index.html

BUILD Notes
-----------
Platforms:
---------
You need to install J2SE JDK 1.5 or above. You can
get the J2SE SDK from

https://www.oracle.com/java/index.html

Dependencies
------------

1. You need to install ant and the junit extension for ant on your machine. 
2. You need to have junit.jar in your classpath to run the co.ecg.jain_sip.tck.
3. You need to have log4j.jar in your classpath (included in this distribution). 

There are versions of the dependent libraries in the lib directory.  
For your build environment, please edit ant-build-config.properties.

YOU DO NOT need jdom.jar and ant.jar. These are strictly for buildng 
the ant tools.

Building It from Scratch
-------------------------
The distribution is pre-built but should you feel inclined to make changes,
or run the examples, you may wish to rebuild everything.

ant make 

Builds everything.


Building the TCK
----------------

Edit co.ecg.jain_sip.tck.properties and set the claspath to your implementation.

ant runtck 

(builds a jar file containing the TCK and runs it).

Look in test-reports  to see the results of your run.

Extensions
----------

IMS Headers, headers in gov.nist.javax.sip.extension and all the classes
that are suffixed with "Ext" in their name can be used without concern as
they will be included in the next generation of the API. These will not 
change as a rule.

You should refrain from using any other internal classes. These are subject
to change without notice.

----------------------------------------------------------------------------
Running the examples

Please ensure that the directory  classes  (relative to where you have
built the distribution) is included in the  classpath. Ant targets
are provided in each example directory to run the examples.

How to get Source Code Refreshes
--------------------------------

git clone https://github.com/usnistgov/jsip.git

----------------------------------------------------------------------------

Credits
--------

Architecture / API design:
-------------------------

JAIN-SIP: Joint Spec Leads -- Phelim O'Doherty (BEA) and M. Ranganathan (NIST). 
JAIN-SDP: The SDP API spec lead is Kelvin Porter from Cisco.

Implementation Lead:
---------------------
"M. Ranganathan" <mranga@nist.gov>

Implementation Team ( version 1.2)
----------------------------------
"M. Ranganathan" <mranga@nist.gov>
"Jeroen van Bemmel" <jeroen@zonnet.nl>

TCK (version 1.2)
----------------
M. Ranganathan  <mranga@nist.gov>
Jeroen van Bemmel <jeroen@zonnet.nl>


Current maintainence lead:

Vladimir Ralev <vralev@gmail.com>



---------------------------------------------------------------------------
LICENSE
-------

The implementation is public domain although the API itself is'nt. 
See the license directory in this distribution for definitive information.

***********************************************************************
* The following applies to the packages "gov.nist", "test" and 
* "tools" and all subpackages thereof
***********************************************************************
*
* Conditions Of Use 
* 
* This software was developed by employees of the National Institute of
* Standards and Technology (NIST), and others. 
* This software has been contributed to the public domain. 
* Pursuant to title 15 Untied States Code Section 105, works of NIST
* employees are not subject to copyright protection in the United States
* and are considered to be in the public domain. 
* As a result, a formal license is not needed to use this software.
* 
* This software is provided "AS IS."  
* NIST MAKES NO WARRANTY OF ANY KIND, EXPRESS, IMPLIED
* OR STATUTORY, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT
* AND DATA ACCURACY.  NIST does not warrant or make any representations
* regarding the use of the software or the results thereof, including but
* not limited to the correctness, accuracy, reliability or usefulness of
* this software.

----------------------------------------------------------------------------

Substantial input by early adopters and fearless users.

See List of Contributions at:

https://github.com/usnistgov/jsip/blob/master/www/README.html


----------------------------------------------------------------------------
