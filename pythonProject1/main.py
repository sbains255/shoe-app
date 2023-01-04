from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from database import DataBase
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout




class MainWindow(Screen):
    pass

class SecondWindow(Screen):
#second window is login page was an error which does not allow me to change
    email = ObjectProperty(None)
    password = ObjectProperty(None)

#fourthbtn is the submit button on the page which would not allow me to change the name
    def fourthBtn(self):
        if db.validate(self.email.text, self.password.text):
            FourthWindow.current = self.email.text
            self.reset()
            sm.current = "customerdash"

        else:
            invalidLogin()

#thirdbtn is the button which customer click if they do not have an account which will redirect them to regist page
    def thirdBtn(self):
        self.reset()
        sm.current = "third"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    pass


class ThirdWindow(Screen):
#third window is the register page it would not let me change the name of this screen
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    firstlineaddy = ObjectProperty(None)
    seclineaddy = ObjectProperty(None)
    postcode = ObjectProperty(None)
    country = ObjectProperty(None)
    city = ObjectProperty(None)


    def submit(self):
        if self.firstname.text != "" and self.lastname.text != "" and self.email.text.count("@") == 1 and self.country.text != "" and self.city.text != "":
            if self.password.text != "":
                db.add_user(self.email.text, self.password.text, self.firstname.text, self.lastname.text)

                self.reset()

                sm.current = "second"



        #this will change to the login page which the code above represents#

            else:
                invalidForm()
        else:
            invalidForm()

    def second(self):
        self.reset()
        sm.current = "second"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.firstname.text = ""
        self.lastname.text = ""
        self.firstlineaddy.text = ""
        self.seclineaddy.text = ""
        self.postcode.text = ""
        self.country.text = ""
        self.city.text = ""
    pass

class FourthWindow(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)




    def submit(self):
        if self.email.text == str("dr1pplugz@outlook.com") and self.password.text == str("Seller123"):
            sm.current = "dashboard"
    pass

class SellerDashWindow(Screen):
    pass

class SellerListProductWindow(Screen):
    pass

class SellerEditDeleteProductWindow(Screen):
    pass

class SellingDataWindow(Screen):
    pass

class CustomerDashWindow(Screen):

    shoesize = ObjectProperty(None)

    def submit(self):
        if self.shoesize != int(3-15):
            db1.add_usersize(self.shoesize.text)

    pass

class CustomerHomeWindow(Screen):
    pass

class Jordan4Window(Screen):
    total = "0"
    pass

class Jordan1Window(Screen):
    pass

class NikeDunkLowWindow(Screen):
    pass

class AirForce1Window(Screen):
    pass

class NewBalance550Window(Screen):
    pass

class YeezyWindow(Screen):
    pass

class CartWindow(Screen):
    total = "0"
    pass

class Jordan4MidnightNavyWindow(Screen):
    pass

class Jordan4BlackCanvasWindow(Screen):
    pass

class Jordan4MilitaryBlackWindow(Screen):
    order_window = StringProperty()
    price_window = StringProperty()

    def add_to_cart(self, item, price):
        self.order.append((self.table, item, price))
        self.order_window += f'{item} {price}\n\n'
        self.total += price
        self.CartWindow = str(self.total)


    def checkout(self):
        pop = Popup(title='Checkout',
            content=Label(text='Please fill in all inputs with valid information.'),
            size_hint=(None, None), size=(400, 400))
        pop.open()

    pass

class WindowManager(ScreenManager):
    pass



def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
            content=Label(text='Please fill in all inputs with valid information.'),
            size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [MainWindow(name="main"), SecondWindow(name="second"), ThirdWindow(name="third"), FourthWindow(name="fourth"), SellerDashWindow(name="dashboard"), SellerListProductWindow(name="listing"), SellerEditDeleteProductWindow(name="edit"), SellingDataWindow(name="selldata"), CustomerDashWindow(name="customerdash"), CustomerHomeWindow(name="customerhome"), Jordan4Window(name="jordan4"), Jordan1Window(name="jordan1"), NikeDunkLowWindow(name="nikedunklow"), AirForce1Window(name="airforce1"), NewBalance550Window(name="newbalance550"), YeezyWindow(name="yeezy"), CartWindow(name="cart"), Jordan4MidnightNavyWindow(name="jordan4midnightnavy"), Jordan4BlackCanvasWindow(name="jordan4blackcanvas"), Jordan4MilitaryBlackWindow(name="jordan4militaryblack")]
for screen in screens:
    sm.add_widget(screen)

im = Image(source='logo.jpg')

class FullImage(Image):
    pass

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ =="__main__":
    MyMainApp().run()

