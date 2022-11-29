<!-- Variables (this block will not be visible in the readme -->
[banner]: https://pcgamingfreaks.at/images/marriagemaster.png
[spigot]: https://www.spigotmc.org/resources/marriage-master.19273/
[spigotRatingImg]: https://img.shields.io/spiget/rating/19273.svg
[spigotDownloadsImg]: https://img.shields.io/spiget/downloads/19273.svg?label=downloads%20%28spigot%29
<!--[spigotRatingImg]: https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=rating&query=%24.rating.average&suffix=%20%2F%205&url=https%3A%2F%2Fapi.spiget.org%2Fv2%2Fresources%2F19273
[spigotDownloadsImg]: https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=downloads%20%28spigotmc.org%29&query=%24.downloads&url=https%3A%2F%2Fapi.spiget.org%2Fv2%2Fresources%2F19273-->
[bukkit]: https://dev.bukkit.org/bukkit-plugins/marriage-master/
[issues]: https://github.com/GeorgH93/MarriageMaster/issues
[wiki]: https://github.com/GeorgH93/MarriageMaster/wiki
[wiki_faq]: https://github.com/GeorgH93/MarriageMaster/wiki/FAQ
[wikiPermissions]: https://github.com/GeorgH93/MarriageMaster/wiki/Permissions
[wikiPlaceholders]: https://github.com/GeorgH93/MarriageMaster/wiki/Placeholders
[release]: https://github.com/GeorgH93/MarriageMaster/releases/latest
[releaseImg]: https://img.shields.io/github/release/GeorgH93/MarriageMaster.svg?label=github%20release
[license]: https://github.com/GeorgH93/MarriageMaster/blob/master/LICENSE
[licenseImg]: https://img.shields.io/github/license/GeorgH93/MarriageMaster.svg
[ci]: https://ci.pcgamingfreaks.at/job/MarriageMaster/
[ciImg]: https://ci.pcgamingfreaks.at/job/MarriageMaster/badge/icon
[ciDev]: https://ci.pcgamingfreaks.at/job/MarriageMaster%20Dev/
[ciDevImg]: https://ci.pcgamingfreaks.at/job/MarriageMaster%20Dev/badge/icon
[apiVersionImg]: https://img.shields.io/badge/dynamic/xml.svg?label=api-version&query=%2F%2Frelease[1]&url=https%3A%2F%2Frepo.pcgamingfreaks.at%2Frepository%2Fmaven-releases%2Fat%2Fpcgamingfreaks%2FMarriageMaster-API%2Fmaven-metadata.xml
[api]: https://github.com/GeorgH93/MarriageMaster/tree/master/API
[apiJavaDoc]: https://ci.pcgamingfreaks.at/job/MarriageMaster%20API/javadoc/
[apiBuilds]: https://ci.pcgamingfreaks.at/job/MarriageMaster%20API/
[featureRequestsImg]: https://img.shields.io/github/issues/GeorgH93/MarriageMaster/enhancement.svg?label=feature%20requests
[featureRequests]: https://github.com/GeorgH93/MarriageMaster/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement
[requestFeature]: https://github.com/GeorgH93/MarriageMaster/issues/new?labels=enhancement&template=feature.md
[bugReportsImg]: https://img.shields.io/github/issues/GeorgH93/MarriageMaster/bug.svg?label=bug%20reports
[bugReports]: https://github.com/GeorgH93/MarriageMaster/issues?q=is%3Aissue+is%3Aopen+label%3Abug
[reportBug]: https://github.com/GeorgH93/MarriageMaster/issues/new?labels=bug&template=bug.md
<!-- End of variables block -->

[![Logo][banner]][spigot]

Marriage Master is a Bukkit/Spigot plugin that allows you to marry another player in Minecraft to gain some extras.

[![ciImg]][ci] [![releaseImg]][release]
[![apiVersionImg]][api] [![licenseImg]][license]

[![featureRequestsImg]][featureRequests] [![bugReportsImg]][bugReports]
[![spigotRatingImg]][spigot] [![spigotDownloadsImg]][spigot]

## Features:
- Players can marry one (or more if configured) players to gain access to a set of special commands and benefits.
- Features for married players:
  - TP - players can teleport to their partner any time
  - Home - any of the two players can set the home for them, then both can teleport to that point at any time
  - Gift - players can gift their partners items
  - PvP - players can disable pvp with their partner
  - Chat - players can chat privately with their partner
- Configuration - The plugin has a huge well documented configuration file where you can adjust almost every aspect of the plugin the way you like it. You can even change the entire plugin to a friends plugin without writing a single line of code!
- Language - The plugin has a language files that store all the messages used, you can translate them into any language, format them the way you like them or even disable them all one by one. Also check the language file tool:
- Database - The plugin currently allows you to store your data in SQLite or MySQL databases.
- [Permissions][wikiPermissions] - If you want to limit features or the whole plugin for certain worlds or groups or even just players you can do that with the huge amount off available permissions. For the whole list please look here:
- [Placeholders][wikiPlaceholders]
- [API][api] - The plugin has a very powerful API for developers

## Requirements:
### Runtime requirements:
* Java 8
* Bukkit, Spigot or Paper for Minecraft 1.7.10 or newer; or Uranium for Minecraft 1.7.10
* (Optional) BungeeCord or Waterfall for Minecraft 1.7.10 or newer
* (Optional) [Vault](https://www.spigotmc.org/resources/vault.34315/) (for economy features)
* (Optional) [PCGF PluginLib](https://github.com/GeorgH93/PCGF_PluginLib) ([Advantages of using the PCGF PluginLib](https://github.com/GeorgH93/MarriageMaster/wiki/Build-and-Mode-comparison#Advantages-of-using-the-PCGF-PluginLib))

### Build requirements:
* JDK for Java 8
* Maven 3
* git

## Build from source:
The plugin can be build in 3 different configurations.
All the details about the different build configs and runtime modes can be found [here](https://github.com/GeorgH93/MarriageMaster/wiki/Build-and-Mode-comparison).

### Normal version:
```
git clone https://github.com/GeorgH93/MarriageMaster.git
cd MarriageMaster
mvn package
```
The final file will be in the `MarriageMaster/target` folder, named `MarriageMaster-<CurrentVersion>.jar`.

### Standalone version:
This version works without the PCGF-PluginLib, however some API features are not available.
```
git clone https://github.com/GeorgH93/MarriageMaster.git
cd MarriageMaster
mvn package -P Standalone
```
The final file will be in the `MarriageMaster/target` folder, named `MarriageMaster-<CurrentVersion>-Standalone.jar`.

### Release version:
This is the version of the plugin published on dev.bukkit.org and spigotmc.org.
```
git clone https://github.com/GeorgH93/MarriageMaster.git
cd MarriageMaster
mvn clean install -P Standalone
mvn clean package -P Release
```
The final file will be in the `MarriageMaster/target` folder, named `MarriageMaster-<CurrentVersion>-Release.jar`.

## API:
Marriage Master V2 comes with a very powerful API that allows you to change almost everything about this plugin.
Most of the plugins commands are implemented only using methods and data provided by the API.
If you think there is something missing feel free to open a [feature request][requestFeature].
Please do not access the data of the plugin over other ways than the provided API, the inner workings will change and I wont keep track of what you are using in your plugin.
For more details about the API please check the following links.

[Source Code & Details][api] ⚫ [JavaDoc][apiJavaDoc] ⚫ [Build Server][apiBuilds]

## Support:
* [Wiki][wiki]
* [Issue tracker][issues]
  * [new feature request][requestFeature]
  * [new bug report][reportBug]
* [FAQ][wiki_faq]

## Links:
* [Spigot][spigot]
* [Dev Bukkit][bukkit]
* [Build Server - Master Builds ![ciImg]][ci]
* [Build Server - Dev Builds ![ciDevImg]][ciDev]
