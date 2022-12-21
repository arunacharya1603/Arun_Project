from sqlite3 import connect
from this import d
from tkinter import *
from textwrap import fill
import tkinter
from tkinter import BOTH, RIDGE, RIGHT, TOP, VERTICAL, W, Y, Entry, Frame, Label, LabelFrame, Scrollbar, Tk, ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.tix import TEXT
from turtle import width
from typing_extensions import Self
import mysql.connector

class MedicalShop:

    def __init__(self,root):
        self.root=root
        self.root.title("Billing Management System")
        self.root.geometry("1280x720")
        self.Cust_Name=StringVar() 
        self.Bill_No=StringVar()
        self.Nameoftablets=StringVar() 
        self.NoOfTablets=StringVar()  
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        
        self.Productprice=StringVar()
        
        
        lbltitle=Label(root,text="Medical Shop Billing Slip",bg="#4D0039",fg="white",bd=20,relief=RIDGE,font=("times new roman",51,"bold"),padx=2,pady=6)
        lbltitle.pack(fill=X)

        #********************************Data Frame*************************************#
        Dataframe = Frame(self.root,bd=20,relief=RIDGE,bg='#4D0039')
        Dataframe.place(x=0,y=130,width=1280,height=380)

        DataframeLeft = LabelFrame(Dataframe,bd=10,padx=10,
                                                  font=('times new rommon',18,'bold'),relief=GROOVE,bg='#4D0039',fg='gold',text="Product Informantion")

        DataframeLeft.place(x=0,y=5,width=850,height=330)

        DataframeRight = LabelFrame(Dataframe,bd=10,padx=10,
                                                  font=('times new rommon',18,'bold'),relief=GROOVE,bg='#4D0039',fg='gold',text="Billing Slip Om Medicine")

        #DataframeRight.place(x=0,y=5,width=850,height=350)
        DataframeRight.place(x=860,y=5,width=360,height=330)

        # *******************************Button Frame********************************
        Buttonframe = Frame(self.root,bd=20,relief=GROOVE,bg='#4D0039')
        Buttonframe.place(x=0,y=500,width=1280,height=70)

        # *******************************Detail Frame********************************
        Detailframe = Frame(self.root,bd=20,relief=RIDGE,bg='#4D0039')
        Detailframe.place(x=0,y=570,width=1280,height=130)

        # -----------------------------Data Frame-------------------------------------

        lblName=Label(DataframeLeft,text="Customer Name:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =10.5,pady=15)
        lblName.grid(row=0,column=0,sticky=W)
        txtName=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.Cust_Name,width=35)
        txtName.grid(row=0,column=1)

        lblNameTablet=Label(DataframeLeft,text="Name of Tablets:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =11, pady = 15)
        lblNameTablet.grid(row=1,column=0,sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arail",8,"bold"),
                                                           width=33)

        comNametablet["values"] = ("Select","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan","Paracetamol","Calcium Carbonate + Vitamin D3","Cetrizine (StayHapppi Generic)","Abarelix","Abacavir Sulfate","Abatacept","Abelcet","Allegra-D","Amino Acids","Amoxicillin","Amphadase","Ampicillin","Aspirin","Omeprazole","Celexa","Morphine","Oxycodone","Adderall")
        comNametablet.current(0)
        comNametablet.grid(row=1,column=1)
     
        lblNoOfTablets=Label(DataframeLeft,text="No of Tablets:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =20,pady=15)
        lblNoOfTablets.grid(row=2,column=0,sticky=W)
        txtNoOfTablets=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.NoOfTablets,width=35)
        txtNoOfTablets.grid(row=2,column=1)


        lblFurtherInfo=Label(DataframeLeft,text="Further Info:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =24,pady=15)
        lblFurtherInfo.grid(row=3,column=0,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=3,column=1)


        lblStorage=Label(DataframeLeft,text="Storage Advice:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =15,pady=15)
        lblStorage.grid(row=4,column=0,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=4,column=1)


        lblProductPrice=Label(DataframeLeft,text="Product Price:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =20,pady=15)
        lblProductPrice.grid(row=5,column=0,sticky=W)
        txtProductPrice=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.Productprice,width=35)
        txtProductPrice.grid(row=5,column=1)

        lblName=Label(DataframeLeft,text="Bill Number:",font=("arail",8,"bold"),relief=GROOVE,bg='#4D0039',fg='gold',padx =20,pady=15)
        lblName.grid(row=0,column=2,sticky=W)
        txtName=Entry(DataframeLeft,font=("arail",8,"bold"),relief=SUNKEN,textvariable=self.Bill_No,width=35)
        txtName.grid(row=0,column=3)


        #************************************Dataframe Right*****************************************
        scroll_yP=Scrollbar(DataframeRight,orient=VERTICAL)
        self.Text_t=Text(DataframeRight,height=300,width=800,font=("arail",10),bg="white",fg="black")
        scroll_yP.pack(side=RIGHT,fill=Y)
        scroll_yP.config(command=self.Text_t.yview)
        self.Text_t.pack(fill=BOTH,expand=1)
        


        # ===============================Buttons==================================
        btnPrint=Button(Buttonframe,command=self.iPrescription,text="Print",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnPrint.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.Update,text="Update",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="gold",fg="white", font=("arail",8,"bold"),width=23)
        btnExit.grid(row=0,column=5)

        btnBill=Button(Buttonframe,command=self.bill,text="Bill",bg="gold",fg="white", font=("arail",8,"bold"),width=24)
        btnBill.grid(row=0,column=6)

        #*******************************Table*****************************
        #**********************Scroll********************************

        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.billing_table=ttk.Treeview(Detailframe,column=("CustomerName","BillNumber","nameoftables","nooftablets","furtherinfo","storage","productprice"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.billing_table.xview)
        scroll_y=ttk.Scrollbar(command=self.billing_table.yview)

        self.billing_table.heading("CustomerName",text="Customer name:")
        self.billing_table.heading("BillNumber",text="Bill Number:")
        self.billing_table.heading("nameoftables",text="Name Of Tables")
        self.billing_table.heading("nooftablets",text="No Of Tablets")
        self.billing_table.heading("furtherinfo",text="Further Information")
        self.billing_table.heading("storage",text="Storage")     
        self.billing_table.heading("productprice",text="Product price")
        

        self.billing_table["show"]="headings"
        self.billing_table.column("CustomerName",width=80)
        self.billing_table.column("BillNumber",width=80)
        self.billing_table.column("nameoftables",width=80)
        self.billing_table.column("nooftablets",width=80)
        self.billing_table.column("furtherinfo",width=80)
        self.billing_table.column("storage",width=80)
        self.billing_table.column("productprice",width=80)
        

        self.billing_table.pack(fill=BOTH,expand=1)
        self.billing_table.bind("<ButtonRelease-1>",self.get_cursor)



        self.fatch_data()


    #****************************Functionality Declaration********************************
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" :
           messagebox.showerror("Error!","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Uiet@143",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into billing values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.Cust_Name.get(),
                                                                                                     self.Bill_No.get(),
                                                                                                     self.Nameoftablets.get(),                                                                                                    
                                                                                                     self.NoOfTablets.get(),                                                                                                  
                                                                                                     self.FurtherInformation.get(),
                                                                                                     self.StorageAdvice.get(),                                                                                                                                                                                                    
                                                                                                     self.Productprice.get(),
                                                                                                        ))
        
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")



    def Update(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Uiet@143",database="mydata")
            my_cursor=conn.cursor()  
            s="update billing set  CustomerName=%s,Nameoftablets=%s,NoOfTablets=%s,FurtherInformation=%s,StorageAdvice=%s,Productprice=%s  where BillNumber=%s"
            my_cursor.execute(s,( 

                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        self.Cust_Name.get(),
                                                                                                                                                                                                        self.Nameoftablets.get(),
                                                                                                                                                                                                        self.NoOfTablets.get(),   
                                                                                                                                                                                                        self.FurtherInformation.get(),
                                                                                                                                                                                                        self.StorageAdvice.get(),                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                        self.Productprice.get(), 
                                                                                                                                                                                                        self.Bill_No.get(), 
                                                                                                                                                                                                                                   

                                                                                                                                                                                            ) )
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Updated!","Record has been Updated")



    def fatch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Uiet@143",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from billing")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.billing_table.delete(*self.billing_table.get_children())
                for i in rows:
                    self.billing_table.insert("",END,values=i)
                conn.commit()
            conn.close()    


    def bill(self):
       num=random.randint(1000,9999)
       self.Bill_No.set(str(num))


    def get_cursor(self,event=""):
        cursor_row=self.billing_table.focus()
        content=self.billing_table.item(cursor_row)
        row=content["values"]
        self.Cust_Name.set(row[0])
        self.Bill_No.set(row[1])
        self.Nameoftablets.set(row[2])                      
        self.NoOfTablets.set(row[3])              
        self.FurtherInformation.set(row[4])         
        self.StorageAdvice.set(row[5])                      
        self.Productprice.set(row[6])         
       


    def iPrescription(self):
        self.Text_t.insert(END,"\t*****Welcome Om Medicine Shop*****\n")
        self.Text_t.insert(END,f"\n=================================================\n")
        self.Text_t.insert(END,"Customer Name:\t\t\t"+self.Cust_Name.get()+"\n")
        self.Text_t.insert(END,"Bill Number:\t\t\t"+self.Bill_No.get()+"\n")
        self.Text_t.insert(END,"Name of tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.Text_t.insert(END,"No of Tablets:\t\t\t"+ self.NoOfTablets.get()+ "\n")
        self.Text_t.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.Text_t.insert(END,"Storage Adivce:\t\t\t"+self.StorageAdvice.get()+"\n")  
        self.Text_t.insert(END,"Product Price:\t\t\t"+self.Productprice.get()+"\n")
        self.Text_t.configure(font='arial 8 ')
        self.Text_t.insert(END,f"\n=================================================\n")
        num=random.randint(1000,9999)
        self.Bill_No.set(str(num))
       
        

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Uiet@143",database="mydata")
        my_cursor=conn.cursor()
        query="delete from billing where Nameoftablets=%s"
        value=(self.Nameoftablets.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been deleted")


    def clear(self):
        self.Cust_Name.set("")
        self.Bill_No.set("")
        self.Nameoftablets.set("")          
        self.NoOfTablets.set("")            
        self.FurtherInformation.set("")   
        self.StorageAdvice.set("")                   
        self.Productprice.set("")         
        self.Text_t.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Billing management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return    




if __name__== "__main__":

 root=Tk()



 ob = MedicalShop(root)
 root.mainloop()