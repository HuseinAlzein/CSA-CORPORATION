import csv
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
def get_verbs():
    with open(r"c:\Users\hussein\Desktop\CSA Corporation\All_Verbs.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        verbs = []
        for row in csv_reader:
            words = row['Verbs'].split()
            for word in words:
                cleaned_word = re.sub("[^a-zàâçéèêëîïôûùüÿñæœ]", "", word)
                if cleaned_word:
                    verbs.append(cleaned_word)
        return verbs

verbs = get_verbs()
class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_enter(self, *args):
        self.add_widget(Image(source=r"C:\Users\hussein\Desktop\CSA Corporation\Corp.png", size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5}, allow_stretch=True))
class MainAppScreen(Screen):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})
        with layout.canvas.before:
            Color(0,3,6,5)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        logo = Image(source='C:\\Users\\hussein\\Desktop\\CSA Corporation\\Jupiter\\favicon.ico')
        self.verb_input = TextInput(hint_text='Input The Verb', multiline=False, font_size="36", background_color=(1,1,1,1), foreground_color=(0,0,0,1))  # white box, black text
        self.pronoun_input = TextInput(hint_text='Input The pronoun', multiline=False, font_size="36", background_color=(1,1,1,1), foreground_color=(0,0,0,1))  # white box, black text
        self.time_input = Spinner(
            values=('Present', 'Futur Simple', 'Futur Anteriur', 'Passe Compose', 'Imparfait', 'Plus-Que-Parfait', 'Subjonctif', 'Conditionnel Passe', 'Conditionnel Present'),
            text='Time',
            size_hint=(0, 1),
            size=(140, 170),
            color = (1, 1, 1, 1),
            pos_hint={'center_x': .5, 'center_y': .5})
        
        self.result_label = Label(font_size="32",color=(0,0,0,1)) 
        submit_button = Button(text='Conjugate',on_press=self.check_time, size_hint=(.5, .5), font_size="50", pos_hint={'center_x': .5, 'center_y': .1}, background_color=(1,0,0,1), color=(1,1,1,1))  # red

        layout.add_widget(logo)
        layout.add_widget(Label(text='Jupiter', font_size="32", color=(0,0,0,1))) 
        layout.add_widget(self.verb_input)
        layout.add_widget(self.pronoun_input)
        layout.add_widget(self.time_input)
        layout.add_widget(self.result_label)
        layout.add_widget(submit_button)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    def check_time(self, instance):
        Time = self.time_input.text.strip()
        Present = "Present"
        F_S = "Futur Simple"
        F_A = "Futur Anteriur"
        P_C = "Passe Compose"
        Im = "Imparfait"
        Plus_que_rarfait = "Plus-Que-Parfait"
        Subjonctif = "Subjonctif"
        conditionnel_passe = "Conditionnel Passe"
        conditionnel_present = "Conditionnel Present"
        
        Verb = self.verb_input.text.strip()
        pase = Verb[:-2]
        if Verb not in verbs:
            self.result_label.text = "Please Write The Verb With The Correct Form "
            return
        Pase = Verb[:-2].lower()
        pronom = self.pronoun_input.text.strip().capitalize()

        def get_result(line_number):
            with open(r"c:\Users\hussein\Desktop\CSA Corporation\All_Verbs.csv") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                Row= []
                for row in csv_reader:
                    line = row[str(line_number)]
                    line = re.sub('[^a-zàâçéèêëîïôûùüÿñæœ]', '', line)
                    Row.extend(line.split())
                return Row

###############__Rows__###############                
###############__Rows__###############                
        Row1 = get_result(1)
        Row2 = get_result(2)
        Row6 = get_result(6)
        Row7 = get_result(7)
        Row8 = get_result(8)
        Row9 = get_result(9)
        Row10 = get_result(10)
        Row11 = get_result(11)
        Row12 = get_result(12)
        Row13 = get_result(13)
        Row14 = get_result(14)
        Row15 = get_result(15)
        Row16 = get_result(16)
        Row17 = get_result(17)
        Row18 = get_result(18)
        Row19 = get_result(19)
        Row20 = get_result(20)
        Row22 = get_result(22)
        Row23 = get_result(23)
        Row24 = get_result(24)
        Row25 = get_result(25) 
        Row26 = get_result(26) 
        Row27 = get_result(27) 
        Row28 = get_result(28) 
        Row29 = get_result(29) 
        Row30 = get_result(30) 
        Row31 = get_result(31) 
        Row32 = get_result(32) 
        Row33 = get_result(33) 
        Row34 = get_result(34) 
        Row35 = get_result(35) 
        Row36 = get_result(36) 
        Row37 = get_result(37) 
        Row38 = get_result(38) 
        Row39 = get_result(39) 
        Row40 = get_result(40) 
        Row41 = get_result(41) 
        Row42 = get_result(42) 
        Row43 = get_result(43) 
        Row44 = get_result(44) 
        Row45 = get_result(45) 
        Row46 = get_result(46) 
        Row47 = get_result(47) 
        Row48 = get_result(48) 
        Row49 = get_result(49) 
        Row50 = get_result(50) 
        Row51 = get_result(51) 
        Row52 = get_result(52) 
        Row53 = get_result(53) 
        Row54 = get_result(54) 
        Row55 = get_result(55) 
        Row56 = get_result(56) 
        Row57 = get_result(57) 
        Row58 = get_result(58) 
        Row59 = get_result(59) 
        Row60 = get_result(60) 
        Row61 = get_result(61) 
        Row62 = get_result(62) 
        Row63 = get_result(63) 
        Row64 = get_result(64) 
        Row65 = get_result(65) 
        Row66 = get_result(66) 
        Row67 = get_result(67) 
        Row68 = get_result(68) 
        Row69 = get_result(69) 
        Row70 = get_result(70) 
        Row71 = get_result(71) 
        Row72 = get_result(72) 
        Row73 = get_result(73) 
        Row74 = get_result(74) 
        Row75 = get_result(75) 
        Row76 = get_result(76) 
        Row77 = get_result(77) 
        Row78 = get_result(78) 
        Row79 = get_result(79) 
        Row80 = get_result(80) 
        Row81 = get_result(81) 
        Row82 = get_result(82) 
