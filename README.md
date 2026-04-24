# 🚀 Auto-Ticket-Closer: Autonomous AIOps SRE Assistant

> **AI-Powered Incident Resolution Engine for Cloud-Native Systems**  
> A production-grade, RAG-driven AIOps platform that autonomously detects, analyzes, and resolves infrastructure incidents in real time.

---

## 📘 Overview

Auto-Ticket-Closer is an enterprise-grade **AIOps + SRE automation system** designed for modern cloud-native environments (Kubernetes, containerized microservices, and distributed systems).

Traditional observability tools stop at **alerting**. This system goes further and delivers **autonomous remediation**.

### What it does:
- 🔍 Detects anomalies from logs and runtime signals  
- 🧠 Performs AI-driven root cause analysis  
- ⚡ Generates safe, executable remediation actions  
- 🛡️ Produces SLA-ready incident summaries  

Built on **Retrieval-Augmented Generation (RAG)** to ensure:

- ❌ No hallucinated fixes  
- ✅ Only verified runbook-based solutions  

---
# 📸 System Overview

## 🖥️ SRE Dashboard
<img width="1512" height="860" alt="Ekran Resmi 2026-04-21 19 12 19" src="https://github.com/user-attachments/assets/1e767b98-cf27-4c9a-a5ef-cd4b8997f3a1" />

## ⚙️ AI Engine (Terminal View)
<img width="1512" height="949" alt="Ekran Resmi 2026-04-21 19 12 27 1" src="https://github.com/user-attachments/assets/9dc540c0-5a57-48ef-a1d9-dee838bab793" />

## 🐳 Containerized Deployment
<img width="1512" height="949" alt="Ekran Resmi 2026-04-21 18 39 41" src="https://github.com/user-attachments/assets/c2470ff3-8359-422c-9f0e-1d3dcc56001e" />

---

## 🎯 Vision

> “Infrastructure should not only be observable — it should be self-healing.”

This system is designed to eliminate manual incident handling by enabling:

- Fully autonomous incident response pipelines  
- AI-assisted DevOps decision-making  
- Knowledge-driven operational intelligence  
- Production-grade SRE automation workflows  

---

## 🏗️ System Architecture

### 🔁 End-to-End Incident Lifecycle

Logs → Analyzer → RAG Engine → Vector DB → LLM Reasoning → Remediation + SLA Output

---

### 📊 Architecture Flow

- Logs are ingested from Kubernetes / services  
- Log Analyzer extracts error patterns  
- RAG Engine retrieves relevant runbooks  
- ChromaDB provides semantic knowledge search  
- Gemini LLM performs reasoning and decision-making  
- System generates:
  - ⚡ Remediation commands  
  - 🛡️ SLA incident reports  

---

## 🧠 Core Components

### 🔍 Log Analyzer
- Parses structured and unstructured logs  
- Detects failure patterns (CrashLoopBackOff, ConfigError, ImagePullError)  
- Normalizes events for downstream AI processing  

---

### 🧠 RAG Engine
- Converts logs into vector embeddings  
- Performs semantic retrieval over runbooks  
- Ensures grounding of AI responses in real operational knowledge  

---

### 📚 Vector Database (ChromaDB)
- Stores incident runbooks and troubleshooting guides  
- Enables high-speed semantic similarity search  
- Acts as the system’s knowledge backbone  

---

### 🤖 LLM Reasoning (Gemini 2.5 Flash)
- Root cause analysis  
- Multi-step reasoning over retrieved context  
- Generates production-safe remediation steps  
- Converts technical data into human-readable explanations  

---

### ⚡ Remediation Engine
Produces executable infrastructure fixes:

kubectl apply -f secret.yaml  
kubectl rollout restart deployment api-service  
kubectl set resources deployment api --limits=cpu=500m,memory=512Mi  

---

