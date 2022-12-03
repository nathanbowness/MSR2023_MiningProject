[![made-with-python](https://img.shields.io/badge/Made%20with-Python3-1f425f.svg)](https://www.python.org/)
[![PyPI download month](https://img.shields.io/pypi/dm/trectools.svg)](https://pypi.python.org/pypi/trectools/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/trectools.svg)](https://pypi.python.org/pypi/trectools/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/joaopalotti/trectools/graphs/commit-activity)
[![GitHub watchers](https://img.shields.io/github/watchers/joaopalotti/trectools?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/joaopalotti/trectools/watchers/)
[![GitHub stars](https://img.shields.io/github/stars/joaopalotti/trectools?style=social&label=Star&maxAge=2592000)](https://GitHub.com/joaopalotti/trectools/stargazers/)

# TREC TOOLS

TrecTools is an open-source Python library for assisting Information Retrieval (IR) practitioners with TREC-like campaigns. 

If this package helps your research somehow, please reference our paper:

```
@inproceedings{palotti2019,
 author = {Palotti, Joao and Scells, Harrisen and Zuccon, Guido},
 title = {TrecTools: an open-source Python library for Information Retrieval practitioners involved in TREC-like campaigns},
 series = {SIGIR'19},
 year = {2019},
 location = {Paris, France},
 publisher = {ACM}
} 
```

## Installing
```
pip install trectools
```

## Background

IR practitioners tasked with activities like building test collections, evaluating systems, or analysing results from empirical experiments commonly have to resort to use a number of different software tools and scripts that each perform an individual functionality – and at times they even have to implement ad-hoc scripts of their own. TrecTools aims to provide a unified environment for performing these common activities.

### Features

TrecTools is implemented in Python using standard data science libraries (NumPy, SciPy, Pandas, and Matplotlib) and using the object-oriented paradigm. 
Each of the key components of an evaluation campaign is mapped to a class: classes for runs (TrecRun),topics/queries (TrecTopic), assessment pools (TrecPools), relevance assessments (TrecQrel) and the evaluation results (TrecRes). [See file format for each object below](https://github.com/joaopalotti/trec_tools#file-formats).
Evaluation results can be produced by TrecTools itself using the evaluation metrics implemented in the tool, or be imported from the output file of trec_eval and derivatives. The features that are currently implemented in TrecTools are:

- **Querying IR Systems:** Benchmark runs can be obtained di-rectly from one of the IR toolkits that are integrated in TrecTools. There is support for issuing full-text queries to [Indri](https://www.lemurproject.org/indri/), [Terrier](http://terrier.org/) and [PISA](https://github.com/pisa-engine/pisa) toolkits. Future releases will include other toolkits (e.g., [Elastic-search](), [Anserini](https://dl.acm.org/citation.cfm?id=3239571), etc.) and support for specific query languages(Indri’s query language, Boolean queries). See code snipets in [Example 1](https://github.com/joaopalotti/trec_tools#example-1).

- **Pooling Techniques:** The following techniques for assessment pool creation from a runs set are implemented: [Depth@K](https://sigir.org/files/museum/pub-14/pub_14.pdf), [Comb[Min/Max/Med/Sum/ANZ/MNZ]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.100.9316&rep=rep1&type=pdf), [Take@N](https://link.springer.com/chapter/10.1007/978-3-319-56608-5_28), [RRFTake@N](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.150.2291&rep=rep1&type=pdf), [RBPTake@N](https://people.eng.unimelb.edu.au/jzobel/fulltext/acmtois08.pdf). [See Example 2](https://github.com/joaopalotti/trec_tools#example-2).

- **Evaluation Measures:** Currently  implemented  and  verified measures include: Precision at depth K, Recall at depth K, MAP, NDCG, Bpref, [uBpref](http://zuccon.net/publications/sigir2016_L2R_readability.pdf), [RBP]((https://people.eng.unimelb.edu.au/jzobel/fulltext/acmtois08.pdf)), [uRBP](https://link.springer.com/chapter/10.1007/978-3-319-30671-1_21). Implemented in TrecTools is the option to break ties using document score (i.e., similar to trec_eval), or document ranking (i.e., similar to the original implementation of [RBP]( https://people.eng.unimelb.edu.au/ammoffat/abstracts/mz08acmtois.html
)). Additionally, TrecTools also allows to compute the residual of the evaluation measure and analyse the relative presence of unassessed documents. [See Example 3](https://github.com/joaopalotti/trec_tools#example-3).

- **Correlation and Agreement Analysis:** The Pearson, Spearman, Kendall and τ-ap correlation between system rankings can be computed [(see Example 4)](https://github.com/joaopalotti/trec_tools#example-4). Agreement measures between relevance assessment sets can be obtained with Kappa or Jaccard [(see Example 5)](https://github.com/joaopalotti/trec_tools#example-5).

- **Fusion Techniques.** Runs can be fused using the following techniques: Comb[Max/Min/Sum/Mnz/Anz/Med] - both using the scores and document rankings, RBPFusion, RRFFusion,or BordaCountFusion. Fusion techniques are provided for meta-analysis. [See Example 6](https://github.com/joaopalotti/trec_tools#example-6).

### File Formats

The three main modules found in TrecTools are inspired by the main files created in TREC campaigns: a participant run (TrecRun), a qrel (TrecQrel) e a result file (TrecRes). 

**TrecRun format**

qid Q0 docno rank score tag

where:  
- **qid**	is the query number
- **Q0**	is the literal Q0
- **docno**	is the id of a document returned for qid
- **rank**	(1-999) is the rank of this response for this qid
- **score**	is a system-dependent indication of the quality of the response
- **tag**	is the identifier for the system

Example:  
1 Q0 nhslo3844_12_012186 1 1.73315273652 mySystem  
1 Q0 nhslo1393_12_003292 2 1.72581054377 mySystem  
1 Q0 nhslo3844_12_002212 3 1.72522727817 mySystem  
1 Q0 nhslo3844_12_012182 4 1.72522727817 mySystem  
1 Q0 nhslo1393_12_003296 5 1.71374426875 mySystem  

**TrecQrel format**

qid 0 docno relevance  

where:  
- **qid**	is the query number
- **0**	is the literal 0
- **docno**	is the id of a document in your collection
- **relevance**	is how relevant is docno for qid

Example:  
1	0	aldf.1864_12_000027	1  
1	0	aller1867_12_000032	2  
1	0	aller1868_12_000012	0  
1	0	aller1871_12_000640	1  
1	0	arthr0949_12_000945	0  
1	0	arthr0949_12_000974	1  

**TrecRes format**

label qid value

where:  
- **label**	is any string, usually representing a metric
- **qid**	is the query number or 'all' to represent a aggregate value
- **value**	is numeral result of a metric

Example:
num_rel_ret             7   77
map                     7   0.4653
P_10                    9   0.9000
num_rel_ret             all 1180 
map                     all 0.1323
gm_map                  all 0.0504

### Code Examples

#### Example 0
Code Snippets and toy examples with TrecTools.
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example0_Basic_Functions.ipynb). 

```python
from trectools import TrecQrel, procedures

qrels_file = "./robust03/qrel/robust03_qrels.txt"
qrels = TrecQrel(qrels_file)

# Generates a P@10 graph with all the runs in a directory
path_to_runs = "./robust03/runs/"
runs = procedures.list_of_runs_from_path(path_to_runs, "*.gz")

results = procedures.evaluate_runs(runs, qrels, per_query=True)
p10 = procedures.extract_metric_from_results(results, "P_10")
fig = procedures.plot_system_rank(p10, display_metric="P@10", outfile="plot.pdf")
fig.savefig("plot.pdf", bbox_inches='tight', dpi=600)
# Sample output with one run for each participating team in robust03:
```
![](examples/robust03/robust03.png)

#### Example 1
Code Snippets for manipulating topic formats and querying different IR toolkits (shown here: Terrier and Indri)

```python
from trectools import TrecTopics, TrecTerrier, TrecIndri

# Loads some topics from a file (e.g., topics.txt)
"""
<topics>
<topic number="201" type="single">
<query>amazon raspberry pi</query>
<description> You have heard quite a lot about cheap computing as being the way of the future,
including one recent model called a Raspberry Pi. You start thinking about buying one, and wonder how much they cost.
</description>
</topic>
</topics>
"""
topics = TrecTopics()
topics.read_topics_from_file("topics.txt")
# Or...load topics from a Python dictionary
topics = TrecTopics(topics={'201': u'amazon raspberry pi'})
topics.printfile(fileformat="terrier")
#<topics>
# <top>
# <num>201</num>
# <title>amazon raspberry pi</title>
# </top>
#</topics>

topics.printfile(fileformat="indri")
#<parameters>
# <trecFormat>true</trecFormat>
# <query>
# <id>201</id>
# <text>#combine( amazon raspberry pi )</text>
# </query>
#</parameters>

topics.printfile(fileformat="indribaseline")
#<parameters>
# <trecFormat>true</trecFormat>
# <query>
# <id>201</id>
# <text>amazon raspberry pi</text>
# </query>
#</parameters>

tt = TrecTerrier(bin_path="<PATH>/terrier/bin/") # where trec_terrier.sh is located
# Runs PL2 model from Terrier with Query Expansion
tr = tt.run(index="<PATH>/terrier/var/index", topics="topics.xml.gz", qexp=True,
model="PL2", result_file="terrier.baseline", expTerms=5, expDocs=3, expModel="Bo1") 

ti = TrecIndri(bin_path="~/<PATH>/indri/bin/") # where IndriRunQuery is located
ti.run(index="<PATH>/indriindex", topics, model="dirichlet", parameters={"mu":2500}, 
result_file="trec_indri.run", ndocs=1000, qexp=True, expTerms=5, expDocs=3)
```

#### Example 2

Code Snippets for generating and exporting document pools using different pooling strategies.
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example2_Making_Doc_Pools.ipynb).

```python
from trectools import TrecPool, TrecRun

r1 = TrecRun("./robust03/runs/input.aplrob03a.gz")
r2 = TrecRun("./robust03/runs/input.UIUC03Rd1.gz")

len(r1.topics()) # 100 topics
 
# Creates document pools with r1 and r2 using different strategies:

# Strategy1: Creates a pool with top 10 documents of each run:
pool1 = TrecPool.make_pool([r1, r2], strategy="topX", topX=10) # Pool with 1636 unique documents.

# Strategy2: Creates a pool with 2000 documents (20 per topic) using the reciprocal ranking strategy by Gordon, Clake and Buettcher:
pool2 = TrecPool.make_pool([r1,r2], strategy="rrf", topX=20, rrf_den=60) # Pool with 2000 unique documents.

# Check to see which pool covers better my run r1
pool1.check_coverage(r1, topX=10) # 10.0
pool2.check_coverage(r1, topX=10) # 8.35 

# Export documents to be judged using Relevation! visual assessing system
pool1.export_document_list(filename="mypool.txt", with_format="relevation")
```

#### Example 3

Code snippets showing case evaluation options available in  TrecTools.
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example3_Comparing_Runs.ipynb).

```python
from trectools import TrecQrel, TrecRun, TrecEval

# A typical evaluation workflow
r1 = TrecRun("./robust03/runs/input.aplrob03a.gz")
r1.topics()[:5] # Shows the first 5 topics: 601, 602, 603, 604, 605

qrels = TrecQrel("./robust03/qrel/robust03_qrels.txt")

te = TrecEval(r1, qrels)
rbp, residuals = te.get_rbp()           # RBP: 0.474, Residuals: 0.001
p100 = te.get_precision(depth=100)     # P@100: 0.186

# Check if documents retrieved by the system were judged:
cover10 = r1.get_mean_coverage(qrels, topX=10)   # 9.99
cover1000 = r1.get_mean_coverage(qrels, topX=1000) # 481.390 
# On average for system 'input.aplrob03a' participating in robust03, 480 documents out of 1000 were judged.
print("Average number of documents judged among top 10: %.2f, among top 1000: %.2f" % (cover10, cover1000))

# Loads another run
r2 = TrecRun("./robust03/runs/input.UIUC03Rd1.gz")

# Check how many documents, on average, in the top 10 of r1 were retrieved in the top 10 of r2
r1.check_run_coverage(r2, topX=10) # 3.64

# Evaluates r1 and r2 using all implemented evaluation metrics
result_r1 = r1.evaluate_run(qrels, per_query=True) 
result_r2 = r2.evaluate_run(qrels, per_query=True)

# Inspect for statistically significant differences between the two runs for  P_10 using two-tailed Student t-test
pvalue = result_r1.compare_with(result_r2, metric="P_10") # pvalue: 0.0167 
```

#### Example 4

Code Snippets for obtaining correlation measures from a set of runs.
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example4_Run_Correlation.ipynb).

```python
from trectools import misc, TrecRun, TrecQrel, procedures

qrels_file = "./robust03/qrel/robust03_qrels.txt"
path_to_runs = "./robust03/runs/"

qrels = TrecQrel(qrels_file)

runs = procedures.list_of_runs_from_path(path_to_runs, "*.gz")

results = procedures.evaluate_runs(runs, qrels, per_query=True)

# check the system correlation between P@10 and MAP using Kendall's tau for all systems participating in a campaign
misc.get_correlation( misc.sort_systems_by(results, "P_10"), 
                      misc.sort_systems_by(results, "map"), correlation = "kendall") # Correlation: 0.7647

# check the system correlation between P@10 and MAP using Tau's ap for all systems participating in a campaign
misc.get_correlation( misc.sort_systems_by(results, "P_10"), 
                      misc.sort_systems_by(results, "map"), correlation = "tauap") # Correlation: 0.77413
```

#### Example 5
Code Snippets for obtaining agreement measures from a pair of relevance assessments.
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example5_Agreement_QRels.ipynb).

```python
# Code snippet to check correlation between two sets of relevance assessment (e.g., made by different cohorts - assessments made by medical doctors Vs. crowdsourced assessments)
from trectools import  TrecQrel

original_qrels_file =  "./robust03/qrel/robust03_qrels.txt"
# Changed the first 10 assessments from 0 to 1
modified_qrels_file = "./robust03/qrel/mod_robust03_qrels.txt"

original_qrels = TrecQrel(original_qrels_file)
modified_qrels = TrecQrel(modified_qrels_file)

# Overall agreement 
original_qrels.check_agreement(modified_qrels) # 0.99
# Fleiss' kappa agreement
original_qrels.check_kappa(modified_qrels) # P0: 1.00, Pe = 0.90
# 3x3 confusion matrix (labels 0, 1 or 2) 
original_qrels.check_confusion_matrix(modified_qrels)
# [[122712     10      0]
# [     0   5667      0]
# [     0      0    407]]
```

#### Example 6

Code Snippets for generating fusing two runs (Reciprocal Rank fusion shown here).
See ipython notebook [here](https://github.com/joaopalotti/trectools/blob/master/examples/Example6_Fusion_Run.ipynb).

```python
from trectools import TrecRun, TrecEval, fusion

r1 = TrecRun("./robust03/runs/input.aplrob03a.gz")
r2 = TrecRun("./robust03/runs/input.UIUC03Rd1.gz")

# Easy way to create new baselines by fusing existing runs:
fused_run = fusion.reciprocal_rank_fusion([r1,r2])
r1_p25 = TrecEval(r1, qrels).get_precision(depth=25)          # P@25: 0.3392
r2_p25 = TrecEval(r2, qrels).get_precision(depth=25)          # P@25: 0.2872
fused_run_p25 = TrecEval(fused_run, qrels).get_precision(depth=25)   # P@25: 0.3436

print("P@25 -- Run 1: %.3f, Run 2: %.3f, Fusion Run: %.3f" % (r1_p25, r2_p25, fused_run_p25))

# Save run to disk with all its topics
fused_run.print_subset("my_fused_run.txt", topics=fused_run.topics())
```


## ToDos
- [x] Upload examples with a famous Trec campaing (e.g., robust3)
- [ ] Explain other file formats, such as TrecPool



