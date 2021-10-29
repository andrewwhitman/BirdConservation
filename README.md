# Bird Conservation

**Authors**: 

- [Scott Schumann](https://github.com/Shoemaker703)
- [Andrew Whitman](https://github.com/andrewwhitman)


## Overview

This repo models the classification of bird species as threatened or not threatened with global extinction. The International Union for Conservation of Nature (IUCN) maintains a [Red List of Threatened Species](https://www.iucnredlist.org/), which is used as the target variable. Our final stacked model equally weighting a logistic regression trained on a feature subspace and a decision tree trained on the entire feature space achieves a recall score of 97% and a precision score of 50% on an unseen holdout set (10% of data). Of 41 bird species with a "data deficient" (DD) target label for making an assessment of the species' globally threatened status according to IUCN's methods, our stacked model predicts 16 of them are likely to be considered threatened.


## Business Understanding

The IUCN works in partnership with [BirdLife International](https://www.birdlife.org/projects/red-list/) to maintain the Red List for bird species. You can find below 7 of the labels assigned to species.

![IUCN Red List Categories, from https://www.birdlife.org/projects/red-list/](https://www.birdlife.org/wp-content/uploads/2021/02/1000px-status_iucn3.1.svg_.png)

In addition to these labels, a small number of the world's over 11,000 bird species are labeled as "Data Deficient" (DD) or "Not Evaluated" (NE).

We assume our stakeholders are BirdLife International and the IUCN, as well as organizations making conservation planning decisions based on the Red List. The Red List is updated yearly for a subset of bird species, and an extensive overhaul is the goal for every 4 years.

We hope that our model can be used as a less scientifically rigorous proxy for a bird's globally threatened status to help guide conservation efforts when a Red List rating may be years old. We also aim to make predictions for the threatened status of species considered DD to both aid conservation efforts and to provide a shortlist of species that ought to be prioritized for data collection and evaluation.


## Data Understanding

The data for this repo was sourced from the [Ecological Society of America](https://figshare.com/collections/EltonTraits_1_0_Species-level_foraging_attributes_of_the_world_s_birds_and_mammals/3306933) and [BirdLife International](https://www.birdlife.org/) by colleagues Jeff Marvel and Crystal Gould Perrot. You can find their data collection [repo here](https://github.com/marvelje/bird-data-exploration), where you can download the [csv](https://github.com/marvelje/bird-data-exploration/blob/main/bird_dataset.csv) to a `data/` folder in your local repo.

Much of the data is already encoded as binary indicators. To prepare the data for modeling, we normalized the continuous columns via min-max scaling, one-hot encoded the categorical columns, and scaled proportional data to be percentages.


## Modeling

The data was split into train (75%), test (15%), and holdout (10%) sets prior to preprocessing steps. We built various types of models and grid searched to tune hyperparameters. The final model chosen is a stacked classifier, equally weighting a logistic regression model trained on a subspace of the features and a decision tree trained on all the features.


## Evaluation

The stacked classifier achieved 97% recall and 50% precision on the holdout set. The business goal was to minimize false negatives, or to avoid classifying a threatened bird species as not threatened, so the high recall score is encouraging. The confusion matrix, ROC curve, and precision-recall curve for the holdout set can be found below.

![holdout data model evaluation viz](https://github.com/andrewwhitman/BirdConservation/blob/main/images/holdout_eval.png)

## Conclusions

We would recommend that our model be used to identify threatened species as a proxy for the rigorous Red List evaluation if a species' evaluation is becoming out of date. If the species is predicted to be threatened, further investigation could be prioritized to confirm or deny this finding. If the species is not predicted to be threatened, it is unlikely to be a false negative.

We would also recommend using our model to predict the threatened status of data deficient birds on the Red List to guide conservation planning and data collection and evaluation efforts.


## Information

Check out our [notebook](https://github.com/andrewwhitman/BirdConservation/blob/main/BirdConservation.ipynb) for a more thorough discussion of our project, as well as our [presentation](https://github.com/andrewwhitman/BirdConservation/blob/main/presentation.pdf).

## Repository Structure

```

├── images                              <- folder containing images for README
│   └── ...
├── notebooks                           <- folder containing additional notebooks for data exploration and modeling
│   └── ...
├── .gitignore                          <- file specifying files/directories to ignore
├── BirdConservation.ipynb              <- notebook detailing the data science process containing code and narrative
├── README.md                           <- Top-level README
├── presentation.pdf                    <- presentation slides for a business audience
└── utils.py                            <- Contains helper function for model evaluation

``` 