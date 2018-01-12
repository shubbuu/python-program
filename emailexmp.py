import sys
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login(sys.argv[1], 'hbpkyxjnuvkdtzll')
conn.sendmail(sys.argv[1], sys.argv[2], ' '.join(sys.argv[3:]))
conn.quit()
