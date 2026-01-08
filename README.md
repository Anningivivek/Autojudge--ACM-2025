# ⚖️ AutoJudge: Programming Problem Difficulty Predictor

AutoJudge is an intelligent system designed to automatically predict the difficulty class and numerical score of programming problems. By analyzing the textual description, input constraints, and output requirements, it provides an automated alternative to manual human judgment used by platforms like Codeforces and Kattis.

##DEMO video - https://drive.google.com/file/d/1jK5fDK97qq-YmvfhQULyXqu1a6c2FjwW/view?usp=sharing
##REPORT LINK - https://drive.google.com/file/d/1J67h8-Vh85Ojsq9lVgtYYOk5JfWZso4T/view?usp=sharing

## 🚀 Project Overview
The tool takes a programming problem's text as input and predicts:
1.  **Problem Class:** Categorization into **Easy, Medium, or Hard**.
2.  **Problem Score:** A precise **numerical difficulty score**.

## 📊 Dataset
The project is built using a dataset of **4,112 programming problems**.
* **Text Features:** Title, Description, Input Description, Output Description.
* **Target Variables:** `problem_class` (Classification) and `problem_score` (Regression).
* DATASET resource:https://github.com/AREEG94FAHAD/TaskComplexityEval-24

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

## Important Note About Model Files

The file **`regressor.pkl`** is **not included** in this repository.

**Reason:**  
GitHub does not allow uploading files larger than **25 MB**, and the regression model exceeds this limit.

The project has been **fully tested locally**, and instructions are provided below to run the project successfully.

---

##  How to Run the Project (Evaluator Instructions)

### STEP 1 : Download the repository

git clone <YOUR_GITHUB_REPO_LINK>
cd AutoJudge

### STEP 2: Install Dependencies
pip install -r requirements.txt

### STEP 3 :Add the Regression Model
Place the file difficulty_regressor.pkl in the same folder as app.py.
link for regressor.pkl - https://drive.google.com/file/d/1nienkJiMkbrSHTZkKI0H9AZdgPaaC5Nu/view?usp=drive_link

### STEP 4 : Run the command in terminal
streamlit run app.py

## 💻 Usage & Installation

### Prerequisites
Ensure you have Python 3.8+ installed. You will need the following libraries:
```bash
pip install pandas numpy scikit-learn nltk streamlit
