# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Start the Backend

```bash
cd /home/user/CCWexp
./start-backend.sh
```

The FastAPI backend will start on `http://localhost:8000`

**API Endpoints:**
- Root: `http://localhost:8000/`
- Hello: `http://localhost:8000/api/hello?name=YourName`
- Health: `http://localhost:8000/api/health`
- Docs: `http://localhost:8000/docs` (Interactive Swagger UI)

### Step 2: Start the Frontend

Open a new terminal and run:

```bash
cd /home/user/CCWexp
./start-frontend.sh
```

The frontend will be available at `http://localhost:3000`

### Step 3: Test the Application

1. Open your browser to `http://localhost:3000`
2. You should see the beautiful gradient interface
3. The API status should show "✅ API is online and ready"
4. Enter your name (optional) and click "Say Hello! 🚀"
5. Watch the personalized greeting appear!

## 🧪 Manual Testing

Test the API directly with curl:

```bash
# Test health
curl http://localhost:8000/api/health

# Test hello without name
curl http://localhost:8000/api/hello

# Test hello with name
curl "http://localhost:8000/api/hello?name=Claude"

# View API docs in browser
open http://localhost:8000/docs
```

## 🐝 Claude Flow Swarm Usage

This project was built using Claude Flow swarm intelligence. To create similar projects:

### Initialize Claude Flow
```bash
claude-flow init
```

### Spawn a Development Swarm
```bash
claude-flow swarm "Build a REST API with frontend" --strategy development --max-agents 3
```

### Analyze Code Quality
```bash
claude-flow swarm "Review code for security and best practices" --analysis --strategy research
```

### Use Hive Mind for Complex Projects
```bash
claude-flow hive-mind wizard
```

## 📝 Project Features

✅ **Backend (FastAPI)**
- RESTful API with automatic documentation
- CORS enabled for cross-origin requests
- Health check endpoint
- Pydantic models for request/response validation
- Async/await support

✅ **Frontend (HTML/CSS/JS)**
- Modern gradient design with purple theme
- Smooth animations and transitions
- Real-time API health monitoring
- Loading states and error handling
- Responsive layout for all screen sizes
- Accessible form controls

✅ **Developer Experience**
- One-command startup scripts
- Virtual environment management
- Comprehensive documentation
- Git workflow with meaningful commits
- Clean project structure

## 🛠️ Tech Stack

- **Backend**: Python 3.x, FastAPI, Uvicorn, Pydantic
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Development**: Claude Flow Swarm, Git
- **Deployment**: Can be containerized with Docker

## 📚 Next Steps

1. **Add Authentication**: Implement JWT or OAuth
2. **Database Integration**: Add PostgreSQL or MongoDB
3. **Testing**: Write unit and integration tests
4. **Docker**: Containerize both services
5. **CI/CD**: Set up GitHub Actions
6. **Monitoring**: Add logging and metrics
7. **WebSockets**: Real-time features

## 🤝 Contributing

This project demonstrates AI-assisted development using Claude Flow. Feel free to:
- Add new features
- Improve the UI/UX
- Enhance security
- Optimize performance
- Write tests

---

**Built with ❤️ using Claude Flow Swarm Intelligence**
