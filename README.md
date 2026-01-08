# ⚖️ AutoJudge: Programming Problem Difficulty Predictor

AutoJudge is an intelligent system designed to automatically predict the difficulty class and numerical score of programming problems. By analyzing the textual description, input constraints, and output requirements, it provides an automated alternative to manual human judgment used by platforms like Codeforces and Kattis.

## 🚀 Project Overview
The tool takes a programming problem's text as input and predicts:
1.  **Problem Class:** Categorization into **Easy, Medium, or Hard**.
2.  **Problem Score:** A precise **numerical difficulty score**.

## 📊 Dataset
The project is built using a dataset of **4,112 programming problems**.
* **Text Features:** Title, Description, Input Description, Output Description.
* **Target Variables:** `problem_class` (Classification) and `problem_score` (Regression).

## 🛠️ Technical Implementation

### 1. Data Preprocessing
* **Text Integration:** Combined separate text fields into a single `combined_text` feature.
* **Cleaning:** Removed HTML tags, converted to lowercase, and stripped special characters.
* **LaTeX Handling:** Replaced complex mathematical delimiters (e.g., `$x^2$`) with a `MATH_EXPRESSION` placeholder to preserve context while reducing noise.

### 2. Feature Extraction
* **Method:** TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization.
* **Configuration:** Extracted the top **2,500 features** and filtered out English stop words.

### 3. Machine Learning Models
After comparing multiple algorithms (Logistic Regression, SVM, Gradient Boosting), **Random Forest** was selected as the final architecture for its superior performance:
* **Classification:** Random Forest Classifier.
* **Regression:** Random Forest Regressor.

## 📈 Performance Results
The models achieved the following results on the test set:

| Task | Model | Metric | Result |
| :--- | :--- | :--- | :--- |
| **Classification** | Random Forest | Accuracy | **50%** |
| **Regression** | Random Forest | Mean Absolute Error (MAE) | **1.73** |
| **Regression** | Random Forest | RMSE | **2.07** |

## 💻 Usage & Installation

### Prerequisites
Ensure you have Python 3.8+ installed. You will need the following libraries:
```bash
pip install pandas numpy scikit-learn nltk streamlit
