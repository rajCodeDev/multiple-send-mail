import smtplib as s

ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('rajkumar7655@gmail.com',6255)
subject = "test python"
body = "i love python"
massage = "subject:{}/n/n{}".format(subject,body)
listadd = ['rajkumar7655@gmail.com,rajaaaaakumar7655@gmail.com,devilsking87@gmail.com']

ob.sendmail('rajkumar7655@gmail.com',listadd,massage)
print("send mail")
ob.quite()

# not right emails