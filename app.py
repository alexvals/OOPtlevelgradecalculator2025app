from flask import Flask, request, redirect, render_template
from flask.views import MethodView

app = Flask(__name__)
animals = {}

class Home(MethodView):
    def get(self):
        return render_template("index.html")

class Calculator(MethodView):
    def get(self):
        return render_template("calculator.html")

class FiftyFifty(Calculator):
    def post(self):
        core = request.form.get("core")
        occupational = request.form.get("occupational")
        if core and occupational:
            if occupational == "Fail":
                answer = "Fail"
            elif core == "A*":
                if occupational == "Distinction":
                    answer = "Distinction *"
                else:
                    answer = "Distinction"
            elif core == "A":
                if occupational != "Pass":
                    answer = "Distinction"
                else:
                    answer = "Merit"
            elif core == "B":
                if occupational != "Distinction":
                    answer = "Merit"
                else:
                    answer = "Distinction"
            elif core == "C":
                if occupational != "Pass":
                    answer = "Merit"
                else:
                    answer = "Pass"
            elif core == "D":
                if occupational == "Distinction":
                    answer = "Merit"
                else:
                    answer = "Pass"
            elif core == "E":
                answer = "Pass"
            else:
                answer = "Fail"
        return render_template("calculator.html", answer=answer)


class FortySixty(Calculator):
    def post(self):
        core = request.form.get("core")
        occupational = request.form.get("occupational")
        if core and occupational:
            if occupational == "Fail":
                answer = "Fail"
            elif core == "A*":
                if occupational == "Distinction":
                    answer = "Distinction *"
                elif occupational == "Merit":
                    answer = "Distinction"
                else:
                    answer = "Merit"
            elif core == "A":
                if occupational != "Pass":
                    answer = "Distinction"
                else:
                    answer = "Merit"
            elif core == "B":
                if occupational != "Distinction":
                    answer = "Merit"
                else:
                    answer = "Distinction"
            elif core == "C":
                answer = occupational
            elif core == "D":
                if occupational == "Distinction":
                    answer = "Merit"
                else:
                    answer = "Pass"
            elif core == "E":
                answer = "Pass"
            else:
                answer = "Fail"
        return render_template("calculator.html", answer=answer)

app.add_url_rule('/', view_func = Home.as_view('index'))
app.add_url_rule('/calc/5050', view_func = FiftyFifty.as_view('fiftyfifty'))
app.add_url_rule('/calc/4060', view_func = FortySixty.as_view('fortysixty'))
app.debug=True
app.run()

#https://www.gov.uk/government/collections/resources-and-materials-for-promoting-t-levels#resources-for-employers-to-promote-t-levels