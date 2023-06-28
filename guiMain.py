from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from data import Motor , User

window = Tk()

window.geometry("1024x768")
window.configure(bg = "#202133")

nama = None
usia = None
noHp = None
domisili = None
noKtp = None
lamaPeminjaman = None
noSim = None
kotaTujuan = None
motor = None
metodePembayaran  = None ; 
usert = None 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = (OUTPUT_PATH.resolve()).joinpath("assets")

def homePage():
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame0") / Path(path)
    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=dataDiri,relief="flat")
    button_1.place(x=405.0,y=505.0,width=214.10406494140625,height=59.158538818359375)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    
    image_1 = canvas.create_image(512.0,339.0,image=image_image_1)
    window.resizable(False, False)
    window.mainloop()




#############################################################
#################
######
#     DATA DIRI GUI
def dataDiri() : 
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame1") / Path(path)

    canvas = Canvas(window,bg = "#202133",height = 768, width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    canvas.create_text(548.0,158.0,anchor="nw",text="Nama Lengkap",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(548.0,231.0,anchor="nw",text="Usia",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(548.0,304.0,anchor="nw",text="Nomor Handphone",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(548.0,377.0,anchor="nw",text="Domisili",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(548.0,450.0,anchor="nw",text="No. KTP",fill="#FFFFFF",font=("Inter", 16 * -1))
    
    # Nama Lengkap
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(698.5,198.0,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0, )
    entry_1.place(x=553.0,y=185.0,width=291.0,height=24.0) 
    
    # Usia
    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(698.5,271.0,image=entry_image_6)
    entry_6 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_6.place(x=553.0,y=258.0,width=291.0,height=24.0)
    
    # No HP
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(698.5,344.0,image=entry_image_3)
    entry_3 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_3.place(x=553.0,y=331.0,width=291.0,height=24.0)
    
    # Domisili
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(698.5,417.0,image=entry_image_4)
    entry_4 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_4.place(x=553.0,y=404.0,width=291.0,height=24.0)

    
    # No KTP
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(698.5,490.0,image=entry_image_5)
    entry_5 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_5.place(x=553.0,y=477.0,width=291.0,height=24.0)

    
    def getNama() :  
        global nama
        nama = entry_1.get()
    
    def getUsia() : 
        global usia 
        usia = entry_6.get()
    
    def getNoHp() : 
        global noHp
        noHp = entry_3.get()
        
    def getDomisili() : 
        global domisili
        domisili = entry_4.get()    
        
    def getNoKtp() : 
        global noKtp
        noKtp = entry_5.get()

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(325.0,354.0,image=image_image_1)

    
    def handleDataDiri () :
        global nama, usia, noHp, domisili, noKtp
        getNama()
        getUsia()
        getNoHp()
        getDomisili()
        getNoKtp()
        jenisMotor()

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))    
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=handleDataDiri,relief="flat")
    button_1.place(x=800.0,y=536.0,width=128.0,height=99.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=homePage,relief="flat")
    button_2.place(x=103.0,y=536.0,width=128.0,height=99.0)
    window.resizable(False, False)
    window.mainloop()




#############################################################################################
####
##
#JENIS MOTOR GUI
def jenisMotor () :
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame2") / Path(path)
    isClick = False
    def handleJenisMotor(jenis , harga): 
        global motor ; 
        motor = Motor(jenis , harga )
        detailTransaksi()

    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
            

        
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Bebek', 10000),relief="flat")
        
    button_1.place(x=247.0,y=220.0,width=235.0,height=100.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Skuter', 15000),relief="flat")


    button_2.place(x=247.0,y=343.0,width=235.0,height=99.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Sport',  40000),relief="flat")
    
        
    button_3.place(x=247.0,y=464.0,width=235.0,height=100.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Retro' , 45000),relief="flat")
    
        
    button_4.place(x=554.0,y=221.0,width=235.0,height=99.0)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Trail' , 90000),relief="flat")

    button_5.place(x=554.0,y=343.0,width=235.0,height=99.0)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda : handleJenisMotor('Touring' , 70000),relief="flat")      
    button_6.place(x=554.0,y=464.0,width=235.0,height=100.0)

    canvas.create_text(380.0,126.0,anchor="nw",text="Jenis Motor",fill="#FFFFFF",font=("Poppins Regular", 48 * -1))

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=dataDiri,relief="flat")
    button_8.place(x=104.0,y=610.0,width=128.0,height=99.0)
    window.resizable(False, False)
    window.mainloop()

  
  
  
  
###########################################
#######    DETAIL TRANSAKSI
def detailTransaksi ()  : 
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame3") / Path(path)
    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    canvas.create_rectangle(204.0,190.98260498046875,849.0,216.00286865234375,fill="#D9D9D9",outline="")
    
    canvas.create_text(204.0,165.0,anchor="nw",text="Lama Peminjaman",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(204.0,235.0,anchor="nw",text="Kota Tujuan",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(204.0,305.49853515625,anchor="nw",text="No SIM",fill="#FFFFFF",font=("Inter", 16 * -1))
    
    
    canvas.create_text(204.0,375.747802734375,anchor="nw",text="Domisili",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(230.0,408.747802734375,anchor="nw",text=domisili,fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(204.0,445.9970703125,anchor="nw",text="No. KTP",fill="#FFFFFF",font=("Inter", 16 * -1))
    canvas.create_text(230.0,477.747802734375,anchor="nw",text=noKtp,fill="#FFFFFF",font=("Inter", 16 * -1))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(526.5,203.49273681640625,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)   
    entry_1.place(x=209.0,y=190.98260498046875,width=635.0,height=23.020263671875)

    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(526.5,273.74200439453125,image=entry_image_5)
    entry_5 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_5.place(x=209.0,y=261.23187255859375,width=635.0,height=23.020263671875)
    
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(526.5,343.9913330078125,image=entry_image_2)
    entry_2 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    entry_2.place(x=209.0,y=331.481201171875,width=635.0,height=23.020263671875)
    
    def inputLamaPeminjaman ()  : 
        global lamaPeminjaman
        lamaPeminjaman = int (entry_1.get())
    
    def noSim () : 
        global noSim ; 
        noSim = entry_2.get()
        
    def kotaTujuan () : 
        global kotaTujuan ; 
        kotaTujuan = entry_5.get()
    

    def handleDetailTransaksi():
        inputLamaPeminjaman()
        noSim()
        kotaTujuan()
        
        verifikasiTransaksi()

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=handleDetailTransaksi,relief="flat")
    button_1.place(x=811.0,y=619.0,width=128.0,height=99.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=jenisMotor,relief="flat")
    button_2.place(x=114.0,y=619.0,width=128.0,height=99.0)
    window.resizable(False, False)
    window.mainloop()

###################################
##############
####     Verivikasi Transaksi
def verifikasiTransaksi () : 
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame4") / Path(path)

    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(512.0,331.0,image=image_image_1)

    canvas.create_text(399.0,79.0,anchor="nw",text="DETAIL TRANSAKSI",fill="#FFFFFF",font=("Inter", 24 * -1))

    canvas.create_text(244.0,159.0,anchor="nw",text="Nama",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(244.0,238.0,anchor="nw",text="Jenis Motor",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(512.0,303.0,anchor="nw",text="Biaya Sewa / Jam",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(512.0,341.0,anchor="nw",text="Lama Peminjaman",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(512.0,384.0,anchor="nw",text="Total Biaya ",fill="#FFFFFF",font=("Inter", 16 * -1))
    
    canvas.create_text(288.0,185.0,anchor="nw",text=nama,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(288.0,264.0,anchor="nw",text=motor.jenis,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(664.0,303.0,anchor="nw",text=motor.harga,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(664.0,341.0,anchor="nw",text=lamaPeminjaman,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(664.0,384.0,anchor="nw",text=lamaPeminjaman*motor.harga,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(244.0,309.0,anchor="nw",text="Lama Peminjaman",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(288.0,335.0,anchor="nw",text=lamaPeminjaman,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_text(244.0,380.0,anchor="nw",text="Kota Tujuan",fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(288.0,406.0,anchor="nw",text=kotaTujuan,fill="#AEAEAE",font=("Inter", 16 * -1))

    canvas.create_rectangle(494.0,240.0,497.0,540.0,fill="#FFFFFF",outline="")

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=metodePembayaran,relief="flat")
    button_1.place(x=572.0,y=441.0,width=146.0,height=35.0)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(691.0,198.0,image=image_image_2)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=detailTransaksi,relief="flat")
    button_3.place(x=99.0,y=602.0,width=128.0,height=99.0)
    window.resizable(False, False)
    window.mainloop()



def metodePembayaran () : 
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame8") / Path(path)
    
    def handleMetodePembayaran (x) : 
        global metodePembayaran ; 
        metodePembayaran = x
        notaPembayaran()
     
    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    canvas.create_text(362.0,84.0,anchor="nw",text="Pilih Metode Pembayaran", fill="#FFFFFF",font=("Inter", 24 * -1))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: handleMetodePembayaran('Ovo'),relief="flat")
    button_1.place(x=244.0, y=388.0, width=535.0,height=99.0)

    button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
    button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: handleMetodePembayaran('ATM'), relief="flat" )
    button_2.place(  x=244.0,y=274.0, width=535.0, height=99.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button( image=button_image_3,borderwidth=0, highlightthickness=0,command=lambda: handleMetodePembayaran('Gopay'), relief="flat")
    button_3.place(x=244.0, y=504.0,width=535.0, height=99.0 )

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4, borderwidth=0,highlightthickness=0,command=lambda: handleMetodePembayaran('Mobile-Banking'),relief="flat")
    button_4.place( x=244.0,y=160.0,width=535.0, height=99.0)
    window.resizable(False, False)
    window.mainloop()
    


   
def notaPembayaran () : 
    
    totalHarga = motor.harga*lamaPeminjaman
    global user , nama ,usia ,noHp , domisili , noKtp , kotaTujuan , noSim , metodePembayaran
    user = User(nama , usia , noHp , domisili , noKtp , kotaTujuan , totalHarga , noSim , metodePembayaran)
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame6") / Path(path)
    canvas = Canvas(window,bg = "#202133",height = 768,width = 1024,bd = 0,highlightthickness = 0,relief = "ridge")

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image( 512.0, 331.0,  image=image_image_1)

    canvas.create_text(399.0,  79.0, anchor="nw",text="NOTA TRANSAKSI", fill="#FFFFFF",font=("Inter", 24 * -1))

    canvas.create_text(244.0, 159.0, anchor="nw",text="Nama", fill="#FFFFFF", font=("Inter", 16 * -1))

    canvas.create_text(288.0,185.0, anchor="nw", text=user.namaLengkap, fill="#AEAEAE", font=("Inter", 16 * -1))

    canvas.create_text(244.0, 238.0, anchor="nw", text="Jenis Motor", fill="#FFFFFF", font=("Inter", 16 * -1) )

    canvas.create_text( 509.0,159.0,anchor="nw", text="Biaya Sewa / Jam", fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(  509.0, 197.0,anchor="nw",text="Lama Peminjaman", fill="#FFFFFF",font=("Inter", 16 * -1) )

    canvas.create_text( 509.0, 240.0, anchor="nw",text="Total Biaya ", fill="#FFFFFF",   font=("Inter", 16 * -1) )

    canvas.create_text(  509.0,  279.0, anchor="nw",text="Pembayaran", fill="#FFFFFF",font=("Inter", 16 * -1) )

    canvas.create_text( 509.0, 314.0, anchor="nw", text="Tanggal Pembayaran",fill="#FFFFFF", font=("Inter", 16 * -1) )

    canvas.create_text( 512.0, 365.0, anchor="nw",text="Jam\nPembayaran", fill="#FFFFFF", font=("Inter", 16 * -1) )

    canvas.create_text( 512.0, 410.0, anchor="nw", text="Status", fill="#FFFFFF",font=("Inter", 16 * -1))

    canvas.create_text(288.0, 264.0, anchor="nw", text=motor.jenis,fill="#AEAEAE", font=("Inter", 16 * -1))

    canvas.create_text(  669.0,  159.0, anchor="nw", text="Rp"+str(motor.harga), fill="#AEAEAE", font=("Inter", 16 * -1) )

    canvas.create_text(679.0,  197.0, anchor="nw",  text=str(lamaPeminjaman)+"Jam", fill="#AEAEAE", font=("Inter", 16 * -1) )

    canvas.create_text( 661.0, 240.0, anchor="nw",  text="Rp"+str(user.totalHarga), fill="#AEAEAE",  font=("Inter", 16 * -1))

    canvas.create_text( 658.0,324.0,  anchor="nw", text="15 / 05 / 2023", fill="#AEAEAE",  font=("Inter", 16 * -1))

    canvas.create_text( 685.0, 371.0, anchor="nw", text="18.00", fill="#AEAEAE", font=("Inter", 16 * -1) )

    canvas.create_text( 646.0, 410.0,  anchor="nw",  text="SUDAH DIBAYAR",   fill="#AEAEAE",    font=("Inter", 16 * -1))

    canvas.create_text( 688.0,    279.0,   anchor="nw",   text=user.motodePembayaran,   fill="#AEAEAE",   font=("Inter", 16 * -1) )

    canvas.create_text( 244.0, 309.0,  anchor="nw",  text="Lama Peminjaman",  fill="#FFFFFF", font=("Inter", 16 * -1)  )

    canvas.create_text( 288.0,  335.0,    anchor="nw", text=str(lamaPeminjaman)+"Jam",  fill="#AEAEAE",  font=("Inter", 16 * -1))

    canvas.create_text( 244.0, 380.0,     anchor="nw",   text="Kota Tujuan",  fill="#FFFFFF",    font=("Inter", 16 * -1) )

    canvas.create_text(  288.0,  406.0, anchor="nw",        text=user.tujuan,        fill="#AEAEAE",        font=("Inter", 16 * -1)    )

    canvas.create_rectangle(        427.0,        122.0,        430.0,        422.0,        fill="#FFFFFF",        outline="")

    image_image_2 = PhotoImage(        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(       984.0,       722.0,        image=image_image_2    )

    button_image_1 = PhotoImage(        file=relative_to_assets("button_1.png"))
    button_1 = Button(       image=button_image_1,        borderwidth=0,        highlightthickness=0,        command=homePage,        relief="flat"    )
    button_1.place( x=439.0,  y=470.0,width=146.0,  height=35.0
    )
    window.resizable(False, False)
    window.mainloop()
homePage()