# 🌱 AgriPlay - Gamified Agriculture Learning Platform

![AgriPlay Banner](https://img.shields.io/badge/AgriPlay-Gamified%20Agriculture%20Learning-green?style=for-the-badge&logo=leaf)

A modern, interactive web application that gamifies agricultural education through engaging learning stages, board games, and achievement systems. Built with React TypeScript frontend and FastAPI Python backend.

## 🚀 Features

### 🎯 Core Learning Experience
- **7-Stage Crop Lifecycle**: From seed selection to harvesting
- **Interactive Quizzes**: Test knowledge with immediate feedback  
- **Progress Tracking**: XP, levels, and achievement system
- **Personalized Dashboard**: Track learning journey and stats

### 🎮 Gamification Elements
- **Harvest Quest**: Educational crop management game
- **Board Games**: Agri-Ludo and Pests & Ladders
- **Achievement System**: Earn badges and rewards
- **Leaderboards**: Compete with other learners

### 🎨 Modern UI/UX
- **Smooth Animations**: Framer Motion powered interactions
- **Responsive Design**: Mobile-first approach
- **Dark/Light Themes**: User preference support
- **Accessible Interface**: WCAG compliant design

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for fast development
- **Redux Toolkit** for state management
- **Framer Motion** for animations
- **Tailwind CSS** for styling
- **React Router** for navigation
- **Axios** for API communication

### Backend
- **FastAPI** with Python 3.12+
- **SQLAlchemy 2.0** with SQLite
- **JWT Authentication** with refresh tokens
- **Pydantic** for data validation
- **Uvicorn** ASGI server
- **Structured logging** with context

### Development Tools
- **TypeScript** for type safety
- **ESLint + Prettier** for code quality
- **Playwright** for E2E testing
- **pytest** for backend testing
- **Docker** ready configuration

## 📦 Installation

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.12+ with pip
- **Git** for version control

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agriplay
   ```

2. **Backend Setup**
   ```bash
   cd agri-play/backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Environment Configuration**
   ```bash
   # Backend - copy and configure
   cp backend/.env.example backend/.env
   
   # Frontend - copy and configure  
   cp frontend/.env.example frontend/.env
   ```

5. **Run the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   
   # Terminal 2: Frontend
   cd frontend
   npm run dev
   ```

6. **Access the Application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Docs**: http://localhost:8000/docs

## 🎮 Usage

### For Learners
1. **Register/Login** to create your farming profile
2. **Complete Learning Stages** in sequential order
3. **Take Quizzes** to test your agricultural knowledge
4. **Earn XP and Achievements** as you progress
5. **Play Board Games** with other users
6. **Track Progress** on your personalized dashboard

### For Educators
- Monitor student progress through analytics
- Create custom learning content
- Organize competitions and challenges
- Access detailed learning reports

## 🏗️ Project Structure

```
agri-play/
├── frontend/                 # React TypeScript frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/           # Route components
│   │   ├── store/           # Redux store and slices
│   │   ├── services/        # API service layer
│   │   └── lib/             # Utility libraries
│   ├── public/              # Static assets
│   └── package.json         # Dependencies and scripts
│
├── backend/                 # FastAPI Python backend
│   ├── app/
│   │   ├── models/          # SQLAlchemy database models
│   │   ├── routers/         # FastAPI route handlers
│   │   ├── schemas/         # Pydantic models
│   │   ├── services/        # Business logic layer
│   │   ├── utils/           # Utility functions
│   │   └── main.py          # FastAPI application
│   ├── tests/               # pytest test suite
│   └── requirements.txt     # Python dependencies
│
└── ops/                     # DevOps and deployment
    ├── docker/              # Docker configurations
    └── scripts/             # Automation scripts
```

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm run test              # Run unit tests
npm run test:e2e          # Run E2E tests with Playwright
npm run type-check        # TypeScript validation
```

### Backend Testing  
```bash
cd backend
python -m pytest tests/  # Run all tests
pytest --cov=app         # Run with coverage report
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
```bash
# Frontend build
cd frontend
npm run build

# Backend production
cd backend
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)  
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Agricultural Experts** who provided domain knowledge
- **Educational Consultants** for learning methodology
- **Open Source Community** for excellent libraries and tools
- **Beta Testers** who helped refine the user experience

## 📞 Support

- **Documentation**: [Wiki](wiki-url)
- **Issues**: [GitHub Issues](issues-url)
- **Discussions**: [GitHub Discussions](discussions-url)
- **Email**: support@agriplay.com

---

**Made with ❤️ for agricultural education and sustainable farming practices.**

![Built with](https://img.shields.io/badge/Built%20with-React%20%2B%20FastAPI-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)
