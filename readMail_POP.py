import poplib

mailServer = 'pop.gmail.com'
emailID = 'id@gmail.com'
emailPass = 'password'

## open connection to mail server (Secured using SSL)
myEmailConnection = poplib.POP3_SSL(mailServer)
## print the response message from server
print(myEmailConnection)
print(myEmailConnection.getwelcome())
## set email address
myEmailConnection.user(emailID)
## set password
myEmailConnection.pass_(emailPass)
## get information about the email address
EmailInformation = myEmailConnection.stat()
print("Number of new emails: %s (%s bytes)" % EmailInformation)
## Reading an email
print("\n\n===\nRead messages\n===\n\n")

## Read all emails
print("*"*10)
print(EmailInformation)
print("*"*10)
numberofmails = EmailInformation[0]
for i in range(numberofmails):
    print("-" * 10)
    print(i)
    print("-" * 10)
for i in range(numberofmails):
    for email in myEmailConnection.retr(i + 1)[1]:
        print(email)