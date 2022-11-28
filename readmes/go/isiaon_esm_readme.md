# An Elasticsearch Migration Tool

Elasticsearch cross version data migration.

[Dec 3rd, 2020: [EN] Cross version Elasticsearch data migration with ESM](https://discuss.elastic.co/t/dec-3rd-2020-en-cross-version-elasticsearch-data-migration-with-esm/256516)

## Features:

*  Cross version migration supported
*  Overwrite index name
*  Copy index settings and mapping
*  Support http basic auth
*  Support dump index to local file
*  Support loading index from local file
*  Support http proxy
*  Support sliced scroll ( elasticsearch 5.0 +)
*  Support run in background
*  Generate testing data by randomize the source document id
*  Support rename filed name
*  Support unify document type name
*  Support specify which _source fields to return from source
*  Support specify query string query to filter the data source
*  Support rename source fields while do bulk indexing
*  Load generating with 

## ESM is fast!

A 3 nodes cluster(3 * c5d.4xlarge， 16C，32GB，10Gbps)

```
root@ip-172-31-13-181:/tmp# ./esm -s https://localhost:8000 -d https://localhost:8000 -x logs1kw -y logs122 -m elastic:medcl123 -n elastic:medcl123 -w 40 --sliced_scroll_size=60 -b 5 --buffer_count=2000000  --regenerate_id
[12-19 06:31:20] [INF] [main.go:506,main] start data migration..
Scroll 10064570 / 10064570 [=================================================] 100.00% 55s
Bulk 10062602 / 10064570 [==================================================]  99.98% 55s
[12-19 06:32:15] [INF] [main.go:537,main] data migration finished.
```
Migrated 10,000,000 documents within a minute, Nginx log generated from kibana_sample_data_logs.


## Example:

copy index `index_name` from `192.168.1.x` to `192.168.1.y:9200`

```
./bin/esm  -s http://192.168.1.x:9200   -d http://192.168.1.y:9200 -x index_name  -w=5 -b=10 -c 10000
```

copy index `src_index` from `192.168.1.x` to `192.168.1.y:9200` and save with `dest_index`

```
./bin/esm -s http://localhost:9200 -d http://localhost:9200 -x src_index -y dest_index -w=5 -b=100
```

support Basic-Auth
```
./bin/esm -s http://localhost:9200 -x "src_index" -y "dest_index"  -d http://localhost:9201 -n admin:111111
```

copy settings and override shard size
```
./bin/esm -s http://localhost:9200 -x "src_index" -y "dest_index"  -d http://localhost:9201 -m admin:111111 -c 10000 --shards=50  --copy_settings

```

copy settings and mapping, recreate target index, add query to source fetch, refresh after migration
```
./bin/esm -s http://localhost:9200 -x "src_index" -q=query:phone -y "dest_index"  -d http://localhost:9201  -c 10000 --shards=5  --copy_settings --copy_mappings --force  --refresh

```

dump elasticsearch documents into local file
```
./bin/esm -s http://localhost:9200 -x "src_index"  -m admin:111111 -c 5000 -q=query:mixer  --refresh -o=dump.bin 
```

loading data from dump files, bulk insert to another es instance
```
./bin/esm -d http://localhost:9200 -y "dest_index"   -n admin:111111 -c 5000 -b 5 --refresh -i=dump.bin
```

support proxy
```
 ./bin/esm -d http://123345.ap-northeast-1.aws.found.io:9200 -y "dest_index"   -n admin:111111  -c 5000 -b 1 --refresh  -i dump.bin  --dest_proxy=http://127.0.0.1:9743
```

use sliced scroll(only available in elasticsearch v5) to speed scroll, and update shard number
```
 ./bin/esm -s=http://192.168.3.206:9200 -d=http://localhost:9200 -n=elastic:changeme -f --copy_settings --copy_mappings -x=bestbuykaggle  --sliced_scroll_size=5 --shards=50 --refresh
```

migrate 5.x to 6.x and unify all the types to `doc`
```
./esm -s http://source_es:9200 -x "source_index*"  -u "doc" -w 10 -b 10 - -t "10m" -d https://target_es:9200 -m elastic:passwd -n elastic:passwd -c 5000 

```

to migrate version 7.x and you may need to rename `_type` to `_doc`
```
./esm -s http://localhost:9201 -x "source" -y "target"  -d https://localhost:9200 --rename="_type:type,age:myage"  -u"_doc"

```

filter migration with range query

```
./esm -s https://192.168.3.98:9200 -m elastic:password -o json.out -x kibana_sample_data_ecommerce -q "order_date:[2020-02-01T21:59:02+00:00 TO 2020-03-01T21:59:02+00:00]"

```

generate testing data, if `input.json` contains 10 documents, the follow command will ingest 100 documents, good for testing
```
./bin/esm -i input.json -d  http://localhost:9201 -y target-index1  --regenerate_id  --repeat_times=10 
```

select source fields

```
 ./bin/esm -s http://localhost:9201 -x my_index -o dump.json --fields=author,title
```

rename fields while do bulk indexing

```
./bin/esm -i dump.json -d  http://localhost:9201 -y target-index41  --rename=title:newtitle
```

user buffer_count to control memory used by ESM， and use gzip to compress network traffic
```
./esm -s https://localhost:8000 -d https://localhost:8000 -x logs1kw -y logs122 -m elastic:medcl123 -n elastic:medcl123 --regenerate_id -w 20 --sliced_scroll_size=60 -b 5 --buffer_count=1000000 --compress false 
```

## Download
https://github.com/medcl/esm/releases


## Compile:
if download version is not fill you environment,you may try to compile it yourself. `go` required.

`make build`
* go version >= 1.7

## Options

```
Usage:
  esm [OPTIONS]

Application Options:
  -s, --source=                    source elasticsearch instance, ie: http://localhost:9200
  -q, --query=                     query against source elasticsearch instance, filter data before migrate, ie: name:medcl
  -d, --dest=                      destination elasticsearch instance, ie: http://localhost:9201
  -m, --source_auth=               basic auth of source elasticsearch instance, ie: user:pass
  -n, --dest_auth=                 basic auth of target elasticsearch instance, ie: user:pass
  -c, --count=                     number of documents at a time: ie "size" in the scroll request (10000)
      --buffer_count=              number of buffered documents in memory (100000)
  -w, --workers=                   concurrency number for bulk workers (1)
  -b, --bulk_size=                 bulk size in MB (5)
  -t, --time=                      scroll time (1m)
      --sliced_scroll_size=        size of sliced scroll, to make it work, the size should be > 1 (1)
  -f, --force                      delete destination index before copying
  -a, --all                        copy indexes starting with . and _
      --copy_settings              copy index settings from source
      --copy_mappings              copy index mappings from source
      --shards=                    set a number of shards on newly created indexes
  -x, --src_indexes=               indexes name to copy,support regex and comma separated list (_all)
  -y, --dest_index=                indexes name to save, allow only one indexname, original indexname will be used if not specified
  -u, --type_override=             override type name
      --green                      wait for both hosts cluster status to be green before dump. otherwise yellow is okay
  -v, --log=                       setting log level,options:trace,debug,info,warn,error (INFO)
  -o, --output_file=               output documents of source index into local file
  -i, --input_file=                indexing from local dump file
      --input_file_type=           the data type of input file, options: dump, json_line, json_array, log_line (dump)
      --source_proxy=              set proxy to source http connections, ie: http://127.0.0.1:8080
      --dest_proxy=                set proxy to target http connections, ie: http://127.0.0.1:8080
      --refresh                    refresh after migration finished
      --fields=                    filter source fields, comma separated, ie: col1,col2,col3,...
      --rename=                    rename source fields, comma separated, ie: _type:type, name:myname
  -l, --logstash_endpoint=         target logstash tcp endpoint, ie: 127.0.0.1:5055
      --secured_logstash_endpoint  target logstash tcp endpoint was secured by TLS
      --repeat_times=              repeat the data from source N times to dest output, use align with parameter regenerate_id to amplify the data size
  -r, --regenerate_id              regenerate id for documents, this will override the exist document id in data source
      --compress                   use gzip to compress traffic
  -p, --sleep=                     sleep N seconds after finished a bulk request (-1)

Help Options:
  -h, --help                       Show this help message


```

## FAQ

- Scroll ID too long, update `elasticsearch.yml` on source cluster.

```
http.max_header_size: 16k
http.max_initial_line_length: 8k
```

Versions
--------

From       | To
-----------|-----------
1.x | 1.x
1.x | 2.x
1.x | 5.x
1.x | 6.x
1.x | 7.x
2.x | 1.x
2.x | 2.x
2.x | 5.x
2.x | 6.x
2.x | 7.x
5.x | 1.x
5.x | 2.x
5.x | 5.x
5.x | 6.x
5.x | 7.x
6.x | 1.x
6.x | 2.x
6.x | 5.0
6.x | 6.x
6.x | 7.x
7.x | 1.x
7.x | 2.x
7.x | 5.x
7.x | 6.x
7.x | 7.x

