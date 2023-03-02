FROM python:3.9.16

WORKDIR /src/

ADD requirements.txt .

# speed up for china, not needed in other area
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip config set install.trusted-host mirrors.aliyun.com

#RUN pip install tiktoken==0.2.0
#RUN pip install openai==0.26.4
#RUN pip install asyncio==3.4.3
#RUN pip install websockets==10.4
#RUN pip install Flask==2.2.2
#RUN pip install Flask-Cors==3.0.10
#RUN pip install loguru==0.6.0
#RUN pip install requests==2.28.2
#RUN pip install pydantic==1.10.4
#RUN pip install pyyaml==6.0

RUN pip install -r requirements.txt

ADD *.yml *.py ./

ENTRYPOINT [ "python3", "app.py"]
