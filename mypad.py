import webbrowser as wb
import datetime
import time
from googletrans.models import Translated
import pyttsx3
from gtts import gTTS
from playsound import  playsound
import tkinter as tk
from tkinter import *
from google_trans_new import google_translator
from tkinter import ttk
import speech_recognition as sr
from englisttohindi.englisttohindi import EngtoHindi
from tkinter.filedialog import *
import pyaudio
import os
import re
from tkinter import font , colorchooser, filedialog, messagebox
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
flopn=None
a=0
b=0
translator = google_translator() 
def speak(audio):
    engine.setProperty("rate", 150)
    engine.say(audio)
    engine.runAndWait()

def opn(event=""):
    try:
        fl=askopenfilename(defaultextension=".txt",title="Select file to open", 
                                    filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
        if(fl!=None):                                 
            top.title(os.path.basename(fl)) 
            mytext.delete(1.0,END) 
            file = open(fl,"r") 
            mytext.insert(1.0,file.read())  
            global flopn
            flopn=fl
            global a
            a=0
            file.close()
    except:
        tk.messagebox.showinfo('Open file', 'No file is selected')    
def new(event=""):
    top.title('Untitled-MyPad')
    mytext.delete(1.0,END)
    global flopn
    flopn=None
def SaveAs(event=""):
    fl =asksaveasfile(mode="w",defaultextension=".txt")
    if(fl!=None):
        fl.write((mytext.get(1.0,END)))
        global flopn
        flopn=fl  
        global a
        a=1
        top.title((fl.name).split('/')[-1]+" MyPad")
        fl.close()
def save(event=""):
    if flopn==None:
        SaveAs()
    else:
        print(flopn)
        if(a==1):
            fl=open(flopn.name,mode="w")
        else:
            fl=open(flopn,mode="w")        
        fl.write((mytext.get(1.0,END)))
        fl.close()    
def qvt(event=""):
    top.quit()        
def stop():
        global b
        b=1
        print('bye')
        return
def select(event=""):
    mytext.tag_add('sel', '1.0', 'end')
def color(event=""):
    back=colorchooser.askcolor()
    fore=colorchooser.askcolor()
    mytext.config(bg=back[1],fg=fore[1],insertbackground="white")
def cut(event=""):
    mytext.event_generate('<<Cut>>')
def copy(event=""):
    mytext.event_generate("<<Copy>>") 
def paste(event=""):
    mytext.event_generate("<<Paste>>")      
def delete(event=""):
    if(flopn!=None):
        if(a==1):
            os.remove(flopn.name)
        else:
            os.remove(flopn)    
        tk.messagebox.showinfo('Removed!', 'Successfully Removed!')
        mytext.delete(1.0,END)
        new()
    else:
        tk.messagebox.showerror('Error!', 'File not found!')

def start():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            print('got it')    
            try:    
                txt=r.recognize_google(audio,language='eng-in')
                print(txt)
                if(not(re.search("^iPad.*$", txt))):
                    mytext.insert(END,txt)
                globals()['b']=0    
                if('iPad stop' in txt or'iPad.' in txt or 'I better stop' in txt ):   
                    print("i am inside stop") 
                    stop()    
                elif 'iPad open' in txt:
                    opn()       
                elif 'iPad delete' in txt:
                    delete()
                elif 'iPad save'in txt or 'iPad sale' in txt:
                    print('i am inside save')
                    save()
                elif 'iPad new file' in txt:
                    new()
                elif 'iPad cut' in txt:
                    cut()
                elif 'iPad paste' in txt:
                    mytext.event_generate("<<Paste>>")
                elif 'iPad color' in txt:
                    color()
                elif 'iPad clear' in txt:
                    mytext.delete(1.0,END)                    
            except Exception as e:
                print(e)
                globals()['b']=1
                print("Unable to Recognize your voice.")
                print('PLZ START OVER AGAIN')
            
            if((globals()['b'])==0):
                print('say sir')
                start() 
            else:
                print('i am inside else')
                stop()
def info():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            print('got it')    
            try:    
                txt=r.recognize_google(audio,language='eng-in')
                print(txt)
                globals()['b']=0    
                if'play song'in txt or 'song'in txt:
                    url = 'https://www.youtube.com/results?search_query='+txt
                    try:
                        wb.get().open_new(url)
                        print("Done")
                    except sr.UnknownValueError:
                        print('error')
                    except sr.RequestError as e:
                        print ('failed'.format(e)) 
                elif'open Google'in txt:
                    url = 'https://www.google.com/'
                    try:
                        wb.get().open_new(url)
                        print("Done")
                    except sr.UnknownValueError:
                        print('error')
                    except sr.RequestError as e:
                        print ('failed'.format(e))
                elif'open Wikipedia'in txt:
                    url = 'https://www.wikipedia.org/'
                    try:
                        wb.get().open_new(url)
                        print("Done")
                    except sr.UnknownValueError:
                        print('error')
                    except sr.RequestError as e:
                        print ('failed'.format(e))
                elif'YouTube'in txt:
                    url = 'https://www.youtube.com/'
                    try:
                        wb.get().open_new(url)
                        print("Done")
                    except sr.UnknownValueError:
                        print('error')
                    except sr.RequestError as e:
                        print ('failed'.format(e))
                elif 'time' in txt:
                    strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%I%p")
                    speak(f"Sir, the time is {strTime}")                                    
            except Exception as e:
                print(e)
                globals()['b']=1
                print("Unable to Recognize your voice.")
                print('PLZ START OVER AGAIN')

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir MAAM!")
            
	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir MAAM!")

	else:
		speak("Good Evening Sir MAAM!")

	speak("I am your Assistant My Pad this is an extended version of note pad providing new feature as first the speech to text second is the text to speech feature for having an idea of what you have noted followed by the speech command features which will edit save clear change color in respone of our speech command thank you")
def T2S():
    speak(mytext.get(1.0,END))
def convert():
    try:
        texttoconvert=mytext.get(1.0,END)
        res = EngtoHindi(str(texttoconvert))
        translate_text = translator.translate(texttoconvert, lang_src='en', lang_tgt='hi')
        print(res.convert)
        print(translate_text)
        language='hi'
        myobj=gTTS(text=translate_text,lang=language,slow=False)
        myobj.save("welcome1.mp3")
        playsound("welcome1.mp3")
        os.remove("welcome1.mp3")
    except Exception as e:
        print(f'Oh No Error {e}')    
top=Tk()
tool_bar = ttk.Label(top)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box=ttk.Combobox(tool_bar, width=30 ,textvariable=font_family,state='readonly' )
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var = tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable = size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


#bold buttonS
bold_icon = tk.PhotoImage(file='bold.png')
bold_btn  =ttk.Button(tool_bar ,image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)


#italic button
italic_icon = tk.PhotoImage(file='italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0, column=3,padx=5)


#underline button
underline_icon = tk.PhotoImage(file='underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0, column=4,padx=5)


#font color button
font_icon = tk.PhotoImage(file='font_color.png')
font_color_btn = ttk.Button(tool_bar,image=font_icon)
font_color_btn.grid(row=0, column=5,padx=5)

# align_left
align_left_icon = tk.PhotoImage(file='align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

#align center
align_center_icon = tk.PhotoImage(file='align_center.png')
align_center_btn= ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

#align right
align_right_icon = tk.PhotoImage(file='align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

myFont = font.Font(family='Times New Roman', size=17)
h = Scrollbar(top, orient = 'horizontal')
h.pack(side = BOTTOM, fill = X)
v = Scrollbar(top)
v.pack(side = RIGHT, fill = Y)
mytext=Text(top,width=400,height=400,undo=True,xscrollcommand = h.set,yscrollcommand = v.set,wrap=NONE)
mytext.pack(side=TOP, fill=X)
h.config(command=mytext.xview)
v.config(command=mytext.yview)
menubar=Menu(top)
#file menu
file = Menu(menubar, tearoff=0)  
file.add_command(label="New",command=new,accelerator="Ctrl-N") 
top.bind('<Control-n>',new) 
file.add_command(label="Open",command=opn,accelerator="Ctrl-O")
top.bind('<Control-o>',opn)  
file.add_command(label="Save",command=save,accelerator="Ctrl-S")
top.bind('<Control-s>',save)  
file.add_command(label="Save as",command=SaveAs,accelerator="Ctrl-B")
top.bind('<Control-b>',SaveAs)    
file.add_separator()  
file.add_command(label="Exit", command=qvt,accelerator='Ctrl-Q')
top.bind('<Control-q>',qvt)  
menubar.add_cascade(label="File", menu=file)
#edit menu  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo",command=mytext.edit_undo,accelerator="Ctrl-Z")
edit.add_command(label="Redo",command=mytext.edit_redo,accelerator="Ctrl-Y")  
edit.add_separator()  
edit.add_command(label="Cut",command=cut,accelerator="Ctrl-X")
top.bind('<Control-x>',cut)  
edit.add_command(label="Copy",command=copy,accelerator="Ctrl-C")
top.bind('<Control-c>',copy)  
edit.add_command(label="Paste",command=paste,accelerator="Ctrl-V")
top.bind('<Control-v>',paste)  
edit.add_command(label="Delete",command=delete,accelerator="Ctrl-E")
top.bind('<Control-e>',delete) 
edit.add_command(label="Select All",command=select,accelerator='Ctrl-A')
top.bind('<Control-a>',select)
edit.add_command(label="Custom color",command=color,accelerator="Ctrl-D")
top.bind('<Control-d>',color)
menubar.add_cascade(label="Edit", menu=edit)
#S2T menu
Speech_To_Text=Menu(menubar,tearoff=0)
Speech_To_Text.add_command(label="Start",command=start)
Speech_To_Text.add_command(label="Stop",command=stop)

menubar.add_cascade(label="Speech_To_Text",menu=Speech_To_Text)
#T2S menu
Text_To_Speech=Menu(menubar,tearoff=0)
Text_To_Speech.add_command(label="Start",command=T2S)
menubar.add_cascade(label="Text_To_Speech",menu=Text_To_Speech)
#information available
information_available=Menu(menubar,tearoff=0)
information_available.add_command(label="Start",command=info)
menubar.add_cascade(label="information_available",menu=information_available)

#help menu  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About",command=wishMe)
help.add_command(label="Translate",command=convert)  
menubar.add_cascade(label="Help", menu=help)  
top.config(menu=menubar)  
#top.attributes('-fullscreen',False)
top.geometry('1000x500+0+0')


current_font_family= 'Arial'
current_font_size= 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    mytext.config(font=(current_font_family,current_font_size))


def change_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    mytext.config(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)


def change_bold():
    try:
        text_property=tk.font.Font(font=mytext['font'])
        text_property.configure(weight="bold")
        mytext.tag_configure("bold",font=text_property)
        current_tag=mytext.tag_names('sel.first')
        if "bold" in current_tag:
            mytext.tag_remove("bold","sel.first","sel.last")
        else:
            mytext.tag_add("bold","sel.first","sel.last")
    except Exception as e:
        print(f'Oh No Error {e}')
bold_btn.configure(command=change_bold)


#italic button functionality

def change_italic():
    try:
        text_property=tk.font.Font(font=mytext['font'])
        text_property.configure(slant="italic")
        mytext.tag_configure("italic",font=text_property)
        current_tag=mytext.tag_names('sel.first')
        if "italic" in current_tag:
            mytext.tag_remove("italic","sel.first","sel.last")
        else:
            mytext.tag_add("italic","sel.first","sel.last")
    except Exception as e:
        print(f'Oh NO Error {e}')
italic_btn.configure(command=change_italic)


#underline button functionality
def underline():
    try:
        text_property=tk.font.Font(font=mytext['font'])
        text_property.configure(underline=True)
        mytext.tag_configure(True,font=text_property)
        current_tag=mytext.tag_names('sel.first')
        if True in current_tag:
            mytext.tag_remove(True,"sel.first","sel.last")
        else:
            mytext.tag_add(True,"sel.first","sel.last")
    except Exception as e:
        print(f'Oh no Error {e}')

underline_btn.configure(command=underline)


#font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    mytext.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)


# align functionality 


def align_left():
    text_content = mytext.get(1.0, 'end')
    mytext.tag_config('left',justify=tk.LEFT)
    mytext.delete(1.0,tk.END)
    mytext.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

#align center

def align_center():
    text_content = mytext.get(1.0, 'end')
    mytext.tag_config('center',justify=tk.CENTER)
    mytext.delete(1.0,tk.END)
    mytext.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)
#align right

def align_right():
    text_content = mytext.get(1.0, 'end')
    mytext.tag_config('right',justify=tk.RIGHT)
    mytext.delete(1.0,tk.END)
    mytext.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

top.mainloop()