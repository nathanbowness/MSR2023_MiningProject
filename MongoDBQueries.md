Navigate to `db1` on the WoC servers. From there you can type `mongo` into the command line to get access to there database.
Next please type in `use WoC` to access the correct database. You can then play around with possible query combinations to your liking.

# Repoduction Package

## Criteria Used for Project Selection
- More than 150 commits
  - NumCommits:{$gt:150}
- More than 10 contributors have commited to the project
  - NumAuthors:{$gt:10}
- More than 10 files for the specific language being queried
  - "FileInfo.Python":{$gt:10}
- More than 20 stars
  - NumStars:{$gt:20}
- Do not include projects with files of the other languages being queried (no cross contamination). A combination of the following criteria would be used, always exluding the non active language:
  - {"FileInfo.Go": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Java": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}}
- The last commit was after Jan 1st, 2021
  - LatestCommitDate:{$gt:1609477200}
- The first commit was before Jan 1st, 2019. We have at least a 2 year lifecyle for the repository to ensure it was actively worked on for a period of time. This also lets us analyze the release cadence of a minimum of 2 years.
  - EarliestCommitDate:{$lt:1546318800000}

## Python
### Python Project Count Query
From within the mongo shell, using the WoC databse on da1. The following command was used to find the number of python projects that meet the criteria discussed above.
```
db.P_metadata.U.count({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Python":{$gt:10}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Java": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]})

--> 4663
```
### Python Project Details Collection
From outside of the mongo shell, but on da1. The following command was used to output python project details for the projects meeting the criteria discussed above. The following project details are output: ProjectID, NumStars, NumAuthors
```
mongo --quiet WoC --eval 'printjson(db.P_metadata.U.find({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Python":{$gt:10}}, {"FileInfo.Java": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]}, {ProjectID: 1, NumStars: 1, NumAuthors: 1}).toArray())' > python_projects.json
```

## Java
### Java Project Count Query
From within the mongo shell, using the WoC databse on da1. The following command was used to find the number of java projects that meet the criteria discussed above.
```
db.P_metadata.U.count({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Java":{$gt:10}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]})

--> 2358
```

### Java Project Details Collection
From outside of the mongo shell, but on da1. The following command was used to output java project details for the projects meeting the criteria discussed above. The following project details are output: ProjectID, NumStars, NumAuthors
```
mongo --quiet WoC --eval 'printjson(db.P_metadata.U.find({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Java":{$gt:10}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]}, {ProjectID: 1, NumStars: 1, NumAuthors: 1}).toArray())' > java_projects.json
```

## Ruby

### Ruby Project Count Query

From within the mongo shell, using the WoC databse on da1. The following command was used to find the number of ruby projects that meet the criteria discussed above.
```
db.P_metadata.U.count({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Ruby":{$gt:10}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.Java": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]})

--> 1141
```

### Ruby Project Details Collection
From outside of the mongo shell, but on da1. The following command was used to output ruby project details for the projects meeting the criteria discussed above. The following project details are output: ProjectID, NumStars, NumAuthors
```
mongo --quiet WoC --eval 'printjson(db.P_metadata.U.find({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Ruby":{$gt:10}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Go": {"$exists":false}}, {"FileInfo.Java": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]}, {ProjectID: 1, NumStars: 1, NumAuthors: 1}).toArray())' > ruby_projects.json
```

## Golang

### Golang Project Count Query

From within the mongo shell, using the WoC databse on da1. The following command was used to find the number of golang projects that meet the criteria discussed above.
```
db.P_metadata.U.count({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Go":{$gt:10}}, {"FileInfo.Java": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]})

--> 927
```

### Golang Project Details Collection
From outside of the mongo shell, but on da1. The following command was used to output golang project details for the projects meeting the criteria discussed above. The following project details are output: ProjectID, NumStars, NumAuthors
```
mongo --quiet WoC --eval 'printjson(db.P_metadata.U.find({$and: [{NumCommits:{$gt:150}}, {NumAuthors:{$gt:10}}, {"FileInfo.Go":{$gt:10}}, {"FileInfo.Java": {"$exists":false}}, {"FileInfo.JavaScript": {"$exists":false}}, {"FileInfo.Python": {"$exists":false}}, {"FileInfo.Ruby": {"$exists":false}},  {NumStars:{$gt:20}}, {LatestCommitDate:{$gt:1609477200}}, {EarliestCommitDate:{$lt:1546318800000}} ]}, {ProjectID: 1, NumStars: 1, NumAuthors: 1}).toArray())' > go_projects.json
```


# Additional Queries

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