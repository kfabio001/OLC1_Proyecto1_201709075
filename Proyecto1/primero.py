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
    pintarComentario=""
    pintarComentarioL=""
    pintarCadena=""
    rmt=""
    
    def __init__(self, window):
        global cadena
        global rmt
        global rees
        global patsi
        global nombre
        global nombres
        global extension
        global errores
        global pintarComentario
        global pintarComentarioL
        global pintarCadena
        rmt=""
        pintarCadena=""
        pintarComentario=""
        pintarComentarioL=""
        errores=""
        nombre=""
        nombres=""
        extension=""
        patsi=""
        rees=""
        cadena=""
        self.ventana = window
        self.ventana.title("Proyecto1- 201709075 Fabio Andre Sanchez Chavez")

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
        global rmt
        pila=list()
        pala=False
        palabra=""
        correcto=True
        resultado=""
        operador=False
        NoD=False
        cierre=False
        cadena=""
        nolinea=1
        rmt=""
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
                if operador==False and NoD==True:
                    correcto=False
                pila.append(lexema)
                noParentesis=noParentesis+1
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=False
                cierre=False
                pala=False
            elif lexema==")":
                if operador==True:
                    correcto=False
                cierre=True
                noParentesisC=noParentesisC+1
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=False
                try:
                    pila.pop()
                
                except:
                    correcto=False
                    #self.cad.insert(INSERT," Inorrecto")
                    #raise ValueError("La pila está vacía")
                    
                
                pala=False
            elif lexema=="*":
                if operador==True:
                    correcto=False
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=True
                pala=False
            elif lexema=="-":
                if(operador==True):
                    correcto=False
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=True
                pala=False
            elif lexema=="+":
                if operador==True:
                    correcto=False
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=True
                pala=False
            elif lexema=="/":
                if operador==True:
                    correcto=False
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=True
                pala=False
            elif lexema=='\n':
                if noParentesisC==noParentesis and correcto==True:
                  #  self.cad.insert(INSERT," Correcto")
                    correcto=True
                else:
                    correcto=False
                if pila==[]:
                    print("aver")
                if correcto==True and cierre==True:
                    self.cad.insert(INSERT," Correcto")
                    resultado="Correcto"
                else:
                    self.cad.insert(INSERT," Inorrecto")
                    resultado="Incorrecto"
                self.cad.insert(INSERT,lexema)
                tr="<tr>"
                td="</td> <td>"
                nolinea=nolinea+1
                rmt=rmt+'\n'+tr+"<td>"+str(nolinea)+td+cadena+td+resultado+"</td> </tr>"
                cadena=""
                resultado=""
                operador=False
                correcto=True
                noParentesis=0
                noParentesisC=0
            elif lexema.isalpha():
                pala=True
                palabra=palabra+lexema
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=False
                NoD=True
            elif lexema.isdigit():
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
                operador=False
                NoD=True
            elif lexema==" ":
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
            elif lexema==".":
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
            elif lexema=="_":
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
            elif lexema=='"':
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema
            else:
                self.cad.insert(INSERT,lexema)
                cadena=cadena+lexema+" (no reconocido)"
                self.cad.insert(INSERT," no reconocido")
        self.reporteRMT()
            
    def reporteRMT(self):
        global nombre
        global nombres
        global rmt
        global patsi
        #if patsi=="":
           # patsi="C:\user\output\js"
        htmls="<html>"+"<head align=center>Reporte RMT</head>"+ "<body> <table border="+"2"+"width="+"850"+ "align=center>"+"<tr> <td>NO.</td> <td>EXPRESION</td> <td>DESCRIPCION</td>"+" </tr>"
        htmlss="</table> </body> </html>"
        archivo=nombre#.split(".")
        archi=""+patsi+"ReporteRMT"+".html"
        print(archi)
        file = open(archi, "w")
        file.write(htmls)
        file.write(rmt)
        file.write(htmlss)
        file.close()
        errores=""
        os.system(archi)
    #END
    #END
    def analizarHTML(self):
        global texto
        global cadena
        global patsi
        global errores
        global pintarComentarioL
        pintarComentarioL=""
        cadena=""
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
            lexema=lexema.lower()
            if letra==False:
                pintarComentarioL=pintarComentarioL+lexema
                
                #self.reescribir(lexema)
                palabra=""
            if unaLinea==True:
                pintarComentarioL=pintarComentarioL+lexema
                if lexema=="-" or lexema==">" or lexema=="/" or lexema==":" or lexema=="\\":
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
                self.find(pintarComentarioL,"gray60")
                pintarComentarioL=""
                #self.reescribir(lexema)
            if lexema=="'":
                self.reescribir(lexema)
                if todoA==True:
                    todoA=False
                    palabra=palabra+lexema
                    self.find(cadena,"yellow")
                    cadena=""
                    self.reservadasHTML(palabra)
                    
                    palabra=""
                    #columna=columna+1
                    lexema=""
                else:
                    cadena=cadena+lexema
                    palabra=palabra+lexema
                    lexema=""
                    todoA=True
            elif lexema=="":
                lexema=""
            elif lexema=='"':
                self.reescribir(lexema)
                if todoC==True:
                    todoC=False
                    self.find(cadena+'"',"yellow")
                    cadena=""
                    palabra=palabra+lexema
                    self.reservadasHTML(palabra)
                    palabra=""
                    lexema=""
                else:
                    cadena=cadena+lexema
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
                cadena=cadena+lexema
            elif todoC==True:
                self.reescribir(lexema)
                palabra= palabra+lexema
                cadena=cadena+lexema
            elif todoM==True:
            
                lexema=""
            elif lexema == espacio:
                #print(lexema)
                columna=1
               # linea=linea+1
                unaLinea==False
                dia=False
                pathw=False
                if lexema != "" and letra==True:
                    
                    self.reservadasHTML(palabra)
                else: 
                    palabra=""
                entreD=False
               # linea=linea+1
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
            #elif lexema=="\\":
                #self.reservadasHTML(palabra)
               # self.reescribir(lexema)
             #   palabra=""
              #  lexema=" "

            
            
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
        global pintarComentario
        hexag=""
        pintarComentario=""
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
            lexema=lexema.lower()
            columna=columna+1
            
            if letra==False:
                palabra=""
                #lexema=""
            if multi3==True:
                pintarComentario=pintarComentario+lexema
                
                if lexema=="-" or lexema==">" :
                        lexema=""
                if noLinea==1 or noLinea==2:
                    pat=pat+lexema
                    print(pat)
                    if lexema=="/" and pathw==False:
                        pat=""
                    elif pat=="PATHW":
                        pathw=True
                        self.find(pat,"red")
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
                    self.find(palabra,"yellow")
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
                self.find(pintarComentario,"gray60")
                pintarComentario=""
                self.find(hexag,"green")
                hexag=""
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
                    hexag=hexag+lexema
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
                    hexag=hexag+lexema
                    self.reescribir(lexema)
                    palabra=palabra+lexema
                else:
                    palabra=palabra+lexema
                    self.find(lexema,"blue")
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
                hexag=""
                hexa=False
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
                self.find("#","orange")
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
                self.find("+","orange")
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
                self.find("-","orange")
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
        #errores
        archi=""+patsi+nombre+".html"
        archi1=patsi+"ExpresionMultilinea.gv.pdf"
        archi2=patsi+"ExpresionVar.gv.pdf"
        archi3=patsi+"ExpresionCadena.gv.pdf"
        print(archi)
        os.system(archi)
        os.system(archi1)
        os.system(archi2)
        os.system(archi3)
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
        errores=""
        #os.system(archi)
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
        global pintarComentario
        global pintarComentarioL
        global pintarCadena
        
        operadores=""
        operador=False
        errores=""
        pintarComentario=""
        pintarComentarioL=""
        pintarCadena=""
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
        num=False
        
        text = self.entrada.get("1.0",END)
        vari=False
        token=list(text)
        separado = text.split()

        for i_lexema in token:
            lexema=str(i_lexema)
            lexema=lexema.lower()
            columna=columna+1

            if letra==False:
                palabra=""
                pintarComentario=pintarComentario+lexema
                pintarComentarioL=pintarComentarioL+lexema
            if letra==True:
                pintarComentarioL=""
                pintarComentario=""
            if unaLinea==True:
                if lexema=="-" or lexema==">":
                        lexema=""
                if noLinea==1 or noLinea==2:
                    pat=pat+lexema
                    if lexema=='\n' and pathw==False:
                        pat=""
                    if pat=="pathw":
                        self.find(pat,"red")
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
                    self.find(palabra,"yellow")
                    palabra=""
                    lexema=""
                else:
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
                    self.find(palabra,"yellow")
                    palabra=""
                    lexema=""
                else:
                    cadenas=cadenas+lexema+" "
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
                if unaLinea==True:

                    self.find(pintarComentarioL,"gray60")
                    
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
                pintarComentarioL=""
                palabra=""
            elif  lexema == " ":
                self.reescribir(lexema)
                if lexema != "" and letra==True:
                    self.reservadas(palabra)
                else: 
                    palabra=""
                palabra=""
                entreD=False
            elif lexema.isalpha():
                self.reescribir(lexema)
                palabra= palabra+lexema
                
                entreD=False
                entreA=False
                num=False
                operadores=""
            elif lexema.isdigit():
                self.reescribir(lexema)
                
                palabra=palabra+lexema
                num=True
                self.find(lexema,"blue")
                entreA=False
                entreD=False
                operadores=""
            elif lexema=="{":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=""
            elif lexema=="}":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="=":
                self.reescribir(lexema)
                if operador==True and (operadores==">" or operadores=="<"or operadores=="!"or operadores=="="):
                    operador=False
                    self.reservadas(operadores+"=")
                    operadores=""
                else:
                    operador=True
                if vari==True:
                    cadena=cadena+"= "
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="“":
                self.reescribir(lexema)
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
            elif lexema=="’":
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema==";":
                self.reescribir(lexema)
                if vari==True:
                    cadena=cadena+"ID ;"
                    print(cadena)
                    self.expreionJS(cadena)
                    cadena=""
                    vari=False
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema==">":
                operadores=">"
                self.find(">","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="<":
                operadores=">"
                self.find("<","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="(":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
                operadores=""
            elif lexema==")":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema==".":
                #if num==True:
                palabra=palabra+lexema
                self.reescribir(lexema)
                lexema=" "
            elif lexema=="_":
                self.reescribir(lexema)
                palabra= palabra+lexema
                lexema=" "
            elif lexema==",":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="!":
                if operador==True:
                    operador=False
                else:
                    operador=True
                self.reescribir(lexema)
                self.reservadas(palabra)
                self.find("!","orange")
                palabra=""
                lexema=" "
            
            elif lexema=="+":
                self.reescribir(lexema)
                self.find("+","orange")
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="-":
                self.find("-","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="|":
                if operador==True and operadores=="|":
                    operador=False
                    self.reservadas("||")
                    operadores=""
                else:
                    operador=True
                self.find("|","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="&":
                if operador==True and operadores=="&":
                    operador=False
                    self.reservadas("&&")
                    operadores=""
                else:
                    operador=True
                self.find("&","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema=="\\":
                self.reescribir(lexema)
                lexema=" "
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
                    self.find(pintarComentario,"gray60")
                    pintarComentario=""
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
               # self.find("&","orange")
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            elif lexema==":":
                self.reescribir(lexema)
                self.reservadas(palabra)
                palabra=""
                lexema=" "
            else: 
                if letra==False:
                    #pintarComentario=pintarComentario+lexema
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
    def find(self, buscar, color): 
      
        #self.entrada.tag_remove(color, '1.0', END)  
        s = buscar  
        if s: 
            idx = '1.0'
            while 1: 
                idx = self.entrada.search(s, idx, nocase=1,  
                              stopindex=END)  
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))  
                self.entrada.tag_add(color, idx, lastidx)  
                idx = lastidx 
            self.entrada.tag_config(color, foreground=color)  
        #edit.focus_set() 
        self.entrada.tag_config("gray60", foreground="gray60") 
    def expreionJS(self, expresion):
        global contVar
        separado=""
        lexL="L"
        lexD="D"
        lexS="S"
        lexCad='"cadena"'
        lexN="num"
        dot = Digraph(comment='Grafo JavaScript')
        dot.attr('node', shape='circle')
       # self.cad.insert(INSERT,expresion)
        if expresion=="var ID = ID L D;":
            countID=0
            countST=0
            
            if contVar==1:
                self.cad.insert(INSERT,"Expresion: ")
                self.cad.insert(INSERT,'"VAR"[ID]=([ID]|[cadena]|[num])')
                self.cad.insert(INSERT," Reconocida")
                separado=expresion.split(" ")
                tokeni=list(expresion)
                for i_lex in separado:
                    lex=str(i_lex)
                    if lex==";":
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST-1), str(countST), label=lexCad)
                        dot.edge(str(countST-1), str(countST), label=lexN)
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                      #  dot.render(patsi+"/ExpresionVar.gv")#, view=True)
                        dot.render("ExpresionVar.gv")#, view=True)
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
                self.cad.insert(INSERT,'"VAR" [ID]=([ID]|[cadena]|[num])')
                self.cad.insert(INSERT," Reconocida")
                separado=expresion.split(" ")
                tokeni=list(expresion)
                for i_lex in separado:
                    lex=str(i_lex)
                    if lex==";":
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST-1), str(countST), label=lexCad)
                        dot.edge(str(countST-1), str(countST), label=lexN)
                        dot.node(str(countST+1), shape='doublecircle')
                        print(dot.source)
                        archi=""+patsi
                        #dot.render(patsi+"/ExpresionVar.gv")#, view=True
                        dot.render("ExpresionVar.gv")#, view=True))
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
            self.cad.insert(INSERT,'"/" "*" (L|D|S)* (*)+ "/"')
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
                        #dot.render(patsi+"/ExpresionMultilinea.gv")#, view=True)
                        dot.render("ExpresionMultilinea.gv")#, view=True)
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
            self.cad.insert(INSERT,'" (S|D|L)* "')
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
                        #dot.render(patsi+"/ExpresionCadena.gv")#, view=True)
                        dot.render("ExpresionCadena.gv")#, view=True)
                        print("AFD Cadena Generado")
                        countST=countST+1
                    elif lex=="TODO":
                        countID=0
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lexS)
                        dot.edge(str(countST), str(countST+1), label=lexD)
                        dot.edge(str(countST), str(countST+1), label=lexL)
                        dot.edge(str(countST+1), str(countST+1), label=lexS)
                        dot.edge(str(countST+1), str(countST+1), label=lexD)
                        dot.edge(str(countST+1), str(countST+1), label=lexL)

                        
                        countST=countST+1
                        countID=countID+1
                    
                    
                    elif lex=="\"" and countC==False:#/*
                        dot.node(str(countST),str(countST))
                        dot.edge(str(countST), str(countST+1), label=lex)
                        dot.edge(str(countST+1), str(countST+3), label=lex)
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
       # elif reservada=='int':
        #    self.find("int","blue")
         #   print ("int")
        elif reservada=='new':
            self.find("new","red")
            print ("new")
        elif reservada=='null':
            self.find("null","red")
            print ("null")
       # elif reservada=='string':
          #  self.find("string","yellow")
           # print ("string")
        #elif reservada=='char':
         #   self.find("char","yellow")
          #  print ("char")
       # elif reservada=='boolean':
        #    self.find("boolean","blue")
         #   print ("boolean")
        elif reservada=='var':
            print ("var")
            self.find("var","red")
            if vari==False:
                cadena=cadena+"var "
                #self.cad.insert(INSERT,"var ")
                vari=True
                contVar=contVar+1
                print(contVar.__str__()+"cont")
        elif reservada=='if':
            self.find("if","red")
            print ("if")
        elif reservada=='else':
            self.find("else","red")
            print ("else")
        elif reservada=='for':
            self.find("for","red")
            print ("for")
        elif reservada=='while':
            self.find("while","red")
            print ("while")
        elif reservada=='do':
            self.find("do","red")
            print ("do")
        elif reservada=='continue':
            self.find("continue","red")
            print ("continue")
        elif reservada=='break':
            self.find("break","red")
            print ("break")
        elif reservada=='return':
            self.find("return","red")
            print ("return")
        elif reservada=='function':
            self.find("function","red")
            print ("function")
        elif reservada=='constructor':
            self.find("constructor","red")
            print ("constructor")
        elif reservada=='class':
            self.find("class","red")
            print ("class")
        elif reservada=='math':
            self.find("math","red")
            print ("math")
        elif reservada=='pow':
            self.find("pow","red")
            print ("pow")
        elif reservada=='true':
            self.find("true","blue")
            print ("true")
        elif reservada=='false':
            self.find("false","blue")
            print ("false")
        elif reservada=='pathl':
            self.find("pathl","green")
            print ("pathl")
        elif reservada=='pathw':
            self.find("pathw","green")
            print ("pathw")
        elif reservada=='==':
            self.find("==","orange")
            #print ("==")
        elif reservada=='!=':
            self.find("!=","orange")
            #print ("pathw")
        elif reservada=='>=':
            self.find(">=","orange")
            #print ("pathw")
        elif reservada=='<=':
            self.find("<=","orange")
           # print ("pathw")
        elif reservada=='&&':
            self.find("&&","orange")
            #print ("pathw")
        elif reservada=='||':
            self.find("||","orange")
            
        else:
            self.find(""+reservada+"","green")
            print("id "+reservada+" no "+ID.__str__())
            
            
            if vari==True :
                ID=ID+1
                if ID==1 or ID==2:
                    cadena=cadena+"ID "
                    #self.cad.insert(INSERT,"ID ")


    def reservadasHTML(self, reservada):
        self.find("<"+reservada+">","red")
        self.find("</"+reservada+">","red")
        if reservada=="":
            reservada=""
        elif reservada=='n':
            #self.find("n","red")
            print ("n")
        elif reservada=='p':
            #self.find("p","red")
            print ("p")
        elif reservada=='br':
            #self.find("br","red")
            print ("br")
        elif reservada=='img':
            #self.find("img","red")
            print ("img")
        
        elif reservada=='a':
            self.find("<a","red")
            print ("a")
        elif reservada=='ol':
            #self.find("ol","red")
            print ("ol")
        elif reservada=='ul':
            #self.find("ul","red")
            print ("ul")
        elif reservada=='style':
            self.find("style","red")
            print ("style")
        elif reservada=='html':
            #self.find("html","red")
            print ("html")
        elif reservada=='head':
            #self.find("head","red")
            print ("head")
        elif reservada=='title':
            #self.find("title","red")
            print ("title")
        elif reservada=='body':
            #self.find("body","red")
            print ("body")
        elif reservada=='table':
            self.find("<table","red")
            self.find("table/","red")
            print ("table")
        elif reservada=='border':
            self.find("border","red")
            print ("border")
        elif reservada=='caption':
            #self.find("caption","red")
            print ("captio")
        elif reservada=='tr':
            #self.find("tr","red")
            print ("tr")
        elif reservada=='th':
            #self.find("th","red")
            print ("th")
        elif reservada=='td':
            #self.find("td","red")
            print ("td")
        elif reservada=='coldgroup':
            #self.find("coldgroup","red")
            print ("coldgroup")
        elif reservada=='col':
            #self.find("col","red")
            print ("col")
        elif reservada=='thead':
            #self.find("thead","red")
            print ("thead")
        elif reservada=='tbody':
            #self.find("tbody","red")
            print ("tbody")
        elif reservada=='tfot':
            #self.find("tfot","red")
            print ("tfot")
        elif reservada=='src':
            #self.find("src","red")
            print ("src")
        elif reservada=='href':
            self.find("href","red")
            print ("href")
        elif reservada=='li':
            #self.find("li","red")
            print ("li")
        elif reservada=='div':
            self.find("div","red")
            print ("div")
        elif reservada=='h1':
            self.find("h1","red")
            print ("h1")
        elif reservada=='h2':
            self.find("h2","red")
            print ("h2")
        elif reservada=='h3':
            self.find("h3","red")
            print ("h3")
        elif reservada=='h4':
            self.find("h4","red")
            print ("h4")
        elif reservada=='h5':
            self.find("h5","red")
            print ("h5")
        elif reservada=='h6':
            self.find("h6","red")
            print ("h6")
        
        else:
            print("id "+reservada)
            #self.find(reservada,"black")
        self.find(">","orange")
        self.find("<","orange")
        self.find("</","orange")
        self.find("//","gray60")
    def reservadasCSS(self, reservada):
        #self.find(reservada,"red")
        if reservada=="":
            reservada=""
        elif reservada=='color':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("color")
        elif reservada=='border':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("border")
        elif reservada=='text-align':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("text-align")
        elif reservada=='font-weight':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-weight")
        elif reservada=='padding-left':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-left")
        elif reservada=='padding-top':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-top")
        elif reservada=='line-height':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("line.height")
        elif reservada=='margin-top':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-top")
        elif reservada=='margin-left':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-left")
        elif reservada=='display':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("display")
        elif reservada=='top':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("top")
        elif reservada=='float':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("float")
        elif reservada=='min-width':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("min-width")
        elif reservada=='background-color':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background-color")
        elif reservada=='opacity':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("opacity")
        elif reservada=='font-family':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-family")
        elif reservada=='font-size':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-size")
        elif reservada=='padding-right':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-right")
        elif reservada=='padding':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding")
        elif reservada=='width':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("width")
        elif reservada=='margin-right':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-right")
        elif reservada=='margin':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin")
        elif reservada=='position':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("position")
        elif reservada=='right':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("right")
        elif reservada=='clear':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("clear")
        elif reservada=='max-height':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("max-height")
        elif reservada=='background-image':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background-image")
        elif reservada=='background':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("background")
        elif reservada=='font-style':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font-style")
        elif reservada=='font':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("font")
        elif reservada=='padding-bottom':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("padding-bottom")
        elif reservada=='display':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("display")
        elif reservada=='height':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("height")
        elif reservada=='margin-bottom':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("margin-bottom")
        elif reservada=='left':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("left")
        elif reservada=='max-width':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("max-width")
        elif reservada=='min-height':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("min-height")
        elif reservada=='px':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("px")
        elif reservada=='em':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("em")
        elif reservada=='vh':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("vh")
        elif reservada=='vw':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("vw")
        elif reservada=='in':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("in")
        elif reservada=='cm':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("cm")
        elif reservada=='mm':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("mm")
        elif reservada=='pt':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("pt")
        elif reservada=='pc':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("pc")
        elif reservada=='rem':
            self.find(reservada,"red")
            bitacora="Token Reconocido: "+" tK_"+reservada +" = "+reservada+'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
            #print ("rem")
        else:
            #self.find(reservada,"green")
            print("id "+reservada)
            #self.find(reservada,"black")
            bitacora="Token Reconocido: "+" tK_ID "+reservada +'\n'
            self.cad.insert(INSERT,bitacora)
            estados=1
            bitacora="Entro a s"+ str(estados-1)+'\n'
            self.cad.insert(INSERT,bitacora)
        self.find("px","red")
        self.find("/*","gray60")
    def printSalida(self):
        #texto = "Finalizo el analisis"
        self.salida.insert(INSERT,rees)
        self.erroresHTML()
       # messagebox.showerror("Error", "Texto a mostrar:\n")
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