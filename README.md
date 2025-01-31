# **Legal Power Analysis of the EU Proposal Directive on Soil Monitoring and Resilience**
This project is part of my Research Practice on Soil Law at the Environmental Law Department of Wageningen University and Research (WUR). The aim of this feature is to process a large amount of textual data, helping to understand how different versions of the same Directive might differ from one another. 


## **Introduction**

In 2024 the EU Commission presented a proposal to establish a unified legislation to safeguard soils at the European level. The EU legislative process needs the proposal to be approved by the Commission, the Parliament, and the Council. Most of the time this means that the proposal undergoes slight changes in order to be approved by the different bodies, resulting in different versions of the proposal.

|  Date  | Legislative stage | EU institution | Information |
|--------|-------------------|----------------|-------------|
|05-07-23|Proposal published | EU Commission  |[COM2023-0416](https://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2023/0416/COM_COM(2023)0416_EN.pdf)|
|10-04-24|Decision by Parliament, 1st reading | EU Parliament  | [T9-0204/2024](https://www.europarl.europa.eu/doceo/document/TA-9-2024-0204_EN.html)|
|17-06-24|Council's position and changes   | Council of EU  | [2023/0232](https://data.consilium.europa.eu/doc/document/ST-11299-2024-INIT/en/pdf)|

Different versions of the proposal carry the will of the institutional body that modified them. This project was focused on analyzing these differences and understanding how the Directive changed over time. A particular interest has been placed on understanding the "legal" power of each different version. Legal power is the power of the Directive to uphold its legislation. In this project, it is theorized that it's possible to understand and evaluate how binding each version is thanks to the use of modal verbs within the text of the Directive. As explained in the rules for the English language in EU legislative documents, it is stated that auxiliaries like “would”, “should”, “could”, “must” and “might” are often unchanged. To express imperative EU legislation uses “shall”. In this case, it is used as a “must”. To express permission EU legislation uses “may”. By using Python to analyze the text and highlighting when certain auxiliaries are used, it is possible to gain a degree of understanding regarding the legal power of each version. This first analysis will be followed by a qualitative analysis to corroborate the results.

## Dependencies

This project uses the following Python libraries:

- **re (Regular Expressions)** → Built-in module for searching and manipulating text patterns.
- **PyMuPDF (fitz)** → Library for handling and extracting text from PDF files.
- **collections.Counter** → Built-in module for counting occurrences of elements in lists, strings, or tuples.
- **matplotlib.pyplot** → A powerful plotting library for visualizing data.

###  Installation

To ensure you have all required dependencies, install them using:

**Data Visualization** 
```sh
pip install pymupdf matplotlib
```
**PDF Handling**
```sh
pip install pymupdf
```

*No installation is needed for "re" and "collections.Counter" as they are built-in Python modules.*

# **References**

1. European Commission. (2024). English Style Guide English Style Guide A handbook for authors and translators in the European Commission. 
2. European Commission. (2023). DIRECTIVE OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on Soil Monitoring and Resilience (Soil Monitoring Law). https://doi.org/10.2777/821504 
