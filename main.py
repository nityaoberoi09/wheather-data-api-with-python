from flask import Flask, render_template
import pandas as pd


app=Flask(__name__)

stations=pd.read_csv("small data/stations.txt", skiprows=17)
stations=stations[["STAID", "STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html",data=stations.to_html())

@app.route("/api/v1/<station>/<date>")#these two denote that user can enter its value
def about(station,date):
    filename="small data/TG_STAID"+str(station).zfill(6)+".txt" # zfills add 0s' to the string such as 1 will be written as 000001
    df=pd.read_csv(filename,skiprows=20, parse_dates=["    DATE"])
    temprature= df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    return {"station":station,"date":date, "temprature":temprature}


if __name__=="__main__":
    app.run(debug=True)