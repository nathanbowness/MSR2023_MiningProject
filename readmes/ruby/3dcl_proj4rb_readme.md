= Proj4rb
This gem provides Ruby bindings for the Proj Library (https://proj.org). The Proj Library supports converting coordinates
between a number of different coordinate systems and projections.

== Documentation
Besides this readme file, reference documentation is available at https://rubydoc.info/github/cfis/proj4rb.

== Installation
First install the gem in the usual manner:

    gem install proj4rb

Next install the Proj Library. This of course varies per system, but you want to install the latest version Proj
possible. Once installed, you'll need to make sure that libproj is installed on your operating system's
load path.

== Usage
To get started first require the gem:

  require 'proj'

If you are using the old Proj4 namespace, then you can do this:

  require 'proj4'

=== Crs
If you are using Proj 6 create a coordinate system. To create a coordinate system, you can use CRS codes, well-known text (WKT) strings
or old-style Proj4 strings (which are deprecated).

    crs1 = Proj::Crs.new('EPSG:4326')

    crs2 = Proj::Crs.new('urn:ogc:def:crs:EPSG::4326')

    crs3 = Proj::Crs.new('+proj=longlat +datum=WGS84 +no_defs +type=crs')

    crs4 = Proj::Crs.new(<<~EOS)
      GEOGCRS["WGS 84",
      DATUM["World Geodetic System 1984",
            ELLIPSOID["WGS 84",6378137,298.257223563,
                      LENGTHUNIT["metre",1]]],
      PRIMEM["Greenwich",0,
             ANGLEUNIT["degree",0.0174532925199433]],
      CS[ellipsoidal,2],
      AXIS["geodetic latitude (Lat)",north,
           ORDER[1],
           ANGLEUNIT["degree",0.0174532925199433]],
      AXIS["geodetic longitude (Lon)",east,
           ORDER[2],
           ANGLEUNIT["degree",0.0174532925199433]],
      USAGE[
          SCOPE["unknown"],
              AREA["World"],
          BBOX[-90,-180,90,180]],
      ID["EPSG",4326]]
    EOS

Notice when using the old-style Proj4 string, the addition of the "+type=crs" value.

If you are using Proj 5, then you should create a transformation using epsg strings (see below). If you are using Proj 4,
you need to use the deprecated Projection class (see documentation).

=== Transformation
After you have created two coordinate systems, you can then create a transformation. For example, if you want to
convert coordinates from the "3-degree Gauss-Kruger zone 3" coordinate system to WGS84 (one version of lat-long)
first create a transformation:

    crs_gk  = Proj::Crs.new('epsg:31467')
    crs_wgs84 = Proj::Crs.new('epsg:4326')
    transform = Proj::Transformation.new(crs_gk, crs_wgs84)

Alternatively, or if you are using Proj 5, you can create a transformation without first
creating Crs instances. Instead, pass the EPSG information directly to the transformation:

    transform = Proj::Transformation.new('epsg:31467', 'epsg:4326')

Once you've created the transformation, you can tranform coordinates using either
the +forward+ or +inverse+ methods. The forward transformation looks like this:

    from = Proj::Coordinate.new(x: 5428192.0, y: 3458305.0, z: -5.1790915237)
    to = transform.forward(from)

    assert_in_delta(48.98963932450735, to.x, 0.01)
    assert_in_delta(8.429263044355544, to.y, 0.01)
    assert_in_delta(-5.1790915237, to.z, 0.01)
    assert_in_delta(0, to.t, 0.01)

While the inverse transformation looks like this:

    from = Proj::Coordinate.new(lam: 48.9906726079, phi: 8.4302123334)
    to = transform.inverse(from)

    assert_in_delta(5428306.389495558, to.x, 0.01)
    assert_in_delta(3458375.3367194114, to.y, 0.01)
    assert_in_delta(0, to.z, 0.01)
    assert_in_delta(0, to.t, 0.01)

=== Coordinate
Notice the examples above transform Coordinate objects. A Coordinate consists
of up to four double values to represent three directions plus time. In general
you will need to fill out at least the first two values:

    from = Proj::Coordinate.new(x: 5428192.0, y: 3458305.0, z: -5.1790915237)
    from = Proj::Coordinate.new(lam: 48.9906726079, phi: 8.4302123334)

Lam is longitude and phi is latitude.

=== Context
Contexts are used to support multi-threaded programs. The bindings expose this object via Context.current
and store it using thread local storage. Use the context object to access error codes, set proj4
compatability settings, set the logging level and to install custom logging code.

Both Crs and Transformation objects take a context object in their constructors. If none is passed, they default
to using Context.current

=== Projection
If you are using Proj 4, then instead of using Coordinates, Crses and Tranformations you need to us Points and Projections.
Those are deprecated classes but will continue to work until the release of Proj 7.  Please refer to the documentation
for more information.

== Error handling
When an error occurs, a Proj::Error instance will be thrown with the underlying message provided
from the Proj library.

== Finding Proj Files (LIB_PROJ)
Starting with version 6, Proj stores its information (datums, ellipsoids, prime meridians, coordinate systems,
units, etc) in a sqlite file called proj.db. If Proj cannot find its database, then the Ruby bindings will
search for it in some well-known locations. Failing that, the Ruby bindings will raise an exception.
In this case, set the environmental variable PROJ_LIB to point at the folder that contains the proj.db file.
Note PROJ_LIB must be set by whatever launches your Ruby program. The Ruby program itself cannot set this
variable and have it work correctly (at least not on windows).

== Backwards Compatibility
Proj versions 5 and 6 are *very* different than Proj version 4. Changes are documented at
https://proj.org/development/migration.html. Note that the gem should gracefully degrade
(as in newer functionality stops working but older functionality keeps working) depending on
the version of Proj you are using.

To ensure backwards compatiblity, the Ruby bindings still include the older Point and Projection
classes. However, these classes are no longer documented in this Readme because they will be
removed upon the release of Proj 7 which will remove the underlying API's they depend on.
So please port your code! But take note of the changes in Proj 6 described below.

Proj 5 introduced the Coordinate, Crs and Tranformation APIs. However, it wasn't until Proj 6 that additional
metadata APIs were added, so the amount of information about each object is somewhat limited in Proj 5.

Proj 6 makes a big change compared to previous releases that is not well documented (see
https://github.com/OSGeo/PROJ/pull/1182). When creating tranformations with EPSG values Proj 6
will assume EPSG axis order and units (typically lat-long degree for geodetic CRS). First,
this means that lat-long should usually be specified in degrees and not radians (breaking change one).
Second, the axis order is likely different than what your previous code assumed (breaking change two).
Note if creating transformations with the deprecated "+init=epsg:XXXX" values, Proj 6 will assume the traditional
axis order and units (long-lat radians for geodetic CRS).

Bottom line - when porting your code to the new Proj 6 APIs generally:

* Use degrees, not radians
* Swap the order of the lat and long values

== Tests
Proj4rb ships with a full test suite designed to work using Proj 6. If you are using an earlier version of Proj,
then expect *many* test failures.

== License
Proj4rb is released under the MIT license.

==Authors
The proj4rb Ruby bindings were started by Guilhem Vellut with most of the code 
written by Jochen Topf.  Charlie Savage ported the code to Windows and added 
the Windows build infrastructure. Later, he rewrote the code to support
Proj version 5 and 6 and ported it to use FFI.