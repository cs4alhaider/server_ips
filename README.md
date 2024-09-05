# IP Logger FastAPI Project

This project is a simple FastAPI application that logs and displays client IP addresses. It demonstrates basic usage of FastAPI, Pydantic models, and request handling.

## Main Features

1. **IP Logging**: The application logs the IP address of each client that accesses the root endpoint ("/").

2. **Display Current IP**: When a client accesses the root endpoint, it returns the client's IP address and the current timestamp.

3. **IP Log Retrieval**: There's an endpoint ("/ip-log") that returns the entire log of IP addresses and their corresponding timestamps.

## Key Components

- **FastAPI Application**: The main FastAPI app is initialized in `main.py`.

- **Pydantic Model**: `IPLogEntry` is a Pydantic model used to structure the IP log entries, ensuring type safety.

- **In-Memory Storage**: The `ip_log` list stores the IP log entries in memory.

- **Endpoints**:
  - `GET /`: Logs the client's IP and returns it with a timestamp.
  - `GET /ip-log`: Returns the entire IP log.

## Note on Middleware

There's a commented-out middleware function that could be used to log IP addresses for all requests. It's currently not in use, but could be enabled for more comprehensive logging.

## Running the Application

The application is containerized using Docker. The `Dockerfile` and `requirements.txt` in the project ensure that all necessary dependencies are installed and the application runs in a consistent environment.

To run the application, build the Docker image and run it, exposing port 80.

This project serves as a simple example of building a FastAPI application with basic logging functionality.
