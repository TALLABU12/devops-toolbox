FROM python:3.11-slim
RUN groupadd -r appuser && useradd -r -g appuser appuser
WORKDIR /app
COPY app.py .
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
