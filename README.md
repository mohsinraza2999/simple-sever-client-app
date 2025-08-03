# Simple FastAPI Server-Client App

This is a lightweight FastAPI-based server-client application. It demonstrates basic API handling with GET and POST endpoints, data validation using Pydantic, and dictionary-based data retrieval simulating a database.

## Features

- `GET /` — Basic endpoint to test server availability.
- `POST /send` — Accepts user input and retrieves corresponding data.
- Uses Python dictionary as a mock database.
- Validates request data with Pydantic's `BaseModel`.
- Lightweight and suitable for learning or quick prototyping.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

Install dependencies:

## bash

pip install -r requirements.txt
Running the App
To start the server:

## bash
python server.py

## bash

uvicorn main:app --host 0.0.0.0 --port 8000

## Example Usage
### Request

POST /send
Content-Type: application/json

{
  "key": "desi"
}
### Response

{
  "value": "Apricote","apple"
}
## File Structure
bash
.
├── server.py             # Main FastAPI application
├── clients_side.ipynb    # send queries and recieves responses
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
License
This project is open-source and available under the MIT License.

## Author
Mohsin Raza

## yaml


---

Let me know if you want to include testing instructions, Docker support, or an OpenAPI schema section.
