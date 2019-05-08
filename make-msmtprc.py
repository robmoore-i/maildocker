import sys

if len(sys.argv) != 3:
  print("Usage: python3 make-msmtprc.py <sender gmail address> <sender gmail password>")
  exit(1)

contents = """
#Gmail account
defaults
logfile ~/msmtp.log

account gmail
auth on
host smtp.gmail.com
from {}
auth on
tls on
tls_starttls on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
user {}
password {}
port 587

account default : gmail
""".format(sys.argv[1], sys.argv[2], sys.argv[1])

with open("msmtprc", "w+") as f:
  f.write(contents)
