import ssl
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import ywc_email_template


sender_email = "ywc@webmaster.or.th"
sender_password = input("Input password and hit enter: ")


subject = "[YWC19] ส่งเอกสารรับรองการคัดเลือกเข้าร่วมโครงการ - กุลกาญจน์ เตชะวณิชย์"


msg = MIMEMultipart()
msg["From"] = sender_email

recipients = "thanapat-ja@hotmail.com"
msg["To"] = recipients

# to = "kunlakarn.tcvn@gmail.com"
# cc = "thanapat-ja@hotmail.com"
# recipients = to.split(",") + cc.split(",")
# msg['To'] = to
# msg['Cc'] = cc


msg["Subject"] = subject

msgText = MIMEText(
    ywc_email_template.build_camper_acceptance_letter_email(
        camper_title="นางสาว",
        camper_fullname="กุลกาญจน์ เตชะวณิชย์",
        camper_major="Sustainablity",
    ),
    "html",
)
msg.attach(msgText)

with open("YWC19 - หนังสือรับรอง camper.pdf", "rb") as file:
    pdf = MIMEApplication(file.read())
    pdf.add_header(
        "Content-Disposition",
        "attachment",
        filename="YWC19 หนังสือรับรองการคัดเลือกเข้าร่วมโครงการ - นางสาวกุลกาญจน์ เตชะวณิชย์.pdf",
    )
    msg.attach(pdf)

with open("เอกสารโครงการ Young Webmaster Camp ครั้งที่ 19.pdf", "rb") as file:
    pdf = MIMEApplication(file.read())
    pdf.add_header(
        "Content-Disposition",
        "attachment",
        filename="เอกสารโครงการ Young Webmaster Camp ครั้งที่ 19.pdf",
    )
    msg.attach(pdf)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(
        sender_email,
        recipients,
        msg.as_string(),
    )

print("success!")
