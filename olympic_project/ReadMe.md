
# Olympic Medals Prediction: End-to-End Machine Learning Project

This project demonstrates how to build an end-to-end machine learning workflow for Data Engineers, using **Python** and **Spark**.

## Project Goal

Predict the number of medals each country will win in the Olympics using a linear regression model.

---

## 7-Step Methodology

1. **Formulate a Hypothesis**  
   Predict Olympic medals using available data.

2. **Find Relevant Data**  
   Use a dataset where each row represents a country in a specific Olympic year.

3. **Reshape the Data**  
   Ensure predictors and the target are in suitable columns.  
   Predictors: number of athletes, previous medals.

4. **Clean the Data**  
   Handle missing values, especially for new countries or non-participants.

5. **Choose an Error Metric**  
   Use Mean Absolute Error (MAE) to measure model performance.

6. **Split the Data**  
   Train on past years, test on the latest two years to evaluate on unseen data.

7. **Train the Model**  
   Implement linear regression with scikit-learn.  
   Train on predictors and predict medals.

---

## Exploratory Data Analysis (EDA)

- Examine correlations between predictors (athletes, previous medals, age) and medals.
- Find strong positive correlation for athletes and previous medals; weak for age.

---

## Model Training and Evaluation

- Fit a linear regression model, make predictions, and handle results (rounding, removing negatives).
- Evaluate model error overall and by individual country.
- Compare absolute and percentage errors.

---

## Model Limitations & Improvements

- Model performs better for countries with more data and higher medals.
- Possible improvements:
  - Add more predictors
  - Use different ML models (e.g., Random Forest)
  - Try athlete-level data

---

## Summary

This project provides a practical introduction to a real-world ML project workflow:  
**Hypothesis → Data Preparation → EDA → Modeling → Evaluation**  
It highlights both successes and challenges for beginners.
