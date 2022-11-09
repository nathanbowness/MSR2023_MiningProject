Navigate to `db1` on the WoC servers. From there you can type `mongo` into the command line to get access to there database.
Next please type in `use WoC` to access the correct database. You can them use any of the following commands. 


Query projects that have the following properties, and return the first result:
* greater than 200 commits
* greater than 20 contributors
* greater than 30 files that are java
* `library` in the project name
```
db.P_metadata.U.findOne({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Java":{$gt:30}} ]})
```

Query projects that have the following properties, and return the first result:
* greater than 200 commits
* greater than 20 contributors
* greater than 30 files that are python
* `library` in the project name
```
db.P_metadata.U.findOne({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:30}} ]})
```

Return the total number of entries in the database for the query:
```
db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:30}} ]})
```



# Results from Various MongoDB Tests on WoC

```
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:30}} ]})
49
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Java":{$gt:30}} ]})
69
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:10}} ]})
71
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:5}}, {"FileInfo.Python":{$gt:10}} ]})
164
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {CommunitySize:{$gt:5}}, {"FileInfo.Python":{$gt:10}} ]})
100
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:100}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:3}}, {"FileInfo.Python":{$gt:5}} ]})
345
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:100}}, {NumAuthors:{$gt:3}}, {"FileInfo.Python":{$gt:5}} ]})
278443
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:10}} ]})
41684
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {NumAuthors:{$gt:30}}, {"FileInfo.Python":{$gt:10}} ]})
29205
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {NumAuthors:{$gt:50}}, {"FileInfo.Python":{$gt:10}} ]})
18166
mongos> db.P_metadata.U.count({$and: [{NumCommits:{$gt:200}}, {NumAuthors:{$gt:100}}, {"FileInfo.Python":{$gt:10}} ]})
9245
```