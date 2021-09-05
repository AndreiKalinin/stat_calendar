import tkinter
import calendar
import datetime

def fill_calendar():
    global y
    for day in days:
        day.destroy()
    for event in events_list:
        event.destroy()
    days.clear()
    events_list.clear()
    stat_end.clear()
    for i in stat:
        i.pop(0)
    lbl_name_month['text'] = dic[m] + ' ' + str(y)
    amount = calendar.monthrange(y, m)[1]
    r = 2
    c = 1 + datetime.date(y, m, 1).weekday()
    global ev_row
    ev_row = 1
    stat_terms()
    for t in range(1, amount + 1):
        h = tkinter.Label(root, text=t, width=4, height=2, font=('Arial', 16, 'bold'), bg='lightskyblue')
        if c == 1:
            h.grid(row=r, column=c, padx=(25, 0))
        else:
            h.grid(row=r, column=c)
        for st in stat_end:    
            if [y, m, t] == st[:3]:
                h['bg'] = 'red'
                if t > 9 and m > 9:
                    for word in stop_words:
                        if word in st[3]:
                            lbl_events = tkinter.Label(root, text=str(t)+'.'+str(m)+' '+st[3]+str(y-1)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                            break
                        else:
                            lbl_events = tkinter.Label(root, text=str(t)+'.'+str(m)+' '+st[3]+str(y)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                elif t < 10 and m > 9:
                    for word in stop_words:
                        if word in st[3]:
                            lbl_events = tkinter.Label(root, text='0'+str(t)+'.'+str(m)+' '+st[3]+str(y-1)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                            break
                        else:
                            lbl_events = tkinter.Label(root, text='0'+str(t)+'.'+str(m)+' '+st[3]+str(y)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                elif t > 9 and m < 10:
                    for word in stop_words:
                        if word in st[3]:
                            lbl_events = tkinter.Label(root, text=str(t)+'.0'+str(m)+' '+st[3]+str(y-1)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                            break
                        else:
                            lbl_events = tkinter.Label(root, text=str(t)+'.0'+str(m)+' '+st[3]+str(y)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                else:
                    for word in stop_words:
                        if word in st[3]:
                            lbl_events = tkinter.Label(root, text='0'+str(t)+'.0'+str(m)+' '+st[3]+str(y-1)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                            break
                        else:
                            lbl_events = tkinter.Label(root, text='0'+str(t)+'.0'+str(m)+' '+st[3]+str(y)+' г.',
                                                       font=('Arial', 12), bg='khaki', height=2)
                lbl_events.grid(row=ev_row, column=8, columnspan=7, sticky='w', padx=(25, 0 ))
                events_list.append(lbl_events)
                ev_row += 1          
        days.append(h)
        t += 1
        c += 1
        if c % 7 == 1:
            r += 1
            c = 1
    
def next_month():        
    global y, m
    m += 1
    if m == 13:
        m = 1
        y += 1
    fill_calendar()

def previous_month(): 
    global y, m
    m -= 1
    if m == 0:
        m = 12
        y -= 1
    fill_calendar()

def stat_terms():
    global y
    for i in stat:
        i.insert(0, y)
        date_stat = datetime.date(*i[:3])
        if date_stat.weekday() == 5:
            date_stat += datetime.timedelta(2)
            if [y, date_stat.month, date_stat.day, i[3]] not in stat_end:
                stat_end.append([y, date_stat.month, date_stat.day, i[3]])
        if date_stat.weekday() == 6:
            date_stat += datetime.timedelta(1)
            if [y, date_stat.month, date_stat.day, i[3]] not in stat_end:
                stat_end.append([y, date_stat.month, date_stat.day, i[3]])
        else:
            if [y, date_stat.month, date_stat.day, i[3]] not in stat_end:
                stat_end.append([y, date_stat.month, date_stat.day, i[3]])
    return stat_end
    
root = tkinter.Tk()
root['bg'] = 'khaki'
root.state('zoomed')
root.title("Календарь статистики")
now = datetime.datetime.now()
y = now.year
m = now.month
dic = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
       9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
stat = [[1, 4, '- форма № П (услуги) за декабрь '], [1, 8, '- форма № П-4(НЗ) за 4 квартал '], [1, 15, '- форма № П-4 за декабрь '],
        [1, 20, '- форма № П-6 за 4 квартал '],
        [1, 21, '- форма № 1-Т за '], [1, 25, '- форма № 7-травматизм (с приложением) за '], [1, 25, '- форма № 4-ОС за '],
        [1, 30, '- форма № П-3 за декабрь '],
        [1, 30, '- форма № 22-ЖКХ за 4 квартал '], [2, 4, '- форма № П (услуги) за январь '], [2, 15, '- форма № П-4 за январь '],
        [2, 15, '- форма № 1-ПИ за 4 квартал '], [2, 28, '- форма № П-3 за январь '], [3, 1, '- форма  № 2-ДМ (с приложением) за '],
        [3, 1, '- форма № 4-ДМ за '], [3, 4, '- форма № П (услуги) за февраль '],
        [3, 15, '- форма № П-4 за февраль '], [3, 28, '- форма № П-3 за февраль '], [4, 1, '- форма № 12-Ф за '],
        [4, 1, '- форма № 1-предприятие за '], [4, 4, '- форма № П (услуги) за март '], [4, 8, '- форма № П-4(НЗ) за 1 квартал '],
        [4, 15, '- форма № П-4 за март '], [4, 20, '- форма № П-6 за 1 квартал '], [4, 30, '- форма № 5-З за 1 квартал '],
        [4, 30, '- форма № П-3 за март '], [4, 30, '- форма № 22-ЖКХ за 1 квартал '], [5, 4, '- форма № П (услуги) за апрель '],
        [5, 15, '- форма № П-4 за апрель '], [5, 15, '- форма № 1-ПИ за 1 квартал '], [5, 28, '- форма № П-3 за апрель '], [6, 4, '- форма № П (услуги) за май '],
        [6, 15, '- форма № П-4 за май '], [6, 28, '- форма № П-3 за май '], [6, 28, '- форма № 11-НА за '],
        [7, 1, '- форма № 11 (сделка) за '], [7, 4, '- форма № П (услуги) за июнь '], [7, 8, '- форма № П-4(НЗ) за 2 квартал '],
        [7, 15, '- форма № П-4 за июнь '], [7, 20, '- форма № П-6 за 2 квартал '],
        [7, 30, '- форма № 5-З за полугодие '], [7, 30, '- форма № П-3 за июнь '],
        [7, 30, '- форма № 22-ЖКХ за 2 квартал '], [8, 4, '- форма № П (услуги) за июль '],
        [8, 5, '- форма № 2-ДМ (с приложением) за полугодие '], [8, 15, '- форма № 1-ПИ за 1 квартал '],
        [8, 15, '- форма № П-4 за июль '], [8, 28, '- форма № П-3 за июль '], [9, 4, '- форма № П (услуги) за август '],
        [9, 15, '- форма № П-4 за август '], [9, 28, '- форма № П-3 за август '], [10, 4, '- форма № П (услуги) за сентябрь '],
        [10, 8, '- форма № П-4(НЗ) за 3 квартал '], [10, 15, '- форма № П-4 за сентябрь '], [10, 20, '- форма № П-6 за 3 квартал '],
        [10, 30, '- форма № 5-З за 9 мес. '], [10, 30, '- форма № П-3 за сентябрь '],
        [10, 30, '- форма № 22-ЖКХ за 3 квартал '], [11, 4, '- форма № П (услуги) за октябрь '], [11, 15, '- форма № 1-ПИ за 1 квартал '],
        [11, 15, '- форма № П-4 за октябрь '], [11, 28, '- форма № П-3 за октябрь '], [12, 4, '- форма № П (услуги) за ноябрь '],
        [12, 15, '- форма № П-4 за ноябрь '], [12, 28, '- форма № П-3 за ноябрь ']]
stat_end = []
stop_words = ["4 квартал", "(сделка)", "12-Ф", "1-предприятие", "за декабрь", "1-Т", "7-травматизм", "11-НА", 
              "4-ОС", "4-ДМ", "  № 2-ДМ"] 
week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
days = []
events_list = []
i = 1
for day in week:
    d = tkinter.Label(root, text=day, width=4, height=2, fg='white', bg='darkblue', font=('Arial', 16, 'bold'))
    if i == 1:
        d.grid(row=1, column=i, padx=(25, 0))
    else:
        d.grid(row=1, column=i)
    i += 1
    if i == 8:
       break 
stat_terms()
btn_back = tkinter.Button(root, text='<<', command=previous_month, font=('Arial', 10, 'bold'), bg='khaki')
btn_back.grid(row=0, column=2, pady=(10,0))
btn_forward = tkinter.Button(root, text='>>', command=next_month, font=('Arial', 10, 'bold'), bg='khaki')
btn_forward.grid(row=0, column=6, pady=(10,0))
lbl_name_month = tkinter.Label(root, text=dic[m] + ' ' + str(y), font=('Arial', 16, 'bold'), bg='khaki')
lbl_name_month.grid(row=0, column=3, columnspan=3, pady=(25, 15))
lbl_events = tkinter.Label(root, text="Сроки сдачи отчетности", font=('Arial', 16, 'bold'), bg='khaki')
lbl_events.grid(row=0, column=8, columnspan=5, ipadx=100, pady=(25, 15))
ev_row = 1
fill_calendar()

root.mainloop()
