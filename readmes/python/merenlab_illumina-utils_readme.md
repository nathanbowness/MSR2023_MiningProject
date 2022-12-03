This is a small library and a bunch of clients to perform various operations on FASTQ files (such as demultiplexing raw Illumina files, merging partial or complete overlaps, and/or performing quality filtering). It works with paired-end FASTQ files and has been tested with Illumina runs processed with CASAVA version 1.8.0 or higher.

This program is maintained by [Sam Miller](https://semiller10.github.io/) (samuelmiller at uchicago dot edu) and [Meren](http://meren.org) (meren at uchicago dot edu). Please feel free to send us an e-mail, or better yet visit the anvi'o Slack for your questions.

### Citation

Feel free to cite [this article](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0066643) (in which the codebase was first introduced) if you are using this codebase (and if you are happy with it).

![Eren et al. 2013](http://i.imgur.com/JLjBWpJ.png)

# Contents

_(the table is not automatically updated, so take it as a 'general' guide rather than accurate representation of the content below)_

- [Contents](#contents)
- [Installing](#installing)
  - [Standard installation](#standard-installation)
  - [Tracking the development branch](#tracking-the-development-branch)
- [Demultiplexing](#demultiplexing)
- [Config File Format](#config-file-format)
  - [[general] section](#general-section)
  - [[files] section](#files-section)
  - [[prefixes] section](#prefixes-section)
- [Merging Partially Overlapping Illumina Pairs](#merging-partially-overlapping-illumina-pairs)
  - [Example STATS output](#example-stats-output)
- [Merging Completely Overlapping Illumina Pairs](#merging-completely-overlapping-illumina-pairs)
- [Rapid Multithreaded Merging by Exact Overlap](#rapid-multithreaded-merging-by-exact-overlap)
- [Quality Filtering](#quality-filtering)
  - [Minoche et al.](#minoche-et-al)
    - [Example STATS output](#example-stats-output-1)
    - [Example PNG files](#example-png-files)
  - [Bokulich et al.](#bokulich-et-al)
    - [Example STATS output:](#example-stats-output-2)
    - [Example PNG files](#example-png-files-1)
- [Questions?](#questions)


# Installing

Here are a couple of ways to install illumina-utilities.

## Standard installation

The easiest way to install illumina-utils is to do it through pip. You can simply run this command, and you should be fine:

```
pip install illumina-utils
```

**Once you have installed illumina-utils, you can type 'iu-' and press your TAB key twice to see all available scripts that are installed on your system.**

## Tracking the development branch

Instead of installing the latest stable version through pip, you can also setup illumina utils to track the development branch. If you follow these steps, you will have illumina utils setup on your system in such a way, every time you initialize your the conda environment for it you will get **the very final state of the illumina-utils code**.

OK. First make sure you are not in any environment by running `conda deactivate`. Then, make sure you don't have an environment called `illumina-utils-dev` (as in *illumina utils development*):

```
conda env remove --name illumina-utils-dev
```

Now we can continue with setting up the conda environment.

### Setting up the conda environment

First create a new conda environment:

``` bash
conda create -y --name illumina-utils-dev python=3.6
```

And activate it:

```
conda activate illumina-utils-dev
```

Now you are ready for the code :)

### Setting up the local copy of the illumina utils codebase

If you are here, it means you have a conda environment with everything except illumina utils itself. We will make sure this environment _has_ illumina utils by getting a copy of the illumina utils codebase from GitHub.

Here I will suggest `~/github/` as the base directory to keep the code, but you can change if you want to something else (in which case you must remember to apply that change all the following commands, of course). Setup the code directory:

``` bash
mkdir -p ~/github && cd ~/github/
```

Get the illumina utils code:

{:.warning}
If you only plan to follow the development branch you can skip this message. But if you are not an official illumina utils developer but intend to change illumina utils and send us pull requests to reflect those changes in the official repository, you may want to clone illumina utils from your own fork rather than using the following URL. Thank you very much in advance and we are looking forward to seeing your PR!

```
git clone --recursive https://github.com/merenlab/illumina-utils.git
```

Now it is time to install the Python dependencies of illumina utils:

``` bash
cd ~/github/illumina-utils/
pip install -r requirements.txt
```

Now all dependencies are in place, and you have the code. One more step.

### Linking conda environment and the codebase

Now we have the codebase and we have the conda environment, but they don't know about each other.

Here we will setup your conda environment in such a way that every time you activate it, you will get the very latest updates from the main illumina utils repository. While you are still in illumina utils environment, copy-paste these lines into your terminal:

``` bash
mkdir -p ${CONDA_PREFIX}/etc/conda/activate.d/

cat <<EOF >${CONDA_PREFIX}/etc/conda/activate.d/illumina-utils.sh
# creating an activation script for the the conda environment for illumina utils
# development branch so (1) Python knows where to find illumina utils libraries,
# (2) the shell knows where to find illumina utils programs, and (3) every time
# the environment is activated it synchronizes with the latest code from
# active GitHub repository:
export PYTHONPATH=\$PYTHONPATH:~/github/illumina-utils/
export PATH=\$PATH:~/github/illumina-utils/scripts
echo -e "\033[1;34mUpdating from illumina utils GitHub \033[0;31m(press CTRL+C to cancel)\033[0m ..."
cd ~/github/illumina-utils && git pull && cd -
EOF
```

{:.warning}
If you are using `zsh` by default these may not work. If you run into a trouble here or especially if you figure out a way to make it work both for `zsh` and `bash`, please let us know.

If everything worked, you should be able to type the following commands in a **new terminal** and see similar outputs:

```
meren ~ $ conda activate illumina-utils-dev
Updating from illumina utils GitHub (press CTRL+C to cancel) ...

(illumina-utils-dev) meren ~ $ which iu-trim-fastq
/Users/meren/github/illumina-utils/scripts/iu-trim-fastq
```

If that is the case, you're all set.

After this, every change you will make in illumina utils codebase will immediately be reflected when you run illumina utils tools (but if you change the code and do not revert back, git will stop updating your branch from the upstream). 

If you followed these instructions, every time you open a terminal you will have to run the following command to activate your illumina utils environment:

```
conda activate illumina-utils-dev
```

Onwards!

# Demultiplexing

If you have raw FASTQ files, you can demultiplex them into samples using `iu-demultiplex` script. In order to demultiplex a run, you will need an extra FASTQ file for indexes, and a TAB-delimited file for barcode-sample associations. The directory [examples/demultiplexing](https://github.com/meren/illumina-utils/tree/master/examples/demultiplexing) contains sample files for demultiplexing. You can start the process by running the following command:

    iu-demultiplex -s barcode_to_sample.txt --r1 r1.fastq --r2 r2.fastq --index index.fastq -o output/

If you have demultiplexed your raw files using this library, you can save yourself from generating config files (properties of which explained in the next section) by hand. The script `iu-gen-configs` takes the report file generated by `iu-demultiplex`, and automatically generates config files for each sample. For instance, the following command would have been an appropriate to run after the previous `iu-demultiplex` example:

    iu-gen-configs output/00_DEMULTIPLEXING_REPORT

# Config File Format

Most scripts that come with illumina-utils require a config file as an input to learn where are the input files, and where the output should go. A config file looks like this (there is also a [sample](https://github.com/meren/illumina-utils/blob/master/examples/merging/general-config-SAMPLE.ini) file in the codebase):

    [general]
    project_name = project name
    researcher_email = reasearcher@institute.edu
    input_directory = /full/path/test_input
    output_directory = /full/path/test_output
    
    
    [files]
    pair_1 = pair_1_aaa, pair_1_aab, pair_1_aac, pair_1_aad, pair_1_aae, pair_1_aaf 
    pair_2 = pair_2_aaa, pair_2_aab, pair_2_aac, pair_2_aad, pair_2_aae, pair_2_aaf
    
    [prefixes]
    pair_1_prefix = ^....TACGCCCAGCAGC[C,T]GCGGTAA.
    pair_2_prefix = ^CCGTC[A,T]ATT[C,T].TTT[G,A]A.T


Before describing the purpose of each section, here is a useful note: in most cases you don't need to generate your config file manually. If you have your FASTQ files for R1 and R2, you can always generate a simple TAB-delimited file that associates FASTQ files with sample names, and use `iu-gen-configs` to generate your configs. Here is an example input for `iu-gen-configs` (the first line is mandatory, and the rest should describe each of your FASTQ files):

    sample	r1	r2
    e_coli	ecoli-R1.fastq	ecoli-R2.fastq
    (...)	(...)	(...)


## [general] section

This is a mandatory section that contains `project_name`, `researcher_email`, `input_directory` and `output_directory` directives.

Two critical declarations in `[general]` section are `input_directory` and `output_directory`:

* `input_directory`: Full path to the directory where FASTQ files reside.
* `output_directory`: Full path to the directory where the output of the operation you will perform on this config to be stored. Since when it is Illumina we are dealing with huge files, the codebase is pretty conservative to protect users from making simple mistakes which may result in huge losses. So, if you don't create the `output_directory`, you will get an error (it will not be automatically generated). If there is already a file in the `output_directory` with the same name with one of the outputs, you will get an error (it will not be overwritten). `project_name` will be used as a prefix for the naming convention of output files, so it would be wise to choose something descriptive and UNIX-compatible.

## [files] section

`files` section is where you list your _file names_ to be found under `input_directory`. Each file name has to be comma separated. The index of each file name in the comma seperated list, *must match* with its pair in the second list (see the example config file above).

## [prefixes] section

`prefixes` section is optional. If you have primers, barcodes or unique molecular identifiers (UMIs) in your reads, and you want them to be trimmed, you can use [regular expression](http://en.wikipedia.org/wiki/Regular_expressions)s to specify them. A UMI, being a random sequence, would be represented by a series of dots (...... would represent a UMI of length 6). If prefixes are defined, results would contain only pairs that matched them.


# Merging Partially Overlapping Illumina Pairs

Pairs generated by paritally overlapping library preperation can be merged using `iu-merge-pairs`. Once you create your config file, you simply call it with the config file as a parameter.

By default, merging program uses Levenshtein distance to find the best merging strategy for two reads in a pair, starting from the minimum expected overlap (15 nt is the default, and can be changed through the appropriate command line parameter).

The merging strategy requires [Levenshtein module](http://code.google.com/p/pylevenshtein/) to be installed.

`iu-merge-pairs` will create FASTA files for reads that were merged successfuly, or failed to merge. In the FASTA file for merged reads, the length of the overlapped region and the number of mismatches found in the overlapped part will be reported in the header line for each entry. The place of mismatch will be shown with capital letters in the sequences.

An example header line from the FASTA file for merged reads is shown below:

    >M01028:4:000000000-A1Y0P:1:1101:18829:1947 1:N:0:1|o:83|m/o:0.048193|MR:n=0;r1=2;r2=2|Q30:p,77;p,76|mismatches:4

Each field is separated from each other by a "|" character. Field one is the original defline from the FASTQ file of read 1. Following items explain details of these fields and command line options that affect them:

* `o`: Length of the overlap.
* `m/o`: The P value. P value is the ratio of the number of mismatches and the length of the overlap. Merged sequences can be discarded based on this ratio. The default is 0.3. This value should be changed through the command line parameter `-P` depending on the expected overlap size (if the expected length of overlap is 100 nts and if you choose to eliminate any pairs with more than 5 mismatches at the overlapping region, you can set the `-P` parameter to 0.05). A more intuitive way to eliminate pairs with more than a certain amount mismatches at the overlapped region is to use the parameter `--max-num-mismatches`.
* `MR`: "Mismatches Recovered". When there is a mismatch in the overlapped region, the base to be used in the final merged sequence is picked from whichever read possesses the higher Q-score (and shown as a capital letter in the merged sequence). If a mismatch is recovered from read 1, it increases the number next to r1 in this field, and so forth. However, if there is a disagreement between two reads, *and* neither of the reads have a Q-score higher than a minimum acceptable value, the corresponding base denoted with an `N` in the merged read, and the number next to `none` is increased by one. By default, the minimum Q-score value is 10. This value can be changed via the command line parameter `--min-qual-score`. Note that if `--ignore-Ns` flag is not declared, all merged sequences that had at least one disagreement which can't be recovered from either read due to `--min-qual-score` value will be discarded.
* `Q30`: By default, quality filtering is being done based only on the mismatches found in the overlapped region, and the beginning and the end of merged reads are not being checked. However a final control can be enforced using the command line flag `--enforce-Q30-check`. This flag turns on the Q30 check, as it was explained by [Minoche _et al_](http://genomebiology.com/2011/12/11/R112). Briefly, Q30-check eliminates pairs if the 66% of bases in the *first half* of each read do not have Q-scores over Q30. Note that Q30 is applied only to the parts of reads that did not overlap. If either of reads fail Q30 check, merged sequence is discarded. `p,77;p,76` in the example header reads as "read 1 passed Q30 check (threfore `p`, failed case denoted by an `f`), and 77 bases in the first half of it had a better Q-score than 30; read 2 passed Q30 check, and 76 bases in the first half of it had a better Q-score than 30". If Q30-check was not enforced `n/a` appears next to it.
* `mismatches`: Number of mismatches at the overlapped region for quick filtering of resulting reads. Using `--max-num-mismatches` parameter, you can remove any pair with more than a certain number of mismatches at the overlapped region.

Here is a snippet from the merged sequences file (reads are trimmed from both ends for readability):

    >M01028:4:000000000-A1Y0P:1:1101:15704:1943 1:N:0:1|o:87|m/o:0.022989|MR:n=0;r1=2;r2=0|Q30:p,77;p,72|mismatches:2
    [...]ggtagatggaatataacatgtagcggtgaaatGctTagatatgttatggaacaccgattgcgaaggcagtctactaagtcgatattgacgctgaggcacgaaagcgtgggtagcgaacag[...]
    >M01028:4:000000000-A1Y0P:1:1101:18231:1947 1:N:0:1|o:86|m/o:0.058140|MR:n=0;r1=5;r2=0|Q30:p,74;p,66|mismatches:5
    [...]ggaaagtggaatttctaGTGTagaggtgaaattcgtagatattagaaagaacatcaaaggcGaaggcaactttctggatcattactgacactgaggaacgaaagcatgggtagcgaagag[...]
    >M01028:4:000000000-A1Y0P:1:1101:18829:1947 1:N:0:1|o:83|m/o:0.048193|MR:n=0;r1=2;r2=2|Q30:p,77;p,76|mismatches:4
    [...]ggggggtagaatTccacgtgtagcagtgaaatgcgtagagatgtggaGgaatAtcaatggcgaaggcagccccctgggataacactgacgCtcatgcacgaaagcgtggggagcgaacag[...]


If the program runs successfully, these files will appear in the `output_directory`:

* `project_name_MERGED` (successfuly merged reads)
* `project_name_FAILED` (failed sequences due to `m/o`)
* `project_name_FAILED_WITH_Ns` (failed merged sequences for having ambiguous bases)
* `project_name_FAILED_Q30` (failed merged sequences for not passing Q30-check, if enforced)
* `project_name_MISMATCHES_BREAKDOWN` (number of mismatches breakdown)
* `project_name_STATS` (numbers regarding the run)

`project_name_MISMATCHES_BREAKDOWN` file can be visualized using the R script, `iu-visualize-mismatch-distribution`, included in the codebase (it will require ggplot2 to be available on the system). Here is an example:



![Example output](http://meren.org/tmp/breakdown.png)


When `iu-merge-pairs` is run with `--compute-qual-dicts` it will also generate visualization of quality scores for different number of mismatch levels. Please see command line options for more information.


## Example STATS output

The `project_name_STATS` file that is created in the output directory contains important information about the merging operation. It is a good practice to check the numbers and make sure there is no anomalies. Here is an example output:

    Number of pairs analyzed        	2500
    Prefix failed in read 1         	0
    Prefix failed in read 2         	0
    Prefix failed in both           	0
    Passed prefix total             	2500
    Failed prefix total             	0
    Merged total                    	1479
    Merge failed total              	1021
    Merge discarded due to P        	598
    Merge discarded due to Ns       	348
    Merge discarded due to Q30      	75
    Total number of mismatches      	13101
    Mismatches recovered from read 1	10360
    Mismatches recovered from read 2	1413
    Mismatches replaced with N      	1328
    
    Mismatches breakdown:
    
    0	372
    1	326
    2	225
    3	154
    4	120
    5	86
    6	70
    7	49
    8	40
    9	21
    10	11
    11	4
    12	1
    
    
    Command line            	iu-merge-pairs miseq_partial_overlap_config.ini z --enforce --compute
    Work directory              	/path/to/the/working/directory
    "p" value                   	0.300000
    Min overlap size            	15
    Min Q-score for mismatches  	10
    Ns ignored?                 	False
    Q30 enforced?               	True
    Slow merge?                 	False




## Recovering high-quality reads from merged reads file

If `iu-merge-pairs` finishes successfuly, it will generate `project_name_MERGED` for successfuly merged reads. A successful merge depends on the `o/r` value, Q30-check and lack of ambiguous bases in the merged sequence. However, succesfully merged reads based on user-defined or default parameters may not be as accurate as needed depending on the project. If you haven't used `--max-num-mismatches` parameter, your merged file may contain sequences that are merged poorly.

Further elimination of reads can be done by filtering out reads based on the number of mismatches they present at the overlapped region. For instance, user can decide to use only merged sequences with 0 mismatches from the resulting FASTA file.

Program `iu-filter-merged-reads` can be used to retain high-quality reads from `project_name_MERGED` file. To retain reads with 0 mismatches at the overlapped region you can simply run this command on your `project_name_MERGED` to generate a file with filtered reads `project_name_FILTERED`:

     iu-filter-merged-reads project_name_MERGED --max-mismatches 0 --output project_name_FILTERED

Resulting file would be the file to use in downstream analyses.

# Merging Completely Overlapping Illumina Pairs

Please use `iu-merge-pairs` the same way explained in the [Merging Partially Overlapping Illumina Pairs](#merging-partially-overlapping-illumina-pairs) section, but include your command line these two flags:

    (...) --marker-gene-stringent --retain-only-overlap

You can be extremely stringent with this approach by allowing 0 mismatches at the overlapped region:

    (...) --marker-gene-stringent --retain-only-overlap --max-num-mismatches 0

Completely overlapping pairs can contain parts of the adapters at the ends of the sequence, as read 1 can continue into the read 2 adapter, and read 2 can continue into the read 1 adapter. By default, these "suffix" sequences are automatically trimmed, but you can prevent trimming by setting the `--untrimmed-suffix` flag.

An example complete overlap analysis is demonstrated in the [examples](https://github.com/meren/illumina-utils/tree/master/examples) directory of the codebase.

# Rapid Multithreaded Merging by Exact Overlap

The option `--rapid-cores` triggers multithreaded merging, where the provided argument is the number of cores to use. This option only works in conjunction with `--max-num-mismatches 0` and does not support `--ignore-Ns` or options for base quality filtering. "Rapid" merging with one core is two orders of magnitude faster than "normal" merging. The speedup scales linearly with additional cores.

# Quality Filtering

## "Complete Overlap" analysis for V6

The workflow for complete overlap analysis for the V6 region has been described in [Eren _et al_](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0066643). With illumina-utils `v1.4.6` we made slight changes to the workflow. Instead of `iu-analyze-v6-complete-overlaps`, we now use `iu-merge-pairs` program and then remove V6 primers from complete overlaps with zero mismatches using `iu-trim-V6-primers`. The script [v6-complete-overlap.sh](https://github.com/meren/illumina-utils/blob/master/examples/v6-complete-overlap.sh) demonstrates the new workflow and contains commands to (1) generate a config file for a given sample, (2) merge reads in FASTQ files with complete overlap and zero mismatches, and (3) remove V6 primers from resulting reads. Please don't hesitate to get in touch if you have any questions.

## Minoche et al.

Quality filtering suggestions made by [Minoche _et al_](http://genomebiology.com/2011/12/11/R112) is implemented in `iu-filter-quality-minoche` script. The output of the script includes these files:

* `project_name-STATS.txt` (file that contains all the numbers about quality filtering process, an example output can be seen below)
* `project_name-QUALITY_PASSED_R1.fa` (pair 1's that passed quality filtering)
* `project_name-QUALITY_PASSED_R2.fa` (matching pair 2's)
* `project_name-READ_IDs.cPickle.z` (gzipped cPickle object for Python that keeps the fate of read IDs, this file may be required by other scripts in the library for purposes such as visualization, or extracting a particular group of reads from the original FASTQ files)

If the program is run with `--visualize-quality-curves` option, these files will also be generated in the output directory:

* `project_name-PASSED.png` (visualization of mean quality scores per tile for pairs that passed the quality filtering)
* `project_name-FAILED_REASON_C33.png` (visualization of mean quality scores per tile for pairs that failed quality filtering due to C33 filtering (C33: less than 2/3 of bases were Q30 or higher in the first half of the read following the B-tail trimming))
* `project_name-FAILED_REASON_N.png` (same above, but for pairs that contained an ambiguous base after B-tail trimming)
* `project_name-FAILED_REASON_P.png` (same above, but for pairs that were too short after B-tail trimming)
* `project_name-Q_DICT.cPickle.z` (gzipped cPickle object for Python that holds mean quality scores for each group of reads)

### Example STATS output

    $ cat 9022_B9-STATS.txt
    number of pairs analyzed      : 122929
    total pairs passed            : 109041 (%88.70 of all pairs)
      total pair_1 trimmed        : 6476 (%5.94 of all passed pairs)
      total pair_2 trimmed        : 9059 (%8.31 of all passed pairs)
    total pairs failed            : 13888 (%11.30 of all pairs)
      pairs failed due to pair_1  : 815 (%5.87 of all failed pairs)
      pairs failed due to pair_2  : 12193 (%87.80 of all failed pairs)
      pairs failed due to both    : 880 (%6.34 of all failed pairs)
      FAILED_REASON_P             : 12223 (%88.01 of all failed pairs)
      FAILED_REASON_N             : 38 (%0.27 of all failed pairs)
      FAILED_REASON_C33           : 1627 (%11.72 of all failed pairs)

### Example PNG files

![Example output](http://meren.org/tmp/minoche.gif)

## Bokulich et al.

Quality filtering suggestions made by [Bokulich _et al_](http://www.nature.com/nmeth/journal/v10/n1/full/nmeth.2276.html) is implemented in `iu-filter-quality-bokulich` script. The output of the script includes these files:

* `project_name-STATS.txt`
* `project_name-QUALITY_PASSED_R1.fa`
* `project_name-QUALITY_PASSED_R2.fa`
* `project_name-READ_IDs.cPickle.z`

If the program is run with `--visualize-quality-curves` option, these files will also be generated in the output directory:

* `project_name-PASSED.png`
* `project_name-FAILED_REASON_P.png` (visualization of mean quality scores per tile for pairs that failed quality filtering for being too short after quality trimming)
* `project_name-FAILED_REASON_N.png` (same above, but having more ambiguous bases than `n` after quality trimming)
* `project_name-Q_DICT.cPickle.z`

### Example STATS output:

    number of pairs analyzed      : 122929
    total pairs passed            : 111598 (%90.78 of all pairs)
      total pair_1 trimmed        : 1994 (%1.79 of all passed pairs)
      total pair_2 trimmed        : 9227 (%8.27 of all passed pairs)
    total pairs failed            : 11331 (%9.22 of all pairs)
      pairs failed due to pair_1  : 738 (%6.51 of all failed pairs)
      pairs failed due to pair_2  : 10159 (%89.66 of all failed pairs)
      pairs failed due to both    : 434 (%3.83 of all failed pairs)
      FAILED_REASON_P             : 11299 (%99.72 of all failed pairs)
      FAILED_REASON_N             : 32 (%0.28 of all failed pairs)

### Example PNG files

![Example output](http://meren.org/tmp/bokulich.gif)


# Questions?

Please don't hesitate to get in touch with me via `a.murat.eren at gmail dot com`.
