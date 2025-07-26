# Simple Login
## Description
Simple login using react (frontend) and django-rest-framework (backend)
- [x] Add docker
- [x] Add frontend
- [x] Add backend
- [ ] Add styles
- [ ] Add validations and errors
- [ ] Add redirect after success login
- [ ] [Using CSRF protection with AJAX or fetch](https://docs.djangoproject.com/en/5.1/howto/csrf/#using-csrf-protection-with-ajax)

## How to Run

### Prerequisites
- Docker and Docker Compose installed on your system
- Git (to clone the repository)

### Option 1: Using Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd simple-login
   ```

2. **Start all services with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Frontend (React): http://localhost:5173
   - Backend API (Django): http://localhost:8000
   - Database: PostgreSQL running on localhost:5432

4. **To run in background:**
   ```bash
   docker-compose up -d --build
   ```

5. **To stop the services:**
   ```bash
   docker-compose down
   ```

### Option 2: Manual Setup (Development)

#### Backend Setup
1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database (PostgreSQL):**
   - Make sure PostgreSQL is running
   - Create database with credentials matching docker-compose.yml:
     - Database: `sampledb`
     - User: `userdb`
     - Password: `secretdb`
     - Port: `5432`

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start Django development server:**
   ```bash
   python manage.py runserver
   ```

#### Frontend Setup
1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

### Application URLs
- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Database:** localhost:5432

### Useful Commands

- **View logs:**
  ```bash
  docker-compose logs -f
  ```

- **Access backend container:**
  ```bash
  docker-compose exec backend bash
  ```

- **Access frontend container:**
  ```bash
  docker-compose exec frontend sh
  ```

- **Rebuild specific service:**
  ```bash
  docker-compose up --build backend
  docker-compose up --build frontend
  ```
