# Dockerfile for Streamlit frontend

# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy frontend files
COPY . /app

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the default Streamlit port
EXPOSE 8501

# 6. Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
