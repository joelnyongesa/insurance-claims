# Insurance Claims Risk Analysis

[Live Demo](https://insurance-claims-0xcn.onrender.com/)

## About the Project

This project turns raw insurance claims data into decision-ready insight, with the analysis in the `notebooks-claims.ipynb` file handling data ingestion, EDA, model selection, validation, and a Flask-backed deployable service that exposes prediction and scoring.

The main objective of the project is to identify risk drivers, forecast expected claim amounts, and package model outputs so underwriting and finance teams can act quickly.

---

## Highlights

- Analytical pipeline, from data to deatures to models to evaluation to deployment.  
- Model selection driven by cross-validated RMSE and downstream interpretability (feature importance + residual checks).  
- Deployed Flask app for live prediction and scoring.  

---

## Key results

- Model Performance
  - **RMSE:** 14,811.97  
  - **MAE:** 5,973.38  
  - **R²:** 0.0864

- Interpretation
  - The model captures some signal but explains ~8.6% of variance in claim amount on holdout. 
  - This is expected for heavy-tailed insurance claims and a dataset with strong imbalance and limited feature coverage.

---

## Methodology

1. Problem framing. Predict claim amount (continuous target) and convert predictions to risk scores that support underwriting decisions.

2. Data loading & cleaning. Null handling, consistent category labels, imputation. Categorical variables encoded; timestamps normalized.

3. Feature engineering. Interaction terms, aggregates, categorical grouping, target transformations.

4. Modeling. Regression learners compared using nested/cross-validated RMSE. Chosen model minimized mean RMSE.

5. Evaluation. Cross-validated RMSE for selection; holdout RMSE/MAE/R² reported above. Residuals and feature importance aid interpretation.

6. Deployment. Flask app for live prediction with UI and API endpoint.

---

## Assumptions and Limitations

### Assumptions

- Claim amounts are final and cleaned.

- Provided features capture key drivers of cost.

### Limitations

- Class imbalance: majority of records are Occupation = CEO. Applied transformations reduce skewness but imbalance remains.

- Heavy-tailed target: claim amounts skewed; regressors influenced by large claims. Transformations help but alter error interpretation.

- Limited covariates: absence of detailed predictors limits predictive power.

---

## Contact / Author

- Joel Nyongesa
- [Live Demo](https://insurance-claims-0xcn.onrender.com/)