# COVID-CT


### The utility of this dataset has been confirmed by a senior radiologist in Tongji Hospital, Wuhan, China, who has performed diagnosis and treatment of a large number of COVID-19 patients during the outbreak of this disease between January and April. 

After releasing this dataset, we received several feedbacks expressing concerns about the usability of this dataset. The major concerns are summarized as follows. First, when the original CT images are put into papers, the quality of these images is degraded, which may render the diagnosis decisions less accurate. The quality degradation includes: the Hounsfield unit (HU) values are lost; the number of bits per pixel is reduced; the resolution of images is reduced. Second, the original CT scan contains a sequence of CT slices, but when put into papers, only a few key slices are selected, which may have negative impact on diagnosis as well. 

We consulted the aforementioned radiologist at Tongji Hospital regarding these two concerns. According to the radiologist, the issues raised in these concerns do not significantly affect the accuracy of diagnosis decision-making. First, experienced radiologists are able to make an accurate diagnosis from low quality CT images. For example, given a photo taken by smart phone of the original CT image, experienced radiologists can make an accurate diagnosis by just looking at the photo, though the CT image in the photo has much lower quality than the original CT image. Likewise, the quality gap between CT images in papers and original CT images will not largely hurt the accuracy of diagnosis. Second, while it is preferable to read a sequence of CT slices, oftentimes a single-slice of CT contains enough clinical information for accurate decision-making. 
 

### Data Description

The COVID-CT-Dataset has 349 CT images containing clinical findings of COVID-19 from 216 patients. They are in `./Images-processed/CT_COVID.zip`

Non-COVID CT scans are in `./Images-processed/CT_NonCOVID.zip`

We provide a data split in `./Data-split`.
Data split information see `README for DenseNet_predict.md`

The meta information (e.g., patient ID, patient information, DOI, image caption) is in `COVID-CT-MetaInfo.xlsx`


The images are collected from COVID19-related papers from medRxiv, bioRxiv, NEJM, JAMA, Lancet, etc. CTs containing COVID-19 abnormalities are selected by reading the figure captions in the papers. All copyrights of the data belong to the authors and publishers of these papers.

The dataset details are described in this preprint: [COVID-CT-Dataset: A CT Scan Dataset about COVID-19](https://arxiv.org/pdf/2003.13865.pdf)

If you find this dataset and code useful, please cite:

    @article{zhao2020COVID-CT-Dataset,
      title={COVID-CT-Dataset: a CT scan dataset about COVID-19},
      author={Zhao, Jinyu and Zhang, Yichen and He, Xuehai and Xie, Pengtao},
      journal={arXiv preprint arXiv:2003.13865}, 
      year={2020}
    }

### Baseline Performance
We developed two baseline methods for the community to benchmark with.
The code are in the "baseline methods" folder and the details are in the readme files under that folder. The methods are described in [Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans](https://www.medrxiv.org/content/10.1101/2020.04.13.20063941v1)

If you find the code useful, please cite:

    @Article{he2020sample,
      author  = {He, Xuehai and Yang, Xingyi and Zhang, Shanghang, and Zhao, Jinyu and Zhang, Yichen and Xing, Eric, and Xie,       Pengtao},
      title   = {Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans},
      journal = {medrxiv},
      year    = {2020},
    }


### Contribution Guide
 - To contribute to our project, please email your data to jiz077@eng.ucsd.edu with the corresponding meta information (Patient ID, DOI and Captions).
 - We recommend you also extract images from publications or preprints. Make sure the original papers you crawled have different DOIs from those listed in `COVID-CT-MetaInfo.xlsx`.
 - In `COVID-CT-MetaInfo.xlsx`, images with the form of `2020.mm.dd.xxxx` are crawled from bioRxiv or medRxiv. The DOIs for these preprints are `10.1101/2020.mm.dd.xxxx`.
 


