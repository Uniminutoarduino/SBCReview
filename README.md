# Dataset for the systematic literature review on Single-Board Computers (SBCs) in engineering and computer science education

<img src="https://github.com/Uniminutoarduino/SBCReview/blob/main/Figures/Fig3.png?raw=true">

**Description:** These are the supplementary materials and dataset for the Systematic Literature Review (SLR) on SBCs in engineering and computer science education. 

**Purpose:** This study aims to analyze how the SBCs are employed in engineering and computer science education and what educational outcomes are derived from their usage during the period 2010-2020.

The review followed the PRISMA(Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines available at [http://www.prisma-statement.org/](http://www.prisma-statement.org/) 

## Files and Folder description

- The folder .RIS(Dataset) contains the .RIS files for the different stages in the review. In the files "Engineering_VillageRIS1-6" is the totality of the identified studies which have been retrieved through the Elsevier tool (Engineering Village). Likewise, the files "SynthesisGroup" and "QualitativeSynthesis" include the selected studies for stage one (overall analysis-n=155) and stage two (qualitative synthesis-n=16) in the SLR. These files are ready to be incorporated in Mendeley. 

- *NVIVO*: This folder contains the coding files for the emerged categories in the stage of qualitative synthesis. 

- *Figures*: In this folder are located the figures for the SLR. 

- *VOSViewer*: This folder contains the files for VOSViewer (1.6.14) which have been used for the cluster analysis (map based on bibliometric data). The software is available at [https://www.vosviewer.com/](https://www.vosviewer.com) 

- *Python Scripts*: It contains the designed algorithms to extract the information of the Crossref API in terms of publications per year, top-cited authors, and type of article (journal, conference proceedings, or book chapter). 

## Python Scripts

The scripts were designed in Python (v3.8). The following packages are needed in order to run them:

- Crossrefapi (v1.5.0): Library with functions to iterate through the Crossref API. [https://pypi.org/project/crossrefapi/1.0.3/](https://pypi.org/project/crossrefapi/1.0.3/)
- Matplotlib (v3.3.0 or higher): Comprehensive library for creating static, animated, and interactive visualizations in Python. [https://matplotlib.org/](https://matplotlib.org/)
- Numpy (v1.20) : Fundamental package for scientific computing with Python. [https://pypi.org/project/numpy/](https://pypi.org/project/numpy/)

To run the scripts, include them in a folder and install the previous packages. The scripts need the DOIs of the studies in a txt file (DOIs.txt). The designed scripts are the following:

- Years: Extract the number of studies per year.
- Citations: Extract the number of cites per article and it generates a list of the studies with these cites.
- Article Type: Extract the type of article in the mentioned categories (journal, conference proceedings, or book chapter).

## Credit
This work has been possible with the efforts of the following persons:


Thank you for your interest in this research :)