###############__Rows__###############                
###############__Rows__###############         
    
###############__1__###############                
###############__Present__###############                
        if Verb in Row1:
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = "ai"
                elif pronom == "Tu" :
                    self.result_label.text = "as"
                elif pronom in ["Il","Elle","On"] :
                    self.result_label.text = "a"
                elif pronom == "Nous" :
                    self.result_label.text = "avons"
                elif pronom == "Vous" :
                    self.result_label.text = 'avez'
                elif pronom in ["Ils","Elles"] :
                    self.result_label.text = 'ont'
###############__Passe_Compose__###############
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai eu"
                elif pronom == "Tu":
                    self.result_label.text = "as eu"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a eu"
                elif pronom == "Nous":
                    self.result_label.text = "avons eu"
                elif pronom == "Vous":
                    self.result_label.text = "avez eu"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont eu" 
########    #######__Imparfait__###############
            elif Time == Im :
                if pronom == "Je":
                    self.result_label.text ="avais"
                elif pronom == "Tu":
                    self.result_label.text = "avais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait"
                elif pronom == "Nous":
                    self.result_label.text = "avions"
                elif pronom == "Vous":
                    self.result_label.text = "aviez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient"
########    #######__Plus-que-rarfait__###############
            elif Time ==  Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais eu"
                elif pronom == "Tu":
                    self.result_label.text = "avais eu"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait eu"
                elif pronom == "Nous":
                    self.result_label.text = "avions eu"
                elif pronom == "Vous":
                    self.result_label.text = "aviez eu"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient eu"
########    #######__Futur_Simple__###############
            elif Time ==  F_S:
                if pronom == "Je":
                    self.result_label.text ="aurai"
                elif pronom == "Tu":
                    self.result_label.text = "auras"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura"
                elif pronom == "Nous":
                    self.result_label.text = "aurons"
                elif pronom == "Vous":
                    self.result_label.text = "aurez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront"
########    #######__Futur_Anterieur__###############
            elif Time ==  F_A:
                if pronom == "Je":
                    self.result_label.text ="aurai eu"
                elif pronom == "Tu":
                    self.result_label.text = "auras eu"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura eu"
                elif pronom == "Nous":
                    self.result_label.text = "aurons eu"
                elif pronom == "Vous":
                    self.result_label.text = "aurez eu"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront eu"
########    #######__Subjonctif__###############
            elif Time ==  Subjonctif:
                if pronom == "Je":
                    self.result_label.text ="que j' aie"
                elif pronom == "Tu":
                    self.result_label.text = "que tu aies"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " ait"
                elif pronom == "Nous":
                    self.result_label.text = "que nous ayons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous ayez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " aient"
########    #######__Conditionnel_Passe__###############
            elif Time ==  conditionnel_passe:
                if pronom == "Je":
                    self.result_label.text ="aurais eu"
                elif pronom == "Tu":
                    self.result_label.text = "aurais eu"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait eu"
                elif pronom == "Nous":
                    self.result_label.text = "aurions eu"
                elif pronom == "Vous":
                    self.result_label.text = "auriez eu"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "aurient eu"
########    #######__Conditionnel_Present__###############
            elif Time ==  conditionnel_present:
                if pronom == "Je":
                    self.result_label.text ="aurais"
                elif pronom == "Tu":
                    self.result_label.text = "aurais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait"
                elif pronom == "Nous":
                    self.result_label.text = "aurions"
                elif pronom == "Vous":
                    self.result_label.text = "auriez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "aurient"
###############__2__###############                
###############__Present__###############                
        elif Verb in Row2:
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = "suis"
                elif pronom == "Tu" :
                    self.result_label.text = "es"
                elif pronom in ["Il","Elle","On"] :
                    self.result_label.text = "est"
                elif pronom == "Nous" :
                    self.result_label.text = "sommes"
                elif pronom == "Vous" :
                    self.result_label.text = 'êtes'
                elif pronom in ["Ils","Elles"] :
                    self.result_label.text = 'sont'
###############__Passe_Compose__###############

            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai été"
                elif pronom == "Tu":
                    self.result_label.text = "as été"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a été"
                elif pronom == "Nous":
                    self.result_label.text = "avons été"
                elif pronom == "Vous":
                    self.result_label.text = "avez été"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont été"
########    #######__Imparfait__###############

            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text ="étais"
                elif pronom == "Tu":
                    self.result_label.text = "étais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "était"
                elif pronom == "Nous":
                    self.result_label.text = "étions"
                elif pronom == "Vous":
                    self.result_label.text = "étiez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "étaient"

########    #######__Plus-que-parfait__###############

            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais été"
                elif pronom == "Tu":
                    self.result_label.text = "avais été"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait été"
                elif pronom == "Nous":
                    self.result_label.text = "avaions été"
                elif pronom == "Vous":
                    self.result_label.text = "avaiez été"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient été"

########    #######__Futur Simple__###############

            if Time == F_S:
                if pronom == "Je":
                    self.result_label.text ="serai"
                elif pronom == "Tu":
                    self.result_label.text = "seras"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "sera"
                elif pronom == "Nous":
                    self.result_label.text = "serons"
                elif pronom == "Vous":
                    self.result_label.text = "serez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "seront"

########    #######__Futur Anteriur__###############

            elif Time == F_A:
                if pronom == "Je":
                    self.result_label.text ="aurai été"
                elif pronom == "Tu":
                    self.result_label.text = "auras été"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura été"
                elif pronom == "Nous":
                    self.result_label.text = "aurons été"
                elif pronom == "Vous":
                    self.result_label.text = "aurez été"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "aurez été"

########    #######__Subjonctif__###############

            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text ="que je sois"
                elif pronom == "Tu":
                    self.result_label.text = "que tu sois"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " soit"
                elif pronom == "Nous":
                    self.result_label.text = "que nous soyons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous soyez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " soient"

