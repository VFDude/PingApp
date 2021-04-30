from guizero import App, Text, TextBox, PushButton, Box
import os
import subprocess

def get_ping(adresy):
    listka = ['ping',adres.value,'-n','5']
    result = subprocess.check_output(listka)
    res.value = result

app = App("PING")

hello = Text(app, "Ping", size=50, color="#000000")

ping_box = Box(app, border=1, width="fill", height=30)
adres_opis = Text(ping_box, "Podaj adres", align="left", size=10, width=10)
adres = TextBox(ping_box, width="fill", height="fill")

button_box = Box(app, border=1, width="fill", height=30)
pinguj = PushButton(button_box, command=get_ping,args=[adres.value] , text="Pinguj!", align="left",
                       width="fill")


result_box = Box(app, width="fill", height="fill")
res = Text(result_box, width="fill", align="bottom")

status_box = Box(app, align="bottom", border=1, width="fill", height=20)
status_label = Text(status_box, "Status:    ", align="left")
status = Text(status_box, "OK", align="left")
app.display()