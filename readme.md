# Hearing Disability Early Detection Model

This project uses Logistic Regression to predict early signs of hearing disability using two input features:

- **Age**
- **Physical Hearing Test Score**

The model outputs:
- **1 → Positive (hearing issue detected)**
- **0 → Negative (no issue)**

This helps healthcare centers automate basic screening and reduces the manual effort needed by audiology staff.

---

## Features
- Binary classification using Logistic Regression
- Input features: age and physical_score
- Predicts early hearing disability
- Helpful for initial screening before full audiology tests

---

## Dataset
| Feature | Description |
|--------|-------------|
| age | Patient age in years |
| physical_score | Score from basic physical hearing test |
| test_result | 1 = positive, 0 = negative |

---

## Model Workflow
1. Load dataset  
2. Train/Test split  
3. Train Logistic Regression  
4. Evaluate model performance  
5. Predict hearing disability for new inputs

---

## Example Prediction
```python
model.predict([[40, 230]])
