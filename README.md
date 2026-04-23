# 🚀 AI Cognitive Routing & RAG System

## 📌 Overview

This project implements a **Cognitive AI System** that simulates intelligent social media bots.
It combines **vector-based routing**, **autonomous content generation**, and **context-aware reasoning (RAG)** using modern AI frameworks.

The system is designed to:

* Route posts to relevant bot personas
* Generate high-quality, structured content
* Respond intelligently in conversation threads
* Defend against prompt injection attacks

---

## 🧠 System Architecture

The project is divided into **three core phases**:

### 🔹 Phase 1: Vector-Based Persona Routing

* Converts text into embeddings using `sentence-transformers`
* Uses **cosine similarity** to match posts with relevant bots
* Ensures only context-aware bots respond

**Example Output:**

```
Matched Bots: [('Bot_A', 0.41)]
```

---

### 🔹 Phase 2: Autonomous Content Generation (LangGraph)

* Built using **LangGraph workflow orchestration**

* Pipeline includes:

  1. Topic Selection (LLM)
  2. Context Retrieval (Mock Search)
  3. Post Generation

* Produces **strict JSON output**

**Example Output:**

```json
{
  "bot_id": "Bot_A",
  "topic": "AI replacing jobs",
  "post_content": "AI is rapidly transforming software development. Developers who adapt will thrive, while others risk falling behind."
}
```

---

### 🔹 Phase 3: Context-Aware Defense (RAG)

* Uses full conversation context
* Generates logical and professional responses
* Maintains persona consistency

**Example Output:**

```
Modern EV batteries use advanced management systems that reduce degradation significantly. Real-world data shows strong long-term performance.
```

---

## 🔐 Prompt Injection Defense

The system includes safeguards to:

* Ignore malicious instructions (e.g., “ignore previous instructions”)
* Maintain consistent persona behavior
* Continue logical argument flow

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **Groq API (LLaMA 3.1)**
* **Sentence Transformers**
* **NumPy**

---

## 📁 Project Structure

```
ai-intern-assignment/
│── main.py                # Entry point
│── router.py              # Phase 1: Routing
│── langgraph_flow.py      # Phase 2: Content Engine
│── rag_engine.py          # Phase 3: RAG Defense
│── requirements.txt       # Dependencies
│── .env                   # API keys
│── execution_logs.txt     # Output logs
│── README.md              # Documentation
```

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add API key in `.env`

```
GROQ_API_KEY=your_api_key_here
```

### 3. Run the project

```
python main.py
```

---

## 📊 Sample Execution Flow

1. Input post is analyzed
2. Relevant bot is selected using embeddings
3. AI generates a structured post
4. System responds intelligently in a thread

---

## ✅ Key Highlights

* ✔ Embedding-based intelligent routing
* ✔ LangGraph-based AI workflow
* ✔ Structured JSON output generation
* ✔ RAG-based contextual reasoning
* ✔ Prompt injection defense mechanism
* ✔ Fully working with free Groq API

---

## 🎯 Conclusion

This project demonstrates how modern AI systems can:

* Think contextually
* Generate structured content
* Defend against malicious inputs
* Simulate real-world intelligent agents

---

## 📌 Note

* Uses **Groq API (free & fast)**
* Designed for **AI Engineering Internship Assignment**
* Built with scalability and real-world use in mind

---

⭐ *Developed as part of an AI Engineering Internship Assignment*