########    #######__Conditionnel_Passe__###############

            elif Time == conditionnel_passe:
                if pronom == "Je":
                    self.result_label.text ="aurais été"
                elif pronom == "Tu":
                    self.result_label.text = "aurais été"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait été"
                elif pronom == "Nous":
                    self.result_label.text = "aurions été"
                elif pronom == "Vous":
                    self.result_label.text = "auriez été"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text =  "auraient été"

########    #######__Conditionnel_Present__###############

            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text ="serais"
                elif pronom == "Tu":
                    self.result_label.text = "serais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "serait"
                elif pronom == "Nous":
                    self.result_label.text = "serions"
                elif pronom == "Vous":
                    self.result_label.text = "seriez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text =  "seraient"
                    
###############__6__###############
###############__Present__###############
        elif Verb in Row6:
            if Time == Present:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Combose__############### 
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée
###############__Imparfait__############### 
            elif Time == Im:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pase + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "aient"  
###############__Plus-que-parfait__############### 
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avient " + pasée
###############__Futur-Simple__############### 
            elif Time == F_S:
                pase = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb + "ont"
###############__Futur-Anteriur__############### 
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée
                    
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée
###############__7__###############                
        if Verb in Row7:
###############__Present__###############                

            if Time == Present:
                pase = Verb[:-2]
                ver7 = str(Verb)
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    Verb_ons = ver7.replace("cer" , "çer")
                    pas_ons = Verb_ons[:-2]
                    self.result_label.text = pas_ons + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("cer" , "çer")
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text == Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + Pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + Pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + Pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée            
                    
         
###############------------8--------------###############                
############### Present ###############               
        elif Verb in Row8:
            if Time == Present:
                pase = Verb[:-2]
                ver7 = str(Verb)
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    Verb_ons = ver7.replace("ger" , "geer")
                    pas_ons = Verb_ons[:-2]
                    self.result_label.text = pas_ons + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("ger" , "geer")
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text == Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + Pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom+" " + Pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + Pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + Pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom+" "+ Pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée
###############------------9--------------###############                
############### Present ###############               
        elif Verb in Row9:
            if Time == "Present":
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "e"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("ger" , "geer")
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = Verb_ons + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb_ons + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb_ons + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb_ons + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb_ons + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb_ons + "ont"     
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = "que je "+pas_ons + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+pas_ons + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom+" " + pas_ons + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom+" " + pas_ons + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = Verb_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb_ons + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb_ons + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb_ons + "aient" 
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée
###############------------10--------------###############                
############### Present ###############               
        elif Verb in Row10:
            if Time == "Present":
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "e"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("ger" , "geer") 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "é" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = Verb_ons + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb_ons + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb_ons + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb_ons + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb_ons + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb_ons + "ont"     
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = "que je "+pas_ons + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+pas_ons + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom+" " + pas_ons + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom+" " + pas_ons + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7[0] + "è" + ver7[2:] 
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = Verb_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb_ons + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb_ons + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb_ons + "aient" 
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée
###############------------11--------------###############                
############### Present ###############               
        elif Verb in Row11:
            if Time == Present:
                pase = Verb[:-2]
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "eller")
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent"
                    #####
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "etter") 
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent" 
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("ger" , "geer")
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "eller")
                    if pronom == "Je":
                        self.result_label.text = Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"       
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "etter")
                    if pronom == "Je":
                        self.result_label.text = Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "eller")
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    #####
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "etter") 
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ions"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "iez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée
###############------------12--------------###############                
############### Present ###############               
        elif Verb in Row12:
            if Time == Present:
                pase = Verb[:-2]
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "èler")
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent"
                    #####
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "èter") 
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent" 
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                Verb_ons = ver7.replace("ger" , "geer")
                pas_ons = Verb_ons[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "èler")
                    if pronom == "Je":
                        self.result_label.text = Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"     
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "èter")
                    if pronom == "Je":
                        self.result_label.text = Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"  
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "èler")
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "ent"
                    #####
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "èter") 
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ions"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "iez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée     
###############------------13--------------###############                
###############__Present__###############
        elif Verb in Row13:
            if Time == Present:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Combose__############### 
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée
###############__Imparfait__############### 
            elif Time == Im:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pase + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "aient"  
###############__Plus-que-parfait__############### 
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avient " + pasée
###############__Futur-Simple__############### 
            elif Time == F_S:
                pase = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb + "ont"
###############__Futur-Anteriur__############### 
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                    
###############------------14--------------###############                
############### Present ###############               
        elif Verb in Row14:
            if Time == Present:
                pase = Verb[:-2]
                if Verb[-3] == "g" or Verb[:-3] == "G":
                    Verb_ons = Verb.replace("éger" , "èger")
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "eons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                pas_ons = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("eler" , "èler")
                    if pronom == "Je":
                        self.result_label.text == Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"     
                elif Verb[-3] == "t" or Verb[:-3] == "T":
                    Verb_ons = Verb.replace("eter" , "èter")
                    if pronom == "Je":
                        self.result_label.text == Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"  
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if Verb[-3] == "l" or Verb[:-3] == "L":
                    Verb_ons = Verb.replace("éger" , "èger")
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                   
###############------------15--------------###############                
###############__Present__###############
        elif Verb in Row15:
            if Time == Present:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Combose__############### 
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée
###############__Imparfait__############### 
            elif Time == Im:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pase + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "aient"  
###############__Plus-que-parfait__############### 
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avient " + pasée
###############__Futur-Simple__############### 
            elif Time == F_S:
                pase = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb + "ont"
###############__Futur-Anteriur__############### 
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée
                    
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                                        
###############------------16-17-18------------###############                
############### Present ###############               
        elif Verb in Row16 or Verb in Row17 or Verb in Row19:
            if Time == Present:
                pase = Verb[:-2]
                if Verb[-3] == "y" or Verb[:-3] == "Y":
                    Verb_ons = Verb.replace("yer" , "ier")
                    paseo = Verb_ons[:-2]
                    if pronom == "Je":
                        self.result_label.text = paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "eons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée      
