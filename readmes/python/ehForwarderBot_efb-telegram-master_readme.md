EFB Telegram Master Channel (ETM)
=================================

.. image:: https://img.shields.io/pypi/v/efb-telegram-master.svg
   :alt: PyPI release
   :target: https://pypi.org/project/efb-telegram-master/
.. image:: https://github.com/ehForwarderBot/efb-telegram-master/workflows/Tests/badge.svg
   :alt: Tests status
   :target: https://github.com/ehForwarderBot/efb-telegram-master/actions
.. image:: https://pepy.tech/badge/efb-telegram-master/month
   :alt: Downloads per month
   :target: https://pepy.tech/project/efb-telegram-master
.. image:: https://d322cqt584bo4o.cloudfront.net/ehforwarderbot/localized.svg
   :alt: Translate this project
   :target: https://crowdin.com/project/ehforwarderbot/

.. image:: https://github.com/ehForwarderBot/efb-telegram-master/raw/master/banner.png
   :alt: Banner

`README in other languages`_.

.. TRANSLATORS: change the URL on previous line as "." (without quotations).
.. _README in other languages: ./readme_translations

**Channel ID**: ``blueset.telegram``

ETM is a Telegram Master Channel for EH Forwarder Bot, based on Telegram
Bot API, ``python-telegram-bot``.

Requirements
------------

-  Python >= 3.6
-  EH Forwarder Bot >= 2.0.0
-  ffmpeg
-  libmagic
-  libwebp

Getting Started
---------------

1. Install all required binary dependencies
2. Install ETM

   .. code:: shell

       pip3 install efb-telegram-master

3. Enable and configure ETM using the *EFB configuration wizard*, or enable
   it manually in the profile’s ``config.yaml``.

   The path of your profile storage directory depends on your
   configuration.

   **(As of EFB 2, default profile storage directory is located at**
   ``~/.ehforwarderbot/profiles/default`` **)**

4. Configure the channel (manual configure instructions as follows)

Alternative installation methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ETM also has other alternative installation methods
contributed by the community, including:

- `AUR package`_ maintained by KeLiu_ (``python-efb-telegram-master-git``)
- Other `installation scripts and containers (e.g. Docker)`_

.. _KeLiu: https://github.com/specter119
.. _AUR package: https://aur.archlinux.org/packages/python-efb-telegram-master-git
.. _installation scripts and containers (e.g. Docker): https://efb-modules.1a23.studio#scripts-and-containers-eg-docker

Manual Configuration
--------------------

Set up a bot
~~~~~~~~~~~~

Create a bot with `@BotFather`_, give it a name and a username.
Then you’ll get a token, which will be used later. Keep this
token secure, as it gives who owns it the full access to the
bot.

.. _@BotFather: https://t.me/botfather

Use ``/setjoingroups`` to allow your bot to join groups.
Use ``/setprivacy`` to disable the privacy restriction
of the bot, so that it can receive all messages in the
group.

Complete configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration file is stored at
``<profile directory>/blueset.telegram/config.yaml``.

A sample config file can be as follows:

.. code:: yaml

    ##################
    # Required items #
    ##################

    # [Bot Token]
    # This is the token you obtained from @BotFather
    token: "012345678:1Aa2Bb3Vc4Dd5Ee6Gg7Hh8Ii9Jj0Kk1Ll2M"

    # [List of Admin User IDs]
    # ETM will only process messages and commands from users
    # listed below. This ID can be obtained from various ways 
    # on Telegram.
    admins:
    - 102938475
    - 91827364

    ##################
    # Optional items #
    ##################
    # [Experimental Flags]
    # This section can be used to toggle experimental functionality.
    # These features may be changed or removed at any time.
    # Options in this section is explained afterward.
    flags:
        option_one: 10
        option_two: false
        option_three: "foobar"

    # [Network Configurations]
    # [RPC Interface]
    # Refer to relevant sections afterwards for details.

Usage
-----

At the beginning, messages from all senders will be sent to the user
directly, that means every message will be mixed in the same
conversation. By linking a chat, you can redirect messages from a
specific sender to an empty group for a more organized conversation.

In a nutshell, ETM offers the following commands, you can also send it
to BotFather for a command list::

    help - Show commands list.
    link - Link a remote chat to a group.
    unlink_all - Unlink all remote chats from a group.
    info - Display information of the current Telegram chat.
    chat - Generate a chat head.
    extra - Access additional features from Slave Channels.
    update_info - Update info of linked Telegram group.
    react - Send a reaction to a message, or show a list of reactors.
    rm - Remove a message from its remote chat.

