# IP Logger Through an API

This project is a simple API application that logs and displays client IP addresses. It demonstrates basic usage of FastAPI, Pydantic models, and request handling.

## Main Features

1. **IP Logging**: The application logs the IP address of each client that accesses the "/capture-my-ip" endpoint.

2. **Display Current IP**: When a client accesses the "/capture-my-ip" endpoint, it returns the client's IP address and the current timestamp.

3. **IP Log Retrieval**: There's an endpoint ("/ip-log") that returns the entire log of IP addresses and their corresponding timestamps.

4. **Clear IP Log**: An endpoint ("/clear-ip-log") allows clearing the entire IP log.

## Key Components

- **FastAPI Application**: The main FastAPI app is initialized in `main.py`.

- **Pydantic Model**: `IPLogEntry` is a Pydantic model used to structure the IP log entries, ensuring type safety. It includes fields for IP address and timestamp.

- **In-Memory Storage**: The `ip_log` list stores the IP log entries in memory.

- **Endpoints**:
  - `GET /`: Returns a welcome message and the source code link.
  - `GET /capture-my-ip`: Logs the client's IP and timestamp, and returns this information.
  - `GET /ip-log`: Returns the entire IP log.
  - `DELETE /clear-ip-log`: Clears the IP log.

## Note on Middleware

There's a commented-out middleware function that could be used to log IP addresses for all requests. It's currently not in use, but could be enabled for more comprehensive logging.

## Running the Application

To run the application, you need to have FastAPI and its dependencies installed. You can then run the FastAPI server using a command like `fastapi run main.py`.

This project serves as a simple example of building a FastAPI application with basic logging functionality and demonstrates how to handle and log client information.

## Source Code

The source code for this project is available at: https://github.com/cs4alhaider/server_ips
