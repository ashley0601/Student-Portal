from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from Location import region, province_select, municipality_select, brgy_select
from PIL import Image, ImageTk
import os 
import json
import re
from datetime import date

class Homepage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Homepage')

        bg_image_path = 'img\\home.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
            self.bg_image = self.bg_image.resize((1166, 718))  # Resize the image to fit the window
        else:
            print(f"Error: {bg_image_path} not found.")
            return

        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill=BOTH, expand=True)
        
        self.Home_button = Button(self.window, text="Homepage",
                                             font=("yu gothic ui", 13, "bold"), fg="#000000", relief=FLAT,
                                             activebackground="#ebe9e9", borderwidth=0, background="#ebe9e9",
                                             cursor="hand2")
        self.Home_button.place(x=320, y=35)
        
        self.About_button = Button(self.window, text="About Us",
                                             font=("yu gothic ui", 13), fg="#000000", relief=FLAT,
                                             activebackground="#ebe9e9", borderwidth=0, background="#ebe9e9",
                                             cursor="hand2",command=self.open_about_window)
        self.About_button.place(x=470, y=35)
        
        self.Feedback_button = Button(self.window, text="Feedback",
                                             font=("yu gothic ui", 13), fg="#000000", relief=FLAT,
                                             activebackground="#ebe9e9", borderwidth=0, background="#ebe9e9",
                                             cursor="hand2",command=self.open_feedback_window)
        self.Feedback_button.place(x=620, y=35)
        
        self.contact_button = Button(self.window, text="Contacts",
                                             font=("yu gothic ui", 13), fg="#000000", relief=FLAT,
                                             activebackground="#ebe9e9", borderwidth=0, background="#ebe9e9",
                                             cursor="hand2", command=self.open_contacts_window)
        self.contact_button.place(x=770, y=35)
        
        self.student_button = Button(self.window, text="STUDENT",
                                             font=("yu gothic ui", 18, "bold"), fg="#8370de", relief=FLAT,
                                             activebackground="#ffffff", borderwidth=0, background="#ffffff",
                                             cursor="hand2", command=self.open_student_window)
        self.student_button.place(x=130, y=582)
        
        self.acc_button = Button(self.window, text="ACCOUNT",
                                             font=("yu gothic ui", 17, "bold"), fg="#8370de", relief=FLAT,
                                             activebackground="#ffffff", borderwidth=0, background="#ffffff",
                                             cursor="hand2", command=self.open_acc_window)
        self.acc_button.place(x=377, y=584)
        
    def open_student_window(self):
        self.window.withdraw()
        student_window = Toplevel(self.window)
        Student(student_window)
    
    def open_contacts_window(self):
        self.window.withdraw()
        Contacts_window = Toplevel(self.window)
        Contacts(Contacts_window)
            
    def open_about_window(self):
        self.window.withdraw()
        about_window = Toplevel(self.window)
        About_Us(about_window)
            
    def open_feedback_window(self):
        self.window.withdraw()
        feed_window = Toplevel(self.window)
        Feedback(feed_window)
        
    def open_acc_window(self):
        self.window.withdraw()
        acc_window = Toplevel(self.window)
        Account(acc_window)
        
class About_Us:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('DLL')
        
        bg_image_path = 'img\\about.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
        else:
            print(f"Error: {bg_image_path} not found.")
            return
        
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes')
        
        back_home = Button(self.window, text="Back to Homepage",font=("Consolas", 12, 'bold'), bg="#cf86fc", fg="black", command=lambda:self.back_home())
        back_home.place(x=950, y=658)

    def back_home(self):
        self.window.withdraw()
        about_window = Toplevel(self.window)
        Homepage(about_window)
        
class Feedback:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Student Portal')
        self.window.configure(bg='#8c6add')
        
        Feedback = Label(self.window, text= "FEEDBACK", font=("Consolas", 42, 'bold'), bg="#8c6add",fg="white")
        Feedback.place(x=50, y=50)
        
        feed_label = Label(self.window, text="Write your suggestions or comments below!!", font=("Consolas", 16, 'bold'), bg="#8c6add",fg="black")
        feed_label.place(x=180, y=190)
        feed_entry = Text(self.window, width="100", height=10)
        feed_entry.place(x=180, y=230)
        
        submit_feed = Button(self.window, text="SUBMIT",font=("Consolas", 16, 'bold'), bg="#cf86fc", fg="black", command=lambda:save_feed())
        submit_feed.place(x=500, y=420)
        
        back_home = Button(self.window, text="Back to Homepage",font=("Consolas", 12, 'bold'), bg="#cf86fc", fg="black", command=lambda:self.backhome())
        back_home.place(x=970, y=618)
        
        def save_feed():
            messagebox.showinfo("FEEDBACK", "Thank you for your feedback!")

    def backhome(self):
        self.window.withdraw()
        feed_window = Toplevel(self.window)
        Homepage(feed_window)

        
class Contacts:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Student Portal')
        
        bg_image_path = 'img\\contacts.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
        else:
            print(f"Error: {bg_image_path} not found.")
            return
            
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes') 
        
        back_home = Button(self.window, text="Back to Homepage",font=("Consolas", 12, 'bold'), bg="#cf86fc", fg="black", command=lambda:self.back_home())
        back_home.place(x=970, y=618)
    
    def back_home(self):
        self.window.withdraw()
        contact_window = Toplevel(self.window)
        Homepage(contact_window)
        
        
