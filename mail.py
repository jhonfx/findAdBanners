import imaplib

msrvr = imaplib.IMAP4_SSL\
  ('mail.twinkey.cool', 993)

user = 'juan.purata@twinkey.cool'
pwd = "Twinkey23"
msrvr.login(user,pwd)

msrvr.select()
typ, data = msrvr.search(None, 'ALL')
for num in data[0].split():
    typ, data = msrvr.fetch(num, '(dashboard)')
    print 'Message %s\n%s\n' % (num, data[0][1])
msrvr.close()

# stat,count = msrvr.select('Inbox')
# stat,data = msrvr.fetch\
#   (count[0],\
#     '(UID BODY[TEXT])')


# print data[0][1]


# msrvr.close()