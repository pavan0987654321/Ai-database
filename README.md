# AskDB AI - Natural Language Database Query System

> **Transform natural language questions into SQL queries with AI-powered intelligence**

A modern, full-stack application that allows users to query MySQL databases using natural language or direct SQL, featuring a beautiful Apple-inspired React dashboard and a Python backend powered by LangChain and OpenRouter.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Security Features](#security-features)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

**AskDB AI** is a dual-interface database query system:

1. **Dashboard (Natural Language)**: Ask questions in plain English, get AI-generated SQL and results
2. **Query Builder (Direct SQL)**: Write and execute SQL queries directly with a visual editor

The system uses **OpenRouter's GPT-4o-mini** for natural language processing and connects to a **MySQL database** containing t-shirt inventory data.

---

## ✨ Features

### 🤖 AI-Powered Query Generation
- Natural language to SQL conversion
- Context-aware query suggestions
- Intelligent error handling

### 🔒 Security & Safety
- **Read-only mode** - Blocks destructive SQL operations (DELETE, DROP, UPDATE, etc.)
- SQL injection prevention
- Query validation before execution

### 🎨 Modern UI/UX
- **Apple-inspired design** with glassmorphism effects
- Dark mode optimized
- Smooth animations and micro-interactions
- Responsive layout (desktop & mobile)

### 📊 Dashboard Features
- Real-time metrics (queries, users, response time, uptime)
- Recent query history with rerun capability
- SQL panel with syntax highlighting
- Query execution stats (time, row count)
- Error states with helpful messages

### 🛠️ Query Builder
- Visual table browser
- SQL editor with auto-complete
- Direct SQL execution (SELECT only)
- Real-time query validation
- Results table with formatting

### 🚀 Performance
- Fast API responses (<1s average)
- Skeleton loaders for better UX
- Optimized database queries
- CORS-enabled for cross-origin requests

---

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool & dev server
- **React Router** - Client-side routing
- **Lucide React** - Icon library
- **Tailwind CSS** - Utility-first CSS (custom design system)

### Backend
- **Python 3.10+** - Runtime
- **Flask** - REST API framework
- **Flask-CORS** - Cross-origin resource sharing
- **PyMySQL** - MySQL database connector
- **LangChain** - AI orchestration (for Streamlit app)
- **OpenRouter** - LLM API gateway

### Database
- **MySQL 8.0+** - Relational database
- **atliq_tshirts** - Sample database with 100 records

### AI/LLM
- **OpenRouter API** - GPT-4o-mini model
- **Few-shot learning** - Example-based query generation

---

## 📁 Project Structure

```
4_sqldb_tshirts/
├── askdb-dashboard/              # React Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── dashboard/        # Dashboard-specific components
│   │   │   │   ├── MetricCard.jsx
│   │   │   │   ├── QuerySection.jsx
│   │   │   │   ├── QueryStats.jsx
│   │   │   │   ├── SQLPanel.jsx
│   │   │   │   └── RecentQueries.jsx
│   │   │   ├── layout/           # Layout components
│   │   │   │   ├── Layout.jsx
│   │   │   │   ├── Navbar.jsx
│   │   │   │   └── Sidebar.jsx
│   │   │   └── ui/               # Reusable UI components
│   │   │       ├── Button.jsx
│   │   │       ├── GlassCard.jsx
│   │   │       ├── DataTable.jsx
│   │   │       ├── Input.jsx
│   │   │       ├── Skeleton.jsx
│   │   │       ├── States.jsx (Empty, Error)
│   │   │       ├── AlertBanner.jsx
│   │   │       └── ReadOnlyBadge.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx     # Main dashboard page
│   │   │   ├── QueryBuilder.jsx  # SQL editor page
│   │   │   ├── History.jsx       # Query history page
│   │   │   ├── Settings.jsx      # Settings page
│   │   │   └── Login.jsx         # Login page
│   │   ├── services/
│   │   │   └── api.js            # API client
│   │   ├── utils/
│   │   │   ├── sqlSafety.js      # SQL validation
│   │   │   └── demoMode.js       # Demo mode utilities
│   │   ├── context/
│   │   │   └── ThemeContext.jsx  # Dark mode context
│   │   ├── App.jsx               # Root component
│   │   ├── index.css             # Global styles
│   │   └── main.jsx              # Entry point
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── database/
│   └── db_setup.sql              # Database schema & seed data
│
├── api_server.py                 # Flask REST API server
├── main.py                       # Streamlit app (alternative UI)
├── langchain_helper.py           # LangChain AI logic
├── .env                          # Environment variables
└── README.md                     # This file
```

---

## 📦 Installation

### Prerequisites

- **Node.js 18+** and npm
- **Python 3.10+** and pip
- **MySQL 8.0+** server running
- **OpenRouter API key** ([Get one here](https://openrouter.ai/))

### Step 1: Clone the Repository

```bash
cd c:\Users\G Pavan\Downloads\langchain-main\langchain-main\4_sqldb_tshirts
```

### Step 2: Set Up the Database

```bash
# Login to MySQL
mysql -u root -p

# Run the setup script
source database/db_setup.sql

# Verify data
USE atliq_tshirts;
SELECT COUNT(*) FROM t_shirts;  # Should return 100
```

### Step 3: Install Python Dependencies

```bash
pip install flask flask-cors pymysql python-dotenv
```

### Step 4: Install Frontend Dependencies

```bash
cd askdb-dashboard
npm install
cd ..
```

---

## ⚙️ Configuration

### Environment Variables

Create/edit `.env` file in the project root:

```env
# AI API Keys
GOOGLE_API_KEY='your_google_api_key_here'
OPENROUTER_API_KEY=sk-or-v1-your_openrouter_key_here

# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=atliq_tshirts
```

> **⚠️ Important**: Never commit `.env` to version control!

### Frontend Configuration (Optional)

Create `askdb-dashboard/.env` if you need custom API URL:

```env
VITE_API_URL=http://localhost:8000/api
```

---

## 🚀 Running the Application

You need to run **3 separate terminals**:

### Terminal 1: MySQL Server
```bash
# Make sure MySQL is running
# On Windows: Check Services or run:
net start MySQL80
```

### Terminal 2: Backend API Server
```bash
cd c:\Users\G Pavan\Downloads\langchain-main\langchain-main\4_sqldb_tshirts
python api_server.py
```

**Output:**
```
============================================================
🚀 AskDB AI - Backend API Server (SQL Execution Only)
============================================================
📊 Database: atliq_tshirts
🌐 API URL: http://localhost:8000
📝 Endpoints:
   - POST /api/execute-sql (Direct SQL execution)
   - GET  /api/database/tables
   - GET  /api/database/info
============================================================
✅ Server is ready! You can now use the Query Builder.
============================================================
```

### Terminal 3: React Frontend
```bash
cd c:\Users\G Pavan\Downloads\langchain-main\langchain-main\4_sqldb_tshirts\askdb-dashboard
npm run dev
```

**Output:**
```
VITE v7.3.1  ready in 1401 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

### Access the Application

Open your browser and navigate to:
- **Dashboard**: http://localhost:5173/
- **Query Builder**: http://localhost:5173/queries

---

## 📖 Usage Guide

### Dashboard (Natural Language Queries)

1. Navigate to **Dashboard** (home page)
2. Type a question in plain English:
   - "How many Nike t-shirts are in stock?"
   - "Show me all t-shirts under $25"
   - "What's the total inventory by brand?"
3. Click **"Ask"** or press Enter
4. View:
   - Generated SQL query (collapsible panel)
   - Query execution stats (time, row count)
   - Results table with formatted data

**Example Questions:**
```
✅ "Show all white t-shirts"
✅ "How many Adidas products do we have?"
✅ "List t-shirts with stock below 50"
✅ "What's the average price by brand?"
```

### Query Builder (Direct SQL)

1. Navigate to **Query Builder** from sidebar
2. Click a table name to auto-fill a SELECT query
3. Or write your own SQL:
   ```sql
   SELECT brand, COUNT(*) as count, AVG(price) as avg_price
   FROM t_shirts
   GROUP BY brand
   ORDER BY count DESC;
   ```
4. Click **"Run"** button
5. View results in the table below

**Allowed Operations:**
- ✅ SELECT queries only
- ❌ INSERT, UPDATE, DELETE (blocked for safety)

---

## 🔌 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Endpoints

#### 1. Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "ok",
  "message": "API is running"
}
```

---

#### 2. Execute SQL Query
```http
POST /api/execute-sql
Content-Type: application/json

{
  "sql": "SELECT * FROM t_shirts LIMIT 10"
}
```

**Response (Success):**
```json
{
  "results": [
    {
      "id": 1,
      "brand": "Nike",
      "color": "White",
      "size": "M",
      "price": 25.99,
      "stock": 150
    }
  ],
  "execution_time": 45,
  "row_count": 10
}
```

**Response (Error):**
```json
{
  "error": "Only SELECT queries are allowed"
}
```

---

#### 3. Get Database Tables
```http
GET /api/database/tables
```

**Response:**
```json
{
  "tables": ["t_shirts", "customers", "orders"]
}
```

---

#### 4. Get Database Info
```http
GET /api/database/info
```

**Response:**
```json
{
  "tables": 3,
  "totalRows": "24,580",
  "lastSync": "Just now"
}
```

---

#### 5. Get Metrics
```http
GET /api/metrics/queries
GET /api/metrics/users
GET /api/metrics/response-time
GET /api/metrics/uptime
```

**Response Example:**
```json
{
  "value": "1,284",
  "change": "+12.5%",
  "changeType": "increase"
}
```

---

## 🔒 Security Features

### SQL Safety System

The application implements multiple layers of security:

1. **Read-Only Mode**
   - Only SELECT queries are allowed
   - All destructive operations are blocked:
     - DELETE, DROP, TRUNCATE
     - UPDATE, INSERT, ALTER
     - CREATE, GRANT, REVOKE

2. **Query Validation**
   - SQL is sanitized before execution
   - Comments are removed
   - Whitespace is normalized

3. **Error Handling**
   - Clear, user-friendly error messages
   - No raw SQL errors exposed to users
   - API key validation

4. **Visual Indicators**
   - "Read-only mode" badge in header
   - Warning messages for blocked queries
   - Connection status indicator

### Implementation

```javascript
// Frontend validation (sqlSafety.js)
function isDestructiveQuery(sql) {
  const destructiveKeywords = [
    'DELETE', 'DROP', 'TRUNCATE',
    'UPDATE', 'INSERT', 'ALTER',
    'CREATE', 'GRANT', 'REVOKE'
  ];
  // ... validation logic
}
```

```python
# Backend validation (api_server.py)
sql_upper = sql.strip().upper()
if not sql_upper.startswith('SELECT'):
    return jsonify({'error': 'Only SELECT queries are allowed'}), 403
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "Backend server is not responding"

**Cause:** API server not running or wrong port

**Solution:**
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Restart API server
python api_server.py
```

---

#### 2. "localhost refused to connect"

**Cause:** React dev server not running

**Solution:**
```bash
cd askdb-dashboard
npm run dev
```

---

#### 3. Database Connection Error

**Cause:** MySQL not running or wrong credentials

**Solution:**
```bash
# Check MySQL service
net start MySQL80

# Verify credentials in .env
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=atliq_tshirts
```

---

#### 4. "Live AI responses are currently unavailable"

**Cause:** Missing or invalid API key

**Solution:**
```bash
# Check .env file
OPENROUTER_API_KEY=sk-or-v1-your_key_here

# Verify key at https://openrouter.ai/
```

---

#### 5. CORS Errors in Browser Console

**Cause:** Flask-CORS not installed

**Solution:**
```bash
pip install flask-cors
```

---

### Debug Mode

Enable detailed logging:

**Frontend (Browser Console):**
```javascript
// Already enabled in QueryBuilder.jsx
console.log('=== Query Builder: Execute Started ===');
```

**Backend (Terminal):**
```python
# Already enabled in api_server.py
print("📥 Received SQL execution request")
print(f"SQL Query: {sql}")
```

---

## 📊 Database Schema

### t_shirts Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key |
| brand | VARCHAR(50) | Brand name (Nike, Adidas, etc.) |
| color | VARCHAR(30) | Color name |
| size | VARCHAR(10) | Size (XS, S, M, L, XL, XXL) |
| price | DECIMAL(10,2) | Price in USD |
| stock | INT | Quantity in stock |

**Sample Data:**
```sql
SELECT * FROM t_shirts LIMIT 3;
```

| id | brand | color | size | price | stock |
|----|-------|-------|------|-------|-------|
| 1 | Nike | White | M | 25.99 | 150 |
| 2 | Adidas | Black | L | 29.99 | 89 |
| 3 | Puma | Red | XL | 27.99 | 67 |

---

## 🎨 Design System

### Color Palette

```css
/* Dark Mode */
--bg-base: #0c0e12;
--bg-elevated: rgba(20, 24, 30, 0.92);
--bg-card: rgba(18, 22, 28, 0.65);

--text-primary: rgba(255, 255, 255, 0.95);
--text-secondary: rgba(255, 255, 255, 0.65);
--text-tertiary: rgba(255, 255, 255, 0.40);

--accent: #3b82f6;
--success: #10b981;
--warning: #f59e0b;
--error: #ef4444;
```

### Typography

```css
font-family: -apple-system, BlinkMacSystemFont, 
             "SF Pro Display", "SF Pro Text", 
             Inter, "Segoe UI", sans-serif;
```

### Glassmorphism

```css
.glass {
  background: var(--bg-card);
  backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06);
}
```

---

## 📝 License

This project is for educational purposes.

---

## 👨‍💻 Author

**G Pavan**

---

## 🙏 Acknowledgments

- **LangChain** - AI orchestration framework
- **OpenRouter** - LLM API gateway
- **Lucide** - Beautiful icon library
- **Apple** - Design inspiration

---

## 📞 Support

If you encounter any issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Enable debug logging (already enabled)
3. Check browser console (F12)
4. Check API server terminal output

---

**Made with ❤️ by G Pavan**
