## Vorab

Dies ist ein aktuell gepflegter Fork von [HBCI4Java](http://hbci4java.kapott.org/),
welcher u.a. in [Hibiscus](http://www.willuhn.de/products/hibiscus) und
[Pecunia-Banking](http://www.pecuniabanking.de/) zum Einsatz kommt.

## Kontakt

Unter https://groups.google.com/forum/?hl=de#!forum/hbci4java findet ihr die
zugehörige Mailingliste.

## Entstehung

Das Projekt entstand 2010 als Fork von http://hbci4java.kapott.org, da dessen Weiterentwicklung eingestellt wurde.

Seither wurden umfangreiche neue Features hinzugefügt wie etwa:

- Die Unterstützung der neuen TAN-Verfahren (smsTAN, photoTAN, chipTAN - incl. Implementierung des HHD-Standards mit Flicker-Code)
- Unterstützung von PC/SC-Kartenlesern via javax.smartcardio API
- Eine aktuelle Bankenliste (mit BLZ, Server-Adresse, HBCI-Version,...)
- Support für alle aktuellen SEPA-PAIN-Versionen
- SEPA-Überweisungen und -Lastschriften (jeweils Einzel- und Sammelaufträge) sowie SEPA-Daueraufträge 
- Abruf des elektronischen Kontoauszuges (HKEKA und HKEKP)
- Unterstützung für chipTAN USB
- Abruf von Umsätzen im CAMT-Format (HKCAZ)

## Lizenz

LGPL 2.1 - GNU Lesser General Public License, version 2.1 (http://www.gnu.org/licenses/old-licenses/lgpl-2.1)

*Hinweis*
Bis 02.05.2016 unterlag HBCI4Java der GPLv2 - wurde mit https://github.com/willuhn/hbci4java/issues/36 aber auf LGPL 2.1 geändert.

## Download

Du kannst die aktuellste Version von HBCI4Java in Maven Central finden:

https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.github.hbci4j%22%20AND%20a%3A%22hbci4j-core%22


*Maven*

```
<dependency>
   <groupId>com.github.hbci4j</groupId>
   <artifactId>hbci4j-core</artifactId>
</dependency>
```

*Gradle*

```
dependencies {
  compile 'com.github.hbci4j:hbci4j-core:+'
}
```



## Selbst compilieren

Du benötigst:

- GIT (https://git-scm.com/)
- Java SDK 8 oder höher (http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- Apache Maven 3.3.9 oder höher (https://maven.apache.org/)

Öffne ein Terminal-Fenster und checke den Quellcode per GIT aus:

    $> git clone https://github.com/hbci4j/hbci4java.git
    
Wechsle in den Ordner "hbci4java":

    $> cd hbci4java

Erzeuge die JAR-Datei per:

    $> mvn package
  
Im Ordner "target" wird die Datei "hbci4j-core-${version}.jar" erzeugt.

## Import in Eclipse

Du benötigst:

- Eine Eclipse-Version mit Maven-Support, z.Bsp.: "Eclipse IDE for Java EE Developers" (http://www.eclipse.org/downloads/eclipse-packages/) 
- Den ausgecheckten Quellcode von HBCI4Java per GIT (siehe oben)

Klicke im Menu von Eclipse auf "File->Import..." und wähle "Maven->Existing Maven Projects". Folge den Anweisungen des Assistenten. Klicke anschließend mit der rechten Maustaste im "Package Explorer" oder "Navigator" auf das Projekt und wähle im Contextmenu "Maven->Update Project...".


## Unit-Tests
Im Ordner "src/main/test/" befinden sich einige JUnit-Tests. Einige davon erfordern jedoch das Vorhandensein spezieller Testumgebungen (Vorhandensein von Bankzugängen oder Chipkartenleser). Diese Tests werden im Zuge der Erstellung von Deployment-Artefakten nur dann ausgeführt, wenn die entsprechenden System-Properties "test.online=true" und "test.chipcard=true" aktiv sind. Die Tests zur Ausführung von HBCI-Geschäftsvorfällen benötigen jedoch weitere Daten (Empfängerkonto, Betrag, Verwendungszweck, usw.). Wenn du diese Tests ausführen möchtest, schaue dir den Quellcode der entsprechenden Tests an.

## Beispiel-Code

Unter https://github.com/hbci4j/hbci4java/blob/master/src/main/java/org/kapott/hbci/examples/UmsatzAbrufPinTan.java findest du Beispiel-Code zum Abrufen des Saldos und der Umsätze eines Kontos per PIN/TAN-Verfahren.
 
