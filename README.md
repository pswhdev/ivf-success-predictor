
# IVF Success Predictor

## Dataset Content

The dataset was retrieved from the [Human Fertilization and Emblriology Authority - HFEA website](https://www.hfea.gov.uk/about-us/data-research/).

The dataset includes information collected during fertility treatment cycles about patient and partner characteristics, treatment details, infertility causes, and outcomes related to pregnancy and live births.

The variables are summarized on the table below, where each row represents a specific variable relevant to fertility treatment cycles and the type of data and Description according to the [HEFA's Guide to anonymised register](https://www.hfea.gov.uk/media/2682/guide-to-the-anonymised-register.pdf).


| Field                                          | Data Type | Description |
|------------------------------------------------|-----------|-------------|
| Patient Age at Treatment                       | Text      | Patient’s age at treatment, banded as follows: 18-34, 35-37, 38-39, 40-42, 43-44, 45-50 |
| Total Number of Previous IVF Cycles            | Number    | How many treatment cycles of IVF the patient has previously had |
| Total Number of Previous DI Cycles             | Number    | How many treatment cycles of DI the patient has previously had |
| Total Number of Previous Pregnancies - IVF and DI | Number | How many times the patient has previously been pregnant through IVF and DI |
| Total Number of Previous Live Births - IVF or DI | Number | How many live births the patient has had through IVF or DI |
| Causes of Infertility - Tubal Disease          | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise |
| Causes of Infertility - Ovulatory Disorder     | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise |
| Causes of Infertility - Male Factor            | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise |
| Causes of Infertility - Patient Unexplained    | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise |
| Causes of Infertility - Endometriosis          | Bit       | 1 if the primary cause of infertility is as detailed, 0 otherwise |
| Main Reason for Producing Embryos Storing Eggs | Text      | A comma separated list of the main reasons for this cycle which can include: Treatment Now, For Donation, For Storing Eggs, For Research |
| Stimulation Used                               | Bit       | 1 if this was a stimulated cycle, 0 otherwise |
| Egg Donor Age at Registration                  | Text      | If donor eggs were used, the donor's age at registration banded as follows: <=20, 21-25, 26-30, 31-35 |
| Sperm Donor Age at Registration                | Text      | If donor sperm was used, the donor's age at registration banded as follows: <=20, 21-25, 26-30, 31-35, 36-40, 41-45, >45 |
| Donated Embryo                                 | Bit       | 1 if this cycle used a donated embryo, 0 otherwise |
| Type of Treatment - IVF or DI                  | Text      | IVF or DI |
| Specific Treatment Type                        | Text      | A comma separated list of specific treatment types used in this cycle |
| PGT-M Treatment                                | Bit       | 1 if this cycle involved the use of preimplantation genetic testing for monogenic disorders (formerly PGD), 0 otherwise |
| PGT-A Treatment                                | Bit       | 1 if this cycle involved the use of preimplantation genetic testing for aneuploidy (formerly PGS), 0 otherwise |
| Elective Single Embryo Transfer                | Bit       | 1 if this cycle involved the deliberate use of only one embryo, 0 otherwise |
| Egg Source                                     | Text      | Indicates whether the eggs used in this cycle came from the patient (P) or a donor (D) |
| Sperm Source                                   | Text      | Indicates whether the sperm used in this cycle came from the patient (P) or a donor (D) |
| Fresh Cycle                                    | Bit       | 1 if this cycle used fresh embryos, 0 otherwise |
| Frozen Cycle                                   | Bit       | 1 if this cycle used frozen embryos, 0 otherwise |
| Eggs Thawed (0/1)                              | Number    | If this cycle used frozen eggs, the number of eggs thawed |
| Fresh Eggs Collected                           | Text      | Number of eggs collected in this cycle, banded into 5 categories for identifiability |
| Fresh Eggs Stored (0/1)                        | Number    | The number of eggs collected in this cycle and subsequently frozen |
| Total Eggs Mixed                               | Text      | Number of eggs mixed with sperm in this cycle, banded into 5 categories for identifiability |
| Total Embryos Created                          | Text      | Number of embryos created in this cycle, banded into 5 categories for identifiability |
| Embryos Transferred                            | Number    | The number of embryos transferred into the patient in this cycle |
| Total Embryos Thawed                           | Text      | Number of embryos thawed in this cycle, banded into 5 categories for identifiability |
| Embryos Transferred from Eggs Micro-injected   | Number    | The number of embryos transferred into the patient in this cycle that were created using ICSI |
| Embryos Stored for Use by Patient              | Text      | Number of embryos created and stored for future use by the patient, banded into 5 categories for identifiability |
| Date of Embryo Transfer                        | Number    | The number of days between embryo transfer and the first date provided in the series: egg collection date; egg thaw date; egg mix date; embryo thaw date; embryo transfer date |
| Year of Treatment                              | Number    | The year in which this cycle took place |
| Live Birth Occurrence                          | Bit       | 1 if there were 1 or more live births as a result of this cycle, 0 otherwise |
| Number of Live Births                          | Number    | The number of live births as a result of this cycle |
| Early Outcome                                  | Text      | A comma separated list of the results of a patient scan |
| Number of Foetal Sacs with Fetal Pulsation     | Number    | If foetal sacs were present in the scan, the number of sacs that evidenced foetal pulsation |
| Heart One Weeks Gestation                      | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks |
| Heart One Birth Outcome                        | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination |
| Heart One Birth Weight                         | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart One Sex                                  | Text      | The sex of the child: Male (M), Female (F) |
| Heart One Delivery Date                        | Number    | Year the child was delivered |
| Heart One Birth Congenital Abnormalities       | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise |
| Heart Two Weeks Gestation                      | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks |
| Heart Two Birth Outcome                        | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination |
| Heart Two Birth Weight                         | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart Two Sex                                  | Text      | The sex of the child: Male (M), Female (F) |
| Heart Two Delivery Date                        | Number    | Year the child was delivered |
| Heart Two Birth Congenital Abnormalities       | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise |
| Heart Three Weeks Gestation                    | Number    | The number of weeks of gestation for this foetal heart: banded for less than 30 weeks or greater than 40 weeks |
| Heart Three Birth Outcome                      | Text      | Comma separated list of the outcome of this pregnancy: Embryo reduction; live birth; miscarriage; still birth; termination |
| Heart Three Birth Weight                       | Text      | Banded birthweight of this child: Less than 1kg; Between 1.5kg and 1.99Kg; Between 1kg and 1.49Kg; Between 2.0kg and 2.49Kg; Between 2.5kg and 2.99Kg; Between 3.0kg and 3.49Kg; Between 3.5kg and 3.99Kg; Between 4.0kg and 4.49Kg; Between 4.5kg and 4.99Kg; Between 5.0kg and 5.49Kg; Between 5.5kg and 5.99Kg; 6kg or greater |
| Heart Three Sex                                | Text      | The sex of the child: Male (M), Female (F) |
| Heart Three Delivery Date                      | Number    | Year the child was delivered |
| Heart Three Birth Congenital Abnormalities     | Bit       | 1 if a congenital abnormality was recorded, 0 otherwise |
| Patient Ethnicity                              | Text      | Information on patient ethnicity has been included |
| Partner Ethnicity                              | Text      | Information on partner ethnicity has been included |
| Partner Type                                   | Text      | Information on partner types has been included (i.e., Male partner, female partner, no partner, surrogate) |
| Partner Age                                    | Text      | Banded partner age information has been added where available |

---

## Project Terms & Jargon

	- IVF(In Vitro Fertilization) is a medical procedure where an egg is fertilized by sperm outside the body, with the resulting embryo being implanted into the uterus.
	- Embryo is the early developmental stage formed after an egg is fertilized by sperm, before implantation in the uterus
	- A patient is an individual undergoing IVF fertility treatment.
	- Number of Previous IVF/DI Cycles: The total number of IVF or donor insemination cycles the patient has previously undergone.
	- Elective Single Embryo Transfer (eSET) is a process where only one embryo is selected for transfer to reduce the risk of multiple pregnancies.
	- Specific Treatment Type is the exact fertility treatment protocol used, such as ICSI (Intracytoplasmic Sperm Injection), FET (Frozen Embryo Transfer), or standard IVF.
	- Ovarian Stimulation is a process where medication is used to induce the ovaries to produce multiple eggs in a single cycle.
	- Fresh vs. Frozen Cycle: A fresh cycle refers to the use of embryos from the current stimulation cycle, while a frozen cycle uses embryos that were frozen from a previous cycle.
	- PGT-M and PGT-A (Preimplantation Genetic Testing): Genetic tests performed on embryos to identify genetic abnormalities before transfer. PGT-M is for monogenic disorders, and PGT-A is for aneuploidy (chromosome abnormalities).
	- Endometriosis is a condition where tissue similar to the lining of the uterus grows outside the uterus, potentially affecting fertility.
	- Sperm Quality are attributes of sperm, including count, motility, and morphology, that affect the likelihood of successful fertilization.
	- Live Birth Occurrence is the successful delivery of a living baby following an IVF cycle.


## Business Requirements

Dr. Emily Davis, chief fertility specialist at Hope Fertility Clinic, has observed varying IVF success rates among patients due to numerous factors. She aims to identify key predictors of IVF success to optimize treatment plans and improve patient outcomes. Dr. Davis seeks to understand how patient attributes and treatment variables correlate with IVF success, focusing on the most impactful factors.

She is particularly interested in **predicting success rates for new patients based on their profiles, using a predictive model for more accurate estimations and personalized treatments**.

To support her team, Dr. Davis requests **detailed data visualizations to illustrate key variable relationships and an interactive dashboard for exploring data and making real-time predictions**.

## Hypothesis and how to validate

1. The success rate of IVF treatments is significantly higher for patients under the age of 35 compared to those aged 35 and above.

2. Elective single embryo transfer (eSET) reduces the likelihood of multiple pregnancies without significantly lowering the overall success rate.

3. Patients with a history of endometriosis have lower IVF success rates compared to those without endometriosis.


## The rationale to map the business requirements to the Data Visualizations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


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

