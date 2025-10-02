# Fact Checker Agent

The **Fact Checker Agent** is an AI-powered system that verifies claims by fetching real-time information, analyzing evidence, and presenting structured fact-checking reports.
It is designed to be modular, interactive, and developer-friendly, leveraging modern agentic AI frameworks and APIs.

Deployed Website : https://factcheckerbyshrikarpatil.in

---

## 🚀 Features

* **Claim Verification**: Input a claim and get a fact-checked result with supporting evidence.
* **LangGraph Orchestration**: Agentic workflow management for step-by-step reasoning.
* **Real-Time Updates**: WebSocket integration provides live progress tracking of fact-checking steps.
* **OpenAI Integration**: Deployed version uses the OpenAI API for reliable language understanding.
* **Automated CI/CD**: GitHub Actions configured for seamless deployment.
* **Explainability**: Outputs include reasoning chains and evidence links for transparency.

---

## 🛠️ Tech Stack

* **Python**
* **LangGraph**
* **WebSockets**
* **OpenAI API** (for deployed version)
* **FastAPI** (backend API)
* **GitHub Actions** (CI/CD)

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fact-checker-agentic-ai.git
   cd fact-checker-agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables in `.env`:

   ```
   API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

---

## ▶️ Usage

Run the backend:

```bash
uvicorn main:app --reload
```

Send a fact-checking request:

```bash
POST /fact-check
{
  "claim": "The Eiffel Tower is taller than the Statue of Liberty."
}
```
