🧠 Lead Response Assistant

An AI-powered customer enquiry response system built using Ollama (llama3) and Streamlit.
This application reads customer queries, understands intent, extracts structured information, and generates safe, human-like responses — all running fully locally using open-source LLMs.

🚀 Features

✅ Intent Detection

✅ Structured Information Extraction (JSON output)

✅ Human-like Response Generation

✅ Follow-up Question Handling (Multi-turn conversation)

✅ Session-Based Conversation Memory

✅ Guardrails to reduce hallucinations

✅ Fully Local LLM (No OpenAI API required)

✅ Clean Streamlit UI

🧠 Architecture Overview

The system follows a modular AI workflow:

User Input is captured through Streamlit.

A Conversation State Manager maintains chat history.

The message passes through:

Intent Classification

Structured Data Extraction

Response Generation

All LLM reasoning is performed locally using Ollama (llama3).

The assistant response is added to session memory and displayed.

This modular design improves interpretability, safety, and extensibility.

🛠️ Tech Stack

Python

Streamlit (Frontend + App Framework)

Ollama (Local LLM runtime)

llama3 / mistral (Open-source language models)

Requests (API communication)


🔒 Safety & Guardrails

The assistant is designed to:

Avoid hallucinated claims

Avoid false guarantees

Avoid diagnosing without sufficient information

Ask clarifying follow-up questions

This makes it suitable for customer-support style automation workflows.

🎯 Why This Project Matters

This project demonstrates:

Applied LLM system design

Modular AI workflow architecture

Open-source LLM integration

Conversation memory management

Guardrail-based response generation

Local AI deployment

It reflects real-world AI product engineering rather than a simple chatbot implementation.