###############__Imparfait__###############                
            elif Time == Im:
                pase = Verb[:-2]
                ver7 = str(Verb)
                pas_ons = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pas_ons + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pas_ons + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pas_ons + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if Verb[-3] == "y" or Verb[:-3] == "y":
                    Verb_ons = Verb.replace("yer" , "ier")
                    if pronom == "Je":
                        self.result_label.text == Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if Verb[-3] == "y" or Verb[:-3] == "Y":
                    Verb_ons = Verb.replace("yer" , "ier")
                    paseo = Verb_ons[:-2]
                    pase = Verb[:-2]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ paseo + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ paseo + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ paseo + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                    
###############__Ir ir ir  ir ir ir ir ir ir ir  ir ir ir __###############                
###############__Ir ir ir  ir ir ir ir ir ir ir  ir ir ir __###############                
###############__19__###############
###############__Present__###############
        elif Verb in Row19:
            if Time == Present:
                pase1 = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "is"
                elif pronom == "Tu":
                    self.result_label.text = pase + "is"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "it"
                elif pronom == "Nous":
                    self.result_label.text = pase + "issons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "issez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "issent"
###############__Passe_Combose__############### 
            elif Time == P_C:
                pasée = Verb[:-2] 
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée
###############__Imparfait__############### 
            elif Time == Im:
                paseIM = Verb[:-2] + "iss"
                if pronom == "Je":
                    self.result_label.text = paseIM + "ais"
                elif pronom == "Tu":
                    self.result_label.text = paseIM + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = paseIM + "ait"
                elif pronom == "Nous":
                    self.result_label.text = paseIM + "ions"
                elif pronom == "Vous":
                    self.result_label.text = paseIM + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = paseIM + "aient"  
###############__Plus-que-parfait__############### 
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] 
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avient " + pasée
###############__Futur-Simple__############### 
            elif Time == F_S:
                pase = Verb[:-2] 
                if pronom == "Je":
                    self.result_label.text = Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb + "ont"
###############__Futur-Anteriur__############### 
            elif Time == F_A:
                pasée = Verb[:-2] 
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée
                    
###############Subjonctif###############   
            elif Time == Subjonctif:
                pasei = Verb[:-2] + "iss"
                if pronom == "Je":
                    self.result_label.text == "que je " + pasei  + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pasei + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pasei + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + pasei+ "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + pasei + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + pasei + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                                  
###############--------------20--------------###############                
############### Present ###############               
        elif Verb in Row20:
            if Time == Present:
                pase = Verb[:-2]
                if Verb[-2] == "ï":
                    Verb_ons = Verb.replace("ïr" , "ir")
                    paseo = Verb_ons[:-2]
                    paseo2 = Verb[:-1]
                    if pronom == "Je":
                        self.result_label.text = paseo + "is"
                    elif pronom == "Tu":
                        self.result_label.text = paseo + "is"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = paseo + "it"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ssons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ssez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = paseo + "ssent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if Verb[-2] == "ï":
                    Verb_ons = Verb.replace("ïr" , "ir")
                    paseo = Verb_ons[:-1]
                    if pronom == "Je":
                        self.result_label.text ="ai " + paseo
                    elif pronom == "Tu":
                        self.result_label.text = "as " + paseo
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "a " + paseo
                    elif pronom == "Nous":
                        self.result_label.text = "avons " + paseo
                    elif pronom == "Vous":
                        self.result_label.text = "avez " + paseo
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "ont " + paseo      
###############__Imparfait__###############                
            elif Time == Im:
                if Verb[-2] == "ï":
                    Verb_ons = Verb.replace("ïr" , "ir")
                    pas_ons = Verb_ons[:-1]
                    if pronom == "Je":
                        self.result_label.text = pas_ons + "ais"
                    elif pronom == "Tu":
                        self.result_label.text = pas_ons + "ais"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = pas_ons + "ait"
                    elif pronom == "Nous":
                        self.result_label.text = pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = pas_ons + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pasée        
###############Futur- Simple###############         
            elif Time == F_S:
                if Verb[-2] == "ï":
                    Verb_ons = Verb.replace("ïr" , "ir")
                    if pronom == "Je":
                        self.result_label.text = Verb_ons + "ai"
                    elif pronom == "Tu":
                        self.result_label.text = Verb_ons + "as"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = Verb_ons + "a"
                    elif pronom == "Nous":
                        self.result_label.text = Verb_ons + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = Verb_ons + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = Verb_ons +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if Verb[-2] == "ï":
                    Verb_ons = Verb.replace("ïr" , "ir")
                    paseo = Verb_ons[:-1]
                    pase = Verb[:-1]
                    if pronom == "Je":
                        self.result_label.text = "que je "+ pase + "e"
                    elif pronom == "Tu":
                        self.result_label.text = "que tu "+ pase + "es"
                    elif pronom in ["Il","Elle","On"]:
                        self.result_label.text = "que "+pronom+" "+ pase + "e"
                    elif pronom == "Nous":
                        self.result_label.text = "que nous "+ pase + "ons"
                    elif pronom == "Vous":
                        self.result_label.text = "que vous "+ pase + "ez"
                    elif pronom in ["Ils","Elles"]:
                        self.result_label.text = "que "+pronom+" "+ pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                                       
###############__Aller --22--__###############                
###############__Present__###############                

        if Verb in Row22:
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = "vais"
                elif pronom == "Tu" :
                    self.result_label.text = "vas"
                elif pronom in ["Il","Elle","On"] :
                    self.result_label.text = "va"
                elif pronom == "Nous" :
                    self.result_label.text = "allons"
                elif pronom == "Vous" :
                    self.result_label.text = 'allez'
                elif pronom in ["Ils","Elles"] :
                    self.result_label.text = 'vont'
