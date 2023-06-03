* Draft: 2020-06-12 (Fri)

# Bank Marketing dataset

* Link: https://www.openml.org/t/14965
* Task ID: 14965

<img src="images/bank_marketing_dataset-features_target-short_version">

> **Author**: Paulo Cortez, Sérgio Moro
> **Source**: [original] (http://www.openml.org/d/1461) - UCI
> **Please cite**: S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology. In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.
>
> - Dataset:
>   Reduced version (10 % of the examples) of bank-marketing dataset.

## Memos

* This dataset is for a binary classification.
* It suffers from the imbalance dataset problem.
  * Class 1 is 4000 and class 2 is 521. Class 1 is 4x larger.
* Down-sample Class 1 & up-sample Class 2 before performing the classification task.

