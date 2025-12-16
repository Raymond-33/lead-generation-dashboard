**Lead Generation and Probability Scoring Tool**

Project Overview
This project is a prototype web-based lead generation tool designed to help business development teams identify and prioritize scientific and biotech professionals who are most likely to work with 3D in-vitro models for drug discovery and safety testing.

The application demonstrates how relevant leads can be identified, enriched with additional information, scored based on predefined criteria, and ranked for decision-making.

This is a demo implementation created as part of an internship assignment.

Problem Statement
Business development teams often spend a lot of time manually searching for the right contacts across platforms such as LinkedIn, research publications, and conference lists.

The goal of this project is to simplify that process by:
- Collecting lead information
- Assigning a probability score to each lead
- Ranking leads based on their likelihood to engage


Solution Approach
The solution is implemented as a simple Streamlit web application that displays a ranked list of leads in a clean and interactive dashboard.

The system follows a clear pipeline:
1. Identification – Lead data is provided using a structured dataset
2. Enrichment – Each lead includes information such as role, company, location, funding stage, and research activity
3. Scoring – Leads are assigned a probability score based on business-relevant factors
4. Ranking – Leads are sorted from highest to lowest score
5. Output – Data is displayed in a searchable table and can be downloaded as CSV

Scoring Logic (Conceptual)
The probability score represents how likely a lead is to engage with advanced in-vitro model solutions.

Factors considered include:
- Job role relevance (toxicology, safety, preclinical roles)
- Company funding stage (Series A, Series B)
- Recent scientific publications
- Conference participation
- Presence in biotech hubs

Higher scores indicate higher likelihood to engage.

How to Run the Application

1. Install dependencies:
```bash
pip install -r requirements.txt

2.Run the Streamlit app:
streamlit run app.py


