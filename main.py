from guizero import App ,Text, TextBox, Box, PushButton, ButtonGroup, ListBox, Window

def  Babynew():
    print("this is a function for a new baby")
def setting ():
    print("this is a function for setting")
def monitering ():
    print("this is a function for monetering")

def change_color(value):
    print(value)

def ExistingBaby ():
    pass
Name = []


def save_name():
    Name.append(name.value)
    listbox.append(name.value)

def open_window():
    window.show()

def close_window():
    window.hide()




""""
def menu_colour(value):
    app.bg =  value


colour_menu = ListBox( setting_box,
    items=["red", "green", "blue", "yellow", "purple", "turquoise", "#ffe085" , "orange", "black", "brown", "cyan"],
    selected="#ffe085" ,
    command= menu_colour,
    scrollbar=True)

"""








# size app when opened on screen
app = App(title="main menu", width= 1000, height= 1000)

#main menue colour
menu_colour = app.bg = "#ffe085"

# the title's size and font
title = Text(app, text="baby temprature",font="leckerli One", size=20)



#box on the right
rightBox = Box(app, width="fill", height="fill", align="right")



#making small diffrent boxes to simplefie my layout on the right
im_box1 = Box(rightBox,width=1000, height=90, align="top")
im_box1.bg = menu_colour
im_box2 = Box(rightBox,width=1000, height=90, align="fill")
im_box2.bg = menu_colour
im_box3= Box(rightBox,width=1000, height=800, align="bottom" )
im_box3.bg = menu_colour


#smaller boxes for presitation
lb_clock = Box(im_box2, align = "right",width=500, height=90)
lb_clock.bg = menu_colour

lb_setting = Box(im_box3,width=500, height=400,align="right")
lb_setting.bg = menu_colour

baby_plus = Box(im_box2, align = "left",width=500, height=90)
baby_plus.bg = menu_colour

lb_existBaby = Box(im_box3,width=600, height=600,align="left")
lb_existBaby.bg = menu_colour


#  clock box on main menu
clock_box = Box(lb_clock,width=350, height= 70, align="bottom")
clock_box.bg = "light blue"

# setting box on main menu
setting_box = Box(lb_setting ,align= "top",width=350, height= 200 )
setting_box .bg = "white"

# existing baby on main menu
ExistBaby = PushButton(lb_existBaby, align="top", width=40, height=3, text = "existing baby", command= ExistingBaby)
ExistBaby.bg = "white"


# saving baby info
listbox = ListBox(
    lb_existBaby,
    items= Name,
    selected="amelia",
    command=change_color,
    scrollbar=True, width=310, height=300 )

#  baby + button
BabyPlus = PushButton(baby_plus, align="bottom", width=40, height=3,text= "baby +",command= open_window)
BabyPlus.bg = "light blue"

#collecting info baby
window = Window(app, title="Second window")
name_label = Text(window, text="Name")
name = TextBox(window)
surname_label = Text(window, text="Surname")
surname = TextBox(window)
dob_label = Text(window, text="Date of Birth")
dob = TextBox(window)

window.hide()

close_button = PushButton(window, text="Close", command=close_window)
save_button = PushButton(window, text="save", command=save_name)


# c° and f° settings
choice = ButtonGroup(setting_box, options=[ "f°", "c°"], width= 30, height=10, align= "left")

#colour main menu change
ccMain_menue = PushButton(setting_box,text="menue colour", )







app.display()

