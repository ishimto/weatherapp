# WeatherApp

A web application for checking weather forecasts with a dynamic UI and a contact form.

## Features

- Search for weather forecasts by city.
- Choose number of forecast days.
- Dynamic backgrounds based on weather conditions.
- Error handling with user-friendly messages.
- Contact form for user feedback.
- Modular code structure and logging.
- Docker support for easy deployment.

## Project Structure

```
.
├── Dockerfile
├── web_app/
│   ├── backend_weather.py
│   ├── requirements.txt
│   ├── server.py
│   ├── wsgi.py
│   ├── background/
│   │   ├── cloudy.txt
│   │   ├── dunny_rope.jpeg
│   │   ├── overcast.txt
│   │   ├── rain.txt
│   │   ├── snow.txt
│   │   └── sunny.txt
│   ├── modules/
│   │   ├── api_request.py
│   │   ├── basemodels.py
│   │   ├── consts.py
│   │   └── envs.py
│   ├── server_logs/
│   │   └── logs.py
│   ├── templates/
│   │   ├── contact_us.html
│   │   ├── error.html
│   │   ├── index.html
│   │   ├── index.html.bak
│   │   └── weather.html
│   └── tests/
│       ├── api_mock.py
│       ├── api_request.py
│       ├── backend_weather.py
│       ├── basemodels.py
│       ├── browser_test.py
│       ├── test_parse.py
│       └── test_response.py
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- (Optional) Docker

### Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd web_app
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```sh
   gunicorn -b 0.0.0.0:8000 wsgi:app
   ```
   The app will be available at [http://localhost:8000](http://localhost:8000).

### Environment Variables

Set the following environment variables (with Docker, Docker Compose, Kubernetes, or your shell):

- `API_KEY`: Your weather API key (required).
- `FLAGS_instanceID`: Instance ID for feature flags or deployment tracking (optional).
- `FLAGS_URL`: URL for feature flags or remote config (optional).
- `FLAGS_APP`: Application name for feature flags or remote config (optional).
- `BG_COLOR`: Default background color for the UI (optional).
- `APP_VERSION`: Application version string (optional).

**Example Docker run:**
```sh
docker run -p 8000:8000 \
  -e API_KEY=your_api_key \
  -e FLAGS_instanceID=your_instance_id \
  -e FLAGS_URL=https://flags.example.com \
  -e FLAGS_APP=weatherapp \
  -e BG_COLOR="#ffffff" \
  -e APP_VERSION="1.0.0" \
  weatherapp
```

**Example Docker Compose:**
```yaml
services:
  weatherapp:
    image: weatherapp
    ports:
      - "8000:8000"
    environment:
      API_KEY: "your_api_key"
      FLAGS_instanceID: "your_instance_id"
      FLAGS_URL: "https://flags.example.com"
      FLAGS_APP: "weatherapp"
      BG_COLOR: "yellow"
      APP_VERSION: "1.0.0"
```

## Running Tests

```sh
pytest tests/
```

## File Overview

- `web_app/backend_weather.py`: Weather data processing logic.
- `web_app/server.py`: Main Flask server.
- `web_app/templates/`: HTML templates for UI.
- `web_app/background/`: Weather background images/links.
- `web_app/modules/`: API requests, models, and constants.
- `web_app/server_logs/logs.py`: Logging utilities (disabled with "#").
- `web_app/tests/`: Unit and integration tests.

## License

This project is for educational purposes.