from tkinter import *
import math,random
from tkinter import messagebox
import os

class bill_app:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Patient Bill")
        bg_color = "light blue"
        title = Label(self.root,text="Patient Bill",bd=12,relief=GROOVE,bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        # variables
        # insurance avriables
        self.life=IntVar()
        self.health=IntVar()
        self.med=IntVar()
        self.l_term=IntVar()
        self.disability=IntVar()
        self.s_term=IntVar()

        # medicine variables
        self.m1=IntVar()
        self.m2=IntVar()
        self.m3=IntVar()
        self.m4=IntVar()
        self.m5=IntVar()
        self.m6=IntVar()

        # consultation variables
        self.cons=IntVar()
        self.xray=IntVar()
        self.inj=IntVar()
        self.drs=IntVar()
        self.bld=IntVar()
        self.mri=IntVar()

        # price and tax variables
        self.insurance=StringVar()
        self.medicine=StringVar()
        self.consultation=StringVar()

        self.insurance_tax=StringVar()
        self.medicine_tax=StringVar()
        self.consultation_tax=StringVar()

        # patient
        self.p_name=StringVar()
        self.phn=StringVar()
        self.bill_no=StringVar()
        n = random.randint(1000,9999)
        self.bill_no.set(n)
        self.search_bill=StringVar()

        #customer deatils frame
        f1 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Patient Details",fg='gray',bg=bg_color,font=("times new roman",15,'bold'))
        f1.place(x=0,y=80,relwidth=1)
        cname_lbl = Label(f1,text='Patient Name',bg=bg_color,font=("times new roman",18,'bold')).grid(row=0,column=0,padx=2,pady=5)
        cname_txt = Entry(f1,width=20,textvariable=self.p_name,bd=7,relief=SUNKEN,font='arial 15').grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(f1,text='Phone No.',bg=bg_color,font=("times new roman",18,'bold')).grid(row=0,column=2,padx=2,pady=5)
        cphn_txt = Entry(f1,width=20,textvariable=self.phn,bd=7,relief=SUNKEN,font='arial 15').grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl = Label(f1,text='Bill No.',bg=bg_color,font=("times new roman",18,'bold')).grid(row=0,column=4,padx=2,pady=5)
        cbill_txt = Entry(f1,width=20,bd=7,textvariable=self.search_bill,relief=SUNKEN,font='arial 15').grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(f1,text='Search',command=self.find_bill,width=10,bg='cadetblue',font=('arial',15,'bold')).grid(row=0,column=6,pady=10,padx=10)

        # Insurance frame
        f2 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Insurance",fg='gray',bg=bg_color,font=("times new roman",15,'bold'))
        f2.place(x=5,y=180,width=325,height=380)

        life_lbl = Label(f2,text='Life',font=('times new roman',16,'bold'),bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        life_txt = Entry(f2,width=10,textvariable=self.life,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        hlt_lbl = Label(f2,text='Health',font=('times new roman',16,'bold'),bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        hlt_txt = Entry(f2,width=10,textvariable=self.health,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        med_lbl = Label(f2,text='Medicine',font=('times new roman',16,'bold'),bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        med_txt = Entry(f2,width=10,textvariable=self.med,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        lng_lbl = Label(f2,text='Long-term',font=('times new roman',16,'bold'),bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        lng_txt = Entry(f2,width=10,textvariable=self.l_term,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        dis_lbl = Label(f2,text='Diasability',font=('times new roman',16,'bold'),bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        dis_txt = Entry(f2,width=10,textvariable=self.disability,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sht_lbl = Label(f2,text='Short-term',font=('times new roman',16,'bold'),bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        sht_txt = Entry(f2,width=10,textvariable=self.s_term,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # medicine frame
        f3 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Medicine",fg='gray',bg=bg_color,font=("times new roman",15,'bold'))
        f3.place(x=340,y=180,width=325,height=380)

        m1_lbl = Label(f3,text='Med 1',font=('times new roman',16,'bold'),bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        m1_txt = Entry(f3,width=10,textvariable=self.m1,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2_lbl = Label(f3,text='Med 2',font=('times new roman',16,'bold'),bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        m2_txt = Entry(f3,width=10,textvariable=self.m2,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3_lbl = Label(f3,text='Med 3',font=('times new roman',16,'bold'),bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        m3_txt = Entry(f3,width=10,textvariable=self.m3,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        m4_lbl = Label(f3,text='Med 4',font=('times new roman',16,'bold'),bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        m4_txt = Entry(f3,width=10,textvariable=self.m4,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        m5_lbl = Label(f3,text='Med 5',font=('times new roman',16,'bold'),bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        m5_txt = Entry(f3,width=10,textvariable=self.m5,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        m6_lbl = Label(f3,text='Med 6',font=('times new roman',16,'bold'),bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        m6_txt = Entry(f3,width=10,textvariable=self.m6,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # hospiatl frame
        f4 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Hospiatl Charges",fg='gray',bg=bg_color,font=("times new roman",15,'bold'))
        f4.place(x=670,y=180,width=325,height=380)

        con_lbl = Label(f4,text='consultation',font=('times new roman',16,'bold'),bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        con_txt = Entry(f4,width=10,textvariable=self.cons,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        xray_lbl = Label(f4,text='X - Ray',font=('times new roman',16,'bold'),bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        xray_txt = Entry(f4,width=10,textvariable=self.xray,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        inj_lbl = Label(f4,text='Injection',font=('times new roman',16,'bold'),bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        inj_txt = Entry(f4,width=10,textvariable=self.inj,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        drs_lbl = Label(f4,text='Dressing',font=('times new roman',16,'bold'),bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        drs_txt = Entry(f4,width=10,textvariable=self.drs,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        bld_lbl = Label(f4,text='Blood Test',font=('times new roman',16,'bold'),bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        bld_txt = Entry(f4,width=10,textvariable=self.bld,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        mri_lbl = Label(f4,text='MRI',font=('times new roman',16,'bold'),bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        mri_txt = Entry(f4,width=10,textvariable=self.mri,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #bill area
        f5 = Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1010,y=180,width=335,height=380)
        bill_title = Label(f5,text='Bill Area',font=('arial 15 bold'),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #button frame
        f6 = LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",fg='gray',bg=bg_color,font=("times new roman",15,'bold'))
        f6.place(x=0,y=560,relwidth=1,height=140)
        b1_lbl = Label(f6,text='Total Insurance Price',bg=bg_color,font=('times new roman',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        b1_txt = Entry(f6,width=18,textvariable=self.insurance,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        b2_lbl = Label(f6,text='Total Medicine Price',bg=bg_color,font=('times new roman',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        b2_txt = Entry(f6,width=18,textvariable=self.medicine,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        b3_lbl = Label(f6,text='Total Consultation Price',bg=bg_color,font=('times new roman',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        b3_txt = Entry(f6,width=18,textvariable=self.consultation,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(f6,text='Insurance Tax',bg=bg_color,font=('times new roman',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt = Entry(f6,width=18,textvariable=self.insurance_tax,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(f6,text='Medicine Tax',bg=bg_color,font=('times new roman',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt = Entry(f6,width=18,textvariable=self.medicine_tax,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(f6,text='Consultation Tax',bg=bg_color,font=('times new roman',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt = Entry(f6,width=18,textvariable=self.consultation_tax,font=('arial 10 bold'),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f = Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn = Button(btn_f,command=self.total,text='Total',bg='cadetblue',pady=15,width=10,font=('arial 15 bold'),bd=5).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_f,text='Genrate Bill',command=self.bill_area,bg='cadetblue',pady=15,width=10,font=('arial 15 bold'),bd=5).grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_f,text='Clear',command=self.clear_data,bg='cadetblue',pady=15,width=9,font=('arial 15 bold'),bd=5).grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_f,text='Exit',command=self.exit_app,bg='cadetblue',pady=15,width=9,font=('arial 15 bold'),bd=5).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.p_l_p=self.life.get()*100000
        self.p_h_p=self.health.get()*50000
        self.p_lt_p=self.l_term.get()*70000
        self.p_m_p=self.med.get()*5000
        self.p_d_p=self.disability.get()*15000
        self.p_st_p=self.s_term.get()*20000
        self.t_ins_price=float(
                            (self.p_l_p)+
                            (self.p_d_p)+
                            (self.p_h_p)+
                            (self.p_lt_p)+
                            (self.p_m_p)+
                            (self.p_st_p)
                        )
        self.insurance.set('Rs. '+str(self.t_ins_price))
        self.i_tax=round(self.t_ins_price*0.03,2)
        self.insurance_tax.set('Rs. '+str(self.i_tax))

        self.m_1_p=self.m1.get()*10
        self.m_2_p=self.m2.get()*20
        self.m_3_p=self.m3.get()*30
        self.m_4_p=self.m4.get()*40
        self.m_5_p=self.m5.get()*50
        self.m_6_p=self.m6.get()*60
        self.t_med_price=float(
                            (self.m_1_p)+
                            (self.m_2_p)+
                            (self.m_3_p)+
                            (self.m_4_p)+
                            (self.m_5_p)+
                            (self.m_6_p)
                        )
        self.medicine.set('Rs. '+str(self.t_med_price))
        self.m_tax=round(self.t_med_price*0.01,2)
        self.medicine_tax.set('Rs. '+str(self.m_tax))

        self.h_c_p=self.cons.get()*500
        self.h_x_p=self.xray.get()*350
        self.h_i_p=self.inj.get()*80
        self.h_d_p=self.drs.get()*100
        self.h_b_p=self.bld.get()*150
        self.h_m_p=self.mri.get()*750
        self.t_con_price=float(
                            (self.h_c_p)+
                            (self.h_x_p)+
                            (self.h_i_p)+
                            (self.h_d_p)+
                            (self.h_b_p)+
                            (self.h_m_p)
                        )
        self.consultation.set('Rs. '+str(self.t_con_price))
        self.c_tax=round(self.t_con_price*0.01,2)
        self.consultation_tax.set('Rs. '+str(self.c_tax))

        self.total_bill=round(float(self.t_ins_price+self.t_med_price+self.t_con_price+self.i_tax+self.m_tax+self.c_tax),2)

    def welcome_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\t     PATIENT BILL\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()} ")
        self.txtarea.insert(END,f"\n Patient Name : {self.p_name.get()} ")
        self.txtarea.insert(END,f"\n Phone Number : {self.phn.get()}")
        self.txtarea.insert(END,"\n************************************")
        self.txtarea.insert(END,"\n Products \t\tQTY\t     Price")
        self.txtarea.insert(END,"\n************************************")

    def bill_area(self):
        if self.p_name.get()==''or self.phn.get()=='':
            messagebox.showerror('Error','Patient details is mandatory')
        elif self.insurance.get()=='Rs. 0.0' and self.medicine.get()=='Rs. 0.0' and self.consultation.get()=='Rs. 0.0':
            messagebox.showerror('Error','No product selected')
        else:
            self.welcome_bill()
            # insurance
            if self.life.get()!=0:
                self.txtarea.insert(END,f'\n Life Ins\t\t{self.life.get()}\t   {self.p_l_p}')
            if self.health.get()!=0:
                self.txtarea.insert(END,f'\n Health Ins\t\t{self.health.get()}\t   {self.p_h_p}')
            if self.med.get()!=0:
                self.txtarea.insert(END,f'\n Medicine Ins\t\t{self.med.get()}\t   {self.p_m_p}')
            if self.l_term.get()!=0:
                self.txtarea.insert(END,f'\n Long Ins\t\t{self.l_term.get()}\t   {self.p_lt_p}')
            if self.disability.get()!=0:
                self.txtarea.insert(END,f'\n Disability Ins\t\t{self.disability.get()}\t   {self.p_d_p}')
            if self.s_term.get()!=0:
                self.txtarea.insert(END,f'\n Short Ins\t\t{self.s_term.get()}\t   {self.p_st_p}')

            # medicine
            if self.m1.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 1\t\t{self.m1.get()}\t   {self.m_1_p}')
            if self.m2.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 2\t\t{self.m2.get()}\t   {self.m_2_p}')
            if self.m3.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 3\t\t{self.m3.get()}\t   {self.m_3_p}')
            if self.m4.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 4\t\t{self.m4.get()}\t   {self.m_4_p}')
            if self.m5.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 5\t\t{self.m5.get()}\t   {self.m_5_p}')
            if self.m6.get()!=0:
                self.txtarea.insert(END,f'\n Medicine 6\t\t{self.m6.get()}\t   {self.m_6_p}')

            # hospital
            if self.cons.get()!=0:
                self.txtarea.insert(END,f'\n Consultation\t\t{self.cons.get()}\t   {self.h_c_p}')
            if self.xray.get()!=0:
                self.txtarea.insert(END,f'\n X - Ray\t\t{self.xray.get()}\t   {self.h_x_p}')
            if self.inj.get()!=0:
                self.txtarea.insert(END,f'\n Injection\t\t{self.inj.get()}\t   {self.h_i_p}')
            if self.drs.get()!=0:
                self.txtarea.insert(END,f'\n Dressing\t\t{self.drs.get()}\t   {self.h_d_p}')
            if self.bld.get()!=0:
                self.txtarea.insert(END,f'\n Blood Test\t\t{self.bld.get()}\t   {self.h_b_p}')
            if self.mri.get()!=0:
                self.txtarea.insert(END,f'\n MRI\t\t{self.mri.get()}\t   {self.h_m_p}')

            self.txtarea.insert(END,"\n************************************")
            if self.insurance_tax.get()!='Rs. 0.0':
                self.txtarea.insert(END,f"\n Insurance Tax \t\t\t{self.insurance_tax.get()}")
            if self.medicine_tax.get()!='Rs. 0.0':
                self.txtarea.insert(END,f"\n Medicine Tax \t\t\t{self.medicine_tax.get()}")
            if self.consultation_tax.get()!='Rs. 0.0':
                self.txtarea.insert(END,f"\n Hospital Tax \t\t\t{self.consultation_tax.get()}")
            self.txtarea.insert(END,f"\n Total Bill \t\t\tRs. {self.total_bill}")
            self.txtarea.insert(END,"\n************************************")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save",'DO you want to save the Bill')
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open('Bills/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('saved',f"Bill no : {self.bill_no.get()} saved successfully!")
        else:
            return        

    def find_bill(self):
        present='no'
        for i in os.listdir('Bills/'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present='yes'
        if present == 'no':
            messagebox.showerror('Error','Invalid Bill no.') 

    def clear_data(self):

        op=messagebox.askyesno('Clear','Do you want to clear ?')
        if op>0:
            #self.txtarea.delete('1.0',END)
            # insurance avriables
            self.life.set(0)
            self.health.set(0)
            self.med.set(0)
            self.l_term.set(0)
            self.disability.set(0)
            self.s_term.set(0)

            # medicine variables
            self.m1.set(0)
            self.m2.set(0)
            self.m3.set(0)
            self.m4.set(0)
            self.m5.set(0)
            self.m6.set(0)

            # consultation variables
            self.cons.set(0)
            self.xray.set(0)
            self.inj.set(0)
            self.drs.set(0)
            self.bld.set(0)
            self.mri.set(0)

            # price and tax variables
            self.insurance.set('')
            self.medicine.set('')
            self.consultation.set('')

            self.insurance_tax.set('')
            self.medicine_tax.set('')
            self.consultation_tax.set('')

            # patient
            self.p_name.set('')
            self.phn.set('')
            self.bill_no.set('')
            n = random.randint(1000,9999)
            self.bill_no.set(n)
            self.search_bill.set('')
            self.welcome_bill()        

    def exit_app(self):
        op=messagebox.askyesno('Exit','Do you want to Exit ?')
        if op>0:
            self.root.destroy()

root = Tk()
obj = bill_app(root)
root.mainloop()
