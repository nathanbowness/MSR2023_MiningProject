Google-Directions-Android
=========================
 [![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.github.jd-alexander/library/badge.svg?style=flat)](https://maven-badges.herokuapp.com/maven-central/com.github.jd-alexander/library/) [![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-Google--Directions--Android-green.svg?style=flat)](https://android-arsenal.com/details/1/2090) [![Build Status](https://travis-ci.org/jd-alexander/Google-Directions-Android.svg?branch=master)](https://travis-ci.org/jd-alexander/Google-Directions-Android)

This project allows you to calculate the direction between two locations and display the route on a Google Map using the Google Directions API - This project isn't actively been maintained. 



![Example Image][1]

Sample
------------

The sample makes use of the Google Places API for Android in order to provide a real life example of how the library can be used.[You can check it out on the store.](https://play.google.com/store/apps/details?id=com.directions.sample)

Download
--------


Grab via Maven:
```xml
<dependency>
  <groupId>com.github.jd-alexander</groupId>
  <artifactId>library</artifactId>
  <version>1.1.0</version>
</dependency>
```
or Gradle:
```groovy
    compile 'com.github.jd-alexander:library:1.1.0'
```

Usage
-----

To calculate the route you simply instantiate a Routing object and trigger the execute function.


*You can execute the task in this manner. ( See the example for more details on the exact implementation)



``` java

        Routing routing = new Routing.Builder()
                    .travelMode(/* Travel Mode */)
                    .withListener(/* Listener that delivers routing results.*/)
                    .waypoints(/*waypoints*/)
                    .key(/*api key for quota management*/)
                    .build();
        routing.execute();
        
```



actual code 
``` java
        start = new LatLng(18.015365, -77.499382);
        waypoint= new LatLng(18.01455, -77.499333);
        end = new LatLng(18.012590, -77.500659);
        
        Routing routing = new Routing.Builder()
                    .travelMode(Routing.TravelMode.WALKING)
                    .withListener(this)
                    .waypoints(start, waypoint, end)
                    .build();
        routing.execute();
        
        .....
        
       @Override
    public void onRoutingSuccess(ArrayList<Route> route, int shortestRouteIndex)
    {
       //code to add route to map here. See sample app for more details.
    }
```

Demostration
------------
*  https://www.youtube.com/watch?v=58AxNh2cWRU

Demo App
------------
*  https://github.com/hamza-ameer/GoogleMaps-Find-Routes/tree/Updated


Known Issues
------------
*  If the AutoComplete TextView/Map of the sample app isnt working then probably the API key hasn't been set in the manifest.

* If the route is not being displayed then type "Routing" in your log cat to see the potential error messages from the library.


Contribution
------------

Please fork  repository and contribute using pull requests.

Any contributions, large or small, major features, bug fixes, additional language translations, unit/integration tests are welcomed and appreciated but will be thoroughly reviewed and discussed.

Contributors
------------
*   [Cyrille Berliat](https://github.com/licryle)
*   [Felipe Duarte](https://github.com/fcduarte)
*   [Kedar Sarmalkar](https://github.com/ksarmalkar)
*   [Fernando Gil](https://github.com/fgil)
*   [Furkan Tektas](https://github.com/furkantektas)
*   [João Pedro Nardari dos Santos](https://github.com/joaopedronardari)
*   [Hesham Saeed](https://github.com/HeshamSaeed)

License
--------

    Copyright 2016 Joel Dean

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.






[1]:http://i57.tinypic.com/2m7j04x.png