class Student:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Student Form')
        tab_control = ttk.Notebook(window)
    
        image_path = "img\\admission.png"
        self.image = Image.open(image_path)
        self.bg_image = ImageTk.PhotoImage(self.image.resize((1166, 718)))

        tab1 = Frame(tab_control)
        tab2 = Frame(tab_control)
        tab3 = Frame(tab_control)
    
        tab_control.add(tab1, text='STUDENT FORM')
        tab_control.add(tab2, text='PERSONAL INFORMATION')
        tab_control.add(tab3, text="ADMISSION")
        tab_control.pack(expand=1, fill="both")
        
        self.canvas1 = Canvas(tab3, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        tab1.configure(bg="#b1a8eb")
        tab2.configure(bg="#b1a8eb")
        
        Tab1Frame = Frame(tab1, bd=2, relief=SOLID, width=1030, height=600)
        Tab1Frame.place(x=65, y=40)

        Tab2Frame = Frame(tab2, bd=2, relief=SOLID, width=1020, height=450)
        Tab2Frame.place(x=70, y=90)
        Tab2Frame.pack_propagate(False)
                
        Tab3Frame = Frame(tab2, bd=2, relief=SOLID, width=1020, height=90)
        Tab3Frame.place(x=70, y=570)

        def search_callback(event=None):
            search_term = search_entry.get()
            update_treeview(search_term) 

        SearchContainer = Frame(tab2, bd=2, relief=SOLID, width=1020, height=70)
        SearchContainer.pack_propagate(False)
        SearchContainer.place(x=70, y=10)

        search_entry = Entry(SearchContainer, width=90, font=("Consolas", 13))
        search_entry.pack(side=LEFT, padx=15)
        search_entry.bind("<KeyRelease>", search_callback)

        #Search Button
        search_button = Button(SearchContainer, width=10, height=3, bg="#cf86fc", fg="White", text="SEARCH")
        search_button.place(x=850, y=7)
                

        personal = Label(Tab1Frame, text= "STUDENT INFORMATION", font=("Consolas", 18, 'bold'))
        personal.place(x=300, y=20)

        stud_ID = Label(Tab1Frame, text="STUDENT ID", font=("Consolas", 9))
        stud_ID.place(x=330, y=60)

        stud_ID_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        stud_ID_entry.place(x=350, y=90)

        stud_Name = Label(Tab1Frame, text="FULL NAME", font=("Consolas", 9))
        stud_Name.place(x=330, y=130)

        stud_Name_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        stud_Name_entry.place(x=350, y=160)

        stud_DOB = Label(Tab1Frame, text="BIRTH DATE", font=("Consolas", 9))
        stud_DOB.place(x=650, y=50)

        stud_DOB_entry = DateEntry(Tab1Frame, width=20, font=("Consolas", 13))
        stud_DOB_entry.set_date(date.today())  # Set to today's date initially
        stud_DOB_entry.place(x=680, y=90)

        stud_SEX = Label(Tab1Frame, text="SEX", font=("Consolas", 9))
        stud_SEX.place(x=650, y=130)

        SexVar = StringVar()
        MaleBtn = Radiobutton(Tab1Frame, text="MALE", font=("Consolas", 10), variable=SexVar, value="Male")
        MaleBtn.place(x=680, y=160)
        FemaleBtn = Radiobutton(Tab1Frame, text="FEMALE", font=("Consolas", 10), variable=SexVar, value="Female")
        FemaleBtn.place(x=780, y=160)

        def validate_email(email):
            pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            return re.match(pattern, email)

        stud_Email = Label(Tab1Frame, text="EMAIL", font=("Consolas", 9))
        stud_Email.place(x=330, y=210)

        stud_Email_entry = Entry(Tab1Frame, width=30, font=("Consolas", 12))
        stud_Email_entry.place(x=350, y=240)

        def validate_numeric(input):
            if input.isdigit() or input == "":
                return True
            else:
                messagebox.showerror("Error", "Please enter only numeric values")
                return False

        validate_numeric_format = Tab1Frame.register(validate_numeric)

        stud_CPNO = Label(Tab1Frame, text="CONTACT NUMBER", font=("Consolas", 9))
        stud_CPNO.place(x=650, y=210)

        stud_CPNO_entry = Entry(Tab1Frame, width=30, font=("Consolas", 12), validate="key", validatecommand=(validate_numeric_format, '%P'))
        stud_CPNO_entry.place(x=680, y=240)

        stud_ADDRESS = Label(Tab1Frame, text="ADDRESS", font=("Consolas", 9))
        stud_ADDRESS.place(x=10, y=290)

        region_lbl = Label(Tab1Frame, text="REGION", font=("Consolas", 12))
        region_lbl.place(x=10, y=320)

        regionCombo = ttk.Combobox(Tab1Frame, values=region,  font=("Consolas", 12))
        regionCombo.place(x=40,y=350)

        province = list()
        city = list()
        brgy = list()

        def region_selector(event):
            selected_region = regionCombo.get()
            province = province_select(selected_region)
            provinceCombo.configure(values=province)

        regionCombo.bind("<<ComboboxSelected>>", region_selector)

        def province_selector(event):
            selected_region = regionCombo.get()
            selected_province = provinceCombo.get()
            municipality = municipality_select(selected_region, selected_province)
            cityCombo.configure(values=municipality)

        province_lbl = Label(Tab1Frame, text="PROVINCE", font=("Consolas", 12))
        province_lbl.place(x=250, y=320)

        provinceCombo = ttk.Combobox(Tab1Frame, values=province, font=("Consolas", 12))
        provinceCombo.place(x=280, y=350)
        provinceCombo.bind("<<ComboboxSelected>>", province_selector)

        def city_selector(event):
            selected_region = regionCombo.get()
            selected_province = provinceCombo.get()
            selected_city = cityCombo.get()

            brgy = brgy_select(selected_region, selected_province, selected_city)
            brgyCombo.configure(values=brgy)

        city_lbl = Label(Tab1Frame, text="MUNICIPALITY", font=("Consolas", 12))
        city_lbl.place(x=490, y=320)

        cityCombo = ttk.Combobox(Tab1Frame, font=("Consolas", 12))
        cityCombo.place(x=520, y=350)
        cityCombo.bind("<<ComboboxSelected>>", city_selector)

        brgy_lbl = Label(Tab1Frame, text="BARANGAY", font=("Consolas", 12))
        brgy_lbl.place(x=730, y=320)

        brgyCombo = ttk.Combobox(Tab1Frame, font=("Consolas", 12))
        brgyCombo.place(x=760, y=350)

        family = Label(Tab1Frame, text= "FAMILY BACKGROUND", font=("Consolas", 14, 'bold'))
        family.place(x=20, y=390)

        mother = Label(Tab1Frame, text="Mother", font=("Consolas", 12))
        mother.place(x=120, y=420)
        mother_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        mother_entry.place(x=150, y=450)

        mother_occ = Label(Tab1Frame, text="Occupation", font=("Consolas", 12))
        mother_occ.place(x=480, y=420)
        mother_occ_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        mother_occ_entry.place(x=510, y=450)

        father = Label(Tab1Frame, text="Father", font=("Consolas", 12))
        father.place(x=120, y=480)
        father_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        father_entry.place(x=150, y=520)

        father_occ = Label(Tab1Frame, text="Occupation", font=("Consolas", 12))
        father_occ.place(x=480, y=480)
        father_occ_entry = Entry(Tab1Frame, width=30, font=("Consolas", 13))
        father_occ_entry.place(x=510, y=520)

        Submit = Button(Tab1Frame, text="SUBMIT", font=("Consolas", 12), bg ="#8370de",fg="#ffffff" ,command=lambda:save_data())
        Submit.place(x=850, y=480)

        def upload_picture():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if file_path:
                image = Image.open(file_path)
                image = image.resize((200, 200))
                photo = ImageTk.PhotoImage(image)
                picture_button.config(image=photo)
                picture_button.image = photo 
                
                # Save image path in JSON
                save_image_path(file_path)

        # Picture Button
        initial_image = Image.new('RGB', (200, 200), color='white')
        photo = ImageTk.PhotoImage(initial_image)

        # Frame for Picture Button
        picture_button = Button(Tab1Frame, image=photo, bg='white')
        picture_button.image = photo
        picture_button.place(x=50, y=20)

        # Insert Photo Button
        photo_button = Button(Tab1Frame, text="INSERT PHOTO", command=upload_picture, font=("Consolas", 9), bg ="#8370de",fg="#ffffff")
        photo_button.place(x=100, y=230)

        def save_image_path(image_path):
            stud_ID = stud_ID_entry.get()
            filename = "student_record.json"
            try:
                if os.path.exists(filename):
                    with open(filename,'r') as read_file:
                        student_info = json.load(read_file)
                else:
                    student_info = {"student_record":[]}
                
                for student in student_info["student_record"]:
                    if student["id"] == stud_ID:
                        student["image_path"] = image_path
                        break
                
                with open(filename, 'w') as update_file:
                    json.dump(student_info, update_file, indent=4)

                messagebox.showinfo("IMAGE", "IMAGE UPLOADED SUCCESSFULLY")
                
                # Update picture button with the new image
                image = Image.open(image_path)
                image = image.resize((200, 200))
                photo = ImageTk.PhotoImage(image)
                picture_button.config(image=photo)
                picture_button.image = photo 
                
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        def save_data():
            id = stud_ID_entry.get()
            name = stud_Name_entry.get()
            dob = stud_DOB_entry.get()
            sex = SexVar.get()
            email = stud_Email_entry.get()
            cpno = stud_CPNO_entry.get()
            region = regionCombo.get()
            province = provinceCombo.get()
            city = cityCombo.get()
            brgy = brgyCombo.get()
            mother = mother_entry.get()
            mother_occ = mother_occ_entry.get()
            father = father_entry.get()
            father_occ = father_occ_entry.get()
 

            if not validate_email(email):
                messagebox.showerror("Error", "Invalid email format")
                return

            if not id or not name or not dob or not sex or not email or not cpno or not region or not province or not city or not brgy:
                messagebox.showerror("Error", "All fields are required")
                return

            new_data = {
                "id": id,
                "name": name,
                "birthdate": dob,
                "sex": sex,
                "email": email,
                "cpno": cpno,
                "region": region,
                "province": province,
                "city": city,
                "brgy": brgy,
                "image_path": image_path, 
                "Mother": mother, 
                "Mother Occupation": mother_occ,  
                "Father": father,  
                "Father Occupation": father_occ  
            }

            filename = "student_record.json"
            try:
                if os.path.exists(filename):
                    with open(filename, 'r') as read_file:
                        student_info = json.load(read_file)
                else:
                    student_info = {"student_record": []}

                student_info["student_record"].append(new_data)

                with open(filename, 'w') as update_file:
                    json.dump(student_info, update_file, indent=4)

                messagebox.showinfo("RECORD", "DATA SAVED SUCCESSFULLY")
                update_treeview()  # Update the treeview after saving data
                clearWidgets()  # Clear input fields
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        Update = Button(Tab3Frame, text="Update", font=("Consolas", 10), width=20, height=4,  bg ="#e3b8fd",fg="black", command=lambda:update_values())
        Update.place(x=80, y=6)
        Update.config(state="disabled")

        myColumns = ("ID", "NAME", "BIRTH DATE", "SEX", "EMAIL", "PHONE NUMBER", "REGION", "PROVINCE", "CITY", "BARANGAY", "IMAGE PATH","MOTHER","MOTHER OCCUPATION", "FATHER","FATHER OCCUPATION")
        tree = ttk.Treeview(Tab2Frame, columns=myColumns, show="headings")
        tree.pack(fill=BOTH, expand=True)

        for col in myColumns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=CENTER)

        def update_treeview(search_term=""):
            for item in tree.get_children():
                tree.delete(item)
            
            with open("student_record.json") as read_file:
                student_record = json.load(read_file)
            
            # Filter data
            filtered_data = []
            for row in student_record['student_record']:
                match = False
                for value in row.values():
                    if search_term.lower() in str(value).lower():
                        match = True
                        break
                if match:
                    filtered_data.append(row)
            
            filtered_data = sorted(filtered_data, key=lambda x: x['id'].lower())
            
            # Insert filtered data
            for row in filtered_data:
                tree.insert("", "end", values=(
                    row.get("id", ""),
                    row.get("name", ""),
                    row.get("birthdate", ""),
                    row.get("sex", ""),
                    row.get("email", ""),
                    row.get("cpno", ""),
                    row.get("region", ""),
                    row.get("province", ""),
                    row.get("city", ""),
                    row.get("brgy", ""),
                    row.get("image_path", ""),
                    row.get("Mother", ""),
                    row.get("Mother Occupation", ""),
                    row.get("Father", ""),
                    row.get("Father Occupation", "")
                ))


        def UpdateTree():
            update_treeview()

        def clearWidgets():
            stud_ID_entry.delete(0, END)
            stud_Name_entry.delete(0, END)
            stud_DOB_entry.set_date(date.today()) 
            SexVar.set(None)
            stud_Email_entry.delete(0, END)
            stud_CPNO_entry.delete(0, END)
            regionCombo.set('')
            provinceCombo.set('')
            cityCombo.set('')
            brgyCombo.set('')
            mother_entry.delete(0, END)
            mother_occ_entry.delete(0, END)
            father_entry.delete(0, END)
            father_occ_entry.delete(0, END)
            # Clear the image on the picture button
            initial_image = Image.new('RGB', (200, 200), color='white')
            photo = ImageTk.PhotoImage(initial_image)
            picture_button.config(image=photo)
            picture_button.image = photo

        vsb = Scrollbar(Tab2Frame, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")

        hsb = Scrollbar(Tab2Frame, orient="horizontal", command=tree.xview)
        hsb.pack(side="bottom", fill="x")

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Delete Button

        delete = Button(Tab3Frame, text="Delete", font=("Consolas", 10), width=20, height=4,  bg ="#e3b8fd",fg="black", command=lambda:delete_selected())
        delete.place(x=305, y=6)


        def delete_selected():
            selected_item = tree.selection()[0]  # Get the ID of the selected item
            selected_id = tree.item(selected_item, "values")[0]  # Get the ID from the selected item
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a record to delete.")
                return
            confirmation = messagebox.askyesno("Delete", "Are you sure you want to delete the selected record?")
            if confirmation:
                print("Selected ID:", selected_item)
                item = tree.item(selected_item)
                values = item['values']
                tree.delete(selected_item)
                print(values)
                try:
                    with open('student_record.json', 'r') as read_file:
                        data = json.load(read_file)
                    
                    # Remove the selected record from the data
                    data["student_record"] = [row for row in data["student_record"] if row["id"] != selected_id]

                    # Write the updated data back to the JSON file
                    with open('student_record.json', 'w') as write_file:
                        json.dump(data, write_file, indent=4)

                    update_treeview()  # Update the TreeView after deletion

                    messagebox.showinfo("Success", "Record deleted successfully.")
                except IndexError:
                    messagebox.showerror("Error", "No item selected.")
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "Error decoding JSON from student_data.json.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

        # Print Button
        print_btn = Button(Tab3Frame, text="Print", font=("Consolas", 10), width=20, height=4,  bg ="#e3b8fd",fg="black", command=lambda:print_records())
        print_btn.place(x=550, y=6)

        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader
        import tempfile
        import os
        import subprocess
        from tkinter import simpledialog, messagebox, filedialog

        def print_records():
            # Ask the user if they want to print all records or only the selected ones
            choice = messagebox.askquestion("Print Options", "Do you want to print all records?", icon='question', type=messagebox.YESNOCANCEL)
            
            if choice == 'yes':
                records = [tree.item(row_id)['values'] for row_id in tree.get_children()]
            elif choice == 'no':
                selected_items = tree.selection()
                if not selected_items:
                    messagebox.showinfo("Print", "No items selected to print")
                    return
                records = [tree.item(row_id)['values'] for row_id in selected_items]
            else:
                return  # Cancel printing

            if not records:
                messagebox.showinfo("Print", "No records available to print")
                return

            # Confirm print action
            confirm = messagebox.askyesno("Print", "Are you sure you want to print the records?")
            if not confirm:
                return

            # Ask for a file name and location
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save as")
            if not file_path:
                return

            # Create a PDF file
            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter

            # Define text styles
            c.setFont("Helvetica", 12)

            y_position = height - 40  # Initial y position
            margin = 40  # Left margin
            image_size = 100  # Size of the image

            for record in records:
                # Draw the image if available
                image_path = record[10]
                if image_path and os.path.exists(image_path):
                    c.drawImage(ImageReader(image_path), margin, y_position - image_size, width=image_size, height=image_size)
                    y_position -= image_size + 20  # Adjust y_position for the image and add extra space

                c.drawString(margin, y_position, f"  Name: {record[1]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Student ID: {record[0]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Birthdate: {record[2]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Sex: {record[3]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Email: {record[4]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Contact Number: {record[5]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Region: {record[6]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Province: {record[7]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  City: {record[8]}")
                y_position -= 20
                c.drawString(margin, y_position, f"  Barangay: {record[9]}")
                y_position -= 30  # Add some space before the next record
                c.drawString(margin, y_position, f"  Mother: {record[11]}")
                y_position -= 30
                c.drawString(margin, y_position, f"  Mother Occupation: {record[12]}")
                y_position -= 30
                c.drawString(margin, y_position, f"  Father: {record[13]}")
                y_position -= 30  # Add some space before the next record
                c.drawString(margin, y_position, f"  Father Occupation: {record[14]}")
                y_position -= 30
                

                if y_position < 100:  # Add a new page if we're near the bottom
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = height - 40

            c.save()

            # Open the PDF file with the default PDF viewer
            if os.name == 'nt':  # Windows
                os.startfile(file_path)
            else:
                try:
                    subprocess.run(['open', file_path], check=True)  # macOS
                except FileNotFoundError:
                    subprocess.run(['xdg-open', file_path], check=True)  # Linux

        # Clear Button
        edit_btn = Button(Tab3Frame, text="Edit", font=("Consolas", 10), width=20, height=4,  bg ="#e3b8fd",fg="black", command=lambda:edit_student())
        edit_btn.place(x=775, y=6)

        def edit_student():
            Update.config(state="normal")
            edit_btn.config(state="disabled")
            Submit.config(state="disabled")
            
            selected_item = tree.selection()
            if selected_item:
                item = tree.item(selected_item)
                record = item['values']
                stud_ID_entry.delete(0, END)
                stud_ID_entry.insert(0, record[0])
                stud_Name_entry.delete(0, END)
                stud_Name_entry.insert(0, record[1])
                stud_DOB_entry.set_date(record[2])
                SexVar.set(record[3])
                stud_Email_entry.delete(0, END)
                stud_Email_entry.insert(0, record[4])
                stud_CPNO_entry.delete(0, END)
                stud_CPNO_entry.insert(0, record[5])
                regionCombo.set(record[6])
                provinceCombo.set(record[7])
                cityCombo.set(record[8])
                brgyCombo.set(record[9])
                mother_entry.delete(0, END)
                mother_entry.insert(0, record[11])
                mother_occ_entry.delete(0, END)
                mother_occ_entry.insert(0, record[12])
                father_entry.delete(0, END)
                father_entry.insert(0, record[13])
                father_occ_entry.delete(0, END)
                father_occ_entry.insert(0, record[14])
                
            filename = "student_data.json"
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    data = json.load(file)
                image_path = data.get(record[0], {}).get('ImagePath', '')
                if image_path and os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((200, 200))
                    photo = ImageTk.PhotoImage(image)
                    picture_button.config(image=photo)
                    picture_button.image = photo
                else:
                    # Clear image if no path or image does not exist
                    picture_button.config(image='')
                    picture_button.image = None
            
        def update_values():
            student_id_to_update = stud_ID_entry.get()
            
            try:
                with open('student_record.json', 'r') as read_file:
                    stud_info = json.load(read_file)
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found")
                return
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Error reading JSON file")
                return

            record_found = False

            for each_record in stud_info.get("student_record", []):
                if each_record.get("id") == student_id_to_update:
                    # Debug statements to check values being updated
                    print(f"Updating record: {each_record}")
                    each_record["name"] = stud_Name_entry.get()
                    each_record["birthdate"] = stud_DOB_entry.get()
                    each_record["sex"] = SexVar.get()
                    each_record["email"] = stud_Email_entry.get()
                    each_record["cpno"] = stud_CPNO_entry.get()
                    each_record["region"] = regionCombo.get()
                    each_record["province"] = provinceCombo.get()
                    each_record["city"] = cityCombo.get()
                    each_record["brgy"] = brgyCombo.get()
                    each_record["Mother"] = mother_entry.get()
                    each_record["Mother Occupation"] = mother_occ_entry.get()
                    each_record["Father"] = father_entry.get()
                    each_record["Father Occupation"] = father_occ_entry.get()
                    
                    record_found = True
                    break

            if record_found:
                try:
                    with open('student_record.json', 'w') as update_file:
                        json.dump(stud_info, update_file, indent=4)
                    
                    messagebox.showinfo("RECORD", "DATA SAVED SUCCESSFULLY")
                    Update.config(state="disabled")
                    edit_btn.config(state="normal")
                    Submit.config(state="normal")
                    UpdateTree()
                    clearWidgets()
                except Exception as e:
                    messagebox.showerror("Error", f"Error saving data: {e}")
            else:
                messagebox.showwarning("RECORD", "No matching student record found.")

        UpdateTree()

        backhome = Button(Tab1Frame, text=">HOMEPAGE<", font=("Consolas", 12), bg ="#8370de",fg="#ffffff" ,command=lambda:self.backtohome())
        backhome.place(x=830, y=520)

    def backtohome(self):
        self.window.withdraw()
        student_window = Toplevel(self.window)
        Homepage(student_window)

    
        
class Account:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Account')
        
        bg_image_path = 'img\\account.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
            self.bg_image = self.bg_image.resize((1166, 718))
        else:
            print(f"Error: {bg_image_path} not found.")
            return
            
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes') 
        
        backhome = Button(self.window, text=">HOMEPAGE<", font=("Consolas", 12), bg ="#8370de",fg="#ffffff" ,command=lambda:self.backtohome())
        backhome.place(x=770, y=28)
        
        def upload_picture():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
            if file_path:
                image = Image.open(file_path)
                image = image.resize((150, 100))
                photo = ImageTk.PhotoImage(image)
                picture_button.config(image=photo)
                picture_button.image = photo 
                

        # Picture Button
        initial_image = Image.new('RGB', (150, 100), color='white')
        photo = ImageTk.PhotoImage(initial_image)

        # Frame for Picture Button
        picture_frame = Frame(self.window, bg='#6533cb', width=150, height=100)
        picture_frame.place(x=220, y=180)

        picture_button = Button(picture_frame, image=photo, bg='black')
        picture_button.image = photo
        picture_button.pack(padx=5, pady=5)

        # Insert Photo Button
        photo_button = Button(picture_frame, text="INSERT PROFILE", command=upload_picture, font=("Consolas", 9), bg='#cf86fc', fg='black')
        photo_button.pack(side=BOTTOM, pady=5)
        
        # Bio Textbox
        self.bio = StringVar()
        self.bio.set("Enter Bio")
        self.bio_textbox = Text(self.window, font=("Consolas", 12), bg='#cf86fc', fg='black', wrap=WORD, height=3, width=40, state='disabled')
        self.bio_textbox.insert(END, self.bio.get())
        self.bio_textbox.place(x=125, y=350)
        
        # Mini Button for Bio
        self.toggle_bio_button = Button(self.window, text="Bio", command=self.toggle_bio_entry, font=("Consolas", 9), width=5, bg='#cf86fc', fg='black')
        self.toggle_bio_button.place(x=120, y=310)
        
        # Username Entry
        self.username = StringVar()
        self.username.set("Enter Username")
        self.username_entry = Entry(self.window, textvariable=self.username, font=("Consolas", 12), bg='#cf86fc', fg='black', width=20)
        self.username_entry.place(x=260, y=435)
        
        # Email Entry
        self.email = StringVar()
        self.email.set("Enter Email")
        self.email_entry = Entry(self.window, textvariable=self.email, font=("Consolas", 12), bg='#cf86fc', fg='black', width=20)
        self.email_entry.place(x=260, y=475)
        
        # Contact Entry
        self.contact = StringVar()
        self.contact.set("Enter Contact")
        self.contact_entry = Entry(self.window, textvariable=self.contact, font=("Consolas", 12), bg='#cf86fc', fg='black', width=20)
        self.contact_entry.place(x=260, y=515)
        
        # Address Entry
        self.address = StringVar()
        self.address.set("Enter Address")
        self.address_entry = Entry(self.window, textvariable=self.address, font=("Consolas", 12), bg='#cf86fc', fg='black', width=40)
        self.address_entry.place(x=125, y=590)
    
        # Mini Button for Address
        self.toggle_address_button = Button(self.window, text="Address", command=self.toggle_address_entry, font=("Consolas", 10), width=10, bg='#cf86fc', fg='black')
        self.toggle_address_button.place(x=125, y=560)
        
        # Enable/Disable Username Entry Button
        self.toggle_username_button = Button(self.window, text="Username:", command=self.toggle_username_entry, font=("Consolas", 10), width=9, bg='#cf86fc', fg='black')
        self.toggle_username_button.place(x=130, y=430)
        
        # Enable/Disable Email Entry Button
        self.toggle_email_button = Button(self.window, text="Email:", command=self.toggle_email_entry, font=("Consolas", 10), width=9, bg='#cf86fc', fg='black')
        self.toggle_email_button.place(x=130, y=470)
        
        # Enable/Disable Contact Entry Button
        self.toggle_contact_button = Button(self.window, text="Contact:", command=self.toggle_contact_entry, font=("Consolas", 10), width=9, bg='#cf86fc', fg='black')
        self.toggle_contact_button.place(x=130, y=510)
        
        # Logout Button
        self.logout_button = Button(self.window, text="Logout", command=self.logout, font=("Consolas", 10), width=10, bg='#b8a0e7', fg='black')
        self.logout_button.place(x=260, y=620)
        
    def logout(self):
        account_data = {
            "username": self.username.get(),
            "email": self.email.get(),
            "contact": self.contact.get(),
            "address": self.address.get(),
            "bio": self.bio_textbox.get("1.0", END).strip(),
        }

        filename = "user_accounts.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        else:
            data = {"accounts": []}

        data["accounts"].append(account_data)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

        self.window.withdraw()
        student_window = Toplevel(self.window)
        LoginPage(student_window)
        
        
    def toggle_bio_entry(self):
        current_state = self.bio_textbox.cget('state')
        new_state = 'normal' if current_state == 'disabled' else 'disabled'
        self.bio_textbox.config(state=new_state)
        if new_state == 'normal':
            self.toggle_bio_button.config(text='Bio')
        else:
            self.toggle_bio_button.config(text='Bio')

    def toggle_username_entry(self):
        current_state = self.username_entry.cget('state')
        new_state = 'normal' if current_state == 'disabled' else 'disabled'
        self.username_entry.config(state=new_state)
        if new_state == 'normal':
            self.toggle_username_button.config(text='Username')
        else:
            self.toggle_username_button.config(text='Username')

        # Save Username Functionality
        if new_state == 'normal':
            saved_username = self.username.get()
            messagebox.showinfo("Username Saved", f"Username '{saved_username}' has been saved!")
    
    def toggle_email_entry(self):
        current_state = self.email_entry.cget('state')
        new_state = 'normal' if current_state == 'disabled' else 'disabled'
        self.email_entry.config(state=new_state)
        if new_state == 'normal':
            self.toggle_email_button.config(text='Email')
        else:
            self.toggle_email_button.config(text='Email')

        # Save Email Functionality
        if new_state == 'normal':
            saved_email = self.email.get()
            messagebox.showinfo("Email Saved", f"Email '{saved_email}' has been saved!")
    
    def toggle_contact_entry(self):
        current_state = self.contact_entry.cget('state')
        new_state = 'normal' if current_state == 'disabled' else 'disabled'
        self.contact_entry.config(state=new_state)
        if new_state == 'normal':
            self.toggle_contact_button.config(text='Contact')
        else:
            self.toggle_contact_button.config(text='Contact')

        # Save Contact Functionality
        if new_state == 'normal':
            saved_contact = self.contact.get()
            messagebox.showinfo("Contact Saved", f"Contact '{saved_contact}' has been saved!")
    
    def toggle_address_entry(self):
        current_state = self.address_entry.cget('state')
        new_state = 'normal' if current_state == 'disabled' else 'disabled'
        self.address_entry.config(state=new_state)
        if new_state == 'normal':
            self.toggle_address_button.config(text='Address')
        else:
            self.toggle_address_button.config(text='Address')

        # Save Address Functionality
        if new_state == 'normal':
            saved_address = self.address.get()
            messagebox.showinfo("Address Saved", f"Address '{saved_address}' has been saved!")
        else:
            self.address_entry.delete(0, END)  # Clear entry when disabling
            
    def backtohome(self):
        self.window.withdraw()
        student_window = Toplevel(self.window)
        Homepage(student_window)

class SignUp:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Sign Up')

        bg_image_path = 'img\\sign_up.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
        else:
            print(f"Error: {bg_image_path} not found.")
            return
        
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes') 

        self.name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69')
        self.name_entry.place(x=740, y=260, width=270)

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69')
        self.email_entry.place(x=740, y=365, width=270)

        self.pass_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69', show='*')
        self.pass_entry.place(x=740, y=475, width=270)

        self.dob_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69')
        self.dob_entry.place(x=740, y=581, width=270)

        self.show_password_image = ImageTk.PhotoImage(file='img\\show.png')
        self.hide_password_image = ImageTk.PhotoImage(file='img\\hide.png')

        self.show_button = Button(self.window, image=self.show_password_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1050, y=475)
        self.hide_button = Button(self.window, image=self.hide_password_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        
        self.login_button_image = Image.open('img\\btn1.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button_image,)
        self.login_button_label = Label(self.window, image=login_button_photo, bg='white')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=750, y=640)
        self.login_button = Button(self.login_button_label, text='Register', font=("yu gothic ui", 13, "bold"), width=25,
                                   bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                   command=self.register)
        self.login_button.place(x=20, y=10)
                                  
        
    def show(self):
        self.hide_button.place(x=1050, y=475)
        self.show_button.place_forget()
        self.pass_entry.config(show='')

    def hide(self):
        self.show_button.place(x=1050, y=475)
        self.hide_button.place_forget()
        self.pass_entry.config(show='*')


    def register(self):
        name = self.name_entry.get()
        password = self.pass_entry.get()
        username = self.email_entry.get()
        dob = self.dob_entry.get()

        if not name or not password or not username or not dob:
            messagebox.showwarning("Register", "Please fill in all fields to register an account")
        else:
            messagebox.showinfo("Register", "You have successfully created a new account")
            self.window.withdraw()
            home_window = Toplevel(self.window)
            Homepage(home_window)



class Forgetpass:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Forgot Password')

        bg_image_path = 'img\\forgot_pass.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
        else:
            print(f"Error: {bg_image_path} not found.")
            return
        
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes') 

        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69')
        self.email_entry.place(x=760, y=240, width=270)

        self.email_line = Canvas(self.window, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=730, y=263)

        self.username_icon = Image.open('img\\account_icon.png')
        username_icon_photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.window, image=username_icon_photo, bg='white')
        self.username_icon_label.image = username_icon_photo
        self.username_icon_label.place(x=730, y=234) 

        self.login_button_image = Image.open('img\\btn1.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button_image,)
        self.login_button_label = Label(self.window, image=login_button_photo, bg='white')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=725, y=290)
        self.login_button = Button(self.login_button_label, text='Continue', font=("yu gothic ui", 13, "bold"), width=25,
                                   bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                   command=self.continue_pass)
        self.login_button.place(x=20, y=10)

    def continue_pass(self):
        username = self.email_entry.get()

        if not username:
            messagebox.showwarning("Forget Password", "Please fill in the username or email")
        else:
            messagebox.showinfo("Forget Password", "You have successfully retrieved your password")
            self.window.withdraw()
            home_window = Toplevel(self.window)
            Homepage(home_window)
        
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.title('Login Page')

        bg_image_path = 'img/login.png'
        if os.path.exists(bg_image_path):
            self.bg_image = Image.open(bg_image_path)
        else:
            print(f"Error: {bg_image_path} not found.")
            return
        
        bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.window, image=bg_photo)
        self.bg_label.image = bg_photo
        self.bg_label.pack(fill='both', expand='yes')
        
        self.email_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69')
        self.email_entry.place(x=760, y=240, width=270)

        self.email_line = Canvas(self.window, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=730, y=263)

        self.username_icon = Image.open('img\\account_icon.png')
        username_icon_photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.window, image=username_icon_photo, bg='white')
        self.username_icon_label.image = username_icon_photo
        self.username_icon_label.place(x=730, y=234)

        self.pass_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                    font=("Arial", 12), insertbackground='#6b6a69',show='*')
        self.pass_entry.place(x=760, y=350, width=270)

        self.pass_line = Canvas(self.window, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.pass_line.place(x=730, y=373)

        self.login_button_image = Image.open('img\\btn1.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button_image,)
        self.login_button_label = Label(self.window, image=login_button_photo, bg='white')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=725, y=435)
        self.login_button = Button(self.login_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25,
                                   bd=0, bg='#3047ff', cursor='hand2', activebackground='blue', fg='white',
                                   command=self.login)
        self.login_button.place(x=20, y=10)

        self.password_icon = Image.open('img\\pass.png')
        password_icon_photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.window, image=password_icon_photo, bg='white')
        self.password_icon_label.image = password_icon_photo
        self.password_icon_label.place(x=730, y=344)

        self.show_password_image = ImageTk.PhotoImage(file='img\\show.png')
        self.hide_password_image = ImageTk.PhotoImage(file='img\\hide.png')

        self.show_button = Button(self.window, image=self.show_password_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1010, y=355)
        self.hide_button = Button(self.window, image=self.hide_password_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")

        self.forgot_password_button = Button(self.window, text="Forgot Password ?",
                                             font=("Calibri Light", 11, "underline"), fg="black", relief=FLAT,
                                             activebackground="white", borderwidth=0, background="white",
                                             cursor="hand2", command=self.forgot_password)
        self.forgot_password_button.place(x=820, y=500)
        
        self.sign_up_label = Label(self.window, text='No account yet?', font=("Calibri LIght", 9),
                                   relief=FLAT, borderwidth=0, background="white", fg='black')
        self.sign_up_label.place(x=775, y=560)

        self.signup_image = ImageTk.PhotoImage(file='img\\register.png')
        self.signup_button_label = Button(self.window, image=self.signup_image, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="white", activebackground="white",
                                          command=self.sign_up)
        self.signup_button_label.place(x=870, y=550, width=111, height=35)

    def show(self):
        self.hide_button.place(x=1010, y=355)
        self.show_button.place_forget()
        self.pass_entry.config(show='')

    def hide(self):
        self.show_button.place(x=1010, y=355)
        self.hide_button.place_forget()
        self.pass_entry.config(show='*')

    def login(self):
        username = self.email_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            messagebox.showwarning("Login", "Please fill in both the username and password fields.")
        else:
            self.window.withdraw()
            home_window = Toplevel(self.window)
            Homepage(home_window)
            
    def forgot_password(self):
        self.window.withdraw()
        forgot_window = Toplevel(self.window)
        Forgetpass(forgot_window)
        
    def sign_up(self):
        self.window.withdraw()
        sign_up_window = Toplevel(self.window)
        SignUp(sign_up_window)
             
    def sign_up(self):
        self.window.withdraw()
        sign_up_window = Toplevel(self.window)
        SignUp(sign_up_window)
        
    def homepage(self):
        self.window.withdraw()
        homepage_window = Toplevel(self.window)
        Homepage(homepage_window)
        
    def student(self):
        self.window.withdraw()
        student_window = Toplevel(self.window)
        Student(student_window)

def create_login_page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    create_login_page()