.. note::

    In case of multiple admins are assigned, they may all send message on
    your behalf, but only the 0th admin can receive direct message from
    the bot.

``/link``: Link a chat
~~~~~~~~~~~~~~~~~~~~~~

1. Create a new group, invite your bot to the group
2. Send ``/link`` directly to the bot, then select your preferred slave
   chat.
3. Tap “Link” and select your new group.
   *You can also choose to unlink or relink a linked chat from this
   menu.*
4. Tap “Start” at the bottom of your screen, and you should see a
   success message: “Chat linked.”

.. note::

    You may introduce non-ETM admin users to the group, however, they:

    -  Can read all messages send from the related remote chat;
    -  May NOT send message on your behalf.

If the “Link” button doesn’t work for you, you may try the “Manual
Link/Relink” button. To manually link a remote chat:

1. Add the bot to the group you want to link to
2. Copy the code provided by the bot, and send it to the group.
3. If the group is linked successfully, you would receive a confirmation
   from the bot.

Also, you can send ``/unlink_all`` to a group to unlink all remote chats
from it.

Also, if you want to link a chat which you just used, you can simply reply
``/link`` quoting a previous message from that chat without choosing from
the long chat list.

Advanced feature: Filtering
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have just too many chats, and being too tired for keep tapping
``Next >``, or maybe you just want to find a way to filter out what
you’re looking for, now ETM has equipped ``/chat`` and ``/list`` with
filtering feature. Attach your keyword behind, and you can get a
filtered result.

E.g.: ``/chat Eana`` will give you all chats has the word “Eana”.

.. admonition:: Technical Details

    The filter query is in fact a regular expression matching. We used
    Python’s ``re.search`` with flags ``re.DOTALL | re.IGNORECASE`` in
    this case, i.e.: ``.`` matches everything including line breaks, and
    the query is NOT case-sensitive. Each comparison is done against a
    specially crafted string which allows you to filter multiple criteria.

::

    Channel: <Channel name>
    Channel ID: <Channel ID>
    Name: <Chat name>
    Alias: (<Chat Alias>|None)
    ID: <Chat Unique ID>
    Type: (Private|Group|System)
    Mode: [Linked]
    Description: <Description>
    Notification: (ALL|MENTION|NONE)
    Other: <Python Dictionary String>


.. note::

    Type can be either “User” or “Group”

    Other is the vendor specific information provided by slave channels.
    Format of such information is specified in their documentations
    respectively.

Examples:

-  Look for all WeChat groups: ``Channel: WeChat.*Type: Group``
-  Look for everyone who has no alias (and those with an alias called “None”): ``Alias: None``
-  Look for all entries contain “John” and “Johnny” in any order:
   ``(?=.*John)(?=.*Johnny)``

Send a message
~~~~~~~~~~~~~~

Send to a linked chat
^^^^^^^^^^^^^^^^^^^^^

You can send message as you do in a normal Telegram chat.

What is supported:

-  Send/forward message in all supported types
-  Quote-reply to a message
-  Send message with inline bot in supported types

What is NOT supported:

-  @ reference
-  Markdown/HTML formatting
-  Inline buttons
-  Messages with unsupported types.

.. note::

    This only applies to Telegram groups that are linked to a single remote
    chat, groups that are linked with multiple remote chats shall work in the
    same way as non-linked chats.

Send to a non-linked chat
^^^^^^^^^^^^^^^^^^^^^^^^^

To send a message to a non-linked chat, you should “quote-reply” to a
message or a “chat head” that is sent from your recipient. Those
messages should appear only in the bot conversation.

In a non-linked chat, quote-reply will not be passed on to the remote
channel, everything else is supported as it does in a linked chat.

Quick reply in non-linked chats
'''''''''''''''''''''''''''''''
ETM provides a mechanism that allow you to keep sending messages to the same
recipient without quoting every single time. ETM will store the remote chat you
sent a message to in every Telegram chat (i.e. a Telegram group or the bot),
which is known as the “last known recipient” of the Telegram chat.

In case where recipient is not indicated for a message, ETM will try to deliver
it to the “last known recipient” in the Telegram chat only if:

1. your last message with the “last known recipient” is with in an hour, and
2. the last message in this Telegram chat is from the “last known recipient”.


Edit and delete message
^^^^^^^^^^^^^^^^^^^^^^^

