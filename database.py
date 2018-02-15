from kivy.app import App
from kivy.uix.widget import Widget
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import cgi
import pymysql
 
#form=cgi.FieldStorage()


class LoginWindow(Widget):
    def login(self, *args):
        username = self.ids.username_input
        username_text = username.text
        
        password = self.ids.password_input
        password_text =password.text
        
        #return username_text
        #return password_text
        print(username_text)
        print(password_text)
                
        
        #data1=LoginWindow()   
            
        conn=pymysql.connect(host='localhost',user='root',password='',db='py_db')
        a=conn.cursor()
        print('database connected')
        
        
            
            #sql=("select * from py_tbl;")
        sql="INSERT INTO student  VALUES(?,?)"
        #sql="DELETE FROM student WHERE username='' "
        #sql=("select * from student")
        a.execute(sql)
        
        #a.execute("""INSERT INTO student ( username, password) VALUES ( %s, %s)"""% (username, password))    
            
            

            

            
            
        #label = self.ids.success
        #label.text = "Success"
        conn.commit()
           
        #data=a.fetchall()
        #print(data)
            
            
            #print(data)

class LatihanApp(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    LatihanApp().run()