# Whiff n Whisk AI Assistant

An intelligent, full-stack e-commerce assistant designed to streamline brownie orders and customer management. This project bridges the gap between natural language processing and relational database management.

## The Problem
Small-scale e-commerce owners often struggle with manual data lookups. This project provides an autonomous agent that allows staff to query customer and order data using natural language, eliminating the need for manual SQL script execution.

## Tech Stack
* **Agentic AI:** Pydantic AI (utilizing `gemini-3.5-flash` for reasoning and tool-calling).
* **Backend:** FastAPI, SQLAlchemy (Async), Python-dotenv.
* **Frontend:** React, Vite, CSS3 (Glassmorphism & Beige Aesthetic).
* **Database:** SQLite (Async).

## Key Features
* **Autonomous Tool Calling:** The AI automatically identifies when to search the database based on the user's input.
* **Conversation Memory:** Maintains context during complex lookups.
* **Secure Implementation:** Follows security best practices by utilizing environment variables for API keys and database credentials.
* **Modern UI:** A polished, branded interface tailored for an artisan bakery brand.

## System Architecture
1.  **React Frontend:** Captures user intent and handles smooth state transitions.
2.  **FastAPI Backend:** Acts as the API gateway and security layer (CORS managed).
3.  **AI Engine:** Pydantic AI agent parses intent and invokes asynchronous database tools.
4.  **Database Layer:** SQLAlchemy handles structured queries to retrieve persistent data.

## How to Get Started

### Prerequisites
- Python 3.12+
- Node.js 20+
