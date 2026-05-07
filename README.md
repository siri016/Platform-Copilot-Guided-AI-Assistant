# 🤖 Platform Copilot — Guided AI Assistant
An intelligent, multi-role AI assistant platform powered by **Groq LLM (LLaMA 3.1)**. This application provides contextual, structured assistance for **Students**, **Referrers**, **HR Professionals**, and **College Administrators**.
---
## 🌟 Features
- **Multi-Role Support** — Choose from Student, Referrer, HR, or College intent categories
- **AI-Powered Responses** — Real-time responses using Groq's LLaMA 3.1 model
- **Follow-Up Suggestions** — Automatically generates relevant follow-up questions
- **Conversation History** — Maintains chat context for coherent multi-turn conversations
- **Responsive UI** — Beautiful, modern interface with smooth animations
- **Category-Based Guidance** — Dropdown options for focused, topic-specific assistance
---
## 📁 Project Structure
```
Platform-Copilot-Guided-AI-Assistant/
├── BACKEND/
│   ├── server.js          # Express API server with Groq integration
│   ├── package.json       # Backend dependencies
│   ├── package-lock.json  # Dependency lock file
│   └── vercel.json        # Vercel deployment config
├── frontend/
│   ├── index.html         # Landing page
│   ├── main.html          # Main chat interface
│   ├── loading.html       # Loading screen
│   ├── style.css          # Styles
│   └── script.js          # Frontend logic
├── .gitignore
└── README.md
```
---
## 🚀 Getting Started
### Prerequisites
- [Node.js](https://nodejs.org/) (v18+)
- [Groq API Key](https://console.groq.com/)
### Backend Setup
```bash
cd BACKEND
npm install
```
Create a `.env` file in the `BACKEND` folder:
```
PORT=3000
GROQ_API_KEY=your_groq_api_key_here
```
Start the server:
```bash
npm start
```
### Frontend Setup
Simply open `frontend/index.html` in your browser, or serve it with any static file server.
---
## 🌐 Deployment (Vercel)
### Deploy Backend
1. Go to [Vercel](https://vercel.com) → **Add New Project** → Import this repo
2. Set **Root Directory** → `BACKEND`
3. Add Environment Variable: `GROQ_API_KEY` = your key
4. Deploy ✅
### Deploy Frontend
1. **Add New Project** → Import the same repo again
2. Set **Root Directory** → `frontend`
3. Framework Preset → **Other**
4. Deploy ✅
> **Note:** Update the `API_URL` in `script.js` to point to your live backend Vercel URL.
---
## 🛠️ Tech Stack
| Layer    | Technology              |
|----------|------------------------|
| Frontend | HTML, CSS, JavaScript  |
| Backend  | Node.js, Express       |
| AI Model | Groq (LLaMA 3.1 8B)   |
| Hosting  | Vercel                 |
---
## 📄 API Endpoints
| Method | Endpoint         | Description                     |
|--------|------------------|---------------------------------|
| GET    | `/api/intents`   | Get all available intent roles  |
| POST   | `/api/chat`      | Send a message and get AI reply |
| POST   | `/api/followup`  | Get follow-up question suggestions |
| GET    | `/api/test`      | Test if the API is working      |
---
## 📝 License
This project is open source and available under the [MIT License](LICENSE).
