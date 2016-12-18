FROM narenm/dev-env

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY test_supd.py /

WORKDIR /

RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor


WORKDIR /
CMD ["/usr/bin/supervisord"]
