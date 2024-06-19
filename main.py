import tkinter as tk
import tkinter.messagebox

import ttkbootstrap as tb
from ttkbootstrap import Style
import joblib
import webbrowser
from tkinter import ttk, Toplevel
from PIL import ImageTk, Image

# style
style = Style()
style = Style(theme='superhero')

window = style.master
window.title("Crop Recommender")
window.geometry("900x675")

# Creating tabs
tab_parent = ttk.Notebook(window)

input_tab = ttk.Frame(tab_parent)
visual_tab = ttk.Frame(tab_parent)

tab_parent.add(input_tab, text='Input Data')
tab_parent.add(visual_tab, text='Visuals')

tab_parent.pack(expand=1, fill='both')

# load model from file
crop_model = joblib.load('crop-recommender.model')


# user input validation method - makes sure the user only inputs numbers
def validate_entry(text):
    return text.isdecimal()


# select an image based on the crop recommended
def get_img(crop):
    img = ImageTk.PhotoImage(Image.open('Images/' + crop + '.png').resize((300, 200)))

    return img


# error popup window
def popup():
    tkinter.messagebox.showerror('Check Inputs', 'Please ensure that all fields have been entered correctly')
    return


# predict crop from model
def predict_crop(model, n, p, k, t, h, pH, r):
    prediction = model.predict([[n, p, k, t, h, pH, r]])[0]

    return prediction


# crop recommendation method
def recommend_crop():
    # ensure all fields are filled out with number values in the correct range
    try:
        n = float(n_spin_box.get())
        p = float(p_spin_box.get())
        k = float(k_spin_box.get())
        t = float(t_spin_box.get())
        h = float(h_spin_box.get())
        pH = float(pH_spin_box.get())
        r = float(r_spin_box.get())

        if n < 0 or n > 150:
            popup()
            return

        if p < 0 or p > 150:
            popup()
            return

        if k < 0 or k > 205:
            popup()
            return

        if t < 0 or t > 50:
            popup()
            return

        if h < 0 or h > 100:
            popup()
            return

        if pH < 3 or pH > 10:
            popup()
            return

        if r < 0 or r > 300:
            popup()
            return

    except:
        popup()
        return

    crop = predict_crop(crop_model, n, p, k, t, h, pH, r)

    wiki_link = ''

    # update photo with original crop name
    crop_image = get_img(crop)

    # ensure image doesn't get garbage collected
    image_panel.configure(image=crop_image)
    image_panel.photo = crop_image

    # image attribution: By 中国新闻网, CC BY 3.0, https://commons.wikimedia.org/w/index.php?curid=108022271
    if crop == 'Rice':
        wiki_link = 'https://en.wikipedia.org/wiki/Rice'

    # image attribution: By Keith Weller, USDA - Public Domain, https://commons.wikimedia.org/w/index.php?curid=185217
    if crop == 'Maize':
        wiki_link = 'https://en.wikipedia.org/wiki/Maize'

    # image attribution: By Sanjay Acharya - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=3131388
    if crop == 'ChickPea':
        crop = 'Chickpeas'
        wiki_link = 'https://en.wikipedia.org/wiki/Chickpea'

    # image attribution: By Prathyush Thomas - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=40703179
    if crop == 'KidneyBeans':
        crop = 'Kidney Beans'
        wiki_link = 'https://en.wikipedia.org/wiki/Kidney_bean'

    # image attribution: By Filo gèn' - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=74524556
    if crop == 'PigeonPeas':
        crop = 'Pigeon Peas'
        wiki_link = 'https://en.wikipedia.org/wiki/Pigeon_pea'

    # image attribution: By Lalitstar at English Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=7410247
    if crop == 'MothBeans':
        crop = 'Moth Beans'
        wiki_link = 'https://en.wikipedia.org/wiki/Vigna_aconitifolia'

    # image attribution: By Ivar Leidus - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=97530683
    if crop == 'MungBean':
        crop = 'Mung Beans'
        wiki_link = 'https://en.wikipedia.org/wiki/Mung_bean'

    # image attribution: By Sanjay Acharya - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=3590757
    if crop == 'Blackgram':
        crop = 'Black Gram'
        wiki_link = 'https://en.wikipedia.org/wiki/Vigna_mungo'

    # image attribution: By User:Justinc - File:3_types_of_lentil.jpg, CC BY-SA 2.5, https://commons.wikimedia.org/w/index.php?curid=70705137
    if crop == 'Lentil':
        crop = 'Lentils'
        wiki_link = 'https://en.wikipedia.org/wiki/Lentil'

    # image attribution: By Augustus Binu, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=75662186
    if crop == 'Pomegranate':
        crop = 'Pomegranates'
        wiki_link = 'https://en.wikipedia.org/wiki/Pomegranate'

    # image attribution: By Steve Hopson, www.stevehopson.com, CC BY-SA 2.5, https://commons.wikimedia.org/w/index.php?curid=1541726
    if crop == 'Banana':
        crop = 'Bananas'
        wiki_link = 'https://en.wikipedia.org/wiki/Banana'

    # image attribution: By Ivar Leidus - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=114780033
    if crop == 'Mango':
        crop = 'Mangoes'
        wiki_link = 'https://en.wikipedia.org/wiki/Mango'

    # image attribution: By © Vyacheslav Argenberg / http://www.vascoplanet.com/, CC BY 4.0, https://commons.wikimedia.org/w/index.php?curid=127002511
    if crop == 'Grapes':
        wiki_link = 'https://en.wikipedia.org/wiki/Grape'

    # image attribution: By Prathyush Thomas - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=41323824
    if crop == 'Watermelon':
        wiki_link = 'https://en.wikipedia.org/wiki/Watermelon'

    # image attribution: By Seth Vidal - originally posted to Flickr as muskmelon, CC BY-SA 2.0, https://commons.wikimedia.org/w/index.php?curid=4832830
    if crop == 'Muskmelon':
        wiki_link = 'https://en.wikipedia.org/wiki/Cucumis_melo'

    # image attribution: By fir0002flagstaffotos [at] gmail.comCanon 20D + Sigma 150mm f/2.8 - Own work, GFDL 1.2, https://commons.wikimedia.org/w/index.php?curid=5765394
    if crop == 'Apple':
        crop = 'Apples'
        wiki_link = 'https://en.wikipedia.org/wiki/Apple'

    # image attribution: By Ivar Leidus - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=98469414
    if crop == 'Orange':
        crop = 'Oranges'
        wiki_link = 'https://en.wikipedia.org/wiki/Orange_(fruit)'

    # image attribution: By H. Zell - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=9438074
    if crop == 'Papaya':
        crop = 'Papayas'
        wiki_link = 'https://en.wikipedia.org/wiki/Papaya'

    # image attribution: pngwing.com
    if crop == 'Coconut':
        crop = 'Coconuts'
        wiki_link = 'https://en.wikipedia.org/wiki/Coconut'

    # image attribution: Public Domain, https://commons.wikimedia.org/w/index.php?curid=689304
    if crop == 'Cotton':
        wiki_link = 'https://en.wikipedia.org/wiki/Cotton'

    # image attribution: By Biswarup Ganguly - Own work, CC BY 3.0, https://commons.wikimedia.org/w/index.php?curid=17426286
    if crop == 'Jute':
        wiki_link = 'https://en.wikipedia.org/wiki/Jute'

    # image attribution: By Marcelo Corrêa - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=85360
    if crop == 'Coffee':
        wiki_link = 'https://en.wikipedia.org/wiki/Coffea'

    output_label['text'] = 'Based on the data, you should plant: ' + crop

    wiki_label['text'] = wiki_link
    wiki_label['cursor'] = 'hand2'
    wiki_label['foreground'] = 'lightblue'
    wiki_label['font'] = 'Calibri 15 underline'


