from flask import Flask , render_template , request, jsonify, session;
##from MailSender import send_my_email
from Chatbotmanager import search_knowledge
from chartgenrator import create_chart
from captchagenrator import create_captcha
app=Flask(__name__)
UPLOAD_FOLDER='static'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# setting secret key for session
app.secret_key="asdasd fdsfdsf"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/developer')
def open_developer():
    return render_template('developer.html')

@app.route('/feedback')
def open_feedback():
    create_captcha()
    pname=create_captcha()
    return render_template('feedback.html', captcha_img_name=pname)

# route to genrate new captcha image
@app.route('/getnew_captcha', methods=["GET"])
def new_captcha():
    pname=create_captcha()
    return jsonify(pname)

@app.route('/faq')
def open_faq():
    return render_template('faq.html')

@app.route('/contact')
def open_contact():
    return render_template('contact.html')


@app.route('/chata')
def open_chata():
    data_df=create_chart()
    return render_template('chata.html', df=data_df)

@app.route('/chat')
def open_chat():
    return render_template('chat.html')

@app.route('/aboutus')
def open_aboutus():
    return render_template('Aboutus.html')


@app.route('/check')
def open_check():
    return render_template('check.html')

# for ajax call
'''@app.route('/addnum', methods=["GET"])
def open_testajax():
    x=request.args.get("fnum")
    y=request.args.get("snum")
    result=int(x)+int(y)
    msg="Addition is: "+str(result)
    return jsonify'''

#Eamil sending
@app.route("/send")
def mail_test():
    r=send_my_email(app, "directorksspl@gmail.com", "Test Message", "sir pahle mera error solve kariyega")
    if r:
        return "Email sent successfully"
    else:
        return "Sorry unable to send"

# to get answer of user query
@app.route('/getbotanswer')
def get_bot_ans():
    user_query=request.args.get("userquery")
    result=search_knowledge(user_query)
    return jsonify(result)

@app.route("/submit_feedback", methods=["POST"])
def save_feedback():
    msg=""
    # reading and validating captcha
    user_code=request.form.get("tcaptcha")
    or_code=session.get("code")
    if user_code==or_code:
        name=request.form.get("name")
        email=request.form.get("email")
        mobile=request.form.get("mobile")
        feedback=request.form.get("feedback")
        gender=request.form.get("gender")
        # creating email message to owner
        mail_msg="Hi Admin, <br> A person with name <b>"+name+"</b>, has submitted a feedback of your <b> Chat Bot </b>. <br> Details of the feedback are:- <br><br><b>Name:</b>"+name+"<br> <b>Email Id for a person:</b>"+email+"<br> <b> Gender:</b>"+gender+"<br><b>Feedback message is:</b>"+feedback+"<br><br><br> from Chat Bot"
        # Sending email alert to owner
        send_my_email(app, "anujkumar40328@gmail.com", "A feedback recived", mail_msg)
        msg="Thanks for your valueable feedback"
    else:
        msg="Invalid Captcha code. Please try again"
    pname=create_captcha()
    return render_template("feedback.html", msg="Thanks for your valueable feedback. we will get back to you shortly")
    
# creating Email message to user 





if __name__=='__main__':
    app.run(debug=True)