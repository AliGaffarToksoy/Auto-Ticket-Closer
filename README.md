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

**Auto-Ticket-Closer** is a production-grade **AIOps platform** built for modern **Site Reliability Engineering (SRE)** teams operating in cloud-native ecosystems.

- 🔍 Detects anomalies from logs  
- 🧠 AI-powered root cause analysis  
- ⚡ Generates remediation commands  
- 🛡️ Produces SLA-ready responses  

> ❌ No hallucinations  
> ✅ Only verified, knowledge-backed outputs  

---

## 🎯 Vision

> “Modern infrastructure shouldn’t just alert — it should resolve itself.”

---

## 🏗️ Architecture

\`\`\`mermaid
flowchart LR
A[Logs] --> B[Analyzer]
B --> C[RAG Engine]
C --> D[(ChromaDB)]
D --> E[LLM]
E --> F[Fix]
E --> G[SLA]
\`\`\`

---

## 🧠 Components

- **Log Analyzer** → Detects failures  
- **RAG Engine** → Finds solutions  
- **Vector DB** → Stores knowledge  
- **LLM** → Generates insights  
- **Remediator** → Produces commands  
- **SLA Generator** → Customer output  

---

## 🧰 Tech Stack

| Layer | Tech |
|------|------|
| AI | LangChain |
| LLM | Gemini |
| DB | ChromaDB |
| Backend | Python |
| UI | Streamlit |
| Infra | Docker |

---

## 📂 Structure

\`\`\`
auto-ticket-closer/
├── Dockerfile
├── docker-compose.yml
├── knowledge_base/
├── src/
└── README.md
\`\`\`

---

## ✨ Features

- Autonomous incident resolution  
- RAG-based reasoning  
- Kubernetes troubleshooting  
- SLA generation  
- Containerized system  

---

## 🚀 Setup

\`\`\`bash
git clone https://github.com/AliGaffarToksoy/Auto-Ticket-Closer.git
cd Auto-Ticket-Closer
\`\`\`

\`\`\`bash
echo "GOOGLE_API_KEY=your_key" > .env
\`\`\`

\`\`\`bash
docker-compose up --build
\`\`\`

App → http://localhost:8501

---

## 🧪 Example

Error:
\`\`\`
CreateContainerConfigError
Secret not found
\`\`\`

Fix:
\`\`\`bash
kubectl apply -f secret.yaml
\`\`\`

---

## ☸️ Deployment

- Kubernetes ready  
- Scalable with HPA  
- Observability integrations  

---

## 👨‍💻 Developer

Ali Gaffar Toksoy  
Cloud & DevOps Engineer  

---

## ⭐

If useful, give a star.