# create method that allows the wiki link to be clickable
def open_url(url):
    webbrowser.open_new_tab(url)


# input tab title
title_label = ttk.Label(input_tab, text="Enter Soil Data for Crop Recommendation", font="Calibri 24 bold")
title_label.pack(pady=(0, 10))

# create frame for entering data
data_entry_frame = ttk.Frame(input_tab)
data_entry_frame.pack()
data_entry_frame.grid_columnconfigure(0, weight=1)
data_entry_frame.grid_columnconfigure(1, weight=1)

# data widgets
n_label = ttk.Label(data_entry_frame, text="Nitrogen Ratio (Value between 0-150)", font="Calibri 12")
n_label.grid(row=0, column=0, sticky='w')
n_var = tk.DoubleVar(value=0)
n_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=150,
    textvariable=n_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
n_spin_box.grid(row=0, column=1, padx=10)

p_label = ttk.Label(data_entry_frame, text="Phosphorous Ratio (Value between 0-150)", font="Calibri 12")
p_label.grid(row=1, column=0, pady=(10, 0), sticky='w')
p_var = tk.DoubleVar(value=0)
p_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=150,
    textvariable=p_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
p_spin_box.grid(row=1, column=1, padx=10)

k_label = ttk.Label(data_entry_frame, text="Potassium Ratio (Value between 0-205)", font="Calibri 12")
k_label.grid(row=2, column=0, pady=(10, 0), sticky='w')
k_var = tk.DoubleVar(value=0)
k_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=205,
    textvariable=k_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
k_spin_box.grid(row=2, column=1, padx=10)

