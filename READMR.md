# 🤖 AI CI/CD Failure Analyzer

> An AI-powered DevOps assistant that analyzes CI/CD pipeline failures, identifies root causes, and recommends actionable fixes using a local Large Language Model (LLM) powered by Ollama.

---

## 📌 Project Overview

Debugging CI/CD pipeline failures often requires manually reading hundreds or even thousands of log lines. This project automates that process using AI.

The AI CI/CD Failure Analyzer reads pipeline logs, understands the failure, identifies the root cause, explains it in simple language, and provides remediation steps.

The project runs entirely on a local LLM using **Ollama**, making it privacy-friendly, cost-free, and suitable for enterprise environments.

---

## 🚀 Features

### ✅ Day 1 (Completed)

* Read Jenkins build logs
* Analyze logs using a local AI model (Qwen2.5-Coder)
* Identify root cause
* Explain the issue
* Suggest remediation steps
* Provide severity assessment
* Recommend prevention strategies
* No cloud API required
* Runs completely offline

---

## 🛠️ Technology Stack

| Category         | Technology                 |
| ---------------- | -------------------------- |
| Language         | Python 3.12                |
| AI Model         | Qwen2.5-Coder 7B           |
| LLM Runtime      | Ollama                     |
| Environment      | Virtual Environment (venv) |
| Version Control  | Git & GitHub               |
| Operating System | Ubuntu (WSL)               |

---

## 📂 Project Structure

```text
ai-cicd-failure-analyzer/
│
├── logs/
│   └── failed_build.log
│
├── prompts/
│   └── system_prompt.txt
│
├── analyzer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/ai-cicd-failure-analyzer.git

cd ai-cicd-failure-analyzer
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

Install the model

```bash
ollama pull qwen2.5-coder:7b
```

Verify

```bash
ollama list
```

---

## ▶️ Run

```bash
python analyzer.py
```

---

## Example Output

```text
========== AI Analysis ==========

Root Cause:
Dependency conflict detected.

Explanation:
The npm dependency tree contains incompatible package versions.

Suggested Fix:
Use compatible package versions
or

npm install --legacy-peer-deps

Severity:
Medium

Prevention:
Pin dependency versions
Maintain package-lock.json
Test dependency updates in CI
```

---

## 🧠 How It Works

```text
Jenkins Log
      │
      ▼
Python Analyzer
      │
      ▼
Ollama
      │
      ▼
Qwen2.5-Coder
      │
      ▼
AI Analysis
      │
      ▼
Root Cause + Fix
```

---

## 🗺️ Roadmap

### Phase 1

* ✅ Jenkins Log Analyzer
* ⏳ Docker Log Analyzer
* ⏳ Kubernetes Log Analyzer
* ⏳ Terraform Log Analyzer
* ⏳ Ansible Log Analyzer
* ⏳ GitHub Actions Support
* ⏳ Azure DevOps Support

### Phase 2

* AI Log Classification
* RCA Report Generator
* Markdown Report Export
* PDF Report Export
* Streamlit Dashboard

### Phase 3

* Jenkins API Integration
* GitHub Actions Integration
* Azure DevOps Integration
* GitLab CI Integration

### Phase 4

* LangGraph Multi-Agent Workflow
* Auto Remediation Suggestions
* Slack Notifications
* Microsoft Teams Integration
* Jira Ticket Creation

---

## 🎯 Target Users

* DevOps Engineers
* Cloud Engineers
* Platform Engineers
* Site Reliability Engineers (SRE)
* Infrastructure Engineers
* Students learning DevOps

---

## 💡 Future Enhancements

* Support multiple LLMs
* Multi-agent architecture
* Kubernetes event analysis
* Docker container troubleshooting
* Security recommendations
* AI-powered deployment validation
* Cost optimization recommendations

---

## 🤝 Contributions

Contributions, ideas, and improvements are welcome.

If you'd like to contribute, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ashish Mondal**

DevOps | Cloud | Kubernetes | AI | Automation

If you find this project useful, consider giving it a ⭐ on GitHub.
