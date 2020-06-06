FROM continuumio/anaconda3

COPY . /quote-notifier

WORKDIR /quote-notifier

RUN conda install -c conda-forge --file requirements.txt

ENTRYPOINT ["python"]

CMD ["quotenotifier.py", "-i", "1440"]
