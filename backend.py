import pyttsx3
import pandas as pd
from sklearn import \
    preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import customtkinter

excel = pd.read_excel('Crop.xlsx', header=0)
print(excel)
print(excel.shape)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
engine.setProperty('voice', voices[0].id)


def speak(
        audio):
    engine.say(audio)
    engine.runAndWait()


le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["CROP"]))
NITROGEN = list(excel["NITROGEN"])
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(
    excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])
features = list(
    zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))  # Zipping all the features together
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,
                     RAINFALL])

features = features.transpose()
print(features.shape)
print(
    crop.shape)
model = KNeighborsClassifier(
    n_neighbors=3)
model.fit(features,
          crop)


def login():
    while True:
        crop_name = str()
        cp = str()

        nitrogen_content = entry1.get()
        phosphorus_content = entry2.get()
        potassium_content = entry3.get()
        temperature_content = entry4.get()
        humidity_content = entry5.get()
        ph_content = entry6.get()
        rainfall = entry7.get()
        predict1 = np.array(
            [nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,
             rainfall], dtype=float)
        print(predict1)
        predict1 = predict1.reshape(1, -1)
        print(predict1)
        predict1 = model.predict(predict1)
        print(predict1)

        if predict1 == 0:
            crop_name = 'Apple(सेब)'
            cp = "No alternatives"
        elif predict1 == 1:
            crop_name = 'Banana(केला)'
            cp = 'Coconut'
        elif predict1 == 2:
            crop_name = 'Blackgram(काला चना)'
            cp = 'No alternative'
        elif predict1 == 3:
            crop_name = 'Chickpea(काबुली चना)'
            cp = "GreenPeas,Soyabeans"
        elif predict1 == 4:
            crop_name = 'Coconut(नारियल)'
            cp = 'Banana,Pepper'
        elif predict1 == 5:
            crop_name = 'Coffee(कॉफ़ी)'
            cp = 'Black Pepper,Cardamom'
        elif predict1 == 6:
            crop_name = 'Cotton(कपास)'
            cp = 'Mung seeds,Peas'
        elif predict1 == 7:
            crop_name = 'Grapes(अंगूर)'
            cp = 'Clover Plants'
        elif predict1 == 8:
            crop_name = 'Jute(जूट)'
            cp = 'No alternatives'
        elif predict1 == 9:
            crop_name = 'Kidneybeans(राज़में)'
            cp = 'No alternatives'
        elif predict1 == 10:
            crop_name = 'Lentil(मसूर की दाल)'
            cp = 'jowar'
        elif predict1 == 11:
            crop_name = 'Maize(मक्का)'
            cp = 'Bajra'
        elif predict1 == 12:
            crop_name = 'Mango(आम)'
            cp = 'Lemon,Guava'
        elif predict1 == 13:
            crop_name = 'Mothbeans(मोठबीन)'
            cp = 'Cotton'
        elif predict1 == 14:
            crop_name = 'Mungbeans(मूंग)'
        elif predict1 == 15:
            crop_name = 'Muskmelon(खरबूजा)'
            cp = 'Cucumber,Watermelon'
        elif predict1 == 16:
            crop_name = 'Orange(संतरा)'
            cp = 'Soyabeans,Peas'
        elif predict1 == 17:
            crop_name = 'Papaya(पपीता)'
            cp = 'Potatoes,Onions,Carrots'
        elif predict1 == 18:
            crop_name = 'Pigeonpeas(कबूतर के मटर)'
            cp = 'Green Lentils'
        elif predict1 == 19:
            crop_name = 'Pomegranate(अनार)'
            cp = 'No alternative'
        elif predict1 == 20:
            crop_name = 'Rice(चावल)'
            cp = "raagi,sajji"
        elif predict1 == 21:
            crop_name = 'Watermelon(तरबूज)'
            cp = 'Muskmelon,Tomatoes,Chillies'
        if int(humidity_content) >= 1 and int(
                humidity_content) <= 33:
            humidity_level = 'low humid'
        elif int(humidity_content) >= 34 and int(humidity_content) <= 66:
            humidity_level = 'medium humid'
        else:
            humidity_level = 'high humid'

        if int(temperature_content) >= 0 and int(
                temperature_content) <= 6:
            temperature_level = 'cool'
        elif int(temperature_content) >= 7 and int(temperature_content) <= 25:
            temperature_level = 'warm'
        else:
            temperature_level = 'hot'

        if int(rainfall) >= 1 and int(
                rainfall) <= 100:
            rainfall_level = 'less'
        elif int(rainfall) >= 101 and int(rainfall) <= 200:
            rainfall_level = 'moderate'
        elif int(rainfall) >= 201:
            rainfall_level = 'heavy rain'

        if int(nitrogen_content) >= 1 and int(
                nitrogen_content) <= 50:
            nitrogen_level = 'less'
        elif int(nitrogen_content) >= 51 and int(nitrogen_content) <= 100:
            nitrogen_level = 'not to less but also not to high'
        elif int(nitrogen_content) >= 101:
            nitrogen_level = 'high'

        if int(phosphorus_content) >= 1 and int(
                phosphorus_content) <= 50:
            phosphorus_level = 'less'
        elif int(phosphorus_content) >= 51 and int(phosphorus_content) <= 100:
            phosphorus_level = 'not to less but also not to high'
        elif int(phosphorus_content) >= 101:
            phosphorus_level = 'high'

        if int(potassium_content) >= 1 and int(
                potassium_content) <= 50:
            potassium_level = 'less'
        elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
            potassium_level = 'not to less but also not to high'
        elif int(potassium_content) >= 101:
            potassium_level = 'high'

        if float(ph_content) >= 0 and float(ph_content) <= 5:
            phlevel = 'acidic'
        elif float(ph_content) >= 6 and float(ph_content) <= 8:
            phlevel = 'neutral'
        elif float(ph_content) >= 9 and float(ph_content) <= 14:
            phlevel = 'alkaline'

        print(crop_name)
        print(humidity_level)
        print(temperature_level)
        print(rainfall_level)
        print(nitrogen_level)
        print(phosphorus_level)
        print(potassium_level)
        print(phlevel)

        screen.configure(text=crop_name)
        screen1.configure(text=cp)

        speak(
            "According to the data that you provided to me. The ratio of nitrogen in the soil is  " + nitrogen_level + ". The ratio of phosphorus in the soil is  " + phosphorus_level + ". The ratio of potassium in the soil is  " + potassium_level + ". The temperature level around the field is  " + temperature_level + ". The humidity level around the field is  " + humidity_level + ". The ph type of the soil is  " + phlevel + ". The amount of rainfall is  " + rainfall_level)  # Making our program to speak about the data that it has received about the crop in front of the user.

        speak("The best crop that you can grow is  " + crop_name)
        speak("The other alternatives are " + cp)
        break


customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Crop Predictor")
frame = root
crop_name = customtkinter.StringVar()
cp = customtkinter.StringVar()
label = customtkinter.CTkLabel(master=frame, text="CROPYPREDO", font=('arial', 50, "bold"))
label.pack(pady=12, padx=10)
product_label = customtkinter.CTkLabel(root, text="Ratio of nitrogen:", font=('arial', 20, 'bold'))
product_label.place(x=40, y=83)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:62")
entry1.place(x=225, y=83)

product_label1 = customtkinter.CTkLabel(root, text="Ratio of phosphorus:", font=('arial', 18, 'bold'))
product_label1.place(x=30, y=132)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:50")
entry2.place(x=225, y=132)

product_label2 = customtkinter.CTkLabel(root, text="Ratio of pottasium:", font=('arial', 18, 'bold'))
product_label2.place(x=30, y=187)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:20")
entry3.place(x=225, y=190)

product_label3 = customtkinter.CTkLabel(root, text="Avg Temperature:", font=('arial', 18, 'bold'))
product_label3.place(x=30, y=232)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:25")
entry4.place(x=225, y=237)

product_label = customtkinter.CTkLabel(root, text="Humidity:", font=('arial', 18, 'bold'))
product_label.place(x=30, y=287)

entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:50")
entry5.place(x=225, y=287)

product_label = customtkinter.CTkLabel(root, text=" Ph:", font=('arial', 18, 'bold'))
product_label.place(x=30, y=342)
entry6 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:7")
entry6.place(x=225, y=340)

product_label = customtkinter.CTkLabel(root, text="Rainfall:", font=('arial', 18, 'bold'))
product_label.place(x=30, y=387)
entry7 = customtkinter.CTkEntry(master=frame, placeholder_text="eg:60")
entry7.place(x=225, y=385)

button = customtkinter.CTkButton(master=frame, text="Submit", command=login)
button.place(x=150, y=500)

screen = customtkinter.CTkLabel(master=root, text="Crop", font=('arial', 18, 'bold'))
screen.place(x=700, y=200)
screen1 = customtkinter.CTkLabel(master=root, text="Alternate Crop", font=('arial', 18, 'bold'))
screen1.place(x=1000, y=200)

root.mainloop()
