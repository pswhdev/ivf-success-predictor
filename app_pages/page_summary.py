import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.success(
        """
        **The project addresses two key business requirements:**

        1. Predicting IVF Treatment Success: A predictive model has been
        integrated into the dashboard to estimate IVF success rates based
        on patient profiles. This tool aids in exploring potential outcomes
        and supporting personalized treatment planning.

        2. Data Visualization and Interactive Dashboard: The dashboard
        features detailed visualizations that reveal key relationships
        between clinical variables. Users can interactively explore the
        data and make real-time predictions, enhancing decision-making
        through a user-friendly interface.
        """
    )

    st.write(
        """
        * For additional information, please visit and **read** the [Project
        README file](https://github.com/pswhdev/ivf-success-predictor/blob/main/README.md).
        """
    )

    st.info(
        """
        **Project Terms & Jargon**
            
        - IVF (In Vitro Fertilization): A medical procedure where an egg is
        fertilized by sperm outside the body, with the resulting embryo being
        implanted into the uterus.
        - Embryo: The early developmental stage formed after an egg is
        fertilized by sperm, before implantation in the uterus.
        - Patient: An individual undergoing IVF fertility treatment.
        - Number of Previous IVF/DI Cycles: The total number of IVF or donor
        insemination cycles the patient has previously undergone.
        - Elective Single Embryo Transfer (eSET): A process where only one
        embryo is selected for transfer to reduce the risk of multiple
        pregnancies.
        - Specific Treatment Type: The exact fertility treatment protocol used,
        such as ICSI (Intracytoplasmic Sperm Injection), FET (Frozen Embryo
        Transfer), or standard IVF.
        - Ovarian Stimulation: A process where medication is used to induce
        the ovaries to produce multiple eggs in a single cycle.
        - Fresh vs. Frozen Cycle: A fresh cycle refers to the use of embryos
        from the current stimulation cycle, while a frozen cycle uses embryos
        that were frozen from a previous cycle.
        - PGT-M and PGT-A (Preimplantation Genetic Testing): Genetic tests
        performed on embryos to identify genetic abnormalities before transfer.
        PGT-M is for monogenic disorders, and PGT-A is for aneuploidy
        (chromosome abnormalities).
        - Endometriosis: A condition where tissue similar to the lining of the
        uterus grows outside the uterus, potentially affecting fertility.
        - Sperm Quality: Attributes of sperm, including count, motility, and
        morphology, that affect the likelihood of successful fertilization.
        - Live Birth Occurrence: The successful delivery of a living baby
        following an IVF cycle.
        """
    )
