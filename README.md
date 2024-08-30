
# IVF Success Predictor

This project was developed to create a machine learning model that predicts the success of IVF (In Vitro Fertilization) treatments based on historical patient data. With infertility affecting millions worldwide, the need for personalized and accurate treatment predictions is addressed through data-driven insights. The project aims to assist Hope Fertility Clinic in enhancing treatment success rates, optimizing patient care, and providing tailored recommendations.

A comprehensive analysis of IVF treatment data was conducted to explore key factors influencing outcomes. A classification model was built to predict the likelihood of successful treatments. Additionally, detailed data visualizations and an interactive dashboard were created to provide clinicians with valuable insights, enabling informed decision-making in real-time.

The project’s ultimate goal is to provide healthcare professionals with a robust tool that not only predicts treatment outcomes but also helps refine treatment strategies, improve patient satisfaction, and maximize success rates.

The deployed project can be accessed [here]()

## Table of contents
- [IVF Success Predictor](#ivf-success-predictor)
  - [Table of contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Project Terms \& Jargon](#project-terms--jargon)
  - [Business Requirements](#business-requirements)
  - [Hypotheses and Validation Methods](#hypotheses-and-validation-methods)
  - [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predicting IVF Treatment Success](#predicting-ivf-treatment-success)
      - [Classification Model](#classification-model)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Quick Project Summary](#page-1-quick-project-summary)
    - [Page 2: Exploratory Analysis of IVF Treatment Data Page](#page-2-exploratory-analysis-of-ivf-treatment-data-page)
    - [Page 3: Prospect IVF Success Predictor](#page-3-prospect-ivf-success-predictor)
    - [Page 4: Project Hypothesis and Validation](#page-4-project-hypothesis-and-validation)
    - [Page 5: Predict Treatment Success](#page-5-predict-treatment-success)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements (optional)](#acknowledgements-optional)


## Dataset Content

The dataset was retrieved from the [Human Fertilization and Emblriology Authority - HFEA website](https://www.hfea.gov.uk/about-us/data-research/).

The dataset includes information collected during fertility treatment cycles about patient and partner characteristics, treatment details, infertility causes, and outcomes related to pregnancy and live births.

The variables are summarized on the table below, where each row represents a specific variable relevant to fertility treatment cycles and the type of data and Description according to the [HEFA's Guide to anonymised register](https://www.hfea.gov.uk/media/2682/guide-to-the-anonymised-register.pdf).


| Field                                             | Data Type | Description                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patient Age at Treatment                          | Text      | Patient’s age at treatment, banded as follows: 18-34, 35-37, 38-39, 40-42, 43-44, 45-50                                                                                                                                                                                                                                           |
| Total Number of Previous IVF Cycles               | Number    | How many treatment cycles of IVF the patient has previously had                                                                                                                                                                                                                                                                   |
| Total Number of Previous DI Cycles                | Number    | How many treatment cycles of DI the patient has previously had                                                                                                                                                                                                                                                                    |
| Total Number of Previous Pregnancies - IVF and DI | Number    | How many times the patient has previously been pregnant through IVF and DI                                                                                                                                                                                                                                                        |
| Total Number of Previous Live Births - IVF or DI  | Number    | How many live births the patient has had through IVF or DI                                                                                                                                                                                                                                                                        |
| Causes of Infertility - Tubal Disease             | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise                                                                                                                                                                                                                                                                 |
| Causes of Infertility - Ovulatory Disorder        | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise                                                                                                                                                                                                                                                                 |
| Causes of Infertility - Male Factor               | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise                                                                                                                                                                                                                                                                 |
| Causes of Infertility - Patient Unexplained       | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise                                                                                                                                                                                                                                                                 |
| Causes of Infertility - Endometriosis             | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise                                                                                                                                                                                                                                                                 |
| Main Reason for Producing Embryos Storing Eggs    | Text      | A comma separated list of the main reasons for this cycle which can include: Treatment Now, For Donation, For Storing Eggs, For Research                                                                                                                                                                                          |
| Stimulation Used                                  | Bit       | 1 if this was a stimulated cycle, 0 otherwise                                                                                                                                                                                                                                                                                     |
| Egg Donor Age at Registration                     | Text      | If donor eggs were used, the donor's age at registration banded as follows: <=20, 21-25, 26-30, 31-35                                                                                                                                                                                                                             |
| Sperm Donor Age at Registration                   | Text      | If donor sperm was used, the donor's age at registration banded as follows: <=20, 21-25, 26-30, 31-35, 36-40, 41-45, >45                                                                                                                                                                                                          |
| Donated Embryo                                    | Bit       | 1 if this cycle used a donated embryo, 0 otherwise                                                                                                                                                                                                                                                                                |
| Type of Treatment - IVF or DI                     | Text      | IVF or DI                                                                                                                                                                                                                                                                                                                         |
| Specific Treatment Type                           | Text      | A comma separated list of specific treatment types used in this cycle                                                                                                                                                                                                                                                             |
| PGT-M Treatment                                   | Bit       | 1 if this cycle involved the use of preimplantation genetic testing for monogenic disorders (formerly PGD), 0 otherwise                                                                                                                                                                                                           |
| PGT-A Treatment                                   | Bit       | 1 if this cycle involved the use of preimplantation genetic testing for aneuploidy (formerly PGS), 0 otherwise                                                                                                                                                                                                                    |
| Elective Single Embryo Transfer                   | Bit       | 1 if this cycle involved the deliberate use of only one embryo, 0 otherwise                                                                                                                                                                                                                                                       |
| Egg Source                                        | Text      | Indicates whether the eggs used in this cycle came from the patient (P) or a donor (D)                                                                                                                                                                                                                                            |
| Sperm Source                                      | Text      | Indicates whether the sperm used in this cycle came from the patient (P) or a donor (D)                                                                                                                                                                                                                                           |
| Fresh Cycle                                       | Bit       | 1 if this cycle used fresh embryos, 0 otherwise                                                                                                                                                                                                                                                                                   |
| Frozen Cycle                                      | Bit       | 1 if this cycle used frozen embryos, 0 otherwise                                                                                                                                                                                                                                                                                  |
| Eggs Thawed (0/1)                                 | Number    | If this cycle used frozen eggs, the number of eggs thawed                                                                                                                                                                                                                                                                         |
| Fresh Eggs Collected                              | Text      | Number of eggs collected in this cycle, banded into 5 categories for identifiability                                                                                                                                                                                                                                              |
| Fresh Eggs Stored (0/1)                           | Number    | The number of eggs collected in this cycle and subsequently frozen                                                                                                                                                                                                                                                                |
| Total Eggs Mixed                                  | Text      | Number of eggs mixed with sperm in this cycle, banded into 5 categories for identifiability                                                                                                                                                                                                                                       |
| Total Embryos Created                             | Text      | Number of embryos created in this cycle, banded into 5 categories for identifiability                                                                                                                                                                                                                                             |
| Embryos Transferred                               | Number    | The number of embryos transferred into the patient in this cycle                                                                                                                                                                                                                                                                  |
| Total Embryos Thawed                              | Text      | Number of embryos thawed in this cycle, banded into 5 categories for identifiability                                                                                                                                                                                                                                              |
| Embryos Transferred from Eggs Micro-injected      | Number    | The number of embryos transferred into the patient in this cycle that were created using ICSI                                                                                                                                                                                                                                     |
| Embryos Stored for Use by Patient                 | Text      | Number of embryos created and stored for future use by the patient, banded into 5 categories for identifiability                                                                                                                                                                                                                  |
| Date of Embryo Transfer                           | Number    | The number of days between embryo transfer and the first date provided in the series: egg collection date; egg thaw date; egg mix date; embryo thaw date; embryo transfer date                                                                                                                                                    |
| Year of Treatment                                 | Number    | The year in which this cycle took place                                                                                                                                                                                                                                                                                           |
| Live Birth Occurrence                             | Bit       | 1 if there were 1 or more live births as a result of this cycle, 0 otherwise                                                                                                                                                                                                                                                      |
| Number of Live Births                             | Number    | The number of live births as a result of this cycle                                                                                                                                                                                                                                                                               |
| Early Outcome                                     | Text      | A comma separated list of the results of a patient scan                                                                                                                                                                                                                                                                           |
| Number of Foetal Sacs with Fetal Pulsation        | Number    | If foetal sacs were present in the scan, the number of sacs that evidenced foetal pulsation                                                                                                                                                                                                                                       |
| Heart One Weeks Gestation                         | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks                                                                                                                                                                                                                    |
| Heart One Birth Outcome                           | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination                                                                                                                                                                                                        |
| Heart One Birth Weight                            | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart One Sex                                     | Text      | The sex of the child: Male (M), Female (F)                                                                                                                                                                                                                                                                                        |
| Heart One Delivery Date                           | Number    | Year the child was delivered                                                                                                                                                                                                                                                                                                      |
| Heart One Birth Congenital Abnormalities          | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise                                                                                                                                                                                                                                                                           |
| Heart Two Weeks Gestation                         | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks                                                                                                                                                                                                                    |
| Heart Two Birth Outcome                           | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination                                                                                                                                                                                                        |
| Heart Two Birth Weight                            | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart Two Sex                                     | Text      | The sex of the child: Male (M), Female (F)                                                                                                                                                                                                                                                                                        |
| Heart Two Delivery Date                           | Number    | Year the child was delivered                                                                                                                                                                                                                                                                                                      |
| Heart Two Birth Congenital Abnormalities          | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise                                                                                                                                                                                                                                                                           |
| Heart Three Weeks Gestation                       | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks                                                                                                                                                                                                                    |
| Heart Three Birth Outcome                         | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination                                                                                                                                                                                                        |
| Heart Three Birth Weight                          | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart Three Sex                                   | Text      | The sex of the child: Male (M), Female (F)                                                                                                                                                                                                                                                                                        |
| Heart Three Delivery Date                         | Number    | Year the child was delivered                                                                                                                                                                                                                                                                                                      |
| Heart Three Birth Congenital Abnormalities        | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise                                                                                                                                                                                                                                                                           |
| Patient Ethnicity                                 | Text      | Information on patient ethnicity has been included                                                                                                                                                                                                                                                                                |
| Partner Ethnicity                                 | Text      | Information on partner ethnicity has been included                                                                                                                                                                                                                                                                                |
| Partner Type                                      | Text      | Information on partner types has been included (i.e., Male partner, female partner, no partner, surrogate)                                                                                                                                                                                                                        |
| Partner Age                                       | Text      | Banded partner age information has been added where available                                                                                                                                                                                                                                                                     |

---

## Project Terms & Jargon

- **IVF(In Vitro Fertilization)** is a medical procedure where an egg is fertilized by sperm outside the body, with the resulting embryo being implanted into the uterus.
  
- **Embryo** is the early developmental stage formed after an egg is fertilized by sperm, before implantation in the uterus.
  
- A **patient** is an individual undergoing IVF fertility treatment.
  
- **Number of Previous IVF/DI Cycles**: The total number of IVF or donor insemination cycles the patient has previously undergone.
  
- **Elective Single Embryo Transfer (eSET)** is a process where only one embryo is selected for transfer to reduce the risk of multiple pregnancies.
  
- **Specific Treatment Type** is the exact fertility treatment protocol used, such as ICSI (Intracytoplasmic Sperm Injection), FET (Frozen Embryo Transfer), or standard IVF.
  
- **Ovarian Stimulation** is a process where medication is used to induce the ovaries to produce multiple eggs in a single cycle.
  
- **Fresh vs. Frozen Cycle**: A fresh cycle refers to the use of embryos from the current stimulation cycle, while a frozen cycle uses embryos that were frozen from a previous cycle.
  
- **PGT-M and PGT-A (Preimplantation Genetic Testing)**: Genetic tests performed on embryos to identify genetic abnormalities before transfer. PGT-M is for monogenic disorders, and PGT-A is for aneuploidy (chromosome abnormalities).
  
- **Endometriosis** is a condition where tissue similar to the lining of the uterus grows outside the uterus, potentially affecting fertility.
  
- **Sperm Quality** are attributes of sperm, including count, motility, and morphology, that affect the likelihood of successful fertilization.
  
- **Live Birth Occurrence** is the successful delivery of a living baby following an IVF cycle.

---

## Business Requirements

Dr. Emily Davis, chief fertility specialist at Hope Fertility Clinic, has observed varying IVF success rates among patients due to numerous factors. She aims to identify key predictors of IVF success to optimize treatment plans and improve patient outcomes. Dr. Davis seeks to understand how patient attributes and treatment variables correlate with IVF success, focusing on the most impactful factors.

She is particularly interested in:

- **Predicting success rates for new patients based on their profiles, using a predictive model for more accurate estimations and personalized treatments**.

To support her team, Dr. Davis requests

- **Detailed data visualizations to illustrate key variable relationships and an interactive dashboard for exploring data and making real-time predictions**.

---

## Hypotheses and Validation Methods

1. Patient age has a direct impact on the success rate of IVF treatments.

2. Elective single embryo transfer (eSET) reduces the likelihood of multiple pregnancies without significantly lowering the overall success rate.

3. Patients with a history of endometriosis have lower IVF success rates compared to those without endometriosis.

4. The age of the semen provider does not influence the success rate of IVF treatments.

All hypotheses will be investigated using correlation studies and graphical evaluation.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Classification and Data Analysis

  - A binary classifier will be developed to predict the success of IVF treatments.

- **Business Requirement 2**: Data Visualization and Correlation Study

  - Correlation analysis (Pearson and Spearman) will be conducted to understand how the variables correlate with successful treatments. The main variables will be plotted against "Live birth occurrence" to provide visual insights.

A dashboard will be developed to allow users to visualize the data and interact with the classifier through a user-friendly interface.

---

## ML Business Case

### Predicting IVF Treatment Success

#### Classification Model

- A machine learning (ML) model was developed to predict the success of IVF treatments based on historical data. The target variable is categorical with two classes, making a binary classification model the appropriate choice. This supervised 2-class, single-label classification model outputs: 0 (no success) or 1 (success).

- The goal is to provide Hope Fertility Clinic with actionable insights to optimize treatment outcomes by selecting the best combination of features.

- Model Success Metrics and Rationale:

  - **Accuracy (≥ 70%)**:
    - Accuracy provides a general overview of the model’s performance, indicating how often the model correctly predicts treatment outcomes. A threshold of 70% was set to ensure the model’s predictions are significantly better than random guessing (50%). This level of accuracy is considered a baseline for the model to be deemed reliable and actionable in clinical use.
  
  - **Recall for "No Success" (≥ 70%) on Training and Test Sets**:
    - High recall for "No Success" minimizes the risk of false negatives—cases where the model incorrectly predicts success when the outcome is actually no success. This is critical in a clinical setting to prevent misplaced optimism and ensure appropriate adjustments to treatment plans. A threshold of 70% ensures that most unsuccessful treatments are identified, allowing for better management of patient expectations.
  
  - **Precision for "Success" (≥ 70%)**:
    - High precision reduces false positives, where the model predicts success, but the treatment fails. In the context of IVF, this helps to prevent unnecessary costs, patient stress, and inappropriate adjustments to treatment protocols. A precision threshold of 70% ensures that when the model predicts success, it does so with a reasonable level of confidence, enhancing the trustworthiness of the predictions.
  
  - **F1 Score (≥ 70%)**:
    - The F1 score is the harmonic mean of precision and recall, balancing the trade-off between false positives and false negatives. The F1 score is particularly valuable when dealing with imbalanced classes, as is common in medical data. A minimum threshold of 70% ensures that the model maintains a balanced performance between detecting successes and failures, making the model both accurate and clinically meaningful.

These metrics ensure that the model not only performs well statistically but also provides meaningful and actionable insights for clinical decision-making at Hope Fertility Clinic. By focusing on these performance indicators, the model aims to support better treatment planning and patient management, ultimately leading to improved IVF outcomes.

- Training Data:
  - The model was trained using data from the HEFA website for the years 2017-2018, containing approximately 150,000 records of IVF treatments.

- Training Data Details:
  - Target: Live birth occurrence;
  - Features: All relevant variables from the dataset.
  - During the data cleaning process, the following irrelevant variables were excluded:
    - 'Total number of previous DI cycles',
    - 'Main reason for producing embroys storing eggs',
    - 'Type of treatment - IVF or DI',
    - 'Donated embryo',
    - 'Eggs thawed (0/1)',
    - 'Year of treatment',
    - 'Number of live births',
    - 'Embryos stored for use by patient',
    - 'Fresh eggs stored (0/1)',
    - 'Heart three birth congenital abnormalities',
    - 'Heart two birth congenital abnormalities',
    - 'Heart three delivery date',
    - 'Heart three sex',
    - 'Heart three birth weight',
    - 'Heart three weeks gestation',
    - 'Heart three birth outcome',
    - 'Heart one birth congenital abnormalities',
    - 'Heart two birth weight',
    - 'Heart two delivery date',
    - 'Heart two sex',
    - 'Heart two weeks gestation',
    - 'Heart two birth outcome',
    - 'Heart one birth weight',
    - 'Heart one weeks gestation',
    - 'Heart one delivery date',
    - 'Heart one sex',
    - 'Heart one birth outcome',
    - 'Number of foetal sacs with fetal pulsation',
    - 'Early outcome',
    - 'Partner ethnicity',
    - 'Partner Type'

---

## Dashboard Design

### Page 1: Quick Project Summary

This section of the dashboard provides a concise overview of the project's objectives, functionalities, and relevant terminology related to IVF treatments.

### Page 2: Exploratory Analysis of IVF Treatment Data Page

This page provides an interactive dashboard for exploring IVF treatment data to identify key factors associated with treatment success at Hope Fertility Clinic.

The dashboard includes data visualizations to highlight relationships between clinical variables and IVF outcomes, assisting in data-driven decision-making.

**Introduction and Data Inspection:**
  - The page introduces users to the exploratory analysis, highlighting its importance in understanding factors influencing IVF success rates.
   - Users can inspect the dataset, which contains various clinical variables, by selecting an option to view the first 10 rows of data.

**Correlation Study Summary:**
   - The results of a correlation study is presented, showing how different variables are associated with successful treatment outcomes.

**Data Visualization Options:**
   - Users can select from various clinical variables to explore through visualizations such as count distributions and pie charts.
   - A special "Parallel Plot" option allows visualization of complex relationships between multiple factors and treatment outcomes.

### Page 3: Prospect IVF Success Predictor



### Page 4: Project Hypothesis and Validation

This page explores the hypotheses regarding factors influencing IVF treatment success rates, using data analysis and visualization to validate or refute each hypothesis.

### Page 5: Predict Treatment Success

- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance

---

## Unfixed Bugs

* No unfixed bugs

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content 

- The Business Case is ficticious and was created with the help from AI, more specifically OpenAI ChatGPT.
- 

### Media

- 



## Acknowledgements (optional)
* Thank the people that provided support through this project.

