import tkinter as tk
import turtle as turtle
import gui as guifile
#JOSUE HERNANDEZ


class Window(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()



    def init_window(self):
        self.master.title("GUI")
        words = tk.Label(self.master, text="choose number of elements up to 54\npress confirm a second time to exit")
        words.grid(row=0, column=0)
        self.word_box = tk.Entry(self.master)
        self.word_box.grid(row=1,column=0)
        confirm = tk.Button(self.master, text='confirm',command=self.callback)
        confirm.grid(row=2,column=0)


    def callback(self):
        global size_n
        try:
            size_n = int(self.word_box.get())
            if size_n >54 or size_n < 0:
                print("only input numbers between 0 and 54!")
                exit()
        except:
            print("input only numerical values!")
            exit()
        self.quit()




def get_n(number):
    """Gets the Nth most occuring elements and returns them in a list with tuples"""
    result = []
    sorted_library = sorted(library.items(), key=lambda x: x[1],reverse=True)
    for counter,object in enumerate(sorted_library,1):
        #we will never go beyond length of dictionary
        if(counter==number):
            result.append(object)
            break
        else:
            result.append(object)
    return result



def import_file():
    with open("Words.txt","r") as file:
        global file_string
        file_string=file.read()
    for i in file_string:
        if (ord(i)>= 65 and ord(i)<=90) or (ord(i)>= 97 and ord(i)<=122) or ord(i)==32 or ord(i)==10 or ord(i)==9:
            if i in library:
                library[i]+=1
            else:
                library[i]=1
        else:
           library['symbol']+=1

    return

def make_global():
    if not file_string:
        import_file()
    return len(file_string)


# def foo(lamb):
#     #i exist solely to explain key=lambda x:x[1] to test replace with key=foo
#     print("i am x",end=" => ")
#     print(lamb)
#     return lamb[0]


def main():
    root = tk.Tk()
    root.geometry("300x200")
    app = Window(root)
    root.mainloop()


    result = get_n(size_n)

    #result is a list of tuples containing the top most nth elements

    guifile.bake_pie(result)



#GLOBALS
file_string=""
library = {'symbol':0}
LENGTH = make_global()
size_n=None


if __name__=='__main__':
    main()