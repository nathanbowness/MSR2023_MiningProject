[![build status](https://travis-ci.org/MatthiasKauer/croncoat.png?branch=master)](https://travis-ci.org/MatthiasKauer/croncoat)

croncoat
========

croncoat extends [cronwrap](https://github.com/Doist/cronwrap), a cron job wrapper that wraps jobs and enables better error reporting and command timeouts.
Major differences between the two are:

* croncoat relies on python email and smtplib libraries (configuration easier if system mailer not setup yet); cronwrap uses the system mailer ```mail``` (configuration more invovled, but maybe already done).
(Note: I started here because I wanted to alter the email from address and the syntax for command-line mail differed between different Linux flavors that I tested.)
* croncoat kills commands if they take longer than the allotted timeout; cronwrap waits (potentially forever) and alerts only a posteriori. **croncoat thus calls commands without full shell.** Some commands may therefore not work although I'm currently only aware of non-relevant examples like ```croncoat -c 'exit(1)'```
* Subject line have been improved to be more helpful in croncoat and there are some other minor formatting improvements.
* Cronwrap is running reliably for many (I suppose) people for many years. Croncoat is new and must be observed more carefully.

Known Issues
===========

* Choosing small times (e.g. -t 3s) won't work b/c the alarm signal will trigger while the smtp server is still being contacted.
* stdout is currently not captured if the command is killed due to timeout.

Installing
===========
**Read path issues below for use in crontab!**

### Pypi
croncoat is on PyPI: https://pypi.python.org/pypi/croncoat

Install via:
```
pip install croncoat
```

### Git installation
To install the bleeding-edge version :

    $ git clone <this repo>
    $ sudo python setup.py install

### Path issues in crontab
WARNING: On my system croncoat wasn't in the shorter path that cron uses during execution. This is very confusing b/c everything works outside cron, but once that comes into play nothing runs anymore. You need to add a line like the following to crontab before the scripts you want to execute.

```
PATH=/usr/local/bin:/usr/bin:/bin
```

Alternatively, you can prefix ```/usr/local/bin/croncoat``` instead of just ```croncoat``` in crontab of course.

Example usage
===========

```
usage: croncoat [-h] [-c CMD] [-e EMAILS] [-t TIME] [--print-ini [PRINT_INI]]
                [--config CONFIG] [-v [VERBOSE]]

Wrap cron jobs for better error email error reporting with command timeouts.
Version 0.3
You must create a config file (~/.croncoat.ini by default) to store smtp server data.
Ideally this would be readable only by you.
To output a config skeleton, use croncoat --print-ini

Usage examples:
===============
Send test email:
croncoat -e test@domain.org

Send email after killing a script that takes longer than 5s
croncoat -t 5s -c 'sleep 10s' -e test@domain.org

Print to stdout after catching error in script;
Note: this won't work with exit(1) b/c no real shell here
croncoat -c 'python -c import sys; sys.exit(1)'

Print no output for successful command
croncoat -c 'ls -la'
Print output of successful command
croncoat -v -c 'ls -la'

optional arguments:
  -h, --help            show this help message and exit
  -c CMD, --cmd CMD     Run a command. Could be `croncoat -c "ls -la"`. No command => test email is sent.
  -e EMAILS, --emails EMAILS
                        Send email to the following addresses if the command crashes or exceeds timeout. Uses Python's email library to send emails (therefore no user namesunlike original cronwrap). If this is not set, only output to stdout.
  -t TIME, --time TIME  Set the maximum running time. If this time is reached, the script will be killed and an alert email will be sent. If the script is killed stdout/stderr cannot be captured at this time! The default is 1 hour `-t 1h`. Possible values include: `-t 2h`,`-t 5m`, `-t 30s`.
  --print-ini [PRINT_INI], --print-config [PRINT_INI]
                        Print the configuration file format. This can be redirected to a file name to have a config skeleton.
  --config CONFIG, --ini CONFIG, -i CONFIG
                        use an .ini file with custom name and path  (not the default .croncoat.ini in users' home directory
  -v [VERBOSE], --verbose [VERBOSE]
                        Will send an email / print to stdout even on successful run.
```

Development tips
=============

## Virtualenv setup
Create virtual environment w/o site-packages. We don't need "complicated" packages for this project.
```
virtualenv --no-site-packages venv  #only required once; excluding site packages is default now mostly
source venv/bin/activate    #activate venv
which pip   #double-check
pip install -r requirements.txt  # install required packages
```

## Running tests
```
py.test croncoat
cram test-cram
```
