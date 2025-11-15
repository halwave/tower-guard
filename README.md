# Tower Guard

Tower-Guard is a lightweight Python service designed to run inside a minimal container and act as a network-awareness monitoring tool.

## 🚀 Features

- Minimal Python application
- Runs inside a lightweight Alpine-based Docker image
- Simple and clean project scaffold
- Easy to build, run, and extend

## ▶️ Running Locally (without Docker)

1. Install Python **3.12+** (Windows users should use the `py` launcher)
2. Install dependencies:

   ```sh
   py -m pip install -r src/requirements.txt
   ```

3. Run the app:

   ```sh
   py src/main.py
   ```

You should see:

```
Hello from Tower-Guard!
```

## 🐳 Running with Docker Compose

### Start the service (build if needed):

```sh
docker compose up --build
```

### Run in detached mode:

```sh
docker compose up -d --build
```

### Stop the service:

```sh
docker compose down
```
