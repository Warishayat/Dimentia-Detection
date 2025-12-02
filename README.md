# 🧠 Dementia Analysis API

FastAPI backend for evaluating dementia risk using LLM-powered clinical reasoning with structured JSON output.

This API accepts basic patient cognitive + MRI metadata and returns:

* ✔ Dementia prediction (yes/no)
* ✔ Severity (if any)
* ✔ Medical reasoning
* ✔ Markdown input table
* ✔ Score table
* ✔ Short summary
* ✔ Full clinical markdown report

No PDF generation is included (as requested).

---

## 🚀 Features

* **FastAPI backend**
* **Pydantic validation**
* **LLM-based dementia classifier**
* **Structured JSON output model**
* **Rule-based sentiment analysis**
* **Two API routes:**

  * `/analyze-dementia` — main analysis
  * `/test` — quick API health check

---

## 📦 Installation

```bash
git clone <your-repo-url>
cd <project-folder>
pip install -r requirements.txt
```

Create a **.env** file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📥 Required Input (Minimal Patient Data)

```json
{
  "Gender": "M",
  "Age": 72,
  "EDUC": 16,
  "MMSE": 28,
  "CDR": 0,
  "eTIV": 1500,
  "nWBV": 0.72,
  "ASF": 1.12
}
```

Only **necessary** fields are included.

---

## 📤 Sample Response

```json
{
  "dementia_result": {
    "has_dementia": false,
    "diagnosis_reason": "...",
    "dementia_severity": null,
    "prevention_or_treatment": "...",
    "markdown_input_table": "...",
    "markdown_score_table": "...",
    "short_summary": "...",
    "full_markdown_report": "..."
  },
  "sentiment": {
    "sentiment": "Positive",
    "score": 2
  }
}
```

---

## 🔥 API Routes

### **POST /analyze-dementia**

Analyze dementia status using LLM and structured response.

### **GET /test**

Simple health check.

---

## 🧪 Example Test Case (Mild Dementia)

```json
{
  "Gender": "F",
  "Age": 76,
  "EDUC": 10,
  "MMSE": 23,
  "CDR": 1.0,
  "eTIV": 1450.0,
  "nWBV": 0.67,
  "ASF": 1.18
}
```

---

## 🛠 Project Structure

```
.
├── agent.py               # LLM dementia analysis logic
├── main.py                # FastAPI backend
├── models.py              # Pydantic models
├── requirements.txt
└── README.md
```

---

## 🧩 Technologies Used

* FastAPI
* Pydantic
* Groq LLM (gpt-oss-20b)
* LangChain
* Python 3.10+

---

## © License

MIT License — Free to use and modify.

