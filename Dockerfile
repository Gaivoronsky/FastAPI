FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt update && apt upgrade -y && apt install python3-pip git -y
EXPOSE 80
WORKDIR /usr/src/app
RUN git clone https://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@github.com/kompotiks/FastAPI.git
WORKDIR FastAPI
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python create_base.py
CMD python -m workshop