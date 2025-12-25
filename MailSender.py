from flask_mail import Mail, Message;
def send_my_email(app_obj,sendto,  subject, message):
  try:
    app_obj.config['MAIL_SERVER']="smtp.gmail.com"
    app_obj.config['MAIL_PORT']=587
    app_obj.config['MAIL_USE_TLS']=True
    app_obj.config['MAIL_USERNAME']='anujkumar40328@gmail.com'
    app_obj.config['MAIL_PASSWORD']='zpml qxvs sccl vdyj'
    app_obj.config['MAIL_DEFAULT_SENDER']='anujkumar40328@gmail.com'
    mail=Mail(app_obj)
    msg=Message(subject=subject,recipients=[sendto], body=message)
    mail.send(msg)
    return True
  except:
    return False

