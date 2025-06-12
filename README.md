# 🕵️‍♂️ CrewAI Website Auditor

**CrewAI Website Auditor** is a modular AI-powered tool that uses multiple agents to:
- 🔍 Scrape content from a website  
- 🔎 Analyze its HTML/CSS/JS structure  
- 📋 Generate actionable improvement reports  

It is built using [CrewAI](https://github.com/joaomdmoura/crewai) and demonstrates the power of agent collaboration for automated website auditing.

---

## 🚀 Features

- **Web Scraper Agent**: Crawls and extracts content from a given website.
- **Code Analyzer Agent**: Reviews frontend code structure and technologies used.
- **Reporting Analyst Agent**: Compiles recommendations into a detailed markdown report.

---

## 🧠 Architecture

This app uses the `@CrewBase` design pattern and organizes logic into agents and tasks:

```
├── latest_ai_development/
│   └── crew.py           # Defines agents, tasks, and execution sequence
├── main.py               # Entry point to run the audit
```

Agents are configured to work sequentially:
1. Scrape Website Content  
2. Analyze Web Code  
3. Generate Improvement Report

---

## 🛠️ Installation

```bash
git clone https://github.com/IrfanPJ/crewai-website_auditor.git
cd crewai-website_auditor
pip install -r requirements.txt
```

Ensure you have your OpenAI or supported LLM API key set:

```bash
export OPENAI_API_KEY=your-key-here
```

---

## 📦 Usage

Run the tool using:

```bash
python main.py
```

You will be prompted:

```
Enter the website URL to analyze:
```

Then it will automatically run the full agent pipeline and generate:
- `scraped_content.txt`
- `web_code_analysis.md`
- `final_report.md`

---

## 📁 Output Example

- `scraped_content.txt`: Raw text scraped from the target website  
- `web_code_analysis.md`: Breakdown of HTML/CSS components and structure  
- `final_report.md`: Suggestions to improve accessibility, performance, and design  

---

## 🧩 Dependencies

- `crewai`
- `crewai_tools`
- `openai`
- `pysbd`
- Other LLM tooling depending on your setup

Install all via:

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- Uses **sequential task processing**, but can be extended to parallel execution.  
- Works with any public website URL.  
- Modify `agents_config` and `tasks_config` to customize agent behavior.

---