### 🛡️ SLA Generator
- Converts technical incidents into customer-facing summaries  
- Produces executive-level incident reports  
- Ensures clarity for non-technical stakeholders  

---

## 🧰 Technology Stack

| Layer              | Technology                 | Purpose |
|--------------------|---------------------------|--------|
| AI Orchestration   | LangChain                 | RAG pipeline management |
| LLM                | Google Gemini 2.5 Flash   | Reasoning & generation |
| Embeddings         | HuggingFace MiniLM        | Semantic representation |
| Vector Database    | ChromaDB                  | Knowledge retrieval |
| Backend            | Python                    | Core system logic |
| UI                 | Streamlit                 | Dashboard interface |
| Containerization   | Docker                    | Deployment portability |

---

## 📂 Project Structure
```
auto-ticket-closer/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── knowledge_base/
│   ├── chroma_db/                  # Persistent vector storage
│   └── runbooks/                   # Operational troubleshooting docs
│
├── src/
│   ├── app.py                     # Streamlit UI
│   ├── main.py                    # System entry point
│   ├── rag_engine.py             # Retrieval-Augmented Generation logic
│   ├── log_analyzer.py           # Log parsing & anomaly detection
│   ├── remediator.py             # Fix generation engine
│   └── test_api.py               # API validation layer
```
---

## ✨ Key Features

- 🧠 **RAG-powered reasoning (zero hallucination design)**  
- ⚡ **Fully autonomous incident resolution pipeline**  
- 🔍 **Semantic runbook search engine**  
- 🛡️ **Enterprise-grade SLA report generation**  
- 🐳 **Fully containerized deployment (Docker-ready)**  
- 🎨 **Interactive Streamlit observability dashboard**  
- ☸️ **Kubernetes-native troubleshooting support**  
- 📚 **Extensible knowledge base architecture**  

---

## 🚀 Quick Start

### 1️⃣ Clone Repository
```
git clone https://github.com/AliGaffarToksoy/Auto-Ticket-Closer.git  
```
```
cd Auto-Ticket-Closer  
```
---

### 2️⃣ Configure Environment
```
echo "GOOGLE_API_KEY=your_gemini_api_key" > .env  
```
---

### 3️⃣ Run with Docker
```
docker-compose up --build  
```
---

### 4️⃣ Access Application
```
http://localhost:8501  
```
---

## 🧪 Example Incident Flow

### ❌ Input (System Log)
CreateContainerConfigError  
Secret "stripe-payment-keys" not found  

---

### 🧠 AI Analysis
- Root Cause: Missing Kubernetes secret dependency  
- Impact: Deployment failure causing service outage  

---

### ⚡ Remediation Output
kubectl apply -f stripe-payment-keys.yaml  
kubectl rollout restart deployment payment-service  

---

### 🛡️ SLA Response
The incident was caused by a missing configuration dependency.  
The issue has been identified, resolved, and services have been restored successfully.

---

## ☸️ Advanced Deployment (Production Ready)

- Kubernetes cluster deployment (EKS / GKE / CCE)  
- Horizontal Pod Autoscaler (HPA) integration  
- Prometheus & Grafana observability stack  
- Persistent ChromaDB volume storage  
- CI/CD pipeline support (GitHub Actions / GitLab CI)  

---

## 🔌 API Usage Example
```
from src.rag_engine import analyze_incident  
```
```
result = analyze_incident(log_data)  
```
```
print(result["root_cause"])  
print(result["remediation"])  
```

---

## 👨‍💻 Developer

**Ali Gaffar Toksoy**  
Cloud & DevOps Engineer  

> “The future of infrastructure is not monitoring — it is autonomy.”

---

## ⭐ Final Statement

Auto-Ticket-Closer demonstrates the next generation of **AIOps engineering**:

✔ Autonomous  
✔ Intelligent  
✔ Context-aware  
✔ Production-ready  
✔ Self-healing by design  

If you found this project valuable, consider giving it a ⭐
