FROM python:3.12.7

COPY ./requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api
COPY ./model /code/model

ENV WEIGHT_PATH=model/mobilenetv3_fashionmnist.pth

EXPOSE 80

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "80"]