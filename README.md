This project is a Split Bill Management API built using FastAPI and SQLAlchemy, designed to help users manage shared expenses easily and securely. The application allows users to create bills, add participants, track who paid and who owes money, and settle expenses transparently.

The API uses JWT (JSON Web Tokens) for authentication, ensuring secure access to protected endpoints. A clean layered architecture is followed (Routes → Services → Repositories → Models) to keep the codebase modular, scalable, and easy to maintain.

✨ Key Features

User authentication using JWT Bearer tokens

Secure password hashing with bcrypt

Create and manage bills

Add bill participants with paid and owed amounts

Track settlement status for bills and participants

Protected endpoints using FastAPI dependencies

Swagger (OpenAPI) support for easy API testing

🛠 Tech Stack

FastAPI – High-performance web framework

SQLAlchemy – ORM for database interactions

JWT – Secure authentication and authorization

PostgreSQL / SQLite – Database support

Pydantic – Data validation and serialization

This project is suitable for learning real-world API design, authentication flows, and clean backend architecture using FastAPI.
