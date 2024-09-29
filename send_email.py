import os
import smtplib
from email.mime.text import MIMEText

# Recuperando as variáveis de ambiente
email_to = os.getenv("EMAIL_TO")
email_from = os.getenv("EMAIL_FROM")
email_password = os.getenv("EMAIL_PASSWORD")

# Mensagem do email
msg = MIMEText("Pipeline executado com sucesso!")
msg['Subject'] = "Resultado do Pipeline"
msg['From'] = email_from
msg['To'] = email_to

# Enviando o email
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(email_from, email_password)
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()
    print(f"E-mail enviado para {email_to}")
except Exception as e:
    print(f"Falha ao enviar e-mail: {e}")
