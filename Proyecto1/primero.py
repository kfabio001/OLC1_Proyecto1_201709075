from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path
from lista_T import lista_T
    
 

class Ejemplo2:
    #lista = []
    texto=""
   # palabra=""
    def __init__(self, window):
        self.ventana = window
        self.ventana.title("Ejemplo 2")

        frame = LabelFrame(self.ventana, text = '')
        frame.grid(row=0,column=0,columnspan=20,pady=20)

        #############################################_MENU_#############################################
        self.nuevo = Button(frame, text ="Nuevo", command = self.fileMenu)
        self.nuevo.grid(row=0,column=0)

        self.guardar = Button(frame, text ="Guardar")
        self.guardar.grid(row=0,column=1)

        self.guardarComo = Button(frame, text ="Guardar Como")
        self.guardarComo.grid(row=0,column=2)

        self.cargar = Button(frame, text ="Cargar", command = self.fileMenu)
        self.cargar.grid(row=0,column=3)

        self.ejecutar = Button(frame, text ="Ejecutar")#, command = self.analizarScript)
        self.ejecutar.grid(row=0,column=4)

        self.salir = Button(frame, text ="Salir", command = self.terminar)
        self.salir.grid(row=0,column=5)

        ############################################_ENTRADA_############################################
        Label(frame,text='Archivo de Entrada:').grid(row=3,column=5)
        self.entrada = Text(frame, height=30, width=60)
        self.entrada.grid(row=4,column=5)

        Label(frame,text='   =>   ').grid(row=4,column=15)

        Label(frame,text='Resultado:').grid(row=3,column=16)
        self.salida = Text(frame, height=30, width=60)
        self.salida.grid(row=4,column=16)

        Label(frame,text='              ').grid(row=3,column=20)
    #END

    

    def fileMenu(self):
        global texto
        filename = askopenfilename()
        
        archivo = open(filename,"r")
        nombre, extension = os.path.splitext(archivo.name)
        
        texto = archivo.read()
        archivo.close()
        
        self.entrada.insert(INSERT,texto)
        if extension == '.js' :
            print("la extension    "+extension) 
            self.analizarScript()
        elif extension == '.html':
            print("la extension  htmal  "+extension)
            self.analizarHTML()
        elif extension == '.css':
            print("la extension  css  "+extension)
            self.analizarCSS()
        return
    #END
    def analizarHTML(self):
        global texto
        palabra =""
        espacio="\n"
        multi1=False
        multi2=False
        multi3=False
        unaLinea=False
        letra=True
        entreD=False
        entreA=False
        todoC=False
        todoA=False
        
        text = self.entrada.get("1.0",END)

        token=list(texto)

        for i_lexema in token:
            lexema=str(i_lexema)

            if letra==False:
                palabra=""
            if lexema=="'":   #var string = “4”   var char = ‘a’
                if todoA==True:
                    todoA=False
                    palabra=palabra+lexema
                    self.reservadas(palabra)
                    palabra=""
                    lexema=""
                else:

                    palabra=palabra+lexema
                    lexema=""
                    todoA=True
            elif lexema=='"':# or lexema=="“" or lexema=="”":
                if todoC==True:
                    todoC=False
                    palabra=palabra+lexema
                    self.reservadas(palabra)
                    palabra=""
                    lexema=""
                else:

                    palabra=palabra+lexema
                    lexema=""
                    todoC=True
            elif todoA==True :
                palabra= palabra+lexema
            elif todoC==True:
                palabra= palabra+lexema
            elif lexema == espacio:

                if unaLinea==True:
                    palabra=""
                    letra=True
                    entreD=False
                    multi1=False
                    multi2=False
                    unaLinea=False
                if lexema != "" and letra==True:
                    self.reservadas(palabra)
                else: 
                    palabra=""
                entreD=False
                
                palabra=""
            elif  lexema == " ":

                if lexema != "" and letra==True:

                    self.reservadas(palabra)
                else: 
                    palabra=""

                palabra=""
                entreD=False
            elif lexema.isalpha():

                palabra= palabra+lexema

                entreD=False
                entreA=False
                
            elif lexema.isdigit():

                palabra=palabra+lexema
                entreA=False
                entreD=False

            elif lexema=="{":
                self.reservadas(palabra)
                palabra=""
                lexema=""

            elif lexema=="}":
                self.reservadas(palabra)
                palabra=""
                lexema=" "

            elif lexema=="=":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="“":
                self.reservadas(palabra)
                palabra=""
                lexema=" "

            elif lexema=="”":
                self.reservadas(palabra)
                palabra=""
                lexema=" "

            elif lexema=="‘":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="’":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==";":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==">":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="<":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="(":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==")":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==".":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="_":
                #self.reservadas(palabra)
                palabra= palabra+lexema
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==",":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="!":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            
            elif lexema=="+":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="-":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="\\":
                lexema=" "
               # palabra=palabra+lexema
            elif lexema=="*":

                if  multi1==True and multi2==True  and letra==False:# and entreD==False:#en medio
                    entreA=True
                    multi2=True
                elif multi1==True and multi2==False and entreD==True:#inicio
                    multi2=True
                    multi3=True
                    letra=False
                
                lexema=""
               # palabra=palabra+lexema
            elif lexema=="/":
                
                if multi1==True and entreD==False and entreA==False and multi3==True:#  hjk / cffc * hhj
                    multi2=True
                elif multi1==True and entreD==False and multi3==False:
                    multi1=False
                   # letra=False
                if multi1==True and multi2==True and entreA==True:#  /*khgk*/  cerrar multi
                    multi1=False
                    multi2=False
                    multi3=False
                    letra=True
                
                elif multi1==False and multi2==False:# /
                    multi1=True
                    entreD=True
                    
                elif multi1==True and entreD==True and multi2==False:#// una linea
                    letra=False
                    unaLinea=True
                    #palabra=palabra+lexema
                lexema=""
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==":":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            else: 
                if letra==False:
                    lexema=""
                else:
                    print(lexema+" lexema no encontrado")

        self.printSalida()
    #END

    def analizarCSS(self):
        global texto
        palabra =""
        pat=""
        espacio="\n"
        multi1=False
        multi2=False
        multi3=False
        unaLinea=False
        letra=True
        entreD=False
        entreA=False
        todoC=False
        todoA=False
        num=False
        asig=False
        hexa=False
        
        text = self.entrada.get("1.0",END)
        token=list(text)

        for i_lexema in token:
            lexema=str(i_lexema)
            #print(token)
            if letra==False:
                palabra=""
            
            if lexema=='"' or lexema=="“" or lexema=="”":
                if todoC==True:
                    todoC=False
                    palabra=palabra+lexema
                    self.reservadasCSS(palabra)
                    palabra=""
                    lexema=""
                else:
                    palabra=palabra+lexema
                    lexema=""
                    todoC=True
            elif todoA==True :
                palabra= palabra+lexema
            elif todoC==True:
                palabra= palabra+lexema
            elif lexema == espacio:

                
                if lexema != "" and letra==True:

                    self.reservadasCSS(palabra)

                else: 
                    palabra=""
                entreD=False
                
                palabra=""
            elif  lexema == " ":

                if lexema != "" and letra==True:

                    self.reservadasCSS(palabra)
                else: 
                    palabra=""
                palabra=""
                entreD=False
            elif lexema.isalpha():
                #if asig==True:
                if hexa==True and asig==True:
                    palabra=palabra+lexema
                elif num==True and asig==True:
                    self.reservadasCSS(palabra)
                    palabra=""
                    palabra=palabra+lexema
                    num=False
                    #else:
                        #palabra= palabra+lexema
                else:
                    palabra= palabra+lexema
                    entreD=False
                    entreA=False
                
            elif lexema.isdigit():
                if hexa==True and asig==True:
                    palabra=palabra+lexema
                else:
                    palabra=palabra+lexema
                    num=True
                    entreA=False
                    entreD=False
            elif lexema=="{":
                self.reservadasCSS(palabra)
                palabra=""
                lexema=""
            elif lexema=="}":
                
                self.reservadasCSS(palabra)
                asig=False
                hexa=False
                palabra=""
                lexema=" "

            elif lexema==";":
                self.reservadasCSS(palabra)
                asig=False
                hexa=False
                palabra=""
                lexema=" "

            elif lexema=="(":
                self.reservadasCSS(palabra)
                palabra=""
                lexema=" "
            elif lexema==")":
                self.reservadasCSS(palabra)
                palabra=""
                lexema=" "
            elif lexema==".":
                if num==True:
                    palabra=palabra+lexema
                else:
                    self.reservadasCSS(palabra)
                    palabra=""
                lexema=" "
            elif lexema=="_":
               # self.reservadasCSS(palabra)
                palabra= palabra+lexema
                lexema=" "
            elif lexema==",":
                self.reservadasCSS(palabra)
                palabra=""
                lexema=" "
            elif lexema=="#":
                hexa=True
                self.reservadasCSS(palabra)
                palabra=""
                lexema=" "
            
            elif lexema=="%":
                self.reservadasCSS(palabra)
                palabra=""
                lexema=" "
            elif lexema=="-":
                
                palabra= palabra+lexema
               # self.reservadasCSS(palabra)
                lexema=" "

            elif lexema=="\\":
                lexema=" "
            elif lexema=="*":
                if  multi1==True and multi2==True  and letra==False:# and entreD==False:#en medio
                    entreA=True
                    multi2=True
                    print("C*")
                elif multi1==True and multi2==False and entreD==True:#inicio
                    print("*")
                    multi2=True
                    multi3=True
                    letra=False
                lexema=""
            elif lexema=="/":
                if multi1==True and entreD==False and entreA==False and multi3==True:#  hjk / cffc * hhj
                    multi2=True
                elif multi1==True and entreD==False and multi3==False:
                    multi1=False
                if multi1==True and multi2==True and entreA==True:#  /*khgk*/  cerrar multi
                    multi1=False
                    multi2=False
                    multi3=False
                    letra=True
                    print("C/")
                elif multi1==False and multi2==False:# /
                    print("/")
                    multi1=True
                    entreD=True
                elif multi1==True and entreD==True and multi2==False:#// una linea
                    letra=False
                    unaLinea=True
                lexema=""
            elif lexema==":":
                self.reservadasCSS(palabra)
                asig=True
                palabra=""
                lexema=" "
            else: 
                if letra==False:
                    lexema=""
                else:
                    print(lexema+" lexema no encontrado")

        self.printSalida()
    #END

    
    def analizarScript(self):
        global texto
        palabra =""
        pat=""
        espacio="\n"
        multi1=False
        multi2=False
        multi3=False
        unaLinea=False
        letra=True
        entreD=False
        entreA=False
        todoC=False
        todoA=False
        
        text = self.entrada.get("1.0",END)
        #print("analizando: "+texto)
        token=list(texto)
        separado = text.split()
        #tupla=[separado]
       # print(token)
        for i_lexema in token:
            lexema=str(i_lexema)
            #cadena="".join(str(_) for _ in token)
          #  print(lexema)
            if letra==False:
                palabra=""
            if lexema=="'":   #var string = “4”   var char = ‘a’
                if todoA==True:
                    todoA=False
                    palabra=palabra+lexema
                    self.reservadas(palabra)
                    palabra=""
                    lexema=""
                else:
                #palabra=""
                    palabra=palabra+lexema
                    lexema=""
                    todoA=True
            elif lexema=='"':# or lexema=="“" or lexema=="”":
                if todoC==True:
                    todoC=False
                    palabra=palabra+lexema
                    self.reservadas(palabra)
                    palabra=""
                    lexema=""
                else:
                #palabra=""
                    palabra=palabra+lexema
                    lexema=""
                    todoC=True
            elif todoA==True :
                palabra= palabra+lexema
            elif todoC==True:
                palabra= palabra+lexema
            elif lexema == espacio:
                
                #if multi1==True and entreD==False:#
                    #multi1=False
               # print(palabra)
                #self.salida.insert(INSERT,palabra+" ")
                if unaLinea==True:
                    palabra=""
                    letra=True
                    entreD=False
                    multi1=False
                    multi2=False
                    unaLinea=False
                if lexema != "" and letra==True:
                   # palabra="self."+palabra+"i()"
                   # self.switch_demo(palabra)
                    self.reservadas(palabra)
                    #print(palabra)
                else: 
                    palabra=""
                entreD=False
                
                palabra=""
            elif  lexema == " ":
                #if multi1==True:
                   # multi1=False
                # print(palabra)
               # self.salida.insert(INSERT,palabra+" ")
                if lexema != "" and letra==True:
                   # palabra="self."+palabra+"i()"
                    #self.switch_demo(palabra)
                    self.reservadas(palabra)
                else: 
                    palabra=""
                #print(palabra)
                palabra=""
                entreD=False
            elif lexema.isalpha():
                #print("add "+lexema)
                palabra= palabra+lexema
                #self.salida.insert(INSERT,palabra)
                entreD=False
                entreA=False
                
            elif lexema.isdigit():
               # print("digit " +lexema)
                palabra=palabra+lexema
                entreA=False
                entreD=False
                #self.salida.insert(INSERT,palabra)
            elif lexema=="{":
                self.reservadas(palabra)
                palabra=""
                lexema=""
                #palabra=palabra+lexema
            elif lexema=="}":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
                #palabra=palabra+lexema
            elif lexema=="=":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
                #palabra=palabra+lexema
            elif lexema=="“":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema=="”":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema=="‘":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="’":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==";":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==">":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="<":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="(":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==")":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==".":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="_":
                #self.reservadas(palabra)
                palabra= palabra+lexema
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==",":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="!":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            
            elif lexema=="+":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="-":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="\\":
                lexema=" "
               # palabra=palabra+lexema
            elif lexema=="*":

                if  multi1==True and multi2==True  and letra==False:# and entreD==False:#en medio
                    entreA=True
                    multi2=True
                elif multi1==True and multi2==False and entreD==True:#inicio
                    multi2=True
                    multi3=True
                    letra=False
                
                lexema=""
               # palabra=palabra+lexema
            elif lexema=="/":
                
                if multi1==True and entreD==False and entreA==False and multi3==True:#  hjk / cffc * hhj
                    multi2=True
                elif multi1==True and entreD==False and multi3==False:
                    multi1=False
                   # letra=False
                if multi1==True and multi2==True and entreA==True:#  /*khgk*/  cerrar multi
                    multi1=False
                    multi2=False
                    multi3=False
                    letra=True
                
                elif multi1==False and multi2==False:# /
                    multi1=True
                    entreD=True
                    
                elif multi1==True and entreD==True and multi2==False:#// una linea
                    letra=False
                    unaLinea=True
                    #palabra=palabra+lexema
                lexema=""
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==":":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            else: 
                if letra==False:
                    lexema=""
                else:
                    print(lexema+" lexema no encontrado")

        self.printSalida()
    #END
    def reservadas(self, reservada):
        if reservada=="":
            reservada=""
        elif reservada=='int':
            print ("int")
        elif reservada=='string':
            print ("string")
        elif reservada=='char':
            print ("char")
        elif reservada=='boolean':
            print ("boolean")
        elif reservada=='var':
            print ("var")
        elif reservada=='if':
            print ("if")
        elif reservada=='else':
            print ("else")
        elif reservada=='for':
            print ("for")
        elif reservada=='while':
            print ("while")
        elif reservada=='do':
            print ("do")
        elif reservada=='continue':
            print ("continue")
        elif reservada=='break':
            print ("break")
        elif reservada=='return':
            print ("return")
        elif reservada=='function':
            print ("function")
        elif reservada=='constructor':
            print ("constructor")
        elif reservada=='class':
            print ("class")
        elif reservada=='math':
            print ("math")
        elif reservada=='pow':
            print ("pow")
        elif reservada=='true':
            print ("true")
        elif reservada=='false':
            print ("false")
        elif reservada=='pathl':
            print ("pathl")
        elif reservada=='pathw':
            print ("pathw")
        else:
            print("id "+reservada)
            
    def reservadasCSS(self, reservada):
        if reservada=="":
            reservada=""
        elif reservada=='color':
            print ("color")
        elif reservada=='border':
            print ("border")
        elif reservada=='text-align':
            print ("text-align")
        elif reservada=='font-weight':
            print ("font-weight")
        elif reservada=='padding-left':
            print ("padding-left")
        elif reservada=='padding-top':
            print ("padding-top")
        elif reservada=='line-height':
            print ("line.height")
        elif reservada=='margin-top':
            print ("margin-top")
        elif reservada=='margin-left':
            print ("margin-left")
        elif reservada=='display':
            print ("display")
        elif reservada=='top':
            print ("top")
        elif reservada=='float':
            print ("float")
        elif reservada=='min-width':
            print ("min-width")
        elif reservada=='background-color':
            print ("background-color")
        elif reservada=='opacity':
            print ("opacity")
        elif reservada=='font-family':
            print ("font-family")
        elif reservada=='font-size':
            print ("font-size")
        elif reservada=='padding-right':
            print ("padding-right")
        elif reservada=='padding':
            print ("padding")
        elif reservada=='width':
            print ("width")
        elif reservada=='margin-right':
            print ("margin-right")
        elif reservada=='margin':
            print ("margin")
        elif reservada=='position':
            print ("position")
        elif reservada=='right':
            print ("right")
        elif reservada=='clear':
            print ("clear")
        elif reservada=='max-height':
            print ("max-height")
        elif reservada=='background-image':
            print ("background-image")
        elif reservada=='background':
            print ("background")
        elif reservada=='font-style':
            print ("font-style")
        elif reservada=='font':
            print ("font")
        elif reservada=='padding-bottom':
            print ("padding-bottom")
        elif reservada=='display':
            print ("display")
        elif reservada=='height':
            print ("height")
        elif reservada=='margin-bottom':
            print ("margin-bottom")
        elif reservada=='left':
            print ("left")
        elif reservada=='max-width':
            print ("max-width")
        elif reservada=='min-height':
            print ("min-height")
        elif reservada=='px':
            print ("px")
        elif reservada=='em':
            print ("em")
        elif reservada=='vh':
            print ("vh")
        elif reservada=='vw':
            print ("vw")
        elif reservada=='in':
            print ("in")
        elif reservada=='cm':
            print ("cm")
        elif reservada=='mm':
            print ("mm")
        elif reservada=='pt':
            print ("pt")
        elif reservada=='pc':
            print ("pc")
        elif reservada=='rem':
            print ("rem")
        else:
            print("id "+reservada)

    def printSalida(self):
        texto = "Finalizo el analisis"
        self.salida.insert(INSERT,texto)

        messagebox.showerror("Error", "Texto a mostrar:\n")
    #END

    def terminar(self):
        
        self.ventana.destroy()
        return
    #END
    
        
###################################################################################################
if __name__ == '__main__':
    window = Tk()
    app = Ejemplo2(window)
    window.mainloop()