t_label = ttk.Label(data_entry_frame, text="Temperature °C (Value between 0-50)", font="Calibri 12")
t_label.grid(row=3, column=0, pady=(10, 0), sticky='w')
t_var = tk.DoubleVar(value=0)
t_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=50,
    textvariable=t_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
t_spin_box.grid(row=3, column=1, padx=10)

h_label = ttk.Label(data_entry_frame, text="Humidity (Value between 0-100)", font="Calibri 12")
h_label.grid(row=4, column=0, pady=(10, 0), sticky='w')
h_var = tk.DoubleVar(value=0)
h_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=100,
    textvariable=h_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
h_spin_box.grid(row=4, column=1, padx=10)

pH_label = ttk.Label(data_entry_frame, text="pH Value (Value between 3-10)", font="Calibri 12")
pH_label.grid(row=5, column=0, pady=(10, 0), sticky='w')
pH_var = tk.DoubleVar(value=3)
pH_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=3,
    to=10,
    textvariable=pH_var,
    wrap=True,
    increment=0.5,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
pH_spin_box.grid(row=5, column=1, padx=10)

r_label = ttk.Label(data_entry_frame, text="Rainfall (Value between 0-300)", font="Calibri 12")
r_label.grid(row=6, column=0, pady=10, sticky='w')
r_var = tk.DoubleVar(value=0)
r_spin_box = ttk.Spinbox(
    data_entry_frame,
    from_=0,
    to=300,
    textvariable=r_var,
    wrap=True,
    validate="key",
    validatecommand=(window.register(validate_entry), "%S")
)
r_spin_box.grid(row=6, column=1, padx=10)

button = ttk.Button(data_entry_frame, text="Submit", command=recommend_crop)
button.grid(row=7, columnspan=2, pady=10, sticky='ew')

# output frame
output_frame = ttk.Frame(input_tab)
output_frame.pack()

# output label
output_label = ttk.Label(output_frame, text="<<Crop recommendation will be output here>>", font="Calibri 15")
output_label.pack(pady=(20, 10))

# wikipedia link
wiki_label = ttk.Label(output_frame, text="<<A wiki link relevant to the recommended crop will appear here>>", font="Calibri 15")
wiki_label.pack(pady=(0, 10))
wiki_label.bind("<Button-1>", lambda e: open_url(wiki_label['text']))

# crop recommendation image
img = ImageTk.PhotoImage(Image.open('Images/crops.png').resize((300, 200)))
image_panel = ttk.Label(output_frame, image=img)
image_panel.pack(pady=(0, 10))

# ### ########### ### #
# ### VISUALS TAB ### #
# ### ########### ### #
# visuals title
title_label = ttk.Label(visual_tab, text="Select an Image to Display", font="Calibri 24 bold")
title_label.pack(pady=(0, 10))

# image display frame
display_image_frame = ttk.Frame(visual_tab)
display_image_frame.pack()

# image title
image_title = ttk.Label(display_image_frame, text='Corellogram', font='Calibri 15')
image_title.pack()

# display image
display_img = ImageTk.PhotoImage(Image.open('corellogram.png').resize((600, 400)))
display_panel = ttk.Label(display_image_frame, image=display_img)
display_panel.pack()

# drop down menu selection
drop_down_label = ttk.Label(display_image_frame,
                            text='Select an image from the menu below: ',
                            font='Calibri 12')
drop_down_label.pack(pady=(10, 5))

OPTIONS = [
    'Corellogram',
    'Confusion Matrix',
    'Histogram',
    'Scatter Matrix'
]

display_var = tk.StringVar(display_image_frame)
display_var.set(OPTIONS[0])  # default value

option_menu = ttk.Combobox(display_image_frame,
                           textvariable=display_var,
                           values=OPTIONS,
                           state='readonly')
option_menu.pack()


# method to change background image based on selection
def get_image():
    image_val = display_var.get()
    selected_img = display_img

    if image_val == 'Corellogram':
        selected_img = ImageTk.PhotoImage(Image.open('corellogram.png').resize((600, 400)))
        image_title['text'] = image_val

    if image_val == 'Confusion Matrix':
        selected_img = ImageTk.PhotoImage(Image.open('crop_confusion_matrix.png').resize((600, 400)))
        image_title['text'] = image_val

    if image_val == 'Histogram':
        selected_img = ImageTk.PhotoImage(Image.open('data_histogram.png').resize((600, 400)))
        image_title['text'] = image_val

    if image_val == 'Scatter Matrix':
        selected_img = ImageTk.PhotoImage(Image.open('data_scatter_matrix.png').resize((600, 400)))
        image_title['text'] = image_val

    # make sure image isn't garbage collected
    display_panel.configure(image=selected_img)
    display_panel.photo = selected_img


image_button = ttk.Button(display_image_frame, text='Submit', command=get_image)
image_button.pack(pady=10)

# run the tkinter app
window.mainloop()
