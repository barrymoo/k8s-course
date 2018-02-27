FROM python:3
ADD app.py requirements.txt /
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
CMD ["flask", "run", "-h", "0.0.0.0"]
