from dotenv import load_dotenv
import json
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Mock search
def mock_searxng_search(query: str):
    if "crypto" in query.lower():
        return "Bitcoin hits new all-time high amid ETF approvals"
    elif "ai" in query.lower():
        return "New AI model may replace junior developers"
    return "Tech industry sees rapid innovation trends"

# Node 1: Decide Topic
def decide_topic(state):
    persona = state["persona"]

    prompt = f"""
You are selecting a topic for a social media post.

Persona: {persona}

Return ONLY a short topic (max 5 words).
Example: "AI replacing jobs"
"""

    res = llm.invoke(prompt)

    return {
        "persona": persona,
        "topic": res.content.strip().replace('"', '')
    }

# Node 2: Search
def search(state):
    return {
        "persona": state["persona"],
        "topic": state["topic"],
        "context": mock_searxng_search(state["topic"])
    }

# Node 3: Generate Post
def generate_post(state):
    prompt = f"""
Persona: {state['persona']}
Topic: {state['topic']}
Context: {state['context']}

Write a strong, confident, professional tweet (max 280 characters).

STRICT RULES:
- Return ONLY valid JSON
- No extra text
- No explanation

FORMAT:
{{
  "bot_id": "Bot_A",
  "topic": "{state['topic']}",
  "post_content": "your tweet"
}}
"""

    res = llm.invoke(prompt)

    content = res.content.strip()

    #  Strong JSON Fix
    try:
        # Remove possible code block formatting
        content = content.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except:
        return {
            "bot_id": "Bot_A",
            "topic": state["topic"],
            "post_content": content[:200]
        }

# Build Graph
def build_graph():
    graph = StateGraph(dict)

    graph.add_node("decide", decide_topic)
    graph.add_node("search", search)
    graph.add_node("generate", generate_post)

    graph.set_entry_point("decide")
    graph.add_edge("decide", "search")
    graph.add_edge("search", "generate")

    return graph.compile()