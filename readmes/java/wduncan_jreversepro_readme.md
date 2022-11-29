                      JReversePro 1.5.2
               Java Decompiler / Disassembler
                 http://jrevpro.sourceforge.net
	             	May 21 2008

This reverse engineering utility has been written in Java.
This code is distributed under the GNU GENERAL PUBLIC LICENSE
(GPL, see www.gnu.org).  See the file "COPYING" for details.

To install, see the file "INSTALL".


Getting Started
================
	See INSTALL file to install the software first.

How do I launch the application ?
================================

The executable jar file jreversepro.jar is present in ./lib directory.
	
	Application in GUI mode: ( Swing )
		jrevpro -g

	Application in GUI mode: ( AWT )
		jrevpro -u		
		
	Application in command-line mode:

	Interactive: 	jrevpro -i  <classfile>
	Disassemble: 	jrevpro -da  <classfile>
	Decompile:  	jrevpro -dc  <classfile>		
	ViewConstantPool: jrevpro -vp  <classfile>			
		

Interactive mode
================
	Let us assume a file xyz.class in our directory.
	
To decompile,

	jrevpro -i xyz.class
	
(jrevpro)dc 
  ... Decompiles File ...
  
(jrevpro)da
  .. Disassembles file ...
  
(jrevpro)viewpool  |  vp  <cp_index>
  .. Views ConstantPool ....
  
(jrevpro)exit
    ...Exits.
  

To Compile:
==========
You need the Maven build tool available at the Apache web site.

http://maven.apache.org/

Having installed Maven, run the following goals:

mvn dependency:copy-dependencies
mvn package
  
Known Bugs
==========
   Known Bugs include live variable analysis across branches.
   Also important is doing a rigorous try..catch.finally analysis.  	
   
Bug Parade
=========
	Please report the bugs in the bugs report page present in 
http://jrevpro.sourceforge.net .
 
    If possible please , try to submit the class files with which you 
 encountered the errors since that would be very helpful to debug the issue.
 
Source Control:
==============
   Started using Git from May 2009.





Copyrights (c) 2000..2008 by  Karthik Kumar 
akkumar@users.sourceforge.net.
