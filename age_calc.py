from customtkinter import *
from datetime import *

root = CTk()
set_appearance_mode('Dark')
root.title('Калькулятор возраста')
frame = CTkFrame(master=root, width=400, height=400, corner_radius=9, fg_color='#272A2B', border_width=1.5, border_color='#FE572F')
frame.pack(padx=10, pady=10)

name = CTkLabel(master=frame, text='Ваше имя:', font=('ALS Hauss', 14))
name.place(relx=0.095, rely=0.08)
name_entr = CTkEntry(master=frame, width=200, height=20, corner_radius=6, border_width=2, border_color='#F7DBD8', font=('Monsterrat', 14), fg_color='#252525', text_color='#E5F0C0')
name_entr.place(relx=0.285, rely= 0.09)

year = CTkLabel(master=frame, text='Год рождения:', font=('ALS Hauss', 14))
year.place(relx=0.02, rely=0.2)
year_entr = CTkEntry(master=frame, width=200, height=20, corner_radius=6, border_width=2, border_color='#F7DBD8', font=('Monsterrat', 14), fg_color='#252525', text_color='#9D87ED')
year_entr.place(relx=0.285, rely= 0.207)

month = CTkLabel(master=frame, text='Месяц (число):', font=('ALS Hauss', 14))
month.place(relx=0.018, rely=0.32)
month_entr = CTkEntry(master=frame, width=200, height=20, corner_radius=6, border_width=2, border_color='#F7DBD8', font=('Monsterrat', 14), fg_color='#252525', text_color='#9D87ED')
month_entr.place(relx=0.285, rely= 0.328)

day = CTkLabel(master=frame, text='День:', font=('ALS Hauss', 14))
day.place(relx=0.175, rely=0.444)
day_entr = CTkEntry(master=frame, width=200, height=20, corner_radius=6, border_width=2, border_color='#F7DBD8', font=('Monsterrat', 14), fg_color='#252525', text_color='#9D87ED')
day_entr.place(relx=0.285, rely= 0.45)

def age_calc(event):
    try:
        birthday = datetime(int(year_entr.get()), int(month_entr.get()), int(day_entr.get()))
        years = date.today().year - birthday.year - ((date.today().month, date.today().day) < (birthday.month, birthday.day))
        months = date.today().month - birthday.month
        days = date.today().day - birthday.day
        if months == 12:
            months -= 12
        if months <= 0:
            months += 12
        if days <= 0:
            months -= 1
            days += 31
        window = CTk()
        window.title('Результат')
        window_frame = CTkFrame(master=window, width=850, height=250, corner_radius=9, fg_color='#272A2B', border_width=1.5, border_color='#FE572F')
        window_frame.pack(padx=10, pady=10)
        window_label = CTkLabel(master=window_frame, height=50, width=300, font=('HeliosExtC', 20))
        window_label.place(relx=0.5, rely=0.27, anchor='center')
        days_label = CTkLabel(master=window_frame, height=20, width=100, font=('HeliosExtC', 20))
        days_label.place(relx=0.07, rely=0.42)
        hours_label = CTkLabel(master=window_frame, height=20, width=100, font=('HeliosExtC', 20))
        hours_label.place(relx=0.07, rely=0.55)
        minutes_label = CTkLabel(master=window_frame, height=20, width=100, font=('HeliosExtC', 20))
        minutes_label.place(relx=0.07, rely=0.67)
        seconds_label = CTkLabel(master=window_frame, height=20, width=100, font=('HeliosExtC', 20))
        seconds_label.place(relx=0.07, rely=0.8)
        def update_sec():
            hours = datetime.now().hour
            minutes = datetime.now().minute
            seconds = datetime.now().second
            all_days = (datetime.now() - birthday).days
            all_hours = (datetime.now() - birthday).days * 24
            all_minutes = (datetime.now() - birthday).days * 24 * 60
            all_seconds = int((datetime.now() - birthday).total_seconds())
            age = f'{name_entr.get()}, Вам {years} лет {months} месяцев {days} дней {hours} часов {minutes} минут {seconds} секунд\n\nИЛИ\n'
            window_label.configure(text=age)
            days_label.configure(text=f'Дней: {all_days}')
            hours_label.configure(text=f'Часов: {all_hours}')
            minutes_label.configure(text=f'Минут: {all_minutes}')
            seconds_label.configure(text=f'Секунд: {all_seconds}')
            window.after(1000, update_sec)
        update_sec()
        window.mainloop()
    except ValueError:
        error = CTk()
        error.title('Ошибка!')
        error_frame = CTkFrame(master=error, width=400, height=50, corner_radius=9, fg_color='#272A2B', border_width=1.5, border_color='#FE572F')
        error_frame.pack(padx=10, pady=10)
        error_text = CTkLabel(master=error_frame, text='Заполните поля корректно!', font=('Jost', 30))
        error_text.place(relx=0.5, rely=0.5, anchor='center')
        error.mainloop()

btn = CTkButton(master=frame, height=35, text='Узнать возраст', 
                border_width=2, border_color='#0F0F6E', corner_radius=9, font=('HeliosExtC', 18), fg_color='#E2B590', text_color='#0F0F6E')
btn.bind('<Button-1>', command=age_calc)
btn.place(relx=0.5, rely=0.6, anchor='center')

def quit(event):
    root.quit()
btn_quit = CTkButton(master=frame, text='Выйти', 
                border_width=4, border_color='#c8003e', height=45, corner_radius=9, font=('HeliosExtC', 18), fg_color='#FFFFFF', text_color='#c8003e')
btn_quit.bind('<Button-1>', command=quit)
btn_quit.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()