from flask import Flask, render_template # Import Flask Class, and render_template
from flask import request
from flask import url_for, redirect
#from flask import Response

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

month_abbvs=dict((m[:3].lower(),m) for m in months)
def valid_month(month):
  if month:
    short_month=month[:3].lower()
    return month_abbvs.get(short_month)
def valid_day(day):
  if day and day.isdigit():
    day=int(day)
    if day>0 and day<=31:
      return day 
def valid_year(year):
  if year and year.isdigit():
    year=int(year)
    if year>1900 and year <2020:
      return year
t1="I think %s is a perfectly normal thing to do in public"      
t2="I think %s and %s is a perfectly normal thing to do in public" 
t3="Im %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s"
def sub1(s):
    return t1 % s
def sub2(s1,s2):
  return t2 % (s1,s2)
def sub_m(name, nickname):
   return t3 %{"name":name,"nickname":nickname}
app = Flask(__name__) # Create an Instance



steve="""
<!DOCTYPE html>
<html>
<body>

<form method="POST">
    What is your birthday?
    <br>
    <br>
    <label> Month
    <input type="text" name="month" value="%(month)s">
    </label>
    <label> Day
    <input type="text" name="day" value="%(day)s">
    </label>
    <label> Year
    <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
</body>
</html>
"""
def escape_html(s):
    for (i,o) in (("&","&amp;"),
                  (">","&gt;"),
                  ("<","&lt;"),
                  ('"',"&quot;")):
      s=s.replace(i,o)              
    return s



@app.route('/',methods=['GET', 'POST']) # Route the Function
def main(): # Run the function
    if request.method == 'POST':
     day=request.form['day']
     year=request.form['year']
     month=request.form['month']
     user_month = valid_month(month)
     user_day = valid_day(day)
     user_year = valid_year(year)
     if not (user_month and user_day and user_year):
      #return render_template('index.html')  
      return write_form("Sjebalo se!",month,day,year)
     else:  
      #return render_template('index.html')
      return redirect('/thanks')
    else :  
     #return render_template('index.html') # Render the template
     return write_form()   
def write_form(error="",month="",day="",year=""):
   print(steve % { "error":error,"month":escape_html(month),"day":escape_html(day),"year":escape_html(year)})
   return steve % { "error":error,"month":escape_html(month),"day":escape_html(day),"year":escape_html(year)}
@app.route('/thanks',methods=['GET', 'POST'])
def reaguj():
  return "Thanks this is a totally valid address."

app.run(host='0.0.0.0', port=5000, debug=True)


