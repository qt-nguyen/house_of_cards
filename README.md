# US House Voting Analysis

## Overview

This project performs an analysis of voting records from the US House of Representatives (potentially extensible to the Senate via parameters) using Singular Value Decomposition (SVD) on roll call records available from [unitedstates/congress](https://github.com/unitedstates/congress). The core objective is to uncover potential latent features in voting patterns and visualize the political alignment of representatives in a reduced k-dimensional space.

## Features

* **Data Collection:** Gathers roll call vote data saved inside the structured directory (`./data/`), expecting JSON files (`data.json`) organized by year and vote ID.
* **Data Processing Pipeline:**
    * Combines voting data across multiple roll calls and specified years.
    * Transforms categorical vote outcomes (e.g., "Yea", "Nay", "Aye", "No", "Present", "Not Voting") into numerical representations (1, -1, 0).
    * Filters out representatives with a high percentage of non-votes or abstentions (default threshold: 20%).
    * Normalizes vote data by centering it relative to the mean vote for each roll call.
* **Dimensionality Reduction:** Employs Singular Value Decomposition (SVD) on the processed vote matrix to extract the principal components (latent factors) that capture the most significant variance in voting behavior.
* **Visualization:** Creates interactive 2D scatter plots using Plotly. These plots position representatives based on their scores along the first two SVD components, color-coded by political party (Democrat: blue, Republican: red), and include hover-tooltips displaying representative details (name, party, state).
* **Analysis & Export:**
    * Facilitates the analysis of SVD results, particularly the vote loadings.
    * Exports intermediate data (raw combined data, SVD matrices) to a `dump/` directory.
    * Exports specific analysis results (e.g., vote loadings merged with metadata) to Excel for self-evaluation.
    * The primary visualization notebook (`make_chart.ipynb`) displays plots inline; saving plots to the `html/` directory requires explicit calls to the relevant function in `decomposer.py`.

## Setting up
This project is implemented using Python 3.11. It is recommended that a virtual environment is set up first to avoid version conflicts with global packages.

### This project 
It is recommended that this project is run in a virtual environment.

After setting up your virtual environment in the root directory, activate it and install dependencies using:
```bash
pip install -r requirement.txt
```


### Data 
Go to 
[unitedstates/congress](https://github.com/unitedstates/congress) and follow their instructions to gather roll call data, then simply copy them to the `./data` sub-folder of this project.

Note: The hierarchy of `./data` must be like this for `Collector` to work:
```bash
data
├───1997
│   ├───h1
│   ├───h2
│   ├───h3
│   ...
│   ├───s1
│   ├───s2
│   ├───s3
│   ...
├───2025
│   ├───h1
│   ├───h2
│   ├───h3
│   ...
│   ├───s1
│   ├───s2
│   ├───s3
│   ...

```
