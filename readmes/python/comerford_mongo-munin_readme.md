
Munin Plugins for MongoDB
============

Plugins
----------
* mongo_ops   : operations/second
* mongo_mem   : mapped, virtual and resident memory usage
* mongo_btree : btree access/misses/etc...
* mongo_conn  : current connections
* mongo_lock  : write lock info
* mongo_docs  : number of documents (inserted, updated...)

Requirements
-----------
* MongoDB 2.4+
* python/pymongo


## Install Requirements (choose one)

#### Ubuntu

Install pymongo:

    sudo apt-get install pip
    sudo apt-get install build-essential python-dev
    sudo pip install pymongo


#### Red Hat and Cent OS

Enable the EPEL Repository:

    sudo yum -y install epel-release
    
Install pymongo:

    sudo yum install pymongo


## Install plugins

    git clone https://github.com/comerford/mongo-munin.git /tmp/mongo-munin
    sudo cp /tmp/mongo-munin/mongo_* /usr/share/munin/plugins
    sudo ln -sf /usr/share/munin/plugins/mongo_btree /etc/munin/plugins/mongo_btree
    sudo ln -sf /usr/share/munin/plugins/mongo_conn /etc/munin/plugins/mongo_conn
    sudo ln -sf /usr/share/munin/plugins/mongo_lock /etc/munin/plugins/mongo_lock
    sudo ln -sf /usr/share/munin/plugins/mongo_mem /etc/munin/plugins/mongo_mem
    sudo ln -sf /usr/share/munin/plugins/mongo_ops /etc/munin/plugins/mongo_ops
    sudo ln -sf /usr/share/munin/plugins/mongo_docs /etc/munin/plugins/mongo_docs
    sudo ln -sf /usr/share/munin/plugins/mongo_collections /etc/munin/plugins/mongo_collections
    sudo ln -sf /usr/share/munin/plugins/mongo_page_faults /etc/munin/plugins/mongo_page_faults    
    sudo chmod +x /usr/share/munin/plugins/mongo_*
    sudo service munin-node restart

Check if plugins are running:

    munin-node-configure | grep "mongo_"

Test plugin output:

    munin-run mongo_ops

### Configuration


**how to configure custom db connection**

munin-node can set env value in below file:

`/etc/munin/plugin-conf.d/munin-node`

    [mongo_*]
    env.MONGO_DB_URI mongodb://user:password@host:port/dbname

