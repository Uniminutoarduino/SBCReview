# Dataset for the systematic literature review on Single-Board Computers (SBCs) in engineering and computer science education

<img src="https://github.com/Uniminutoarduino/SBCReview/blob/main/Figures/fig3.png?raw=true">

**Description:** These are the supplementary materials and dataset for the Systematic Literature Review (SLR) on SBCs in engineering and computer science education. 

**Purpose:** This study aims to analyze how the SBCs are employed in engineering and computer science education and what educational outcomes are derived from their usage during the period 2010-2020.

**Included SBCs :** Raspberry Pi, Beaglebone, Beagleboard, Odroid, Intel Edison, Orange Pi, Tinker Board, and Intel Galileo.

**Tertiary Levels:** Undergraduate, Master, and PhD. In addition, some proposals for persons with disabilities were include since they can be use in any of the mentioned tertiary levels.

**Scope:** Engineering and Computer Science Education.

The review followed the PRISMA(Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines available at [http://www.prisma-statement.org/](http://www.prisma-statement.org/) 

## Files and Folders description

- The folder *.RIS(Dataset)* contains the .RIS files for the different stages in the review. In the files "Engineering_VillageRIS1-6" is the totality of the identified studies which have been retrieved through the Elsevier tool (Engineering Village). Likewise, the files entitled "SynthesisGroup" and "QualitativeSynthesis" include the selected studies for stage one (overall analysis-n=154) and stage two (qualitative synthesis-n=16) in the SLR. These files are ready to be incorporated in Mendeley. 

- *NVIVO*: This folder contains the coding files for the emerged categories in the stage of qualitative synthesis. 

- *Figures*: In this folder are located the figures for the SLR. 

- *VOSViewer*: This folder contains the files for VOSViewer (1.6.14) which have been used for the cluster analysis (map based on bibliometric data). The software is available at [https://www.vosviewer.com/](https://www.vosviewer.com) 

- *Python Scripts*: It contains the designed algorithms to extract the information of the Crossref API in terms of publications per year, top-cited authors, and type of article (journal, conference proceedings, or book chapter). 

- *Studies qualitative Synthesis F*: Selected studies (n=16) for stage 2 (qualitative synthesis) in the SLR. The document is classified by educational methodologies, research approach, participants, tertiary level, and learning outcomes. 

- *List of studies*: The file contains the attributes (title, author, main topic, tertiary level, DOI, SBC, etc.) of each one of the studies selected for the stages in the review (overall analysis (n=154) and qualitative synthesis (n=16)).

- *State of art (Areas)*: State of art with the selected works by areas (Laboratories and e-learning, computing education, robotics, Internet of Things (IoT), and persons with disabilities). 

## Python Scripts

The scripts were designed in Python (v3.8). The following packages are needed in order to run them:

- Matplotlib (v3.3.0 or higher): Comprehensive library for creating static, animated, and interactive visualizations in Python. [https://matplotlib.org/](https://matplotlib.org/)
- Numpy (v1.20) : Fundamental package for scientific computing with Python. [https://pypi.org/project/numpy/](https://pypi.org/project/numpy/)
- urllib3 : Powerful, user-friendly HTTP client for Python. https://pypi.org/project/urllib3/

To run the scripts, include them in a folder and install the previous packages. The scripts need the DOIs of the studies in a txt file (DOIs.txt). The designed scripts are the following:

- Years: Extract the number of studies per year. To run this script, please follow these instructions:
  - Run the script ExtractYears.py. This file extract the publication years per article and it will save them in the file "YearsPublications.txt".
  - Please, fix some corrupted entries in the previous .txt file. Then, run the file Years.py to plot the number of publications per year.
- Citations: Extract the number of cites per article and it generates a list of the studies with these cites.
- Article Type: Extract the type of article in the mentioned categories (journal, conference proceedings, or book chapter).

## Credit
This work has been possible with the efforts of the following persons:

- MEd Jonathan Álvarez Ariza: jalvarez@uniminuto.edu
- MSc Heyson Báez Ramos: heysonbaez@gmail.com

Engineering Professors

Program of Technology in Electronics

Corporación Universitaria Minuto de Dios-UNIMINUTO

Bogotá, Colombia

**Thank you for your interest in this research :wink:**
