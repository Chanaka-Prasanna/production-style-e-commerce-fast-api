# 1. Base image
FROM python:3.12.4

# 2. Set working directory
WORKDIR /app

# 3. Copy & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy app code
COPY . .

# 5. Expose port & startup command
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
