# Resume Screener Pipeline (LangChain + OpenAI)

This project implements an end-to-end **resume screening pipeline** using
LangChain, OpenAI models, and structured outputs.  
It compares resumes against a selected job description and produces
machine-readable screening results.

---

## 🚀 Features

- Supports resumes in **TXT, DOCX, PDF**
- Supports job descriptions with **any filename**
- Automatic **serial ID assignment** for resumes and JDs
- Uses **LangChain structured output** with Pydantic schemas
- Outputs:
  - Individual JSON results per resume
  - Final Excel report with all screening results

---

## 🧠 High-Level Flow

1. Load resumes into a DataFrame
2. Load job descriptions into a DataFrame
3. Select a Job Description by ID
4. Call LLM for each resume using LangChain
5. Parse structured output into Python objects
6. Save:
   - Per-resume JSON
   - Final Excel summary

---

## 📁 Project Structure

ResumeScreenerLangchain/
│
├── data_loader/
│ ├── data_loader.py
│ ├── file_reader.py
│ ├── exce
│
├── llm/
│ ├── llm_calls.py
│ ├── schema.py
│
├── pipeline/
│ ├── resume_screener_pipeline.py
│
├── config/
│ ├── config_reader.py
│
├── output/
│ ├── llm_json/
│ ├── resume_screening_results.xlsx
│
├── requirements.txt
├── README.md
└── venv/



---

## 📦 Installation

### 1️⃣ Create and activate virtual environment (Windows)

```powershell
python -m venv venv
venv\Scripts\activate

### 2️⃣ Configure Environment

Create a `.env` file (optional) or set the environment variable directly:

```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

### 3️⃣ Run the Pipeline

Run the main script:

```powershell
python main.py
```

The script will:
1. Load resumes from `data/resumes`
2. Load job descriptions from `data/JobDescription`
3. Select `Job_Details_IAM.txt` (configured in `main.py`)
4. Screen all resumes against the JD
5. Save results in `output/`

### 4️⃣ Check Outputs

- **JSON Files**: Individual screening results in `output/Resume Screener_<run_id>/llm_outputs/`
- **Excel Report**: Consolidated results in `output/Resume Screener_<run_id>/resume_screening_results.xlsx`

To avoid permission errors, ensure the Excel file is closed before re-running. To start a fresh run, update `run` ID in `config.yaml`.

pip install -r requirements.txt

Supported file types

| Type    | Supported                      |
| ------- | ------------------------------ |
| `.txt`  | ✅                              |
| `.docx` | ✅                              |
| `.pdf`  | ✅                              |
| `.doc`  | ⚠️ (best-effort, not reliable) |



