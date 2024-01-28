from tkinter import*
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlite3 import*
from datetime import datetime
a=Tk()
a.title("BMI CALCULATOR")
a.geometry("450x400")
font1=("Times",30,"bold")
title=Label(a,font=font1,text="BMI CALCULATOR")
title.place(x=50,y=10)
height=Label(a,text="Your Height:")
conn=connect("History.db")
c= conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weight REAL,
            height REAL,
            bmi REAL)
            """)
def metric():
    conn=connect("History.db")
    c= conn.cursor()
    var1=Feet_Entry.get()
    var2=Inches_Entry.get()
    y=Weight_Entry.get()
    x=float(var1)
    z=float(var2)
    x=x*12+z
    bmi=703*((float(y)*2.205)/x**2)
    bmi=round(bmi,2)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    n6=Label(a,text="Your bmi is "+str(bmi))
    if(bmi<=18.5):
        n5=Label(a,text="Under Weight")
        req=((18.5-bmi)* x**2)/703
        req=round(req,2)
        n7=Label(a,text=str(req) +" weight required for normal weight")
        n7.place(x=100,y=360)
    elif(bmi>18.5 and bmi<24.9):
        n5=Label(a,text="Normal Weight")
        n7=Label(a,text="                                                                                                                            ")
        n7.place(x=100,y=360)
    elif(bmi>25 and bmi<29.9):
        n5=Label(a,text="Over Weight")
        req=((bmi-24.9)* x**2)/703
        req=round(req,2)
        n7=Label(a,text=str(req) +" weight need to be reduced for normal weight")
        n7.place(x=100,y=360)
    elif(bmi>=30):
        n5=Label(a,text="Obesity")
        req=((bmi-24.9)* x**2)/703
        req=round(req,2)
        n7=Label(a,text=str(req) +" weight need to be reduced for normal weight")
        n7.place(x=100,y=360)
    else:
        n5=Label(a,text="Enter Proper Values")
    
    c.execute('''
                INSERT INTO history (date, weight, height, bmi)
                VALUES (?, ?, ?, ?)
            ''', (date, y, x, bmi))
    n6.place(x=100,y=320)
    n5.place(x=100,y=340)
    
    conn.commit()
    conn.close()
def view_history():
        
    conn=connect("History.db")
    cursor =conn.cursor()
    cursor.execute('''
                SELECT date, weight, height, bmi FROM history
            ''')
    data = cursor.fetchall()

    history_window = Toplevel(a)
    history_window.title("BMI History")
    for i, row in enumerate(data):
        history_label = Label(history_window, text=f"{row[0]} - Weight: {row[1]}, Height: {row[2]}, BMI: {row[3]:.2f}")
        history_label.grid(row=i, column=0, padx=10, pady=5)
    conn.commit()
    conn.close()
        
def plot_trend():
    conn=connect("History.db")   
    cursor = conn.cursor()
    cursor.execute('''
                SELECT date, bmi FROM history
            ''')
    data = cursor.fetchall()

    dates = [entry[0] for entry in data]
    bmi_values = [entry[1] for entry in data]

        
    fig, ax = plt.subplots()
    ax.plot(dates, bmi_values, marker='o')
    ax.set_title('BMI Trend')
    ax.set_xlabel('Date')
    ax.set_ylabel('BMI')

        
    trend_window = Toplevel(a)
    trend_window.title("BMI Trend Analysis")
    canvas = FigureCanvasTkAgg(fig, master=trend_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    conn.commit()
    conn.close()

height.place(x=50,y=100)
Feet_label=Label(a,text="Feet")
Inches_label=Label(a,text="inches")
Feet_label.place(x=50,y=120)
Inches_label.place(x=50,y=150)
Feet_Entry=Entry(a)
Feet_Entry.place(x=150,y=120)
Inches_Entry=Entry(a)
Weight_label=Label(a,text="Your Weight(kgs)")
Weight_label.place(x=50,y=180)
Weight_Entry=Entry(a)
Weight_Entry.place(x=150,y=180)
Metric_label=Label(a,text="Metric")
Metric_label.place(x=50,y=80)
Inches_Entry.place(x=150,y=150)
Calculate_Button=Button(a,text="Calculate",command=lambda:metric())
History_Button=Button(a,text="View History",command=lambda:view_history())
History_Button.place(x=100,y=260)
Calculate_Button.place(x=100,y=230)
BMITrendAnalysis_Button=Button(a,text="BMI Trend Analysis",command=lambda:plot_trend())
BMITrendAnalysis_Button.place(x=80,y=290)
conn.commit()
conn.close()
a.mainloop()
