from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'hamed'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = '10.0.0.66'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
	print('hello')
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
	    print ("ok we are here")            
            conn = mysql.connect()
            cursor = conn.cursor()
            print (cursor)
            # hasing password doesnt write to database
	    #_hashed_password = generate_password_hash(_password)
            #print _hashed_password
	    #cursor.callproc('sp_createUseri',(_name,_email,_hashed_password))
           
 	    #cursor.execute('''SELECT * FROM tbl_user''')
            cursor.callproc('sp_createUser',(_name,_email,_password))
            data = cursor.fetchall()
	    print("about to print data")
	    print data
            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)
