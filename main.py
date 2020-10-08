import threading
from tkinter import *
from tkinter import ttk

def calculatedamage(*args):
    basedamage = (5 + int(WeaponDamage.get()) + (int(Strength.get()) / 5)) * (1 + int(Strength.get()) / 100)
    damagemultiplier = 1 + (int(CombatLevel.get()) * 0.04) + (float((int(SharpnessLevel.get()) * 0.05))) + (
                int(FirstStrikeLevel.get()) * 0.25)
    finaldamagetemp = basedamage * damagemultiplier * (1 + int(CritDamage.get()))
    FinalDamage.set(round(finaldamagetemp))


root = Tk()
root.title("Damage Calculator")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

WeaponDamage = IntVar()
Strength = IntVar()
CritDamage = IntVar()
SharpnessLevel = IntVar()
FirstStrikeLevel = IntVar()
CombatLevel = IntVar()
FinalDamage = StringVar()
#feet = StringVar()
#meters = StringVar()

# Weapon Damage Textbox
WeaponDamageEntry = ttk.Entry(mainframe, width=7, textvariable=WeaponDamage)
WeaponDamageEntry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Weapon Damage").grid(column=3, row=1, sticky=W)

#Strength Textbox
StrengthEntry = ttk.Entry(mainframe, width=7, textvariable=Strength)
StrengthEntry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Strength").grid(column=3, row=2, sticky=W)

#Crit Damage Textbox
CritDamageEntry = ttk.Entry(mainframe, width=7, textvariable=CritDamage)
CritDamageEntry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Crit Damage").grid(column=3, row=3, sticky=W)

#Sharpness Level Textbox
SharpnessLevelEntry = ttk.Entry(mainframe, width=7, textvariable=SharpnessLevel)
SharpnessLevelEntry.grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Sharpness Level").grid(column=3, row=4, sticky=W)

#First Strike Level Textbox
FirstStrikeLevelEntry = ttk.Entry(mainframe, width=7, textvariable=FirstStrikeLevel)
FirstStrikeLevelEntry.grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, text="First Strike Level").grid(column=3, row=5, sticky=W)

#Combat Level Entry
CombatLevelEntry = ttk.Entry(mainframe, width=7, textvariable=CombatLevel)
CombatLevelEntry.grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, text="Combat Level").grid(column=3, row=6, sticky=W)

#Final Damage Entry
FinalDamageEntry = ttk.Label(mainframe, textvariable=FinalDamage).grid(column=2, row=7, sticky=(W, E))
FinalDamageButton = ttk.Button(mainframe, text="Calculate", command=calculatedamage).grid(column=1, row=7, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

WeaponDamageEntry.focus()
root.bind('<Return>', calculatedamage)
root.mainloop()
