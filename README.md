#  Intelligent Classification of Rural Infrastructure Projects

This project leverages **IBM AutoAI** to classify rural development projects under the correct **PMGSY (Pradhan Mantri Gram Sadak Yojana)** scheme — such as PMGSY-I, PMGSY-II, or RCPLWEA — based on physical and financial project features. The solution aims to support better planning, fund allocation, and monitoring of rural infrastructure initiatives.

---

##  Problem Statement

Efficient classification of large-scale rural infrastructure projects is essential for effective policy implementation and fund distribution. Manual tagging of schemes is slow, error-prone, and inconsistent. This project uses machine learning to automate the classification of projects into the appropriate PMGSY scheme, improving decision-making and accountability.

---

##  Tools & Technologies

- **IBM Cloud Watson Studio**  
- **IBM AutoAI**  
- **Python** – Data preprocessing & analysis  
- **Pandas, Scikit-learn**  
- **Jupyter Notebooks**  
- (Optional) **Streamlit / Flask** – For interactive UI  
- **Git & GitHub** – Version control  

---

##  Project Structure
IBM_Rural_Infrastrucutre/
│
├── data/
│ └── PMGSY_DATASET.csv #  dataset (non-sensitive)
│
├── notebooks/
│ └── Rural_Infrastructure.ipynb # EDA and data preprocessing steps
│
├── app/
│ └── app1.py # Web frontend for predictions 
│
├── assets/
│ └── images/ # Visuals, charts, screenshots
│
├── requirements.txt # Python package dependencies
├── README.md # Project documentation (this file)
└── .gitignore # Ignore unnecessary files

Future Scope
Integrate real-time data pipelines using IBM Cloud Functions

Enhance features using GIS/geolocation data

Deploy model on IBM Cloud with a web-based dashboard

Expand to other government schemes (e.g., BharatNet, RURBAN)

Use Explainable AI (XAI) to improve trust and transparency



