# TradeReads Backend

This is the backend API and real-time messaging server for the TradeReads book exchange platform. It is built with Django, Django REST Framework, and Django Channels, providing robust APIs for user management, book listings, wishlists, and real-time chat.

---

## Features

- **User Authentication**: Register, login, and logout with JWT-based authentication using `dj-rest-auth` and `djangorestframework-simplejwt`.
- **Book Listings**: Users can add, view, and search for books. Each book is linked to its owner and supports image uploads.
- **Wishlist**: Users can add books to their wishlist (many-to-many relationship).
- **Real-Time Messaging**: WebSocket-based chat between users, powered by Django Channels and Daphne.
- **Profile Avatars**: Users can upload and display profile images.
- **RESTful API**: All core features are exposed via REST endpoints.
- **Environment Variables**: Secure configuration using `python-dotenv`.
- **Docker Support**: Ready-to-use Docker and Docker Compose setup for easy deployment.

---

## Tech Stack

- **Django 5**
- **Django REST Framework**
- **Django Channels** (WebSockets)
- **dj-rest-auth**
- **djangorestframework-simplejwt**
- **Pillow** (image handling)
- **python-dotenv**
- **Daphne** (ASGI server)
- **PostgreSQL** (recommended, but SQLite for dev)

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd backend
```

### 2. Environment Variables

Copy `.env.dev` and set your secrets and database config:

```bash
cp .env.dev .env
```

Edit `.env` as needed (see comments in the file for guidance).

### 3. Install Dependencies

Create a virtual environment and install requirements:

```bash
python3 -m venv env
source env/bin/activate
pip install -r trade_reads_backend/requirements.txt
```

### 4. Database Migrations

```bash
python trade_reads_backend/manage.py migrate
```

### 5. Run the Development Server

```bash
python trade_reads_backend/manage.py runserver
```

Or, for real-time features (WebSockets):

```bash
daphne -b 0.0.0.0 -p 8000 trade_reads_backend.trade_reads_backend.asgi:application
```

### 6. Docker (Recommended for Production)

```bash
docker-compose up --build
```

---

## API Overview

- **User Auth**: `/api/auth/register/`, `/api/auth/login/`, `/api/auth/logout/`, `/api/auth/<uuid:pk>/`
- **Books**: `/api/books/`, `/api/books/create/`, `/api/books/<uuid:pk>`, `/api/books/<uuid:pk>/toggle_interest/`
- **Chat**: `/api/chat/`, `/api/chat/start/<uuid:user_id>/`, `/api/chat/<uuid:pk>/`

---

## Core Models

- **User**: Custom user model with UUID primary key, email login, avatar support.
- **Book**: UUID primary key, owner (FK), interested users (M2M), image, metadata.
- **Conversation**: Many-to-many users, tracks chat sessions.
- **ConversationMessage**: Linked to Conversation, sender, recipient, and message body.

---

## Real-Time Messaging

- **WebSocket Endpoint**: `/ws/<room_name>/`
- **Authentication**: JWT token passed as query param.
- **Features**: Join/leave rooms, send/receive messages, persistent chat history.

---

## Testing

Basic test files are scaffolded in each app. Extend these for your own test coverage.

---

## Screenshots

Place backend/admin/API screenshots in `backend/screenshots/` and reference them here:

```
backend/
└── screenshots/
    ├── admin.png
    ├── api-example.png
```

Example:

![Admin Panel](screenshots/admin.png)
![API Example](screenshots/api-example.png)

---

## Development Workflow

- **Agile**: Features developed in small, testable increments.
- **Branching**: Use feature branches for new functionality.
- **CI/CD**: Integrate with your preferred CI for automated testing.

---

## License

MIT

---

## Contact

For questions or contributions, please open an issue or pull request.
