## Data Description

### Data Source
This project relies on data contained in 7 .csv files, which were converted from 7 SQLite databases maintained by the
Fung Institute at the College of Engineering, U.C. Berkeley:<sup>1</sup>
- [patent.csv](): Identifying information for each patent
- [assignee.csv]():
- [citation.csv]()
- [class.csv]()
- [inventor.csv](): for each patent, basic inventor information

May not use:
- [patdesc.csv]()
- [invpat.csv]()


The inventor, assignee, citation, patent and classification datasets were built using primary data sources from the USPTO and the NBER. The USPTO makes up-to-date patent data available on their public web resource. The
NBER patent database contains patents granted from 1975-1999 and is publicly available. Since the patent office only began automating data storage in 1975, the Fung Institue databases only contain information from 1975 onwards.



### File and varaible descriptions:

##### Patent
*  Patent: Refers to USPTO granted patent number. Numbers are structured in such a way that the type of patent can be inferred from the numbering. For example, utility patents have eight numberic digits and a leading zero.

* Kind: Refers to [USPTO kind code](https://www.uspto.gov/learning-and-resources/support-centers/electronic-business-center/kind-codes-included-uspto-patent), indicating the type of patent filing. Roughly $\frac{1}{3}$ blank. **A1** prion to January 2, 2001 indicates Utility patent grant, **B1** or **B2** indicates utility patent grants on or after January 2, 2001

* Claims: Number of claims in the patent. Roughly $\frac{1}{3}$ blank.
* AppType: DROP
* AppNum: DROP
* GDate: Date patent was granted
* GYear: Year patent was granted
* AppDate: Date patent application was filed. Blank. DROP.
* AppYear: Year patent application was filed. Blank. DROP.
* pattype: Only 579435 not blank. Incomplete? INVESTIGATE


##### Assignnee:

USPTO assignee categories:
- 01 Unassigned
- 02 United States company or corporation
- 03 Foreign company or corporation
- 04 United States individual
- 05 Foreign individual
- 06 U.S. Federal government
- 07 Foreign government
- 08 U.S. county government
- 09 U.S. state government

** This is out of date- have reached out to USPTO for comment**

##### Citation

##### Class

##### Inventor


<sup>1</sup> Ronald Lai; Alexander D'Amour; Amy Yu; Ye Sun; David M. Doolin, Lee Fleming, 2013,
"Disambiguation and Co-authorship Networks of the U.S. Patent Inventor Database (1975 - 2013)
