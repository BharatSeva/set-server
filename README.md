# Bharatseva Server Repository

This repository provides **Docker** service containers that enable frontend developers to test and integrate their applications in a production-like environment. Use these containers to quickly set up the backend services needed for the Bharatseva project.

## Features

- **Dockerized Environment:** All services are containerized for easy deployment.
- **Modular Setup:** Each service runs in its own container, making it simpler to manage and scale.
- **Quick Testing:** Rapidly spin up the necessary backend environment to test frontend changes.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/bharatseva-server.git
    cd bharatseva-server
    ```

2. **Build and Run Docker Containers:**

    ```bash
    docker-compose up -d --build
    ```

3. **Create User Profiles:**

    ```bash
    python createuser.py
    ```

##### You'll get profile.txt file after above step, use it as your credentials for login

## Service Ports

Ensure the following ports are **not** in use before running the containers:

- **3001**
- **3002**
- **5432**
- **27017**
- **5672**
- **15672**
- **6379**

These ports are reserved for the respective backend services.

---

If you encounter any issues or have suggestions, feel free to open an issue in this repository. Happy coding!
