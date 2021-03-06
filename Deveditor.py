import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
application = tk.Tk()
application.geometry('1200x800')
application.title('Dev-editor')
###################################################   MAIN MENU ##############################################
main_menu = tk.Menu(application)

new_icon=tk.PhotoImage(file='deveditor icons/new.png')
open_icon=tk.PhotoImage(file='deveditor icons/open.png')
save_icon=tk.PhotoImage(file='deveditor icons/save.png')
saveas_icon=tk.PhotoImage(file='deveditor icons/save_as.png')
exit_icon=tk.PhotoImage(file='deveditor icons/exit.png')
file = tk.Menu(main_menu,tearoff=0)
#cascading
main_menu.add_cascade(label='File',menu=file)

cut_icon=tk.PhotoImage(file='deveditor icons/cut.png')
copy_icon=tk.PhotoImage(file='deveditor icons/copy.png')
paste_icon=tk.PhotoImage(file='deveditor icons/paste.png')
clearall_icon=tk.PhotoImage(file='deveditor icons/clear_all.png')
find_icon=tk.PhotoImage(file='deveditor icons/find.png')
edit = tk.Menu(main_menu, tearoff=0)
#cascading-edit
main_menu.add_cascade(label='Edit',menu=edit)

view = tk.Menu(main_menu, tearoff=0)
tool_icon = tk.PhotoImage(file='deveditor icons/tool_bar.png')
status_icon = tk.PhotoImage(file='deveditor icons/status_bar.png')
#cascading-view
main_menu.add_cascade(label='View',menu=view)

light_default_icon = tk.PhotoImage(file='deveditor icons/light_plus.png')
light_plus_icon = tk.PhotoImage(file='deveditor icons/light_plus.png')
dark_icon = tk.PhotoImage(file='deveditor icons/dark.png')
night_blue_icon = tk.PhotoImage(file='deveditor icons/night_blue.png')
# monokai_icon = tk.PhotoImage(file='deveditor icons/monokai.png')
red_icon = tk.PhotoImage(file='deveditor icons/red.png')
color_theme = tk.Menu(main_menu, tearoff=0)

# color_theme.add_radiobutton(label='Light-Default',image=light_default_icon,compound=tk.LEFT)
# color_theme.add_radiobutton(label='Light-plus',image=light_plus_icon,compound=tk.LEFT)
# color_theme.add_radiobutton(label='Dark',image=dark_icon,compound=tk.LEFT)
# color_theme.add_radiobutton(label='Night-Blue',image=night_blue_icon,compound=tk.LEFT)
# color_theme.add_radiobutton(label='Monokai',image=monokai_icon,compound=tk.LEFT)
# color_theme.add_radiobutton(label='Red',image=red_icon,compound=tk.LEFT)

theme_choice = tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,night_blue_icon,red_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Night Blue':('#ededed','#6b9dc2'),
    # 'Monokai':('#2d2d2d','#ffe8e8'),
    'Red':('#2d2d2d','#ffe8e8')
}
#cascading-color_theme
main_menu.add_cascade(label='Color Theme',menu=color_theme)
###################################################   END MAIN MENU

###################################################   TOOLBAR
tool_bar=ttk.Label(application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=25,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size-box
size_var=tk.StringVar()
font_size=ttk.Combobox(tool_bar,width=10,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(2,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#bold-button
bold_icon=tk.PhotoImage(file='deveditor icons/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
italic_icon=tk.PhotoImage(file='deveditor icons/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
underline_icon=tk.PhotoImage(file='deveditor icons/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

font_color_icon=tk.PhotoImage(file='deveditor icons/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=6,padx=5)

align_left_icon=tk.PhotoImage(file='deveditor icons/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=7,padx=5)

align_center_icon=tk.PhotoImage(file='deveditor icons/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=8,padx=5)

align_right_icon=tk.PhotoImage(file='deveditor icons/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=9,padx=5)
###################################################   END TOOLBAR ##############################################

###################################################   TEXT EDIOTR ##############################################
text_editor=tk.Text(application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll = tk.Scrollbar(application)
text_editor.focus_set()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll.set)

#FUNCTIONALITY OF TEXT EDITOR
current_font_family = 'Arial'
current_font_size=12

def change_font(application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))
font_box.bind("<<ComboboxSelected>>",change_font)

def change_font_size(application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.config(font=(current_font_size,current_font_size))
font_size.bind("<<ComboboxSelected>>",change_font_size)


#Buttons _functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.config(font=(current_font_family,current_font_size,'normal'))
bold_btn.config(command=change_bold)

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['weight']=='italic':
        text_editor.config(font=(current_font_family,current_font_size,'roman'))
italic_btn.config(command=change_italic)

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))
underline_btn.config(command=change_underline)


def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1])

font_color_btn.config(command=change_font_color)


#ALIGN-FUNCTIONALITY
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.config(command=align_left)

def align_center():
    text_content = text_editor.get(1.0,tk.END)
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.config(command=align_center)


def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.config(command=align_right)


###################################################   END TEXT EDITOR ##############################################

###################################################   MAIN STATUS BAR ##############################################
status_bar = ttk.Label(application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_change = False
def status(event = None):
    if text_editor.edit_modified():
        global text_change
        text_change=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f"characters:{characters} words :{words}")
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',status)

##################################################   END STATUS BAR ##############################################

###################################################   MAIN FUNCTIONALITY ##############################################
#variable
url=''


def new(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new)

def open_file(event =None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title='SELECT A FILE',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(tk.INSERT,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    application.title(os.path.basename(url))

file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command = open_file)

def save_file(event = None):
    global url
    try:
        if url:
            content=text_editor.get(1.0,tk.END)
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)

def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='ctrl+shift+S',command = save_as)

def exit_func(event = None):
        global url,text_change
        try:
            if text_change:
                mbox = messagebox.askyesnocancel('Warning',"Devender do u want to save it or not?")
                if mbox is True:
                    content = text_editor.get(1.0,tk.END)
                    if url:
                        content=text_editor.get(1.0,tk.END)
                        with open(url ,'w',encoding='utf-8') as fw:
                            fw.write(content)
                            application.destroy()
                    else:
                        content2 = str(text_editor.get(1.0,tk.END))
                        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
                        url.write(content2)
                        url.close()
                        application.destroy()
                elif mbox is False:
                    application.destroy()
            else:
                application.destroy()
        except:
            return


file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Alt+F4',command=exit_func)

edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command =lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command =lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+Y',command =lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Clear All',image=clearall_icon,compound=tk.LEFT,command =lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT)


view.add_checkbutton(label='ToolBar',image=tool_icon,compound=tk.LEFT)
view.add_checkbutton(label='StatusBar',image=status_icon,compound=tk.LEFT)



def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound = tk.LEFT,command=change_theme)
    count+=1

#bind keys
application.bind("<Control-n>",new)
application.bind("<Control-o>",open_file)
application.bind("<Control-s>",save_file)
application.bind("<Control-Shift-s>",save_as)
application.bind("<Alt-F4>",exit_func)


###################################################   END MAIN FUNCTIONALITY ##############################################
application.config(menu = main_menu)
print("THE APPLICATION IS OPEN NOW")
application.mainloop()