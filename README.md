# client-mgmt


This project provides a web interface for managing clients using the Arianee Custody API. Users can create clients, view client information, and update existing clients.

## Prerequisites

- Python 3 or higher
- Flask
- Requests

## Installation

1. **Clone the repository:**
   ```bash
  git clone https://github.com/radia2/client-mgmt.git
  cd client-mgmt


2. **Set up a virtual environment:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set environment variables:**
 ```bash
   REACT_APP_API_KEY=your_api_key
```
## Usage

1 **Run the flask app**
   ```bash
   flask run
   ```
3. **Access the application**
   Open your web browser and go to http://127.0.0.1:5000

## Features
You will find the different features listed in this miro: 
<img width="784" alt="Screenshot 2024-06-12 at 11 50 25" src="https://github.com/user-attachments/assets/c9d64434-c632-4892-921c-1bfad6fec3d2">

- Create Client: Allows you to create a new signing client.
- View Client Information: Retrieves and displays information about a specific signing client.
- Update Client: Updates the details of an existing signing client.
















