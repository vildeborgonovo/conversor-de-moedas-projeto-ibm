from tkinter import *
from tkinter import messagebox
from requests import *

# WEB SCRAPING #

url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
url_format = url.json()

dolar_hj = url_format['USDBRL']['bid']
dolar_hj = float(dolar_hj)
dolar_hj = round(dolar_hj, 2)

euro_hj = url_format['EURBRL']['bid']
euro_hj = float(euro_hj)
euro_hj = round(euro_hj, 2)

# INTERFACE GRAFICA #

janela_principal = Tk()
janela_principal.title('Conversor de Moedas')
janela_principal.geometry('310x430+400+200')
janela_principal.resizable(False, False)
janela_principal.config(background='#EDE5BA')

# FUNCOES #


def converter():
    try:
        if text_real.get() == '' and text_euro.get() == '':
            dolar = float(text_dolar.get())

            real = dolar * dolar_hj
            text_real.insert(0, round(real, 3))

            euro = real / euro_hj
            text_euro.insert(0, round(euro, 3))

        elif text_dolar.get() == '' and text_euro.get() == '':
            real = float(text_real.get())

            dolar = real / dolar_hj
            text_dolar.insert(0, round(dolar, 3))

            euro = real / euro_hj
            text_euro.insert(0, round(euro, 3))

        elif text_real.get() == '' and text_dolar.get() == '':
            euro = float(text_euro.get())

            real = euro * euro_hj
            text_real.insert(0, round(real, 3))

            dolar = real / dolar_hj
            text_dolar.insert(0, round(dolar, 3))

    except ValueError:
        messagebox.showerror(
            'Atenção', 'Por favor, coloque um valor numérico!')


def limpar():
    text_dolar.delete(0, END)
    text_real.delete(0, END)
    text_euro.delete(0, END)


# COMPONENTES (WIDGETS) #

logo = PhotoImage(file='moeda.png')
logo = logo.subsample(4, 4)
figura1 = Label(image=logo, bg='#EDE5BA')

lixeira = PhotoImage(file='lixeira.png')
lixeira = lixeira.subsample(10, 10)
figura2 = Label(image=lixeira, bg='#EDE5BA')

converta = PhotoImage(file='converta.png')
converta = converta.subsample(5, 5)
figura3 = Label(image=converta, bg='#EDE5BA')

frame_dolar = Frame(janela_principal, borderwidth=1.5,
                    relief='solid', bg='#EDE5BA')
label_dolar = Label(janela_principal, text='Dolar', bg='#EDE5BA')
text_dolar = Entry(frame_dolar, width=40)

frame_real = Frame(janela_principal, borderwidth=1.5,
                   relief='solid', bg='#EDE5BA')
label_real = Label(janela_principal, text='Real', bg='#EDE5BA')
text_real = Entry(frame_real, width=40)

frame_euro = Frame(janela_principal, borderwidth=1.5,
                   relief='solid', bg='#EDE5BA')
label_euro = Label(janela_principal, text='Euro', bg='#EDE5BA')
text_euro = Entry(frame_euro, width=40)

botao_converter = Button(janela_principal, image=converta, font=('Georgia, 14'),
                         highlightthickness=0, bd=0, bg='#EDE5BA', command=converter)

botao_limpar = Button(janela_principal, image=lixeira,
                      highlightthickness=0, bd=0, bg='#EDE5BA', command=limpar)

# LAYOUT - POSICIONAMENTO #
figura1.place(x=23, y=20)

frame_dolar.place(x=25, y=156, width=260, height=48)
label_dolar.place(x=29, y=145)
text_dolar.place(x=5, y=15)

frame_real.place(x=25, y=227, width=260, height=48)
label_real.place(x=29, y=215)
text_real.place(x=5, y=12)

frame_euro.place(x=25, y=298, width=260, height=48)
label_euro.place(x=29, y=285)
text_euro.place(x=5, y=15)

botao_converter.place(x=75, y=368)
botao_limpar.place(x=251, y=371)

janela_principal.mainloop()
