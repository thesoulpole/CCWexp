# Hello API - FastAPI + Frontend Application

A simple but elegant full-stack application built with FastAPI backend and a modern frontend interface. This project was created using Claude Flow swarm intelligence for coordinated development.

## 🚀 Features

- **FastAPI Backend**: RESTful API with automatic documentation
- **Modern Frontend**: Beautiful, responsive UI with animations
- **CORS Enabled**: Frontend can communicate with backend seamlessly
- **Health Checks**: Monitor API status in real-time
- **Personalized Greetings**: Optional name parameter for custom messages

## 📁 Project Structure

```
.
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html          # Frontend application
└── README.md               # This file
```

## 🛠️ Setup & Installation

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   python main.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Serve the HTML file using any web server. Options include:

   **Option 1: Python's built-in server**
   ```bash
   python -m http.server 3000
   ```

   **Option 2: Node's http-server (if installed)**
   ```bash
   npx http-server -p 3000
   ```

   **Option 3: Open directly in browser**
   Simply open `frontend/index.html` in your web browser.

The frontend will be available at `http://localhost:3000` (or file://... if opened directly)

## 🌐 API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /api/hello?name=YourName` - Get personalized greeting
- `GET /api/health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## 🎯 Usage

1. Start the backend server (port 8000)
2. Open the frontend in your browser
3. The page will automatically check if the API is online
4. Enter your name (optional) and click "Say Hello!"
5. See the personalized greeting from the API

## 🐝 Built with Claude Flow Swarm

This application demonstrates the power of AI-driven swarm development using Claude Flow:
- Multi-agent coordination for backend and frontend development
- Intelligent code generation and optimization
- Integrated testing and validation

To use Claude Flow swarm for similar projects:
```bash
claude-flow swarm "Build a REST API with authentication" --strategy development
```

## 🔧 Development

### Run Backend in Development Mode
```bash
cd backend
uvicorn main:app --reload
```

### Customize the Application

**Backend (backend/main.py)**:
- Add new endpoints
- Integrate database
- Add authentication
- Implement business logic

**Frontend (frontend/index.html)**:
- Modify styles in the `<style>` section
- Update UI elements in the `<body>` section
- Enhance functionality in the `<script>` section

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 💡 Future Enhancements

- Database integration
- User authentication
- WebSocket support for real-time updates
- Docker containerization
- Unit and integration tests
- CI/CD pipeline

---

**Created with ❤️ using Claude Flow and AI Swarm Intelligence**
