# 🎬 AI Story Studio

**AI Story Studio** is a generative AI web application that transforms a user's creative idea into an immersive fictional story.

Users can provide a story idea, choose a genre and tone, and generate an AI-written story. The application is designed to support interactive storytelling through features such as continuing the story, rewriting scenes, and generating alternative endings.

---

## ✨ Features

- **Story Idea Input** — Enter any creative story concept.
- **Genre Selection** — Choose from multiple genres such as Science Fiction, Fantasy, Mystery, Thriller, Horror, Romance, Adventure, and Drama.
- **Tone Selection** — Generate stories with different tones such as Cinematic, Dark, Emotional, Suspenseful, Funny, Inspirational, and Mysterious.
- **AI Story Generation** — Generate original stories using Generative AI.
- **Story Continuation** — Continue an existing story.
- **Scene Rewriting** — Rewrite scenes with a different style or direction.
- **Alternative Ending** — Generate a different ending for the story.
- **Responsive Interface** — Designed for desktop and mobile screens.

---

## 🧠 How It Works

**User Input**

↓

**Story Idea + Genre + Tone**

↓

**Frontend — HTML / CSS / JavaScript**

↓

**Flask Backend**

↓

**Generative AI Model**

↓

**AI-Generated Story**

↓

**Interactive Story Controls**

---

## 🛠️ Technologies Used

- **Python** — Backend programming
- **Flask** — Backend framework and REST API
- **HTML5** — Frontend structure
- **CSS3** — Interface styling and responsive design
- **JavaScript** — Frontend logic and API communication
- **Google Gemini API** — Generative AI story generation
- **Gunicorn** — Production WSGI server
- **GitHub** — Source-code management
- **Render** — Cloud deployment

---

## 📁 Project Structure

**AI-STORY-STUDIO**

**backend/**
- **app.py** — Flask backend, API routes, and Generative AI integration

**frontend/**
- **index.html** — Main application interface
- **style.css** — Application styling and responsive layout
- **script.js** — Frontend interactions and API communication

**data/**
- Dataset and supporting data files

**models/**
- Model files and AI components

**requirements.txt**
- Python dependencies required by the application

**render.yaml**
- Render deployment configuration

**.gitignore**
- Files excluded from version control

**README.md**
- Project documentation

---

## 🔄 Application Architecture

**Frontend**

HTML + CSS + JavaScript

↓

**Flask REST API**

↓

**Generative AI Engine**

↓

**Story Generation**

↓

**Frontend Story Display**

---

## 🔐 Security

The Generative AI API key is **not stored in the source code or GitHub repository**.

The application reads the API key from an environment variable:

**GEMINI_API_KEY**

The API key will be configured securely through the deployment platform.

---

## 🚀 Deployment

The application is designed for deployment using **Render**.

Deployment workflow:

**GitHub Repository**

↓

**Render**

↓

**Flask + Gunicorn**

↓

**Live AI Story Studio**

---

## 🎯 Project Goal

The goal of **AI Story Studio** is to demonstrate how Generative AI can be integrated into a complete web application to create an interactive and personalized storytelling experience.

The project combines **Generative AI, backend API development, frontend development, and cloud deployment** into one application.

---

## 👩‍💻 Author

**AI Story Studio Project**
