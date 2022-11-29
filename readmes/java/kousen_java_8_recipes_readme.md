# java_8_recipes
Source code for Modern Java Recipes (O'Reilly, 2017)

http://shop.oreilly.com/product/0636920056669.do

For IntelliJ:
* clone repo or download zip and extract
* Use `File -> Open` or if not project is open, `Import`
* Navigate to the `build.gradle` file inside the project
* Click enter and accept all the defaults

For Eclipse (and Eclipse-based tools, like STS):
* Open a command prompt in the root of the unzipped project
* Type `gradlew cleanEclipse eclipse` (Note: if you're on a Unix-based system, including Macs, you need to use `./gradlew …`)
* Wait for the dependencies to be downloaded
* Choose `File -> Import… -> General -> Existing Projects into Workspace`
* Navigate to the root of the project and select it
