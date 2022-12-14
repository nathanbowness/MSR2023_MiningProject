# MemorizingTrustManager - Private Cloud Support for Your App

MemorizingTrustManager (MTM) is a project to enable smarter and more secure use
of SSL on Android. If it encounters an unknown SSL certificate, it asks the
user whether to accept the certificate once, permanently or to abort the
connection. This is a step in preventing man-in-the-middle attacks by blindly
accepting any invalid, self-signed and/or expired certificates.

MTM is aimed at providing seamless integration into your Android application,
and the source code is available under the MIT license.

## Screenshots

![MemorizingTrustManager dialog](mtm-screenshot.png)
![MemorizingTrustManager notification](mtm-notification.png)
![MemorizingTrustManager server name dialog](mtm-servername.png)

## Status

MemorizingTrustManager is in production use in the
[yaxim XMPP client](https://yaxim.org/). It is usable and easy to integrate,
though it does not yet support hostname validation (the Java API makes it
**hard** to integrate).

## Integration

MTM is easy to integrate into your own application. Follow these steps or have
a look into the demo application in the `example` directory.

### 1. Add MTM to your project

Download the MTM source from GitHub, or add it as a
[git submodule](http://git-scm.com/docs/git-submodule):

	# plain download:
	git clone https://github.com/ge0rg/MemorizingTrustManager
	# submodule:
	git submodule add https://github.com/ge0rg/MemorizingTrustManager

Then add a library project dependency to `default.properties`:

	android.library.reference.1=MemorizingTrustManager

### 2. Add the MTM (popup) Activity to your manifest

Edit your `AndroidManifest.xml` and add the MTM activity element right before the
end of your closing `</application>` tag.

			...
			<activity android:name="de.duenndns.ssl.MemorizingActivity"
				android:theme="@android:style/Theme.Translucent.NoTitleBar"
				/>
		</application>
	</manifest>

### 3. Hook MTM as the default TrustManager for your connection type

Hooking MemorizingTrustmanager in **HTTPS connections**:

	// register MemorizingTrustManager for HTTPS
	SSLContext sc = SSLContext.getInstance("TLS");
	MemorizingTrustManager mtm = new MemorizingTrustManager(this);
	sc.init(null, new X509TrustManager[] { mtm }, new java.security.SecureRandom());
	HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());
	HttpsURLConnection.setDefaultHostnameVerifier(
		mtm.wrapHostnameVerifier(HttpsURLConnection.getDefaultHostnameVerifier()));

For **SSLSocket** you should do the following:

	// register MemorizingTrustManager for all SSLSockets
	SSLContext sc = SSLContext.getInstance("TLS");
	MemorizingTrustManager mtm = new MemorizingTrustManager(this);
	HostnameVerifier hv = mtm.wrapHostnameVerifier(new org.apache.http.conn.ssl.StrictHostnameVerifier());
	sc.init(null, new X509TrustManager[] { mtm }, new java.security.SecureRandom());
	SSLContext.setDefault(sc);
	
	// connect a socket
	SSLSocket s = ...;
	s.startHandshake();
	if (!hv.verify(your_domain_name, sslSocket.getSession())) {
	    throw new CertificateException("Server failed to authenticate as " + your_domain_name);
	}

Or, for **Smack** you can use `setCustomSSLContext()`:

	org.jivesoftware.smack.ConnectionConfiguration connectionConfiguration = ???
	SSLContext sc = SSLContext.getInstance("TLS");
	MemorizingTrustManager mtm = new MemorizingTrustManager(this);
	sc.init(null, new X509TrustManager[] { mtm }, new java.security.SecureRandom());
	connectionConfiguration.setCustomSSLContext(sc);
	connectionConfiguration.setHostnameVerifier(
		mtm.wrapHostnameVerifier(new org.apache.http.conn.ssl.StrictHostnameVerifier()));

By default, MTM falls back to the system `TrustManager` before asking the user.
If you do not trust the establishment, you can enforce a dialog on *every new
connection* by supplying a `defaultTrustManager = null` parameter to the
constructor:

	MemorizingTrustManager mtm = new MemorizingTrustManager(this, null);

If you want to use a different underlying `TrustManager`, like
[AndroidPinning](https://github.com/moxie0/AndroidPinning), just supply that to
MTM's constructor:

	X509TrustManager pinning = new PinningTrustManager(SystemKeyStore.getInstance(),
		new String[] {"f30012bbc18c231ac1a44b788e410ce754182513"}, 0);
	MemorizingTrustManager mtm = new MemorizingTrustManager(this, pinning);

### 4. Profit!

### Logging

MTM uses java.util.logging (JUL) for logging purposes. If you have not
configured a Handler for JUL, then Android will by default log all
messages of Level.INFO or higher. In order to get also the debug log
messages (those with Level.FINE or lower) you need to configure a
Handler accordingly. The MTM example project contains
de.duenndns.mtmexample.JULHandler, which allows to enable and disable
debug logging at runtime.

## Alternatives

MemorizingTrustManager is not the only one out there.

[**NetCipher**](https://guardianproject.info/code/netcipher/) is an Android
library made by the [Guardian Project](https://guardianproject.info/) to
improve network security for mobile apps. It comes with a StrongTrustManager
to do more thorough certificate checks, an independent Root CA store, and code
to easily route your traffic through
[the Tor network](https://www.torproject.org/) using [Orbot](https://guardianproject.info/apps/orbot/).

[**AndroidPinning**](https://github.com/moxie0/AndroidPinning) is another Android
library, written by [Moxie Marlinspike](http://www.thoughtcrime.org/) to allow
pinning of server certificates, improving security against government-scale
MitM attacks. Use this if your app is made to communicate with a specific
server!

## Contribute

Please [help translating MTM into more languages](https://translations.launchpad.net/yaxim/master/+pots/mtm/)!
