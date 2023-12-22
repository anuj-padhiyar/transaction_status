# Zywa Card Status API with Flask and MongoDB

## Project Overview

This project implements a RESTful API using Flask and MongoDB, housed within a Docker container. The API exposes two main endpoints:

1. `/update_details`: This API endpoint is designed to update all data from CSV files to the MongoDB database.

2. `/get_card_details/<card_id>`: This API endpoint takes a `card_id` parameter and returns the status of the specified card from the MongoDB database.

## Technology Stack

- Language: Python
- Framework: Flask
- Database: MongoDB
- Containerization: Docker

## Implementation Details

### Flask and MongoDB

- **Flask Framework**: Flask is utilized as a micro web framework written in Python. Its simplicity and flexibility make it well-suited for building the API endpoints.

- **MongoDB Database**: MongoDB, a NoSQL document database, is chosen for its flexibility in handling JSON-like documents, making it suitable for storing card details.

### Docker Container

- **Dockerfile**: Docker is employed for containerization. The Dockerfile sets up the necessary environment and dependencies to run the Flask application within a Docker container.

### API Endpoints

1. **Update Details API** (`/update_details`):
   - This endpoint triggers the update of card details from CSV files to the MongoDB database.
   - It reads data from CSV files in the data folder and updates the corresponding records in the database.

2. **Get Card Details API** (`/get_card_details/<card_id>`):
   - This endpoint takes a `card_id` as a parameter and returns the status of the specified card from the MongoDB database.

## Card Status API Live Demo

Explore the live demo of the Zywa Card Status API at [https://status-uoo3.onrender.com](https://status-uoo3.onrender.com). This interactive demonstration enables you to interact with the API's functionality, allowing you to update card details by making a POST request to the `/update_details` endpoint. Additionally, you can retrieve the status of a specific card by making a GET request to the `/get_card_details/<card_id>` endpoint. The web application provides a hands-on experience of the API's capabilities, offering a real-time glimpse into its functionality. Try it out to see how the API works in action!