###############__Passe_Compose__###############
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="suis allé"
                elif pronom == "Tu":
                    self.result_label.text = "es allé"
                elif pronom in ["Il","Elle","On"]:
                    if pronom == "Elle":
                        self.result_label.text = "est allée"
                    else:
                        self.result_label.text = "est allé"
                elif pronom == "Nous":
                    self.result_label.text = "sommes allés"
                elif pronom == "Vous":
                    self.result_label.text = "êtes allés"
                elif pronom in ["Ils","Elles"]:
                    if pronom == "Elles":
                        self.result_label.text = "est allées"
                    else:
                        self.result_label.text = "est allés"
########    #######__Imparfait__###############
            elif Time == Im :
                if pronom == "Je":
                    self.result_label.text ="allais"
                elif pronom == "Tu":
                    self.result_label.text = "allais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "allait"
                elif pronom == "Nous":
                    self.result_label.text = "allions"
                elif pronom == "Vous":
                    self.result_label.text = "alliez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "allaient"
########    #######__Plus-que-rarfait__###############
            elif Time ==  Plus_que_rarfait:
                if pronom == "Je": 
                    self.result_label.text ="étais allé"
                elif pronom == "Tu":
                    self.result_label.text = "étais allé"
                elif pronom in ["Il","Elle","On"]:
                    if pronom == "Elle":
                        self.result_label.text = "était allée"
                    else:
                        self.result_label.text = "était allé"
                elif pronom == "Nous":
                    self.result_label.text = "étions allé"
                elif pronom == "Vous":
                    self.result_label.text = "étiez allé"
                elif pronom in ["Ils","Elles"]:
                    if pronom == "Elles":
                        self.result_label.text = "étaient allées"
                    else:
                        self.result_label.text = "était allés"
########    #######__Futur_Simple__###############
            elif Time ==  F_S:
                if pronom == "Je":
                    self.result_label.text ="irai"
                elif pronom == "Tu":
                    self.result_label.text = "iras"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "ira"
                elif pronom == "Nous":
                    self.result_label.text = "irons"
                elif pronom == "Vous":
                    self.result_label.text = "irez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "iront"
########    #######__Futur_Anterieur__###############
            elif Time ==  F_A:
                if pronom == "Je":
                    self.result_label.text ="serai allé"
                elif pronom == "Tu":
                    self.result_label.text = "seras allé"
                elif pronom in ["Il","Elle","On"]:
                    if pronom == "Elle":
                        self.result_label.text = "sera allée"
                    else:
                        self.result_label.text = "sera allé"
                elif pronom == "Nous":
                    self.result_label.text = "serons allés"
                elif pronom == "Vous":
                    self.result_label.text = "serez allés"
                elif pronom in ["Ils","Elles"]:
                    if pronom == "Elles":
                        self.result_label.text = "seront allées"
                    else:
                        self.result_label.text = "seront allés"
########    #######__Subjonctif__###############
            elif Time ==  Subjonctif:
                if pronom == "Je":
                    self.result_label.text ="que j' aille"
                elif pronom == "Tu":
                    self.result_label.text = "que tu ailles"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " aille"
                elif pronom == "Nous":
                    self.result_label.text = "que nous allions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous alliez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "qu' " + (pronom.lower()) + " aillent"
########    #######__Conditionnel_Passe__###############
            elif Time ==  conditionnel_passe:
                if pronom == "Je":
                    self.result_label.text ="serais allé"
                elif pronom == "Tu":
                    self.result_label.text = "serais allé"
                elif pronom in ["Il","Elle","On"]:
                    if pronom == "Elle":
                        self.result_label.text = "serait allée"
                    else:
                        self.result_label.text = "serait allé"
                elif pronom == "Nous":
                    self.result_label.text = "serions allés"
                elif pronom == "Vous":
                    self.result_label.text = "seriez allés"
                elif pronom in ["Ils","Elles"]:
                    if pronom == "Elles":
                        self.result_label.text = "seraient allées"
                    else:
                        self.result_label.text = "seraient allés"
########    #######__Conditionnel_Present__###############
            elif Time ==  conditionnel_present:
                if pronom == "Je":
                    self.result_label.text ="irais"
                elif pronom == "Tu":
                    self.result_label.text = "irais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "irait"
                elif pronom == "Nous":
                    self.result_label.text = "irions"
                elif pronom == "Vous":
                    self.result_label.text = "iriez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "iraient"
###############--------------23--------------###############                
############### Present ###############               
        elif Verb in Row23:
            pase1 = Verb[0] + "i" + Verb[1:3]
            pase2 = Verb[:-2]
            pase3 = Verb[0] + "i" + Verb[1:3] + "n"
            pascom = pase2 +"u"
            pasfs = pase1 +"dr"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------24--------------###############                
############### Present ###############               
        elif Verb in Row24:
            pase1 = Verb[:-4] + "e"
            pase2 = Verb[:-2]
            pase3 = Verb[:-4] + "è"
            pascom = Verb[:-1] +"s"
            pasfs = pase1 +"rr"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------25--------------###############                
############### Present ###############               
        elif Verb in Row25:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-1] +"s"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------26--------------###############                
############### Present ###############               
        elif Verb in Row26:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"u"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------27--------------###############                
############### Present ###############               
        elif Verb in Row27:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"t"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------28--------------###############                
############### Present ###############               
        elif Verb in Row28:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------29--------------###############                
############### Present ###############               
        elif Verb in Row29:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------30--------------###############                
############### Present ###############               
        elif Verb in Row30:
            pase1 = Verb[1]+"au"
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------31--------------###############                
############### Present ###############               
        elif Verb in Row31:
            pase1 = Verb[:-5]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------32--------------###############                
############### Present ###############               
        elif Verb in Row32:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------33--------------###############                
############### Present ###############               
        elif Verb in Row33:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb[:-2]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "rai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------34--------------###############                
