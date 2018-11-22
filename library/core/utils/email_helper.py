import smtplib
from email.mime.text import MIMEText


def send_email(to_addr, subject, body):
    """
    使用公共邮箱发送邮件
    :param to_addr:
    :param subject:
    :param body:
    :return:
    """
    import settings
    import uuid
    sender_name = settings.EMAIL.get('USERNAME')
    receivers = to_addr if isinstance(to_addr, list) else [to_addr]
    # 在主题后面加UUID，防止邮件被判定为垃圾邮件
    uid = uuid.uuid4().__str__()
    subject = '{} - {}'.format(subject, uid)
    message = _build_email_header(sender_name, receivers, subject, body)

    with _get_email_server() as server:
        server.login(settings.EMAIL.get('USERNAME'), settings.EMAIL.get('PASSWORD'))
        server.sendmail(settings.EMAIL.get('USERNAME'), receivers, message)


def _get_email_server():
    import settings
    server = smtplib.SMTP_SSL(settings.EMAIL.get('SMTP_SERVER'), settings.EMAIL.get('SSL_PORT'))
    return server


def _build_email_header(sender, receivers, subject, body):
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ','.join(receivers)
    message['Subject'] = subject
    message['X-Coremail-Locale'] = 'zh_CN'
    message['X-Mailer'] = 'Coremail Webmail Server Version SP_ntes V3.5 build'
    return message.as_string()
