FROM ubuntu:12.04

EXPOSE 587
EXPOSE 25
EXPOSE 465

COPY msmtprc /root/.msmtprc
COPY mailrc /root/.mailrc
COPY send-mail /send-mail

RUN apt-get update && \
    apt-get install  -y --no-install-recommends ca-certificates && \
    apt-get -y dist-upgrade && \
    apt-get -y install msmtp-mta && \
    apt-get -y install heirloom-mailx