############### Present ###############               
        elif Verb in Row34:
            pase1 = Verb[0]+"e"+Verb[2:4]
            pase2 = Verb[:-2]
            pase3 = Verb[0]+"e"+Verb[2:4]
            pascom = Verb[0]+Verb[1:2]+"rt"
            pasfs = Verb[:-2]+"r"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------35--------------###############                
############### Present ###############               
        elif Verb in Row35:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------36--------------###############                
############### Present ###############               
        elif Verb in Row36:
            pase1 = Verb[:-1]
            pase2 = Verb[:-2]+"y"
            pase3 = Verb[:-1]
            pascom = Verb[:-2] +"i"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------37--------------###############                
############### Present ###############               
        elif Verb in Row37:
            pase1 = Verb[:-2]+"i"
            pase2 = Verb[:-3]+"y"
            pase3 = Verb[:-2]+"y"
            pascom = Verb[:-1]
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text == pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------38--------------###############         
############### Present ###############               
        elif Verb in Row38:
            pase1 = Verb[:2]+"çoi"
            pase2 = Verb[:-3]
            pase3 = Verb[:2]+"çoiv"
            pascom = Verb[:2]+"çu"
            pasfs = Verb[:-3]+"r"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------39--------------###############         
############### Present ###############               
        elif Verb in Row39:
            pase1 = Verb[:-1]
            pase2 = Verb[:-2]+"y"
            pase3 = Verb[:-2]
            pascom = Verb[:-3]+"u"
            pasfs = Verb[:-3]+"err"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------40--------------###############         
############### Present ###############               
        elif Verb in Row40:
            pase1 = Verb[:-1]
            pase2 = Verb[:-2]+"y"
            pase3 = Verb[:-2]
            pascom = Verb[:-3]+"u"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------41--------------###############         
############### Present ###############               
        elif Verb in Row41:
            pase1 = Verb[:-4]+"i"
            pase2 = Verb[:-3]
            pase3 = Verb[:-3]
            pascom = Verb[:-5]+"u"
            pasfs = Verb[:-4]+"ur"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------42--------------###############         
############### Present ###############               
        elif Verb in Row42:
            pase1 = Verb[:-5]+"oi"
            pase2 = Verb[:-3]
            pase3 = Verb[:-5]+"oiv"
            pascom = Verb[:-5]+"û"
            pasfs = Verb[:-3]+"r"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------43--------------###############         
############### Present ###############               
        elif Verb in Row43:
            pase1 = Verb[-7]+"e"+Verb[-5]
            pase2 = Verb[:-3]
            pase3 = Verb[-7]+"e"+Verb[-5]+Verb[-4]
            pascom = Verb[:-7]+"u"
            pasfs = Verb[:-4]+"rr"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------44--------------###############         
############### Present ###############               
        elif Verb in Row44:
            pase1 = Verb[-7]+"e"+Verb[-5]
            pase2 = Verb[:-3]
            pase3 = Verb[-7]+"e"+Verb[-5]+Verb[-4]
            pascom = Verb[-7]+"û"
            pasfs = Verb[:-3]+"r"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom                       
###############--------------45--------------###############         
############### Present ###############               
        elif Verb in Row45:
            pase1 = Verb[:-4]+"t"
            pase2 = Verb[:-4]+"t"
            pase3 = Verb[:-4]+"t"
            pascom = Verb[:-7]+"lu"
            pasfs = Verb[:-3]+"r"
            if Time == Present:
                if pronom == "Il":
                    self.result_label.text = pase1
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Il":
                    self.result_label.text ="a " + pascom
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Il":
                    self.result_label.text =Verb[:-3]+"ait"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Il":
                    self.result_label.text ="avait " + pascom
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Il":
                    self.result_label.text = pasfs + "a"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                if pronom == "Il":
                    self.result_label.text ="aura " + pascom
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Il":
                    self.result_label.text = "qu'il  " + Verb[:-3]+"e"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Il":
                    self.result_label.text = pasfs + "ait"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                if pronom == "Il":
                    self.result_label.text = "aurait " + pascom
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"                       
###############--------------46--------------###############         
############### Present ###############               
        elif Verb in Row46:
            if Time == Present:
                if pronom == "Il":
                    self.result_label.text = "faut"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Il":
                    self.result_label.text = "a fallu"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Il":
                    self.result_label.text ="fallait"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Il":
                    self.result_label.text ="avait fallu" 
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Il":
                    self.result_label.text ="faudra"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                if pronom == "Il":
                    self.result_label.text ="aura fallu"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Il":
                    self.result_label.text = "qu'il faille "
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Il":
                    self.result_label.text = pasfs + "faudrait"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                if pronom == "Il":
                    self.result_label.text = "aurait fallu"
                else:
                    self.result_label.text = "this verb doesn't cojugates except with il" 
###############--------------47--------------###############         
############### Present ###############               
        elif Verb in Row47:
            pase1 = Verb[:-4]+"u"
            pase2 = Verb[:-3]
            pase3 = Verb[:-3]
            pascom = Verb[:-3]+"u"
            pasfs = Verb[:-4]+"udr"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                      
###############--------------48--------------###############         
############### Present ###############               
        elif Verb in Row48:
            pase1 = Verb[0]+"eu"
            pase2 = Verb[:-3]
            pase3 = Verb[0]+"eul"
            pascom = Verb[:-3]+"u"
            pasfs = Verb[:-4]+"udr"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                      
###############--------------49--------------###############         
############### Present ###############               
        elif Verb in Row49:
            pase1 = Verb[:-4]+"ied"
            pase2 = Verb[:-3]+"y"
            pase3 = Verb[:-3]+"y"
            pascom = Verb[:-4]+"is"
            pasfs = Verb[:-4]+"iér"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "x"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "x"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pascom
###############--------------51--------------###############         
############### Present ###############               
        elif Verb in Row51:
            pase1 = Verb[:-4]+"oi"
            pase2 = Verb[:-4]+"oy"
            pase3 = Verb[:-4]+"oi"
            pascom = Verb[:-4]+"is"
            pasfs = Verb[:-4]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------52--------edit------###############         
