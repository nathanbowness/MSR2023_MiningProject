Python Firefox Sync client
##########################

Old fork of https://github.com/eNote-GmbH/syncclient that auto decrypts, but it doesn't handle login well. Instead now see https://github.com/clach04/firefox_syncclient/tree/enote_docs

This is a python client for Firefox Sync. Check it out with::

  $ pip install -e .
  $ python syncclient/main.py --help

For instance, if you want to get all passwords (decrypted) use the
`get_records` action:

.. code-block::

  $ python syncclient/main.py alexis@notmyidea.org $PASSWORD
  $ python syncclient/main.py alexis@notmyidea.org $PASSWORD info_collections
  $ python syncclient/main.py alexis@notmyidea.org $PASSWORD get_records tabs
  $ python syncclient/main.py alexis@notmyidea.org $PASSWORD get_records passwords
  [u'{1c1e0eea-d9c2-4c59-b95e-4dbe0800639f}',
   u'{0a76ec08-ba7c-48b1-b026-1d65085f789e}',
   u'{7482b391-bf2f-4542-8ebd-27c4398487ff}',
   u'{37bc9298-ac49-c54e-a73d-d817434ed0b2}',
   u'{d5ff4718-d4a0-4703-b0af-7d1c79c3a099}']

NOTE 2FA means that mail for account needs to be manually checked and allowed, to get past:

  Traceback (most recent call last):
    File "syncclient/main.py", line 34, in <module>
      main()
    File "syncclient/main.py", line 23, in main
      bid_assertion_args = get_browserid_assertion(args.login, args.password)
    File "syncclient\client.py", line 68, in get_browserid_assertion
      bid_assertion = session.get_identity_assertion(tokenserver_url)
    File "...\lib\site-packages\fxa\core.py", line 398, in get_identity_assertion
      cert = self.sign_certificate(public_key, duration * 1000, **kwds)
    File "...\lib\site-packages\fxa\core.py", line 363, in sign_certificate
      resp = self.apiclient.post(url, body, auth=self._auth)
    File "...\lib\site-packages\fxa\_utils.py", line 338, in post
      return self.request("POST", url, json, **kwds)
    File "...\lib\site-packages\fxa\_utils.py", line 324, in request
      raise fxa.errors.ClientError(body)
  fxa.errors.ClientError: Unverified session
