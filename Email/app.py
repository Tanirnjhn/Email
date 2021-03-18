from flask import Flask,render_template,request
import smtplib
import details
app=Flask(__name__)
@app.route('/')
def first():
    return render_template('email.html')
@app.route('/detail',methods=['GET','POST'])
def sec():
    if(request.method=='POST'):
        x=request.form['a']
        y=request.form['course']
        z=request.form['b']
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(details.mail,details.pas)
        sub = "4 Achievers"   
        msg=f"""Hi {x},
        Thanks for registering in {y.upper()}.
        Team 4 Achievers"""
        message = 'Subject: {}\n\n{}'.format(sub,msg)
        server.sendmail(details.mail,z,message)
        server.close()
        return render_template('email.html')
if __name__=='__main__':
    app.run()      