############### Present ###############               
        elif Verb in Row52:
            pase1 = Verb[:-1]
            pase2 = Verb[:-1]
            pase3 = Verb[:-1]
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Il":
                    self.result_label.text = pase1 + "t"
                elif pronom  == "Ils":
                    self.result_label.text = pase3 + "ent"
                else:
                    self.result_label.text = "this verb doesn't support " + pronom
###############__Passe_Compose__###############                
            elif Time == P_C:
                self.result_label.text = "this verb doesn't support passe compose"   
###############__Imparfait__###############                
            elif Time == Im:
                self.result_label.text = "this verb doesn't support Imparfait"  
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                self.result_label.text = "this verb doesn't support Plus-Que-Parfait"         
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                else:
                    self.result_label.text = "this verb doesn't support " + pronom       
###############Futur- Anteriur###############         
            elif Time == F_A:
                self.result_label.text = "this verb doesn't support Futur Anteriur"    
###############Subjonctif###############   
            elif Time == Subjonctif:
                self.result_label.text = "this verb doesn't support subjonctif" 
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                else:
                    self.result_label.text = "this verb doesn't support " + pronom 
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                self.result_label.text = "this verb doesn't support Conditionnel Passe"
###############--------------53--------------###############         
############### Present ###############               
        elif Verb in Row53:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2]+"u"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------54--------------###############         
############### Present ###############               
        elif Verb in Row54:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]
            pase3 = Verb[:-3]+"n"
            pascom = Verb[:-5]+"is"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------55--------------###############         
############### Present ###############               
        elif Verb in Row55:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2]+"u"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------56--------------###############         
############### Present ###############               
        elif Verb in Row56:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-5]+"is"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------57--------------###############         
############### Present ###############               
        elif Verb in Row57:
            pase1 = Verb[:-3]
            pase2 = Verb[:-4]+"gn"
            pase3 = Verb[:-4]+"gn"
            pascom = Verb[:-3]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------58--------------###############         
############### Present ###############               
        elif Verb in Row58:
            pase1 = Verb[:-3]
            pase2 = Verb[:-4]+"gn"
            pase3 = Verb[:-4]+"gn"
            pascom = Verb[:-3]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------59--------------###############         
############### Present ###############               
        elif Verb in Row59:
            pase1 = Verb[:-3]
            pase2 = Verb[:-4]+"gn"
            pase3 = Verb[:-4]+"gn"
            pascom = Verb[:-3]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------60--------------###############         
############### Present ###############               
        elif Verb in Row60:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"qu"
            pase3 = Verb[:-4]+"gn"
            pascom = Verb[:-2]+"u"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------61--------------###############         
############### Present ###############               
        elif Verb in Row61:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"y"
            pase3 = Verb[:-2]
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------62--------------###############         
############### Present ###############               
        elif Verb in Row62:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"s"
            pasvo = Verb[:-2]+"tes"
            pase3 = Verb[:-4]+"ont"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-4]+"er"
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1 + "t"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasvo
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------63--------------###############         
############### Present ###############               
        elif Verb in Row63:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"s"
            pase3 = Verb[:-4]+"s"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------64--------------###############         
############### Present ###############               
        elif Verb in Row64:
            pase1 = Verb[:-4]+"i"
            pase2 = Verb[:-4]+"iss"
            pase3 = Verb[:-4]+"iss"
            pascom = Verb[:-5]+"u"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------65--------------###############         
############### Present ###############               
        elif Verb in Row65:
            pase1 = Verb[:-4]+"i"
            pase2 = Verb[:-4]+"iss"
            pase3 = Verb[:-4]+"iss"
            pascom = Verb[:-5]+"é"
            pasfs = Verb
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco
###############--------------66--------------###############         
############### Present ###############               
        elif Verb in Row66:
            pase1 = Verb[:-4]+"i"
            pase2 = Verb[:-4]+"iss"
            pase3 = Verb[:-4]+"iss"
            pascom = Verb[:-5]+"é"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:    
                self.result_label.text = "This Verb doesn't support passe compose" 
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                self.result_label.text = "This Verb doesn't support passe compose"        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                self.result_label.text = "This Verb doesn't support Futur Anteriur"     
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                self.result_label.text = "This Verb doesn't support Conditionnel-Passe" 
###############--------------67--------------###############         
############### Present ###############               
        elif Verb in Row67:
            pase1 = Verb[:-3]
            pase2 = Verb[:-4]+"iss"
            pase3 = Verb[:-4]+"iss"
            pascom = Verb[:-5]+"û"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------68--------------###############         
############### Present ###############               
        elif Verb in Row68:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"y"
            pase3 = Verb[:-2]
            pascom = Verb[:-5]+"û"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------69--------------###############         
############### Present ###############               
        elif Verb in Row69:
            pase1 = Verb[:-2]
            pase2 = Verb[:-4]+"uv"
            pase3 = Verb[:-2]+"v"
            pascom = Verb[:-4]+"u"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco     
                    
                    
                                   
###############--------------70--------------###############         
############### Present ###############               
        elif Verb in Row70:
            pase1 = Verb[:-2]
            pase2 = Verb[:-4]+"uv"
            pase3 = Verb[:-2]+"v"
            pascom = Verb[:-4]+"u"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco 
                    
                    
                    
                                       
###############--------------71--------------###############         
############### Present ###############               
        elif Verb in Row71:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2]
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------72--------------###############         
############### Present ###############               
        elif Verb in Row72:
            pase1 = Verb[:-3]
            pase2 = Verb[:-3]+"lv"
            pase3 = Verb[:-3]+"lv"
            pascom = Verb[:-3]+"s"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------73--------------###############         
############### Present ###############               
        elif Verb in Row73:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"s"
            pase3 = Verb[:-3]+"s"
            pascom = Verb[:-3]+"su"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------74--------------###############         
############### Present ###############               
        elif Verb in Row74:
            pase1 = Verb[:-2]
            pase2 = Verb[:-3]+"l"
            pase3 = Verb[:-3]+"l"
            pascom = Verb[:-3]+"lu"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------75--------------###############         
