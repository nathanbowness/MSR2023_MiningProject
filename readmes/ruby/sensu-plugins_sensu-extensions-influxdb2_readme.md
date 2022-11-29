__NOTE:__ running `sensu-install -e sensu-extensions-influxdb` will __NOT__ install this extension, as a project with the same name already exists on Rubygems.org. Before reporting any issues here, make sure you are using this version of the extension. (_hint:_ check the version number on the logs) In order to install this extension, run `sensu-install -e sensu-extensions-influxdb2`.

# Requirements

This extension uses InfluxDB [Line Protocol](https://influxdb.com/docs/v0.9/write_protocols/line.html) over HTTP to send metrics.

Since Sensu already uses [eventmachine](https://github.com/eventmachine/eventmachine), you just have to ensure that em-http-request gem is present inside Sensu's embedded Ruby :
* `em-http-request` ruby gem

By default, this extension uses in memory metrics caching : it makes InfluxDB writes batched.
This cache is flushed every __500 items__ or __6 seconds__ (this values can be changed in conf).

## Caveat
* SSL/TLS connection to InfluxDB is still broken in Sensu `0.20.6`. We're waiting for a Ruby / EM upgrade in Sensu project :
    * https://github.com/sensu/sensu/issues/1084

# Usage
The configuration options are pretty straight forward.

Metrics are inserted into the database using the check's key name as _measurement_ name. So if you're using the `sensu-plugins-load-checks` community plugin :
```
my-host-01.load_avg.one 0.02 1444824197
my-host-01.load_avg.five 0.04 1444824197
my-host-01.load_avg.fifteen 0.09 1444824197
```
In this example, you'll have 3 differents _measurements_ in your database :
```
> show measurements
name: measurements
------------------
name
my-host-01.load_avg.fifteen
my-host-01.load_avg.five
my-host-01.load_avg.one
```

```
> select * from "my-host-01.load_avg.one";
name: my-host-01.load_avg.one
------------------
time                  host        value  duration
2015-10-14T13:53:22Z  my-host-01  0.34   0.399
2015-10-14T13:53:32Z  my-host-01  0.29   0.419
2015-10-14T13:53:42Z  my-host-01  0.39   0.392
2015-10-14T13:53:52Z  my-host-01  0.41   0.398
[...]
```

Additionally a `duration` value will be present based on the time it took the check to run (this is gleaned from the sensu event data).

The name of the _measurement_ is based on the value of `strip_metric` and/or a template, as described below.
The name of the key ```host``` is grabbed from sensu event client name.

## Extension not a handler
Note that the first push of this was a handler that could be called via `pipe`. This is now an actual extension that's more performant since it's actually in the sensu-server runtime. Additionally it's now using batch submission to InfluxDB by writing all the points for a given series at once.

To [load the extension](https://sensuapp.org/docs/latest/reference/extensions.html), you will need to install the gem into the sensu ruby, and then add the following config file
```json
{
  "extensions": {
    "influxdb": {
      "gem": "sensu-extensions-influxdb2"
    },
    "history": {
      "gem": "sensu-extensions-history"
    }
  }
}
```

**NOTE**: Even though this gem is called `sensu-extensions-influxdb`, the way sensu loads the extension is by parsing the name of the gem, and loading the library. This is why we have to specify `sensu-extensions-history`, even though that gem doesn't exist.

Create a set to wrap this extension into a callable handler. In this example, we created a ```metrics``` handler wrapping a debug output and this Influx extension :

_/etc/sensu/conf.d/handlers/metrics.json_ :
```json
{
  "handlers": {
    "metrics": {
      "type": "set",
      "handlers": [
        "debug",
        "influxdb"
      ]
    }
  }
}
```

_Note :_ Since Sensu 0.17.1 you can also use extension name directly :
```
Check definitions can now specify a Sensu check extension to run,
"extension", instead of a command.
```

## Handler config

`/etc/sensu/conf.d/influxdb.json`
```json
{
  "influxdb": {
    "database": "stats",
    "host": "localhost",
    "port": "8086",
    "username": "stats",
    "password": "stats",
    "use_ssl": false,
    "strip_metric": "host",
    "tags": {
      "region": "my-dc-01",
      "stage": "prod"
    },
    "templates": [
      {"^sensu\\.checks\\..*": "source.measurement.field*"},
      {".*\\.cgroup\\..*": "host.path.component"}
    ]
  }
}
```

### Config attributes

* `host`, `port`, `username`, `password` and `database` are pretty straight forward. If `use_ssl` is set to true, the connection to the influxdb server will be made using https instead of http.

* `use_basic_auth` if your InfluxDB is behind a proxy that requires authentication you can set this to `true`, in that case you also have to define `basic_user` and `basic_pass`.

* `filters` allow's you to "find and replace" words/patterns in the key, it's a Hash where the key is a regex pattern and the value is a string that should replace it. (these are passed directly to the gsub method). Filters are applyed before any other transformations like templates.

* `templates` like with the InfluxDB Graphite plugin, you can specify patterns and formats, if the metric name matches the pattern, the template will be applied. Templates can be defined per check, in the check configuration, or globaly in the handler's configuration. Parts of the metric name will be converted into tags, reducing the measurement name in InfluxDB whilst keeping all the information as tags or fields.
You can specifty multiple templates, if your metric matches more than one the first one will be used.
For example, if you have a metric named:
```
  ip-10-0-1-32.host_stats.load_avg 3
```
You can set a template like:
```json
  "templates": {
    ".*\\.host_stats\\..*": "host.type"
  }
```
And as a result the following will be sent to InfluxDB:
```
  load_avg,host=ip-10-0-1-32,type=host_stats value=3
```
You can also use three special keywords in your templates, `void`, `measurement` and `field` and these can be used with a `*` at the end.
Example, considereing the following metrics:
```
  ip-10-0-1-32.host_stats.load_avg.one 3
  ip-10-0-1-32.host_stats.load_avg.five 9
  ip-10-0-1-32.host_stats.load_avg.fifteen 13
```
You could create a template like this:
```json
  "templates": {
    ".*\\.host_stats\\..*": "host.measurement.field*"
  }
```
And you would get:
```
  host_stats,host=ip-10-0-1-32 load_avg.one=3
  host_stats,host=ip-10-0-1-32 load_avg.five=9
  host_stats,host=ip-10-0-1-32 load_avg.fifteen=13
```
Or, a template like this:
```json
  "templates": {
    ".*\\.host_stats\\..*": "host.measurement.field.aggregation"
  }
```
Would get you:
```
  host_stats,host=ip-10-0-1-32,aggregation=one load_avg=3
  host_stats,host=ip-10-0-1-32,aggregation=five load_avg=9
  host_stats,host=ip-10-0-1-32,aggregation=fifteen load_avg=13
```
the `void` keyword will make the handler ignore that part of the metric name.

* `tags` hash is also pretty straight forward. Just list here in a flat-hash design as many influxdb tags you wish to be added in your measures. This can also be set both in the handler configuration or as part of the check configuration.

* `strip_metric` however might not be. This is used to "clean up" the data sent to influxdb. Normally everything sent to handlers is akin to the `graphite`/`stats` style:
```
  something.host.metrictype.foo.bar
```
or
```
  host.stats.something.foo.bar
```

Really the pattern is irrelevant. People have different tastes. Adding much of that data to the column name in InfluxDB is rather silly so `strip_metric` provides you with a chance to add a value that strips off everything up to (and including that value). This allows you to continue sending to graphite or statsd or whatever and still use this handler.

Using the examples above, if you set the `strip_metric` to `host`, then the measurement in InfluxDB would be called `metrictype.foo.bar` or `stats.something.foo.bar`. If you set the value to `foo` then the measurement would simply be called `foo`

Note that :
* `strip_metric` isn't required.
* `strip_metric` can be set either in the handler configuration or as part of the check configuration, check configuration takes precedence.
* you can cleanup an arbitrary string from your keyname or use `host` as special value to cleanup the sensu event client name from your key.

#### Other attributes

* `time_precision` : global checks time precision (default is `'s'`)
* `buffer_max_size` : buffer size limit before flush - This is the amount of points in the InfluxDB batch - (default is `500`)
* `buffer_max_age` : buffer maximum age - Flush will be forced after this amount of time - (default is `6` seconds)
* `Proxy mode` : If the extension is configured to be in proxy mode, it will skip the transformation step and assume that the data is valid [line protocol](https://docs.influxdata.com/influxdb/latest/write_protocols/line_protocol_reference). It will not take into account any tags defined in the sensu-configuration.
* `enhanced_history`: by default this extension writes checks history as separated measurements on InfluxDB. Setting this attribute to true will write all check history in the same metric (sensu.checks), tagging check name and subscriptions (if any), allowing the user to write InfluxDB queries filtering by check name and subscriptions.

## Check options

In the check config, an optional `influxdb` section can be added, containing a `database` option and `tags`.
You can also set `proxy_mode` in this section on the checks to override the default configuration set on the handler. This way checks that use the InfluxDB line protocol can coexsist with checks that use the Graphite format and use the same handler.
As mentioned above you can also specify `strip_metric`, `templates` and `filters`,  in the check configuration.
If specified, this overrides the default `database` and `strip_metric` options in the handler config and adds (or overrides) influxdb tags and templates.

This allows events to be written to different influxdb databases and modify key indexes on a check-by-check basis.

You can also specify the time precision of your check script in the check config with the `time_precision` attribute.

### Example check config

`/etc/sensu/conf.d/checks/metrics-load.json`
```json
{
  "checks": {
    "metrics-load": {
      "type": "metric",
      "command": "metrics-load.rb",
      "standalone": true,
      "handlers": [
        "metrics"
      ],
      "interval": 60,
      "time_precision": "s",
      "influxdb": {
        "database": "custom-db",
        "tags": {
           "stage": "prod",
           "region": "eu-west-1"
        },
        "templates": {
          "^load_avg\\..*": "measurement.field"
        }
      }
    }
  }
}
```

_Result_ :
```
load_avg,stage:prod,region:eu-west-1,host:iprint-test-sa-01.photobox.com one=1.04,duration=0.402  1444816792147
load_avg,stage:prod,region:eu-west-1,host:iprint-test-sa-01.photobox.com five=0.86,duration=0.398 1444816792147
load_avg,stage:prod,region:eu-west-1,host:iprint-test-sa-01.photobox.com fifteen=0.84,duration=0.375 1444816792147

 * will be sent to -> http://my-influx09.company.com:8086/db/custom-db/series?time_precision=s&u=sensu&p=sensu
```

Without the tags and templates you would get:
```
load_avg.one,host:iprint-test-sa-01.photobox.com value=1.04,duration=0.402  1444816792147
load_avg.five,host:iprint-test-sa-01.photobox.com value=0.86,duration=0.398 1444816792147
load_avg.fifteen,host:iprint-test-sa-01.photobox.com value=0.84,duration=0.375 1444816792147
```
