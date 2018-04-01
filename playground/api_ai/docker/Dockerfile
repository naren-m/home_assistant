FROM narenm/dev-env

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN apt-get update -y && apt-get install -y python-pyaudio 

RUN pip install apiai