############### Present ###############               
        elif Verb in Row75:
            pase1 = Verb[:-3]
            pase2 = Verb[:-3]+"v"
            pase3 = Verb[:-3]+"v"
            pascom = Verb[:-3]+"vi"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------76--------------###############         
############### Present ###############               
        elif Verb in Row76:
            pase1 = Verb[:-3]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-4]+"écu"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------77--------------###############         
############### Present ###############               
        elif Verb in Row77:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"s"
            pase3 = Verb[:-2]+"s"
            pascom = Verb[:-3]+"u"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------78--------------###############         
############### Present ###############               
        elif Verb in Row78:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"s"
            pase3 = Verb[:-2]+"s"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------79--------------###############         
############### Present ###############               
        elif Verb in Row79:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]
            pase3 = Verb[:-2]
            pascom = Verb[:-2]
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------80--------------###############         
############### Present ###############               
        elif Verb in Row80:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"v"
            pase3 = Verb[:-2]+"v"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------81--------------###############         
############### Present ###############               
        elif Verb in Row81:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"s"
            pase3 = Verb[:-2]+"s"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco                    
###############--------------82--------------###############         
############### Present ###############               
        elif Verb in Row82:
            pase1 = Verb[:-2]
            pase2 = Verb[:-2]+"s"
            pase3 = Verb[:-2]+"s"
            pascom = Verb[:-2]+"t"
            pasfs = Verb[:-1]
            if Time == Present:
                if pronom == "Je":
                    self.result_label.text = pase1 + "s"
                elif pronom == "Tu":
                    self.result_label.text = pase1 + "s"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase1[:-1] + "ît"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase3 + "ent"
###############__Passe_Compose__###############                
            elif Time == P_C:
                if pronom == "Je":
                    self.result_label.text ="ai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "as " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pascom    
###############__Imparfait__###############                
            elif Time == Im:
                if pronom == "Je":
                    self.result_label.text = pase2 + "ais"
                elif pronom == "Tu":
                    self.result_label.text =pase2 + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase2 + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase2 + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase2 + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase2 + "aient"
###############Plus-Que-Parfait###############         
            elif Time == Plus_que_rarfait:
                if pronom == "Je":
                    self.result_label.text ="avais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avaient " + pascom        
###############Futur- Simple###############         
            elif Time == F_S:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ai"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "a"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"ont"       
###############Futur- Anteriur###############         
            elif Time == F_A:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurai " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pascom      
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text = "que je "+ pase3 + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu "+ pase3 + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous "+ pase3 + "ons"
                elif pronom == "Vous":
                    self.result_label.text = "que vous "+ pase3 + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que "+pronom+" "+ pase3 + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text = pasfs + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pasfs + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pasfs + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pasfs + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pasfs + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pasfs +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-1]
                if pronom == "Je":
                    self.result_label.text = "aurais " + pascom
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pascom
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pascom
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pascom
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pascom
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasco    
###############__6__###############
###############__Present__###############
        else:
            if Time == Present:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ons"
                elif pronom == "Vous":
                    self.result_label.text = pase + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "ent"
###############__Passe_Combose__############### 
            elif Time == P_C:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="ai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "as " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "a " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "avez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "ont " + pasée
###############__Imparfait__############### 
            elif Time == Im:
                pase = Verb[:-2]
                if pronom == "Je":
                    self.result_label.text = pase + "ais"
                elif pronom == "Tu":
                    self.result_label.text = pase + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = pase + "ait"
                elif pronom == "Nous":
                    self.result_label.text = pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = pase + "aient"  
###############__Plus-que-parfait__############### 
            elif Time == Plus_que_rarfait:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text ="avais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "avais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "avait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "avions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aviez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "avient " + pasée
###############__Futur-Simple__############### 
            elif Time == F_S:
                pase = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = Verb + "ai"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "as"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "a"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ons"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "ez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb + "ont"
###############__Futur-Anteriur__############### 
            elif Time == F_A:
                pasée = Verb[:-2] + "é"
                if pronom == "Je":
                    self.result_label.text = "aurai " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "auras " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aura " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurons " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "aurez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auront " + pasée
                    
###############Subjonctif###############   
            elif Time == Subjonctif:
                if pronom == "Je":
                    self.result_label.text == "que je " + Pase + "e"
                elif pronom == "Tu":
                    self.result_label.text = "que tu " + pase + "es"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "que " + pronom + pase + "e"
                elif pronom == "Nous":
                    self.result_label.text = "que nous " + pase + "ions"
                elif pronom == "Vous":
                    self.result_label.text = "que vous " + pase + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "que " + pronom + pase + "ent"
###############Conditionnel-Present###############   
            elif Time == conditionnel_present:
                if pronom == "Je":
                    self.result_label.text == Verb + "ais"
                elif pronom == "Tu":
                    self.result_label.text = Verb + "ais"
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = Verb + "ait"
                elif pronom == "Nous":
                    self.result_label.text = Verb + "ions"
                elif pronom == "Vous":
                    self.result_label.text = Verb + "iez"
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = Verb +"aient"
###############Conditionnel-Passe###############   
            elif Time == conditionnel_passe:
                pasée = Verb[:-2] +"é"
                if pronom == "Je":
                    self.result_label.text = "aurais " + pasée
                elif pronom == "Tu":
                    self.result_label.text = "aurais " + pasée
                elif pronom in ["Il","Elle","On"]:
                    self.result_label.text = "aurait " + pasée
                elif pronom == "Nous":
                    self.result_label.text = "aurions " + pasée
                elif pronom == "Vous":
                    self.result_label.text = "auriez " + pasée
                elif pronom in ["Ils","Elles"]:
                    self.result_label.text = "auraient " + pasée                
###############__end of rules __###############                
class JupiterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MainAppScreen(name='main'))
        Clock.schedule_once(self.change_screen,3)
        return sm
    def change_screen(self, dt):
        self.root.current = 'main'
if __name__ == '__main__':
    JupiterApp().run()