import tkinter as tk
import requests as rq
from PIL import ImageTk, Image

# получение данных о погоде
s_city = "Saransk"
city_id = 498698
appid = "bd10ff915d7a867b9b15b3d453de38b3"
try:
    res = rq.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    temp = data['main']['temp']
except Exception as e:
    print("Exception (weather):", e)

# создание окна
root = tk.Tk()
root.geometry('640x490')
root['bg']="#86c7dd"
root.resizable(0, 0)
root.title('Температура')

frame2 = tk.Frame(root,
                  width=171, height=80,
                  )
frame2.place(x=380, y=200)

lab1 = tk.Label(frame2,
                bg="#86c7dd",
                fg="black",
                text=(s_city, ':', temp, 'C°'),
                font='arial 14'
                )
lab1.pack()

canvas = tk.Canvas(root,
                   width=89, height=460,
                   bg="#86c7dd"
                   )
pilImage = Image.open("S2.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(0, 0, anchor='nw', image=image)
canvas.place(x=95, y=10)

for i in range(7):
    canvas.create_line(0, 230-38.3*i, 100, 230-38.3*i)
    canvas.create_line(0, 230+38.3*i, 100, 230+38.3*i)
    text_1 = tk.Label(root, bg="#86c7dd", text=(i*5, "C°"), font='arial 14')
    text_1.place(x=188, y=230-38.3*i)
    text_1 = tk.Label(root, bg="#86c7dd", text=(i * -5, "C°"), font='arial 14')
    text_1.place(x=188, y=230 + 38.3 * i)

if temp > 0:
    canvas.create_line(0, (230 - temp * (38.3 / 5)), 100, (230 - temp * (38.3 / 5)), dash=(1, 1))
    text_temp = tk.Label(root, bg="#86c7dd", text=(temp, 'C°'), font='arial 14')
    text_temp.place(x=13, y=(230 - temp * (38.3 / 5)))
else:
    canvas.create_line(0, (230 + abs(temp) * (38.3 / 5)), 100, (230 + abs(temp) * (38.3 / 5)), dash=(1, 1))
    text_temp = tk.Label(root, bg="#86c7dd", text=(temp, 'C°'), font='arial 14')
    text_temp.place(x=13, y=(230 + abs(temp) * (38.3 / 5)))

root.mainloop()




