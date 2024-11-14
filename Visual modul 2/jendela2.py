import PySimpleGUI as sg
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM : 2210010633")],
                   [sg.Text("NAMA : Muhammad Aqli Andi Basith")],
                   [[sg.Text("KELAS : 5A NONREG BJM")]],
                   [[sg.Text("MATKUL : Pemrograman Visual 3")]]], 

                   size=(400,200))
window()
window.close()