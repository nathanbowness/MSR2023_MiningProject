Navigate to `db1` on the WoC servers. From there you can type `mongo` into the command line to get access to there database.
Next please type in `use WoC` to access the correct database. You can them use any of the following commands. 


Query to projects that have the following poperties:
* greater than 200 commits
* greater than 20 contributors
* greater than 30 files that are java
* `library` in the project name
```
db.P_metadata.U.findOne({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Java":{$gt:30}} ]})
```

Query projects that have the following properties:
* greater than 200 commits
* greater than 20 contributors
* greater than 30 files that are python
* `library` in the project name
```
db.P_metadata.U.findOne({$and: [{NumCommits:{$gt:200}}, {ProjectID:{$regex:"library"}}, {NumAuthors:{$gt:20}}, {"FileInfo.Python":{$gt:30}} ]})
```