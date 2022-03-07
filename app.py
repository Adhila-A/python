import csv
import names
import  random
import datetime
from flask import Flask, render_template,request
app=Flask(__name__,template_folder='template')
@app.route("/")
def start():
    return render_template("index.html")
@app.route("/download" ,methods=["GET","POST"])
def filsav():
    if request.method=="POST":
        Student_dict=[]
        for i in range(5):
            a=(names.get_first_name())
            b=(names.get_last_name())
            fullname=(a+" "+b)
            emailid=a+b+"@gmail.com"
            random_number = random.randint(9000000000, 10000000000)
            salary=random.randrange(25000,75000,100)
            start_date = datetime.date(2000, 1, 1)
            end_date = datetime.date(2021, 1, 1)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            experience=end_date.year-random_date.year
            profession=["Web Developer ","Physician",  "Auditor" ,"Health Educator"  ,"RestaurantManager" ,
            "Executive Director"  ,"Front Desk Coordinator" ,"Clerk" "Paramedic", "IT Support Staff",
            "Laboratory Technician", "Software Engineer", "Webmaster" ,"Business Broker" ,"Software  Developer",  "Mobile Developer"]

            Student_dict += [
            {"id":i+1,'Name':fullname,'email': emailid ,'phonenumber':random_number ,
            'Profession':(random.choice(profession)),'Salary':salary ,'Date Of Joining':random_date,'year of experience':experience}]
            return render_template("index.html",Student_dict=Student_dict)
if(__name__)=="__main__":
    app.run(debug=True)
