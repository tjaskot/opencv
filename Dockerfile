FROM python:3.10
#ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD ["python3", "main2.py", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]