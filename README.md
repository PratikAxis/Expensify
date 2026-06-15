
# **Expensify**

An AI-powered expense prediction system that forecasts future expenses using machine learning and time-series forecasting techniques.
# Overview
## Problem Statement:
While learning the backend and Machine learning deployment, I need to learn how Machine learning model are deploy using API and connect with the frontend. Most tutorial and textbook are explain it individually, rarrly explain both together.

## Solution
To address this, I make a Expense prediction system that predict the student basic expense using Machine Learning model (prophet) and expose the model through FastAPI intigration and to connect it with frontend. I packed the entire application using Dockerization which demontrating the mordern software engineer and deployment practices.

## Objectives

- Develop a RESTful API using FastAPI for machine learning inference.
- Integrate frontend and backend components into a unified application.
- Deploy and containerize the application using Docker.
- Gain hands-on experience with end-to-end ML application development.# Features
- Forecast future expenses using machine learning and time-series forecasting techniques.
- RESTful API built with FastAPI for seamless model inference.
- Interactive frontend interface for user input and result visualization.
- Input validation and structured request handling using Pydantic.
- Real-time prediction generation through API endpoints.
- Modular backend architecture following software engineering best practices.
- Dockerized application for consistent development and deployment environments.
- Auto-generated API documentation using Swagger UI.
- Environment-based configuration management for improved maintainability.
- Scalable project structure suitable for future feature expansion.

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## Frontend

- HTML
- CSS
- JavaScript

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Prophet

## Deployment & DevOps

- Docker

## Development Tools

- Git
- GitHub
- VS Code

---


# Project Structure

```bash
expense-predictor/

├── backend/
│   ├── src/
│   │   ├── api/
│   │   ├── services/
│   │   ├── model/
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│
├── Dockerfile
├── README.md
└── .gitignore
```

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd expense-predictor
```