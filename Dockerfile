FROM python:3.12
WORKDIR /dkr/foxcalc-cli

COPY * ./
EXPOSE 5000

CMD ["python", "fxclcc.py"]