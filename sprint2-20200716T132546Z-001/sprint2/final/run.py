from routes import app
import csv

if __name__ == '__main__':
    with open("user.csv","w") as csvfile: 
        writer = csv.writer(csvfile) 
        writer = writer.writerow(['user_name','email','password','logged'])

    # SIGINT to stop (Ctrl + C)
    app.run(debug=True)