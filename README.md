# Customer Support Analytics Pipeline

**Turning unstructured customer messages into actionable business insights using Python, LLMs, and Power BI.**

## Overview

Customer support teams receive large volumes of messages about delayed deliveries, payment issues, damaged products, refunds, and exchanges. Manually reviewing every message makes it difficult to identify recurring problems and understand customer needs at scale.

This project explores how a Data Engineering pipeline can transform raw customer messages into structured, analytics-ready data using Python and a Large Language Model (LLM).

The goal is to automate message analysis, standardize the extracted information, and prepare the results for business intelligence reporting.

## Business Objectives

- Ingest customer messages from CSV files.
- Validate source data before processing.
- Use an LLM to extract the main problem, customer request, and complaint category.
- Validate and store structured results.
- Prepare transformed data for Power BI dashboards.
- Identify recurring complaint patterns and opportunities to improve customer experience.

## Architecture

```text
Customer Messages (CSV)
          |
          v
   Data Ingestion
   Python + Pandas
          |
          v
   Data Validation
          |
          v
   LLM Transformation
   Llama 3 + Ollama
          |
          v
   Structured Output
          |
          v
   Processed CSV
          |
          v
   Power BI Analytics
```

**Execution environment:** The initial data pipeline is developed in GitHub Codespaces. The Llama 3 model is being explored in Google Colab. Connecting these environments is a planned integration step.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline development and orchestration |
| Pandas | CSV ingestion and data manipulation |
| LangChain | Prompt construction and LLM integration |
| Ollama | Local model runtime |
| Llama 3 | Customer message analysis |
| GitHub Codespaces | Development environment |
| Google Colab | Model experimentation |
| Power BI | Planned business intelligence reporting |

## Repository Structure

```text
customer-support-analytics-pipeline/
├── data/
│   ├── processed/
│   └── sample_customer_messages.csv
├── notebooks/
│   └── customer_support_pipeline.ipynb
├── src/
│   ├── ingest.py
│   ├── transform.py
│   ├── validate.py
│   └── main.py
├── powerbi/
│   └── dashboard_screenshots/
├── .gitignore
├── requirements.txt
└── README.md
```

## Data Flow

### 1. Ingestion

Read customer messages from a CSV source and verify that required fields are present.

Expected input fields:

- `ticket_id`: Unique identifier for a support ticket.
- `customer_message`: Original customer message.

### 2. Transformation

Use an LLM to extract structured information from each message.

Target output fields:

| Field | Description |
|---|---|
| `ticket_id` | Original support ticket identifier |
| `problem` | Main issue described by the customer |
| `customer_request` | Action requested by the customer |
| `category` | Standardized complaint category |

Example categories include `Refund`, `Delivery`, `Product`, `Payment`, and `Exchange`.

### 3. Validation

Check for missing fields, invalid categories, and incomplete model responses before saving the results.

### 4. Storage

Save the validated results as a processed CSV file that can be consumed by downstream analytics tools.

### 5. Analytics

The planned Power BI dashboard will explore complaint volume by category, common customer requests, and recurring delivery or product issues.

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- Ollama and a compatible Llama 3 model, when running the LLM stage locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-support-analytics-pipeline
```

Replace the placeholder with your repository URL.

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the ingestion stage

```bash
python src/ingest.py
```

The ingestion script reads the sample CSV, validates the required columns, and displays the loaded messages.

### 4. Run the LLM stage

The LLM transformation requires a reachable Ollama service and an available Llama 3 model. The Codespaces and Google Colab environments are separate, so the model connection must be configured before running the complete pipeline.

## Current Project Status

- [x] Repository structure created.
- [x] Sample customer messages prepared.
- [x] CSV ingestion implemented.
- [x] Required-column validation implemented.
- [ ] LLM transformation integrated with the complete pipeline.
- [ ] Structured output validation implemented.
- [ ] Processed results saved to CSV.
- [ ] End-to-end pipeline tested.
- [ ] Power BI dashboard developed.

## Future Improvements

- Process larger volumes of customer messages in batches.
- Add structured JSON output and stronger error handling.
- Track failed records and retry transient model errors.
- Add automated tests and data quality checks.
- Store processed records in a relational database.
- Orchestrate scheduled pipeline runs.
- Build Power BI dashboards to monitor complaint trends.
- Evaluate LLM extraction accuracy against manually reviewed examples.