In EFB v2, the framework added support to message editing and removal,
and so does ETM. However, due to the limitation of Telegram Bot API,
although you may have selected “Delete for the bot”, or “Delete for
everyone” while deleting messages, the bot would **not** know anything 
about it. Therefore, if you want your message to be removed from a 
remote chat, edit your message and prepend it with ``rm``` 
(it’s ``R``, ``M``, and ``~```, not single quote), so that the bot knows 
that you want to delete the message.

Alternatively, you can also reply ``/rm`` to a message to remove it from its
remote chat. This can be useful when you cannot edit the message directly
(sticker, location, etc.), or when the message is not sent via ETM.

Please also notice that some slave channels may not support editing and/or
deleting messages depends on their implementations.

``/chat``: Chat head
^^^^^^^^^^^^^^^^^^^^

If you want to send a message to a non-linked chat which has not yet
sent you a message, you can ask ETM to generate a “chat head”. Chat head
works similarly to an incoming message, you can reply to it to send
messages to your recipient.

Send ``/chat`` to the bot, and choose a chat from the list. When you see
“Reply to this message to chat with ...”, it’s ready to go.

Advanced feature: Filtering
'''''''''''''''''''''''''''

Filter is also available in ``/chat`` command. Please refer to the
same chapter above, under ``/link`` for details.


``/extra``: External commands from slave channels (“additional features”)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some slave channels may provide commands that allows you to remotely
control those accounts, and achieve extra functionality, those commands
are called “additional features”. To view the list of available extra
functions, send ``/extra`` to the bot, you will receive a list of
commands available.

Those commands are named like “\ ``/<number>_<command_name>``\ ”, and can be
called like an CLI utility. (of course, advanced features like
piping etc would not be supported)


``/update_info``: Update details of linked Telegram group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ETM can help you to update the name and profile picture of a group to
match with appearance in the remote chat. This will also add a list of
current members to the Telegram group description if the remote chat is
a group.

This functionality is available when:

* This command is sent to a group
* The bot is an admin of the group
* The group is linked to **exactly** one remote chat
* The remote chat is accessible

Profile picture will not be set if it’s not available from the slave
channel.

``/react``: Send reactions to a message or show a list of reactors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reply ``/react`` to a message to show a list of chat members who
have reacted to the message and what their reactions are.

Reply ``/react`` followed by an emoji to react to this message, e.g.
``/react 👍``. Send ``/react -`` to remove your reaction.

Note that some slave channels may not accept message reactions, and
some channels have a limited reactions you can send with. Usually
when you send an unaccepted reaction, slave channels can provide
a list of suggested reactions you may want to try instead.

``/rm``: Delete a message from its remote chat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can reply ``/rm`` to a message to remove it from its remote chat.
Comparing to prepending ``rm``` to a message, you can use this command
even when you cannot edit the message directly (sticker, location, 
etc.), or when the message is not sent via ETM. It can also allow you
to remove messages sent by others if provided by the slave channel. 

Please notice that some slave channels may not support removing messages 
depends on their implementations.


Telegram Channel support
~~~~~~~~~~~~~~~~~~~~~~~~

ETM supports linking remote chats to Telegram Channels with partial
support.

The bot can:

-  Link one or more remote chats to a Telegram Channel
-  Check and manage link status of the channel
-  Update channel title and profile pictures accordingly

It cannot:

-  Process messages sent by you or others to the channel
-  Accept commands in the channel

Currently the following commands are supported in channels:

-  ``/start`` for manual chat linking
-  ``/link`` to manage chats linked to the channel
-  ``/info`` to show information of the channel
-  ``/update_info`` to update the channel title and picture

How to use:

1. Add the bot as an administrator of the channel
2. Send commands to the channel
3. Forward the command message to the bot privately

.. admonition:: Technical Details

    Telegram Bot API prevents bot from knowing who actually sent a message
    in a channel (not including signatures as that doesn't reflect the numeric
    ID of the sender). In fact, that is the same for normal users in a channel
    too, even admins.

    If messages from channels are to be processed unconditionally, not only
    that other admins in existing channels can add malicious admins to it,
    anyone on Telegram, once knows your bot username, can add it to a channel
    and use the bot on your behalf. Thus, we think that it is not safe to
    process messages directly from a channel.

Limitations
-----------

Due to the technical constraints of both Telegram Bot API and EH Forwarder
Bot framework, ETM has the following limitations:

- Some Telegram message types are **not** supported:
    - Game messages
    - Invoice messages
    - Payment messages
    - Passport messages
    - Vote messages
- ETM cannot process any message from another Telegram bot.
- Some components in Telegram messages are dropped:
    - Original author and signature of forwarded messages
    - Formats, links and link previews
    - Buttons attached to messages
    - Details about inline bot used on messages
- Some components in messages from slave channels are dropped:
    - @ references not referring to you.
- The Telegram bot can only
    - send you any file up to 50 MB,
    - receive file from you up to 20 MB.


Experimental flags
------------------

The following flags are experimental features, may change, break, or
disappear at any time. Use at your own risk.

Flags can be enabled in the ``flags`` key of the configuration file,
e.g.:

.. code:: yaml

    flags:
        flag_name: flag_value

-  ``chats_per_page`` *(int)* [Default: ``10``]

   Number of chats shown in when choosing for ``/chat`` and ``/link``
   command. An overly large value may lead to malfunction of such
   commands.

-  ``network_error_prompt_interval`` *(int)* [Default: ``100``]

   Notify the user about network error every ``n`` errors received. Set
   to 0 to disable it.

-  ``multiple_slave_chats`` *(bool)* [Default: ``true``]

   Link more than one remote chat to one Telegram group. Send and reply
   as you do with an unlinked chat. Disable to link remote chats and
   Telegram group one-to-one.

-  ``prevent_message_removal`` *(bool)* [Default: ``true``]

   When a slave channel requires to remove a message, EFB will ignore
   the request if this value is ``true``.

-  ``auto_locale`` *(str)* [Default: ``true``]

   Detect the locale from admins’ messages automatically. Locale
   defined in environment variables will be used otherwise.

-   ``retry_on_error`` *(bool)* [Default: ``false``]

    Retry infinitely when an error occurred while sending request
    to Telegram Bot API. Note that this may lead to repetitive
    message delivery, as the respond of Telegram Bot API is
    not reliable, and may not reflect the actual result.

-   ``send_image_as_file`` *(bool)* [Default: ``false``]

    Send all image messages as files, in order to prevent Telegram’s
    image compression in an aggressive way.

-   ``message_muted_on_slave`` *(str)* [Default: ``normal``]

    Behavior when a message received is muted on slave channel platform.

    - ``normal``: send to Telegram as normal message
    - ``silent``: send to Telegram as normal message, but without notification
      sound
    - ``mute``: do not send to Telegram

-   ``your_message_on_slave`` *(str)* [Default: ``silent``]

    Behavior when a message received is from you on slave channel platform.
    This overrides settings from ``message_muted_on_slave``.

    - ``normal``: send to Telegram as normal message
    - ``silent``: send to Telegram as normal message, but without notification
      sound
    - ``mute``: do not send to Telegram

-   ``animated_stickers`` *(bool)* [Default: ``false``]

    Enable experimental support to animated stickers. Note: you need to
    install binary dependency ``libcairo`` on your own, and additional
    Python dependencies via ``pip3 install "efb-telegram-master[tgs]"``
    to enable this feature.

-   ``send_to_last_chat`` *(str)* [Default: ``warn``]

    Enable quick reply in non-linked chats.

    - ``enabled``: Enable this feature without warning.
    - ``warn``: Enable this feature and issue warnings every time when you
      switch a recipient with quick reply.
    - ``disabled``: Disable this feature.

-   ``default_media_prompt`` *(str)* [Default: ``emoji``]

    Placeholder text when the a picture/video/file message has no caption.

    - ``emoji``: Use emoji like 🖼️, 🎥, and 📄.
    - ``text``: Use text like “Sent a picture/video/file”.
    - ``disabled``: Use empty placeholders.

-   ``api_base_url`` *(str)* [Default: ``null``]

    Base URL of the Telegram Bot API.
    Defaulted to ``https://api.telegram.org/bot``.

-   ``api_base_file_url`` *(str)* [Default: ``null``]

    Base file URL of the Telegram Bot API.
    Defaulted to ``https://api.telegram.org/file/bot``.

-   ``local_tdlib_api`` *(bool)* [Default: ``false``]

    Enable this option if the bot API is running in ``--local`` mode and
    is using the same file system with ETM.

Network configuration: timeout tweaks
-------------------------------------

   This chapter is adapted from `Python Telegram Bot wiki`__, licensed
   under CC-BY 3.0.

__ https://github.com/python-telegram-bot/python-telegram-bot/wiki/Handling-network-errors#tweaking-ptb

``python-telegram-bot`` performs HTTPS requests using ``urllib3``.
``urllib3`` provides control over ``connect_timeout`` & ``read_timeout``.
``urllib3`` does not separate between what would be considered read &
write timeout, so ``read_timeout`` serves for both. The defaults chosen
for each of these parameters is 5 seconds.

The ``connect_timeout`` value controls the timeout for establishing a
connection to the Telegram server(s).

Changing the defaults of ``read_timeout`` & ``connect_timeout`` can be
done by adjusting values ``request_kwargs`` section in ETM’s
``config.yaml``.

.. code:: yaml

   # ...
   request_kwargs:
       read_timeout: 6
       connect_timeout: 7

Run ETM behind a proxy
----------------------

   This chapter is adapted from `Python Telegram Bot
   wiki`__, licensed under CC-BY 3.0.

__ https://github.com/python-telegram-bot/python-telegram-bot/wiki/Working-Behind-a-Proxy

You can appoint proxy specifically for ETM without affecting other
channels running in together in the same EFB instance. This can also be
done by adjusting values ``request_kwargs`` section in ETM’s
``config.yaml``.

HTTP proxy server
~~~~~~~~~~~~~~~~~

.. code:: yaml

   request_kwargs:
       # ...
       proxy_url: http://PROXY_HOST:PROXY_PORT/
       # Optional, if you need authentication:
       username: PROXY_USER
       password: PROXY_PASS

SOCKS5 proxy server
~~~~~~~~~~~~~~~~~~~

This is configuration is supported, but requires an optional/extra
python package. To install:

.. code:: shell

   pip install python-telegram-bot[socks]

.. code:: yaml

   request_kwargs:
       # ...
       proxy_url: socks5://URL_OF_THE_PROXY_SERVER:PROXY_PORT
       # Optional, if you need authentication:
       urllib3_proxy_kwargs:
           username: PROXY_USER
           password: PROXY_PASS

RPC interface
-------------

A standard `Python XML RPC server`__ is implemented in ETM 2. It can be
enabled by adding a ``rpc`` section in ETM’s ``config.yml`` file.

__ https://docs.python.org/3/library/xmlrpc.html

.. code:: yaml

   rpc:
       server: 127.0.0.1
       port: 8000

..

.. warning::
   The ``xmlrpc`` module is not secure against maliciously
   constructed data. Do not expose the interface to untrusted parties or
   the public internet, and turn off after use.

Exposed functions
~~~~~~~~~~~~~~~~~

Functions in `the db (database manager) class`_ and
`the RPCUtilities class`_ are exposed. Refer to the source code
for their documentations.

How to use
~~~~~~~~~~

Set up a ``SimpleXMLRPCClient`` in any Python script and call any of the
exposed functions directly. For details, please consult `Python
documentation on xmlrpc`__.

__ https://docs.python.org/3/library/xmlrpc.html

.. _the db (database manager) class: https://etm.1a23.studio/blob/master/efb_telegram_master/db.py
.. _the RPCUtilities class: https://etm.1a23.studio/blob/master/efb_telegram_master/rpc_utilities.py

Setup Webhook
-------------

For details on how to setup a webhook, please visit this `wiki article`_.

.. _wiki article: https://github.com/ehForwarderBot/efb-telegram-master/wiki/Setup-Webhook

License
-------

ETM is licensed under `GNU Affero General Public License 3.0`_ or later versions::

    EFB Telegram Master Channel: A master channel for EH Forwarder Bot.
    Copyright (C) 2016 - 2020 Eana Hufwe, and the EFB Telegram Master Channel contributors
    All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _GNU Affero General Public License 3.0: https://www.gnu.org/licenses/agpl-3.0.txt

Translation support
-------------------

ETM supports translated user interface with the help of community.
The bot detects languages of Telegram Client of the admins
from their messages, and automatically matches with a supported
language on the go. Otherwise, you can set your language by
turning off the ``auto_locale`` feature, and then setting
the locale environmental variable (``LANGUAGE``,
``LC_ALL``, ``LC_MESSAGES`` or ``LANG``) to one of our
supported languages. Meanwhile, you can help to translate
this project into your languages on `our Crowdin page`_.

.. _our Crowdin page: https://crowdin.com/project/ehforwarderbot/

.. note::

    If your are installing from source code, you will not get translations
    of the user interface without manual compile of message catalogs (``.mo``)
    prior to installation.
