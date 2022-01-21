from tkinter import*
root=Tk()

tunnid={}
with open("tunnide_info.txt","r") as info_:
    for i in info_:
        v,r=i.strip().split(" - ")
        tunnid[v.strip()]=r.strip()

def uus_a(k):
    k_=k.replace("")
    ti=Toplevel()
    tu=Label(ti,text=tunnid.get(a1),font="Calibri 23",fg="black",justify=CENTER)
    ti.geometry("500x90")
    tu.pack()


Label(text="esmaspäev:",relief="solid").grid(row=1,rowspan=2,column=0,sticky=N+S+W+E)
Label(text="teisipäev:",relief="solid").grid(row=3,rowspan=2,column=0,sticky=N+S+W+E)
Label(text="kolmapäev:",relief="solid").grid(row=5,rowspan=2,column=0,sticky=N+S+W+E)
Label(text="neljapäev:",relief="solid").grid(row=7,rowspan=2,column=0,sticky=N+S+W+E)
Label(text="reede:",relief="solid").grid(row=9,rowspan=2,column=0,sticky=N+S+W+E)
Label(text=" ",relief="solid").grid(row=0,column=0,sticky=N+S+W+E)
Label(text="0\n7.40-8.25:",relief="solid").grid(row=0,column=1,sticky=N+S+W+E)
Label(text="1\n8.30-9.15:",relief="solid").grid(row=0,column=2,sticky=N+S+W+E)
Label(text="2\n9.20-10.05:",relief="solid").grid(row=0,column=3,sticky=N+S+W+E)
Label(text="3\n10.10-10.55:",relief="solid").grid(row=0,column=4,sticky=N+S+W+E)
Label(text="4\n11.00-11.45:",relief="solid").grid(row=0,column=5,sticky=N+S+W+E)
Label(text="5\n11.30-12.35:",relief="solid").grid(row=0,column=6,sticky=N+S+W+E)
Label(text="6\n12.40-13.25:",relief="solid").grid(row=0,column=7,sticky=N+S+W+E)
Label(text="7\n13.30-14.15:",relief="solid").grid(row=0,column=8,sticky=N+S+W+E)
Label(text="8\n14.20-15.05:",relief="solid").grid(row=0,column=9,sticky=N+S+W+E)
Label(text="9\n15.10-15.55:",relief="solid").grid(row=0,column=10,sticky=N+S+W+E)
Label(text="10\n16.00-16.45:",relief="solid").grid(row=0,column=11,sticky=N+S+W+E)

Button(text="tuge_est2:",bg="#8A726B",relief="solid").grid(row=2,column=2,sticky=N+S+W+E,command=lambda)
Label(text=" ").grid(row=1, column=2, sticky=N+S+W+E)
Button(text="logistika:",bg="lightgreen",relief="solid").grid(row=1,rowspan=2,column=3,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="matemaatika:", bg="pink",relief="solid").grid(row=1,rowspan=2,column=5,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text=" ",relief="solid").grid(row=1,rowspan=2,column=7,sticky=N+S+W+E,command=lambda)
Button(text="keel:",bg="#8FEA67",relief="solid").grid(row=1,rowspan=2,column=8,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="tuge_matem:",bg="pink",relief="solid").grid(row=1,rowspan=2,column=10,sticky=N+S+W+E,command=lambda)

Button(text="tuge_keemia:", bg="#B104C3",relief="solid").grid(row=3,rowspan=2,column=2,sticky=N+S+W+E,command=lambda)
Button(text="programmeerimine:", bg="lightblue",relief="solid").grid(row=3,rowspan=2,column=3,columnspan=3,sticky=N+S+W+E,command=lambda)
Button(text=" ",relief="solid").grid(row=3,rowspan=2,column=6,sticky=N+S+W+E,command=lambda)
Button(text="füüsika:", bg="pink",relief="solid").grid(row=3,rowspan=2,column=7,columnspan=2,sticky=N+S+W+E,command=lambda)

Button(text="tuge_est1:", bg="#DC29EE",relief="solid").grid(row=5,column=2,sticky=N+S+W+E,command=lambda)
Label(text=" ").grid(row=6, column=2, sticky=N+S+W+E)
Button(text="kunstiained:", bg="#AE4A8A",relief="solid").grid(row=5,rowspan=2,column=3,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text=" ",relief="solid").grid(row=5,rowspan=2,column=5,sticky=N+S+W+E,command=lambda)
Button(text="kehaline kasvatus:", bg="#A94E88",relief="solid").grid(row=5,rowspan=2,column=6,columnspan=2,sticky=N+S+W+E,command=lambda)

Button(text="logistika:", bg="lightgreen",relief="solid").grid(row=7,rowspan=2,column=2,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text=" ",relief="solid").grid(row=7,rowspan=2,column=4,sticky=N+S+W+E,command=lambda)
Button(text="programmeerimine:", bg="lightblue",relief="solid").grid(row=7,rowspan=2,column=5,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="inglise keel 1:", bg="lightyellow",relief="solid").grid(row=7,column=7,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="arenduskeskkonna loomine 2:", bg="#CF4141",relief="solid").grid(row=8,column=7,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="arenduskeskkonna loomine 1:", bg="#CF4141",relief="solid").grid(row=7,column=9,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="eesti keel 2:", bg="#8A726B",relief="solid").grid(row=8,column=9,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="rühmajuhataja tund:", bg="#DC29EE",relief="solid").grid(row=7,rowspan=2,column=11,columnspan=2,sticky=N+S+W+E,command=lambda)

Button(text="eesti keel 1:", bg="#DC29EE",relief="solid").grid(row=9,column=2,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="arenduskeskkonna loomine 2:", bg="#CF4141",relief="solid").grid(row=10,column=2,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="programmeerimine:", bg="lightblue",relief="solid").grid(row=9,rowspan=2,column=4,columnspan=5,sticky=N+S+W+E,command=lambda)
Button(text="arenduskeskkonna loomine 1:", bg="#CF4141",relief="solid").grid(row=9,column=9,columnspan=2,sticky=N+S+W+E,command=lambda)
Button(text="inglise keel 2:", bg="#8FEA67",relief="solid").grid(row=10,column=9,columnspan=2,sticky=N+S+W+E,command=lambda)

root.mainloop()
