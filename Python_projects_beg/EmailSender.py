import smtplib
#https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4PLt7PKxWXD-qwDCIM7KhihnMX0zd6nsNdUkw-Kq5BlVji2n-2aslKjRo1-VVWs75MZC6RyynGu0KAol5DGDSEEyWp52ZpUewns555QiKqYb2tzg_E 
EMAIL1 = 'xxxxxxxx@gmail.com'
STUDENT_EMAIL = 'xxxxxxxx@st.swps.edu.pl'
price = 4 # price is the 2nd element in the list
if price<10:
    #For Gmail, we use port number 587
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # start TLS for security
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Authentication
    server.login(EMAIL1, "xxxxxxxxx")
    subj = "The price is now lower!"
    body = "Go and buy it on Amazon"
    # message to be sent
    message = f"Subject: {subj}\n\n{body}"
        # sending the mail
    server.sendmail(EMAIL1,STUDENT_EMAIL,message)
    # terminating the session
    server.quit()