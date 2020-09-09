from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import messagebox
from graphviz import Digraph
import os.path
import os
from lista_T import lista_T

    
 

class Ejemplo2:
    archivos=""
    texto=""
    cadena=""
    cadenas=""
    contVar=0
    ID=0
    noComentario=0
    noCadena=0
    nombre=""
    nombres=""
    extension=""
    estados=1
    rees=""
    patsi=""
    errores=""
    
    def __init__(self, window):
        global cadena
        global rees
        global patsi
        global nombre
        global nombres
        global extension
        global errores
        errores=""
        nombre=""
        nombres=""
        extension=""
        patsi="W/"
        rees=""
        cadena=""
        self.ventana = window
        self.ventana.title("Ejemplo 2")

        frame = LabelFrame(self.ventana, text = '')
        frame.grid(row=0,column=0,columnspan=20,pady=20)

        #############################################_MENU_#############################################
        self.nuevo = Button(frame, text ="Nuevo", command = self.nuevof)
        self.nuevo.grid(row=0,column=0)

        self.guardar = Button(frame, text ="Guardar", command=self.guardarArchivo)
        self.guardar.grid(row=0,column=1)

        self.guardarComo = Button(frame, text ="Guardar Como", command=self.guardarComof)
        self.guardarComo.grid(row=0,column=2)

        self.cargar = Button(frame, text ="Cargar", command = self.fileMenu)
        self.cargar.grid(row=0,column=3)
        completo=nombre+extension
        self.ejecutar = Button(frame, text ="Ejecutar", command =self.crear)#, command=self.expreionJS(cadena))
        self.ejecutar.grid(row=0,column=4)

        self.salir = Button(frame, text ="Salir", command = self.terminar)
        self.salir.grid(row=0,column=5)

        ############################################_ENTRADA_############################################
        Label(frame,text='Archivo de Entrada:').grid(row=3,column=5)
        self.entrada = Text(frame, height=25, width=60)
        self.entrada.grid(row=4,column=5)

        Label(frame,text='   =>   ').grid(row=4,column=15)

        Label(frame,text='Resultado:').grid(row=3,column=16)
        self.salida = Text(frame, height=20, width=60)
        self.salida.grid(row=4,column=16)

        self.cad = Text(frame, height=10, width=60)
        self.cad.grid(row=5,column=16)


        Label(frame,text='              ').grid(row=3,column=20)
    #END

    def nuevof(self):
        global archivos
        self.entrada.delete(1.0, END)#ELIMINAR EL CONTENIDO
        self.salida.delete('1.0', END)
        self.cad.delete('1.0', END)
        archivos = ""


    def guardarArchivo(self):
        global archivos
        if archivos == "":
            self.guardarComof()
        else:
            guardarc = open(archivos, "w")
            guardarc.write(self.entrada.get(1.0, END))
            guardarc.close()

    def guardarComof(self):
        global archivos
        guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
        fguardar = open(guardar, "w+")
        fguardar.write(self.entrada.get(1.0, END))
        fguardar.close()
        archivos = guardar 

    def fileMenu(self):
        global texto
        global archivos
        global nombre
        global extension
        global nombres
        filename = askopenfilename()
        
        archivo = open(filename,"r")
        nombres, extension = os.path.splitext(archivo.name)
        ruta, nombre=os.path.split(archivo.name)
        texto = archivo.read()
        archivo.close()
        self.entrada.delete('1.0', END)
        self.salida.delete('1.0', END)
        self.cad.delete('1.0', END)
        self.entrada.insert(INSERT,texto)
        if extension == '.js' :
            print("la extension    "+extension) 
            self.analizarScript()
        elif extension == '.html':
            print("la extension  htmal  "+extension+"el nombre"+nombre)
            
            self.analizarHTML()
        elif extension == '.css':
            print("la extension  css  "+extension)
            self.analizarCSS()
        elif extension == '.rmt':
            print("la extension  rmt  "+extension)
            self.analizarRMT()
        return
    #END
    def analizarRMT(self):
        pila=list()
        pala=False
        palabra=""
        text = self.entrada.get("1.0",END)
        #separado=str(text)
        #linea=separado.split('\n')
        
        noParentesis=0
        noParentesisC=0
        token=list(text)
        #for lin in linea:
            #token=list(lin)
            
            #print(token)
        for i_lexema in token:
            lexema=str(i_lexema)
            #print(lexema)
            if lexema=="(":
                pila.append(lexema)
                noParentesis=noParentesis+1
                self.cad.insert(INSERT,lexema)
                pala=False
            elif lexema==")":
                noParentesisC=noParentesisC+1
                self.cad.insert(INSERT,lexema)
                try:
                    pila.pop()
                
                except:
                    self.cad.insert(INSERT," Inorrecto")
                    #raise ValueError("La pila está vacía")
                    
                
                pala=False
            elif lexema=="*":
                self.cad.insert(INSERT,lexema)
                pala=False
            elif lexema=="-":
                self.cad.insert(INSERT,lexema)
                pala=False
            elif lexema=="+":
                self.cad.insert(INSERT,lexema)
                pala=False
            elif lexema=="/":
                self.cad.insert(INSERT,lexema)
                pala=False
            elif lexema=='\n':
                if noParentesisC==noParentesis:
                    self.cad.insert(INSERT," Correcto")
                if pila==[]:
                    print("aver")
                else:
                    self.cad.insert(INSERT," Inorrecto")
                self.cad.insert(INSERT,lexema)
                noParentesis=0
                noParentesisC=0
            elif lexema.isalpha():
                pala=True
                palabra=palabra+lexema
                self.cad.insert(INSERT,lexema)
            elif lexema.isdigit():
                self.cad.insert(INSERT,lexema)
            elif lexema==" ":
                self.cad.insert(INSERT,lexema)
            else:
                self.cad.insert(INSERT,lexema)
                self.cad.insert(INSERT," no reconocido")
            

    #END
    def analizarHTML(self):
        global texto
        global cadena
        global patsi
        global errores
        noErrores=0
        linea=1
        columna=1
        palabra =""
        espacio="\n"
        multi1=False
        multi2=False
        letra=True
        entreD=False
        unaLinea=False
        noLinea=0
        pat=""
        pats=""
        patsi=""
        pathw=False
        todoC=False
        todoA=False
        todoM=False
        diago=False
        dia=False
        abre=False
        
        
        text = self.entrada.get("1.0",END)

        token=list(text)

        for i_lexema in token:
            lexema=str(i_lexema)
            columna=columna+1

            if letra==False:
                #self.reescribir(lexema)
                palabra=""
            if unaLinea==True:
                
                if lexema=="-" or lexema==">" or lexema=="/":
                        lexema=" "
                if noLinea==0 or noLinea==1 :
                    pat=pat+lexema
                    print(pat)
                    #lexema=" "
                    if lexema=='\n' and pathw==False:
                        print(pat)
                        pat=""
                        #lexema=" "
                        
                    if pat=="PATHW":
                        
                        pathw=True
                        pat=""
                        lexema=" "
                    if lexema!='\n' and pathw ==True and(lexema=='\\'or lexema.isalpha() or lexema!=" "):
                        patsi=patsi+lexema
                        lexema=""
                    else:
                        if pathw==True:
                            print(patsi)
                            try:
                                os.makedirs(patsi)
                            except OSError:
                                print("La creación del directorio %s falló" % patsi)
                            else:
                                print("Se ha creado el directorio: %s " % patsi)
                                pathw=False
                                unaLinea=False
            
            
            if todoM==True and lexema!="<":
                self.reescribir(lexema)
                palabra=""
            if lexema==espacio:
                linea=linea+1
                unaLinea=False
                dia=False
                pathw=False
                noLinea=noLinea+1
                #print("linea"+str(noLinea))
                columna=0
                #self.reescribir(lexema)
            if lexema=="'":
                self.reescribir(lexema)
                if todoA==True:
                    todoA=False
                    palabra=palabra+lexema
                    self.reservadasHTML(palabra)
                    
                    palabra=""
                    #columna=columna+1
                    lexema=""
                else:

                    palabra=palabra+lexema
                    lexema=""
                    todoA=True
            elif lexema=="":
                lexema=""
            elif lexema=='"':
                self.reescribir(lexema)
                if todoC==True:
                    todoC=False
                    palabra=palabra+lexema
                    self.reservadasHTML(palabra)
                    palabra=""
                    lexema=""
                else:
                    palabra=palabra+lexema
                    lexema=""
                    todoC=True
            elif lexema=="<":
                self.reescribir(lexema)
                abre=True
                todoM=False
                if diago==True:
                    diago==False
                palabra=""
                lexema=" "
              
            elif lexema==">":
                self.reescribir(lexema)
                abre=False
                todoM=True
                self.reservadasHTML(palabra)
                palabra=""
                lexema=" "
             
            elif todoA==True :
                self.reescribir(lexema)
                palabra= palabra+lexema
            elif todoC==True:
                self.reescribir(lexema)
                palabra= palabra+lexema
            elif todoM==True:
            
                lexema=""
            elif lexema == espacio:
                #print(lexema)
                columna=1
                linea=linea+1
                unaLinea==False
                dia=False
                pathw=False
                if lexema != "" and letra==True:
                    
                    self.reservadasHTML(palabra)
                else: 
                    palabra=""
                entreD=False
                linea=linea+1
                #print(linea)
                palabra=""
            elif  lexema == " ":
                if noLinea!=0 and noLinea!=1:
                    self.reescribir(lexema)
                if lexema != "" and letra==True:

                    self.reservadasHTML(palabra)
                else: 
                    palabra=""
                
                palabra=""
                entreD=False
            elif lexema.isalpha():
                if unaLinea==False:
                    self.reescribir(lexema)
                    dia=False
                if abre==True:
                    palabra= palabra+lexema
                

                
            elif lexema.isdigit():
                self.reescribir(lexema)
                dia=False
                if abre==True:
                    palabra=palabra+lexema
            
            elif lexema=="=":
                self.reservadasHTML(palabra)
                self.reescribir(lexema)
                palabra=""
                lexema=" "
            elif lexema=="“":
                self.reservadasHTML(palabra)
              #  self.reescribir(lexema)
                palabra=""
                lexema=" "

            elif lexema=="”":
                self.reservadasHTML(palabra)
               # self.reescribir(lexema)
                palabra=""
                lexema=" "

            elif lexema=="‘":
                self.reservadasHTML(palabra)
               # self.reescribir(lexema)
                palabra=""
                lexema=" "
             
            elif lexema=="’":
                self.reservadasHTML(palabra)
               # self.reescribir(lexema)
                palabra=""
                lexema=" "
              

            
            
           # elif lexema=="\\":
                #self.reescribir(lexema)
               # lexema=" "
            
          #  elif lexema=="*":
              #  self.reescribir(lexema)

              #  if  multi1==True and multi2==True  and letra==False:
               #     entreA=True
               #     multi2=True
               # elif multi1==True and multi2==False and entreD==True:
                  #  multi2=True
                  #  multi3=True
                 #   letra=False
                
               # lexema=""
            
            elif lexema=="/":
                if dia==False:# and unaLinea==False and dia==False:
                    dia=True
                    
                    #print("1")
                elif dia==True:
                    dia=False
                    unaLinea=True
                    #unaLinea=False
                    #print("2")
                    #noLinea=noLinea+1
                if noLinea!=0 and noLinea!=1:
                    self.reescribir(lexema)
                
                else:
                    #self.reescribir(lexema)
                    diago=True
                
                lexema=""
             
            
            
            else: 
                if letra==False:
                    lexema=""
                else:
                    tr="<tr>"
                    td="</td> <td>"
                    noErrores=noErrores+1
                    print(lexema+" lexema no encontrado "+linea.__str__()+" "+columna.__str__()+" ")
                    errores=errores+'\n'+tr+"<td>"+str(noErrores)+td+lexema+td+"Elemento lexico desconocido."+td+str(linea)+td+str(columna)+"</td> </tr>"
        

        self.printSalida()
    #END

    def analizarCSS(self):
        global texto
        global estados
        global patsi
        global errores
        noErrores=0
        estados=0
        palabra =""
        pat=""
        pats=""
        patsi=""
        pathw=False
        linea=1
        columna=1
        espacio="\n"
        multi1=False
        multi2=False
        multi3=False
        noLinea=0
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
            columna=columna+1
            
            if letra==False:
                palabra=""
                #lexema=""
            if multi3==True:
                if lexema=="-" or lexema==">" :
                        lexema=""
                if noLinea==1 or noLinea==2:
                    pat=pat+lexema
                    print(pat)
                    if lexema=="/" and pathw==False:
                        pat=""
                    elif pat=="PATHW":
                        pathw=True
                        pat=""
                        lexema=" "
                    if lexema==" ":
                        lexema=""
                    if lexema!='\n' and pathw ==True and lexema!="*" or lexema==":" and(lexema=='\\'or lexema.isalpha()):
                        patsi=patsi+lexema
                    else:
                        if pathw==True:
                            print(patsi)
                            try:
                                os.makedirs(patsi)
                            except OSError:
                                print("La creación del directorio %s falló" % patsi)
                            else:
                                print("Se ha creado el directorio: %s " % patsi)
                                pathw=False
            if lexema==espacio:
                linea=linea+1
                columna=0
            
            
            if lexema=='"' or lexema=="“" or lexema=="”":
                if letra==False:
                    lexema=""
                self.reescribir(lexema)
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
                self.reescribir(lexema)
                palabra= palabra+lexema
            elif todoC==True:
                self.reescribir(lexema)
                palabra= palabra+lexema
            elif lexema == espacio:
                self.reescribir(lexema)

                
                if lexema != "" and letra==True:
                    
                    self.reservadasCSS(palabra)

                else: 
                    palabra=""
                entreD=False
                
                palabra=""
            elif  lexema == " ":
                self.reescribir(lexema)
                if lexema != "" and letra==True:

                    self.reservadasCSS(palabra)
                else: 
                    palabra=""
                palabra=""
                entreD=False
            elif lexema.isalpha():
                
                if hexa==True and asig==True:
                    self.reescribir(lexema)
                    palabra=palabra+lexema
                elif num==True and asig==True:
                    self.reescribir(lexema)
                    self.reservadasCSS(palabra)
                    palabra=""
                    palabra=palabra+lexema
                    num=False
                    
                else:
                    palabra= palabra+lexema
                    if letra==True:
                        self.reescribir(lexema)
                        bitacora="Entro a s"+ str(estados)+ " con "+lexema +'\n'
                        self.cad.insert(INSERT,bitacora)
                        estados=estados+1
                    entreD=False
                    entreA=False
                
            elif lexema.isdigit():
                #self.reescribir(lexema)
                if hexa==True and asig==True:
                    self.reescribir(lexema)
                    palabra=palabra+lexema
                else:
                    palabra=palabra+lexema
                    num=True
                    entreA=False
                    entreD=False
                    if letra==True:
                        self.reescribir(lexema)
            elif lexema=="*":
                if  multi1==True and multi2==True  and letra==False:# and entreD==False:#en medio
                    entreA=True
                    multi2=True
                    pathw=False
                    print("C*")
                elif multi1==True and multi2==False and entreD==True:#inicio
                    print("*")
                    multi2=True
                    multi3=True
                    noLinea=noLinea+1
                    letra=False
                else:
                    self.reescribir(lexema)
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
            elif letra==False:
                lexema=""
            elif lexema=="{":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_llave_A "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=""
            elif lexema=="}":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_llave_C "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                asig=False
                hexa=False
                palabra=""
                lexema=" "

            elif lexema==";":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_puntoYcoma "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                asig=False
                hexa=False
                palabra=""
                lexema=" "

            elif lexema=="(":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_parentesisA "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema==")":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_parentesisC "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema==".":
                self.reescribir(lexema)
                if num==True:
                    palabra=palabra+lexema
                else:
                    self.reservadasCSS(palabra)
                    bitacora="Token Reconocido: "+" tK_punto "+lexema +'\n'
                    self.cad.insert(INSERT,bitacora)
                    estados=1
                    bitacora="Entro a s"+ str(estados-1)+'\n'
                    self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema=="_":
                self.reescribir(lexema)
                palabra= palabra+lexema
                bitacora="Entro a s"+ str(estados-1)+" con "+lexema+'\n'
                self.cad.insert(INSERT,bitacora)
                estados=estados+1
                lexema=" "
            elif lexema==",":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_coma "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema=="#":
                self.reescribir(lexema)
                hexa=True
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_numeral "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            
            elif lexema=="%":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_porcentaje "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema=="+":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_mas "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                palabra=""
                lexema=" "
            elif lexema=="-":
                self.reescribir(lexema)
                
                palabra= palabra+lexema
                bitacora="Entro a s"+ str(estados-1)+" con "+lexema+'\n'
                self.cad.insert(INSERT,bitacora)
                estados=estados+1
                lexema=" "

           # elif lexema=="\\":
               # self.reescribir(lexema)
              #  lexema=" "
            
            elif letra==False:
                lexema=""
                palabra=""
            elif lexema==":":
                self.reescribir(lexema)
                self.reservadasCSS(palabra)
                bitacora="Token Reconocido: "+" tK_dosPuntos "+lexema +'\n'
                self.cad.insert(INSERT,bitacora)
                estados=1
                bitacora="Entro a s"+ str(estados-1)+'\n'
                self.cad.insert(INSERT,bitacora)
                asig=True
                palabra=""
                lexema=" "
            else: 
                if letra==False:
                    lexema=""
                else:
                    bitacora="lexema no encontrado"+ " con "+lexema +'\n'
                    self.cad.insert(INSERT,bitacora)
                    estados=1
                    bitacora="Entro a s"+ str(estados-1)+'\n'
                    self.cad.insert(INSERT,bitacora)
                    #estados=estados+1
                    tr="<tr>"
                    td="</td> <td>"
                    noErrores=noErrores+1
                    print(lexema+" lexema no encontrado "+linea.__str__()+" "+columna.__str__()+" ")
                    errores=errores+'\n'+tr+"<td>"+str(noErrores)+td+lexema+td+"Elemento lexico desconocido."+td+str(linea)+td+str(columna)+"</td> </tr>"

        self.printSalida()
    #END
    def reescribir(self,letra):
        global rees
        rees=rees+letra
    #END
    def crear(self):
        global rees
        global nombre
        global extension
        global patsi
        completo=patsi+nombre
        print("crear"+completo)
        file = open(completo, "w")
        file.write(rees)
        file.close()
    #END
    def erroresHTML(self):
        global nombre
        global nombres
        global errores
        global patsi
        htmls="<html>"+"<head align=center>ERRORES</head>"+ "<body> <table border="+"2"+"width="+"850"+ "align=center>"+"<tr> <td>NO.</td> <td>ERROR</td> <td>DESCRIPCION</td>"+"<td>FILA</td> <td>COLUMNA</td> </tr>"
        htmlss="</table> </body> </html>"
        archivo=nombre#.split(".")
        archi=""+patsi+nombre+".html"
        print(archi)
        file = open(archi, "w")
        file.write(htmls)
        file.write(errores)
        file.write(htmlss)
        file.close()
    #END
    
    def analizarScript(self):
        global texto
        global cadena
        global cadenas
        global vari
        global contVar
        global ID
        global noComentario
        global noCadena
        global patsi
        global errores
        
        errores=""
        noErrores=0
        ID=0
        cadenas=""
        contVar=0
        noComentario=0
        noCadena=0
        palabra =""
        pat=""
        pats=""
        patsi=""
        pathw=False
        espacio="\n"
        multi1=False
        multi2=False
        multi3=False
        unaLinea=False
        noLinea=0
        letra=True
        entreD=False
        entreA=False
        todoC=False
        todoA=False
        linea=1
        columna=1
        
        
        text = self.entrada.get("1.0",END)
        vari=False
        token=list(text)
        separado = text.split()

        for i_lexema in token:
            lexema=str(i_lexema)
            columna=columna+1

            if letra==False:
                palabra=""
            if unaLinea==True:
                if lexema=="-" or lexema==">":
                        lexema=""
                if noLinea==1 or noLinea==2:
                    pat=pat+lexema
                    if lexema=='\n' and pathw==False:
                        pat=""
                    if pat=="PATHW":
                        pathw=True
                        pat=""
                        lexema=" "
                    if lexema!='\n' and pathw ==True and(lexema=='\\'or lexema.isalpha() or lexema!=" "):
                        patsi=patsi+lexema
                    else:
                        if pathw==True:
                            print(patsi)
                            try:
                                os.makedirs(patsi)
                            except OSError:
                                print("La creación del directorio %s falló" % patsi)
                            else:
                                print("Se ha creado el directorio: %s " % patsi)
                                pathw=False
                        
            if lexema==espacio:
                linea=linea+1
                columna=0
            if lexema=="'":
                self.reescribir(lexema)   #var string = “4”   var char = ‘a’
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
            elif lexema=='"':
                self.reescribir(lexema)# or lexema=="“" or lexema=="”":
                if todoC==True:
                    todoC=False
                    noCadena=noCadena+1
                    
                    if noCadena==1:
                        cadenas=cadenas+"TODO"
                        cadenas=cadenas+" "+lexema
                        print(cadenas+noCadena.__str__())
                        self.expreionJS(cadenas)
                        cadenas=""
                        
                    palabra=palabra+lexema
                    self.reservadas(palabra)
                    palabra=""
                    lexema=""
                else:
                #palabra=""
                    cadenas=cadenas+lexema+" "
                    palabra=palabra+lexema
                    lexema=""
                    
                    todoC=True
            elif todoA==True :
                self.reescribir(lexema)
                palabra= palabra+lexema
            elif todoC==True:
                self.reescribir(lexema)
                #if noCadena==0:
                    
                palabra= palabra+lexema
            elif lexema == espacio:
                self.reescribir(lexema)
                
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
                self.reescribir(lexema)
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
                self.reescribir(lexema)
                #print("add "+lexema)
                palabra= palabra+lexema
                #self.salida.insert(INSERT,palabra)
                entreD=False
                entreA=False
                
            elif lexema.isdigit():
                self.reescribir(lexema)
               # print("digit " +lexema)
                palabra=palabra+lexema
                entreA=False
                entreD=False
                #self.salida.insert(INSERT,palabra)
            elif lexema=="{":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=""
                #palabra=palabra+lexema
            elif lexema=="}":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
                #palabra=palabra+lexema
            elif lexema=="=":
                self.reescribir(lexema)
                if vari==True:
                    cadena=cadena+"= "
                    #self.cad.insert(INSERT,"= ")
                self.reservadas(palabra)
                palabra=""
                lexema=" "
                #palabra=palabra+lexema
            elif lexema=="“":
                self.reescribir(lexema)
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
                self.reescribir(lexema)
                if vari==True:
                    cadena=cadena+";"
                    print(cadena)
                    self.expreionJS(cadena)
                    cadena=""
                    vari=False
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==">":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="<":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="(":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==")":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==".":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="_":
                self.reescribir(lexema)
                #self.reservadas(palabra)
                palabra= palabra+lexema
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema==",":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="!":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            
            elif lexema=="+":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="-":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
              #  palabra=palabra+lexema
            elif lexema=="\\":
                self.reescribir(lexema)
                lexema=" "
               # palabra=palabra+lexema
            elif lexema=="*":
                self.reescribir(lexema)

                if  multi1==True and multi2==True  and letra==False:# and entreD==False:#en medio
                    entreA=True
                    multi2=True
                elif multi1==True and multi2==False and entreD==True:#inicio
                    multi2=True
                    multi3=True
                    letra=False
                    cadena=cadena+"* TODO "

                
                lexema=""
               # palabra=palabra+lexema
            elif lexema=="/":
                self.reescribir(lexema)
                
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
                    noComentario=noComentario+1
                    cadena=cadena+"* /"
                    print(cadena)
                    if noComentario==1:
                        print(cadena)
                        self.expreionJS(cadena)
                        cadena=""
                    else:
                        cadena=""
                
                elif multi1==False and multi2==False:# /
                    multi1=True
                    entreD=True
                    cadena=cadena+"/ "
                    
                elif multi1==True and entreD==True and multi2==False:#// una linea
                    letra=False
                    unaLinea=True
                    noLinea=noLinea+1
                    cadena=""
                    #palabra=palabra+lexema
                lexema=""
              #  palabra=palabra+lexema
            elif lexema=="&":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            elif lexema==":":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
               # palabra=palabra+lexema
            else: 
                if letra==False:
                    lexema=""
                elif lexema=="	" or lexema=="	":
                    print("")
                else:
                    tr="<tr>"
                    td="</td> <td>"
                    noErrores=noErrores+1
                    print(lexema+" lexema no encontrado "+linea.__str__()+" "+columna.__str__()+" ")
                    errores=errores+'\n'+tr+"<td>"+str(noErrores)+td+lexema+td+"Elemento lexico desconocido."+td+str(linea)+td+str(columna)+"</td> </tr>"
        self.printSalida()
    #END
    def expreionJS(self, expresion):
        global contVar
        separado=""
        lexL="L"
        lexD="D"
        lexS="S"
        dot = Digraph(comment='Grafo JavaScript')
        dot.attr('node', shape='circle')
       # self.cad.insert(INSERT,expresion)
        if expresion=="var ID = ID L D;":
            countID=0
            countST=0
            
            if contVar==1:
                self.cad.insert(INSERT,"Expresion: ")
                self.cad.insert(INSERT,expresion)
                self.cad.insert(INSERT," Reconocida")
                separado=expresion.split(" ")
                tokeni=list(expresion)
                for i_lex in separado:
                    lex=str(i_lex)
                    if lex==";":
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST-1), str(countST), label=lexL)
                        dot.edge(str(countST-1), str(countST), label=lexD)
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                        dot.render('/home/hp/Escritorio/ExpresionVar.gv', view=True)
                        print("AFD var Generado")
                        countST=countST+1
                    elif lex==ID and countID==0:
                        countID=0
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                        countID=countID+1
                    elif lex==ID and countID!=0:
                        lex=lex+"_asig"
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST),str(countST+1), label=lex)
                        countST=countST+1
                    else:
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                   
        elif expresion=="var ID = ID ;":
            countID=0
            countST=0
            if contVar==1:
                self.cad.insert(INSERT,"Expresion: ")
                self.cad.insert(INSERT,expresion)
                self.cad.insert(INSERT," Reconocida")
                separado=expresion.split(" ")
                tokeni=list(expresion)
                for i_lex in separado:
                    lex=str(i_lex)
                    if lex==";":
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST-1), str(countST), label=lexL)
                        dot.edge(str(countST-1), str(countST), label=lexD)
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                        dot.render('/home/hp/Escritorio/ExpresionVar.gv', view=True)
                        print("AFD var Generado")
                        countST=countST+1
                    elif lex==ID and countID==0:
                        countID=0
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                        countID=countID+1
                    elif lex==ID and countID!=0:
                        lex=lex+"_asig"
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST),str(countST+1), label=lex)
                        countST=countST+1
                    else:
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
        elif expresion=="/ * TODO * /":
            countID=0
            countA=False
            countST=0
            self.cad.insert(INSERT,"Expresion: ")
            self.cad.insert(INSERT,expresion)
            self.cad.insert(INSERT," Reconocida")
            separado=expresion.split(" ")
            print(separado)
            for i_lex in separado:
                    lex=str(i_lex)
                    if lex=="/" and countA==True:
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                        dot.render('/home/hp/Escritorio/ExpresionMultilinea.gv', view=True)
                        print("AFD Multilinea Generado")
                        countST=countST+1
                    elif lex=="TODO":
                        countID=0
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lexS)
                        dot.edge(str(countST), str(countST+1), label=lexD)
                        dot.edge(str(countST), str(countST+1), label=lexL)

                        dot.edge(str(countST+2), str(countST), label=lexS)
                        dot.edge(str(countST+2), str(countST), label=lexD)
                        dot.edge(str(countST+2), str(countST), label=lexL)
                        countST=countST+1
                        countID=countID+1
                    elif lex=="/" and countA==False:#/
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                    elif lex=="*" and countA==False:#/*
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                        countA=True
                    elif lex=="*" and countA==True:#todo *
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST-1), str(countST+1), label=lex)
                        dot.edge(str(countST+1), str(countST-1), label=lex)
                        countST=countST+1
                        countA=True
                    

        elif expresion=="\" TODO \"":
            self.cad.insert(INSERT,"Expresion: ")
            self.cad.insert(INSERT,expresion)
            self.cad.insert(INSERT," Reconocida")
            print(expresion)
            countID=0
            countC=False
            countST=0
            
            separado=expresion.split(" ")
            print(separado)
            for i_lex in separado:
                    lex=str(i_lex)
                    if lex=="\"" and countC==True:
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                        dot.render('/home/hp/Escritorio/ExpresionCadena.gv', view=True)
                        print("AFD Cadena Generado")
                        countST=countST+1
                    elif lex=="TODO":
                        countID=0
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lexS)
                        dot.edge(str(countST), str(countST+1), label=lexD)
                        dot.edge(str(countST), str(countST+1), label=lexL)

                        
                        countST=countST+1
                        countID=countID+1
                    
                    
                    elif lex=="\"" and countC==False:#/*
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        countST=countST+1
                        countC=True
        #elif expresion==""
        self.cad.insert(INSERT,'\n')


    def reservadas(self, reservada):
        global cadena
        global vari
        global contVar
        global ID
        
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
            if vari==False:
                cadena=cadena+"var "
                #self.cad.insert(INSERT,"var ")
                vari=True
                contVar=contVar+1
                print(contVar.__str__()+"cont")
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
            
            print("id "+reservada+" no "+ID.__str__())
            
            
            if vari==True :
                ID=ID+1
                if ID==1 or ID==2:
                    cadena=cadena+"ID "
                    #self.cad.insert(INSERT,"ID ")


    def reservadasHTML(self, reservada):
        if reservada=="":
            reservada=""
        elif reservada=='n':
            print ("n")
        elif reservada=='p':
            print ("p")
        elif reservada=='br':
            print ("br")
        elif reservada=='img':
            print ("img")
        
        elif reservada=='a':
            print ("a")
        elif reservada=='ol':
            print ("ol")
        elif reservada=='ul':
            print ("ul")
        elif reservada=='style':
            print ("style")
        elif reservada=='html':
            print ("html")
        elif reservada=='head':
            print ("head")
        elif reservada=='title':
            print ("title")
        elif reservada=='body':
            print ("body")
        elif reservada=='table':
            print ("table")
        elif reservada=='border':
            print ("border")
        elif reservada=='caption':
            print ("captio")
        elif reservada=='tr':
            print ("tr")
        elif reservada=='th':
            print ("th")
        elif reservada=='td':
            print ("td")
        elif reservada=='coldgroup':
            print ("coldgroup")
        elif reservada=='col':
            print ("col")
        elif reservada=='thead':
            print ("thead")
        elif reservada=='tbody':
            print ("tbody")
        elif reservada=='tfot':
            print ("tfot")
        elif reservada=='src':
            print ("src")
        elif reservada=='href':
            print ("href")
        elif reservada=='li':
            print ("li")
        elif reservada=='h1':
            print ("h1")
        elif reservada=='h2':
            print ("h2")
        elif reservada=='h3':
            print ("h3")
        elif reservada=='h4':
            print ("h4")
        elif reservada=='h5':
            print ("h5")
        elif reservada=='h6':
            print ("h6")
        
        else:
            print("id "+reservada)
            
    def reservadasCSS(self, reservada):
        if reservada=="":
            reservada=""
        elif reservada=='color':
            
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("color")
        elif reservada=='border':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("border")
        elif reservada=='text-align':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("text-align")
        elif reservada=='font-weight':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-weight")
        elif reservada=='padding-left':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-left")
        elif reservada=='padding-top':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-top")
        elif reservada=='line-height':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("line.height")
        elif reservada=='margin-top':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-top")
        elif reservada=='margin-left':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-left")
        elif reservada=='display':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("display")
        elif reservada=='top':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("top")
        elif reservada=='float':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("float")
        elif reservada=='min-width':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("min-width")
        elif reservada=='background-color':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background-color")
        elif reservada=='opacity':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("opacity")
        elif reservada=='font-family':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-family")
        elif reservada=='font-size':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-size")
        elif reservada=='padding-right':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-right")
        elif reservada=='padding':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding")
        elif reservada=='width':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("width")
        elif reservada=='margin-right':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-right")
        elif reservada=='margin':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin")
        elif reservada=='position':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("position")
        elif reservada=='right':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("right")
        elif reservada=='clear':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("clear")
        elif reservada=='max-height':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("max-height")
        elif reservada=='background-image':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background-image")
        elif reservada=='background':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background")
        elif reservada=='font-style':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-style")
        elif reservada=='font':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font")
        elif reservada=='padding-bottom':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-bottom")
        elif reservada=='display':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("display")
        elif reservada=='height':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("height")
        elif reservada=='margin-bottom':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-bottom")
        elif reservada=='left':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("left")
        elif reservada=='max-width':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("max-width")
        elif reservada=='min-height':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("min-height")
        elif reservada=='px':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("px")
        elif reservada=='em':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("em")
        elif reservada=='vh':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("vh")
        elif reservada=='vw':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("vw")
        elif reservada=='in':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("in")
        elif reservada=='cm':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("cm")
        elif reservada=='mm':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("mm")
        elif reservada=='pt':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("pt")
        elif reservada=='pc':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("pc")
        elif reservada=='rem':
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("rem")
        else:
            print("id "+reservada)
            bitacora="Token Reconocido: "+" tK_ID "+reservada +'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)

    def printSalida(self):
        #texto = "Finalizo el analisis"
        self.salida.insert(INSERT,rees)
        self.erroresHTML()
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