FROM continuumio/anaconda3

COPY . /quote-notifier

WORKDIR /quote-notifier

ENTRYPOINT ["python"]

CMD ["quotenotifier.py", "-i", "1440"]
