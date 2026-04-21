Ali tamam.
Sadece dosya. Sadece markdown. Eksiksiz. Baştan sona tek bir ```markdown bloğu içinde.
Bu sefer hiçbir yer yarım kalmayacak.
Aşağıdaki TAMAMI tek bir dosyadır:
---
# 🚀 Auto-Ticket-Closer: Autonomous AIOps SRE Assistant

> **AI-Powered Incident Resolution Engine for Cloud-Native Systems**  
> Autonomous, RAG-driven SRE assistant that detects, analyzes, and resolves production incidents in real time.

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG_Engine-1C3C3C?logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-8E75B2?logo=googlebard&logoColor=white)

</div>

---

## 📘 Overview

**Auto-Ticket-Closer** is a next-generation **AIOps platform** designed for **Site Reliability Engineering (SRE)** teams operating in cloud-native environments such as Kubernetes and Huawei Cloud CCE.

Traditional monitoring tools only **detect incidents** —  
this system goes further:

- 🔍 **Detects anomalies from logs**
- 🧠 **Identifies root cause using AI**
- ⚡ **Generates exact remediation commands**
- 🛡️ **Creates professional SLA-ready responses**

All powered by a **Retrieval-Augmented Generation (RAG)** architecture to ensure:

> ❌ No hallucination  
> ✅ Only verified, documented solutions

---

## 🎯 Vision

> “Modern infrastructure shouldn’t just alert — it should resolve itself.”

This project represents:

- Autonomous incident management  
- AI-assisted DevOps workflows  
- Production-grade SRE automation  
- Knowledge-driven decision systems  

---

## 🏗️ System Architecture

### 🔁 AI-Powered Incident Resolution Pipeline

```mermaid
flowchart LR

classDef input fill:#1f77b4,color:#fff,stroke:#0d3b66,stroke-width:2px
classDef ai fill:#2ca02c,color:#fff,stroke:#145a14,stroke-width:2px
classDef db fill:#9467bd,color:#fff,stroke:#4b2c73,stroke-width:2px
classDef output fill:#ff7f0e,color:#fff,stroke:#a04e00,stroke-width:2px

A[📥 Incident Input<br/>Logs & Ticket Data]:::input
B[🧠 Log Analyzer<br/>Pattern Detection]:::ai
C[🔎 RAG Engine<br/>Semantic Search]:::ai
D[(📚 ChromaDB<br/>Vector Database)]:::db
E[🤖 LLM Reasoning<br/>Gemini]:::ai
F[⚡ Remediation Engine<br/>kubectl Commands]:::output
G[🛡️ SLA Generator<br/>Customer Response]:::output

A --> B --> C
C --> D
D --> E
E --> F
E --> G
```

---
🧠 Core Components
1️⃣ Log Analyzer
Parses Kubernetes logs
Detects error patterns (CrashLoopBackOff, ConfigError, etc.)
2️⃣ RAG Engine
Converts logs into embeddings
Performs semantic search on runbooks
Retrieves relevant, trusted solutions only
3️⃣ Vector Database (ChromaDB)
Stores runbooks & SOPs
Enables fast similarity search
4️⃣ LLM Reasoning (Gemini)
Generates:
Root cause analysis
Remediation steps
Human-readable explanations
5️⃣ Remediation Engine
Produces real-world commands:
kubectl apply -f secret.yaml
kubectl set resources deployment api

6️⃣ SLA Response Generator
Creates customer-facing incident summaries
Professional, non-technical communication
---
🧰 Technology Stack
Layer                Technology              Purpose
AI Orchestration     LangChain               RAG pipeline
LLM                  Google Gemini 2.5 Flash Reasoning engine
Embeddings           HuggingFace MiniLM      Semantic understanding
Vector DB            ChromaDB                Knowledge retrieval
Backend              Python                  Core logic
UI                   Streamlit               Interactive dashboard
Containerization     Docker                  Portable runtime

---
📂 Project Structure
auto-ticket-closer/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── knowledge_base/
│   ├── chroma_db/                # Vector database (persistent storage)
│   └── huawei_runbook.txt        # Official troubleshooting knowledge
│
├── src/
│   ├── app.py                    # Streamlit UI
│   ├── main.py                   # Entry point
│   ├── rag_engine.py             # RAG pipeline logic
│   ├── log_analyzer.py           # Log parsing & detection
│   ├── remediator.py             # Fix generation engine
│   └── test_api.py               # API testing

---
✨ Key Features
🧠 RAG-Based AI Reasoning (zero hallucination)
⚡ Autonomous incident resolution
🔍 Semantic search over runbooks
🛡️ Enterprise SLA response generation
🐳 Fully containerized system
🎨 Interactive Streamlit dashboard
📚 Custom knowledge base ingestion
☸️ Kubernetes-native troubleshooting
---
📸 System Overview
🖥️ SRE Dashboard
⚙️ AI Engine (Terminal View)
🐳 Containerized Deployment
---
🚀 Quick Start
1️⃣ Clone Repository
git clone https://github.com/AliGaffarToksoy/Auto-Ticket-Closer.git

cd Auto-Ticket-Closer

2️⃣ Configure Environment
Create .env file:
GOOGLE_API_KEY=your_gemini_api_key

3️⃣ Run with Docker
docker-compose up --build

4️⃣ Access UI
http://localhost:8501

---
🧪 Example Use Case
Scenario: Missing Kubernetes Secret

Symptom:
    • 502 error after deployment
    • Logs show:

CreateContainerConfigError
Secret "stripe-payment-keys" not found

🤖 AI Output:
Root Cause
    • Missing Kubernetes Secret configuration

Remediation Command

kubectl apply -f stripe-payment-keys.yaml

SLA Response

“The issue was caused by a missing configuration dependency.
It has been identified and resolved. Service is now fully operational.”

---
☸️ Advanced Deployment (Optional)
Deploy to Kubernetes cluster
Use Persistent Volumes for ChromaDB
Scale via Horizontal Pod Autoscaler (HPA)
Integrate with Prometheus & Grafana
---
👨‍💻 Developer
Ali Gaffar Toksoy
Cloud & DevOps Engineer
“Systems shouldn’t just detect failures — they should resolve them autonomously.”
---
⭐ Final Note
This project demonstrates the future of AIOps & SRE:
Intelligent
Autonomous
Context-aware
Production-ready
If you found this valuable, consider giving it a ⭐

---


