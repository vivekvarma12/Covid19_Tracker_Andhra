from tkinter import *
import json
import requests as r
master = Tk()
master.title("Covid19 Andhra Status")
master.geometry("600x400")
master.configure(bg="light green")
url = 'https://api.covid19india.org/data.json'
class Covid_Report:
    def __init__(self, url):
        self.url = url
    def ap_covid(self):
        try:
            x = r.get(self.url).content
            k = json.loads(x)['statewise']
            return k[2]
        except Exception as e:
            print(e)
    @classmethod
    def initiate_call(cls):
        report = Covid_Report(url)
        return report.ap_covid()

def refresh():
    data = Covid_Report.initiate_call()
    return data

def data_set():
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()

    report = refresh()
    #for debugging
    print(report)

    #New_Confirmed
    Label(master, text = "Confirmed Cases (Last 24 hrs):", font=("Times New Roman", 13)).place(x = 80, y = 60)
    Confirmed_cases = Label(master, textvariable = var1, font=("Calibri", 13), relief = RAISED).place(x = 360, y = 60)
    var1.set(report['deltaconfirmed'])
    #New_Recovered
    Label(master, text = "Recovered Cases (Last 24 hrs):", font=("Times New Roman", 13)).place(x = 80, y = 100)
    Label(master, textvariable = var2, font=("Calibri", 13), relief = RAISED).place(x = 360, y = 100)
    var2.set(report['deltarecovered'])
    #New_Deaths
    Label(master, text = "Fatility (Last 24 hrs):", font=("Times New Roman", 13)).place(x = 80, y = 140)
    Label(master, textvariable = var3, font=("Calibri", 13), relief = RAISED).place(x = 360, y = 140)
    var3.set(report['deltadeaths'])
    #Total_Active Cases
    Label(master, text = "Total Active Cases:", font=("Times New Roman", 13)).place(x = 80, y = 180)
    Label(master, textvariable = var4, font=("Calibri", 13), relief = RAISED).place(x = 360, y = 180)
    var4.set(report['active'])
    #Total_Recovered_Cases
    Label(master, text = "Total Recovered Cases:", font=("Times New Roman", 13)).place(x = 80, y = 220)
    Label(master, textvariable = var5, font=("Calibri", 13), relief = RAISED).place(x = 360, y = 220)
    var5.set(report['recovered'])
    #Total_Deaths
    Label(master, text = "Total Fatility:", font=("Times New Roman", 13)).place(x = 80, y = 260)
    Label(master, textvariable = var6, font=("Calibri", 13), relief = RAISED).place(x=360, y = 260)
    var6.set(report['deaths'])
    #Last_Updated
    Label(master, text="Last Updated Date & Time :", font=("Times New Roman", 13)).place(x=80, y=300)
    Label(master, textvariable=var7, font=("Calibri", 13), relief=RAISED).place(x=360, y=300)
    var7.set(report['lastupdatedtime'])

btn = Button(master, text = "Click me! (for Refresh)", font=("Times New Roman", 13), command=data_set).place(x=200,y=340)
data_set()
master.mainloop()
