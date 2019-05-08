# Mailbot

- Docker image based on this blog post: http://tuxtweaks.com/2012/10/send-gmail-from-the-linux-command-line/

- Make the file `msmtprc` by running `python3 make-msmtprc.py <sender gmail account> <sender gmail password>`

- Build the image by running `./build-image`

- You can open the container with `./open-container` script if you like but probably easier to run an instance
of the image and use `docker run ...` from the host machine instead. I should have added some scripts for that.

- Send emails from within the container by running `./send-mail <recipient email address> <subject> <message>`
