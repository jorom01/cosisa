def arcgis(MW,uriSalidaMapas,SATURADO,uriMapaPendientes,uriMapaIA,uriMapaPGA,uriMapaDensidad,num_niveles, uriMapaFriccion10,uriMapaFriccion50,uriMapaFriccion90,uriMapaCohesion10,uriMapaCohesion50,uriMapaCohesion90,JR07_1,JR07_2,JR07_3,JR07_4,BT07,SR08_1,SR08_2,RS09,HL11,JL18,DJ20):
    import arcpy, os, shutil, math
    from arcpy import env
    from arcpy.sa import *
    arcpy.CheckOutExtension("Spatial")
    path = uriSalidaMapas
    carpeta = "NewmarkMethods"
    env.workspace = path
    env.overwriteOutput = True
    if os.path.exists(path):
        shutil.rmtree(path) 
    try:
      os.stat(path)
    except:
      os.mkdir(path) 
    geodata = path +"\\"+"DATOS"
    if os.path.exists(geodata):
        shutil.rmtree(geodata) 
    try:
      os.stat(geodata) 
    except:
      os.mkdir(geodata)
    arcpy.CreateFileGDB_management(geodata, "datos_partida.gdb")
    gbd_dp = geodata + "\\" + "datos_partida.gdb"
    calculos = path +"\\"+"CALCULOS"
    if os.path.exists(calculos):
        shutil.rmtree(calculos) 
    try:
      os.stat(calculos) 
    except:
      os.mkdir(calculos)
    arcpy.CreateFileGDB_management(calculos, "calculos_intermedios.gdb")
    gbd_ci = calculos + "\\" + "calculos_intermedios.gdb"
    resultados = path +"\\"+"RESULTADOS"
    if os.path.exists(resultados):
        shutil.rmtree(resultados) 
    try:
      os.stat(resultados)
    except:
      os.mkdir(resultados)
    m = float(SATURADO) 
    pendiente = uriMapaPendientes 
    rasPendientes = gbd_dp + "\\pendiente" 
    arcpy.CopyRaster_management(pendiente, rasPendientes, "", "", "", "", "", "")
    IA = uriMapaIA 
    rasIa = gbd_dp + "\\IA" 
    arcpy.CopyRaster_management(IA, rasIa, "", "", "", "", "", "")
    pga = uriMapaPGA  
    rasPGA = gbd_dp + "\\PGA" 
    arcpy.CopyRaster_management(pga, rasPGA, "", "", "", "", "", "")
    pesico = uriMapaDensidad 
    peso =  Divide(Times(pesico,9.81),1000) 
    rasDensidad = gbd_dp + "\\densidad" 
    arcpy.CopyRaster_management(peso, rasDensidad, "", "", "", "", "", "")
    Rad = float(math.pi/180) 
    rasM = MW 
    y = float("9.810")
    depths = num_niveles
    direcciones_de_mapas_de_friccion = [uriMapaFriccion10,uriMapaFriccion50,uriMapaFriccion90] 
    direcciones_de_mapas_de_cohesion = [uriMapaCohesion10,uriMapaCohesion50,uriMapaCohesion90] 
    for prof_t in depths:
        k = 10
        t = prof_t 
        nivel=resultados+"\\"+"Nivel_"+str(prof_t)+"_m"
        os.mkdir(nivel)
        arcpy.CreateFileGDB_management(nivel, "resultados_desplazamientos.gdb")
        gbd_rd = nivel + "\\" + "resultados_desplazamientos.gdb"
        for fri in direcciones_de_mapas_de_friccion:
          j = 10 
          friccion = Times(fri,1) 
          rasFriccion = gbd_dp + "\\friccion"
          arcpy.CopyRaster_management(friccion, rasFriccion, "", "", "", "", "", "")
          for nu in direcciones_de_mapas_de_cohesion:
            cohesion = Times(nu,1) 
            rasCohesion = gbd_dp + "\\cohesion"
            arcpy.CopyRaster_management(cohesion, rasCohesion, "", "", "", "", "", "")
            o1 = Sin(Times(rasPendientes,Rad))
            sin_alfa = gbd_ci + "\\sin_alfa"
            arcpy.CopyRaster_management(o1, sin_alfa, "", "", "", "", "", "")
            o2 = Tan(Times(rasFriccion,Rad))
            tan_fi = gbd_ci + "\\tan_fi"
            arcpy.CopyRaster_management(o2, tan_fi, "", "", "", "", "", "")
            o3 = Tan(Times(rasPendientes,Rad))
            tan_alfa = gbd_ci + "\\tan_alfa"
            arcpy.CopyRaster_management(o3, tan_alfa, "", "", "", "", "", "")
            o4 = Cos(Times(rasPendientes,Rad))
            cos_alfa = gbd_ci + "\\cos_alfa"
            arcpy.CopyRaster_management(o4, cos_alfa, "", "", "", "", "", "")
            o5 = Minus(Plus(Divide(rasCohesion,Times(rasDensidad,Times(t,sin_alfa))),Divide(tan_fi,tan_alfa)),Divide(Times(Times(y,m),tan_fi),Times(rasDensidad,tan_alfa)))
            FS = gbd_rd + "\\FS"
            FSorg = gbd_ci + "\\FS_fi"+str(k)+"_c"+str(j)
            arcpy.CopyRaster_management(o5, FS, "", "", "", "", "", "")
            arcpy.CopyRaster_management(o5, FSorg, "", "", "", "", "", "")
            o6 = Con(Divide(Minus(FS,1),Plus(Times(cos_alfa,tan_fi),Divide(1,tan_alfa))),Divide(Minus(FS,1),Plus(Times(cos_alfa,tan_fi),Divide(1,tan_alfa))), "0.001", "VALUE > 0")
            Ac= gbd_rd + "\\Ac"
            Acorg = gbd_ci + "\\Ac_fi"+str(k)+"_c"+str(j)
            arcpy.CopyRaster_management(o6, Ac, "", "", "", "", "", "")
            arcpy.CopyRaster_management(o6, Acorg, "", "", "", "", "", "")
            if JR07_1 == True:
              o7 = Exp10(Plus(0.215,Log10(Times(Power(Minus(1,ExtractByAttributes(Divide(Ac,rasPGA),"VALUE < 1")),2.341),Power(Divide(Ac,rasPGA),-1.438)))))
              Dn1 = gbd_rd + "\\J07_1_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o7, Dn1, "", "", "", "", "", "")
            if JR07_2 == True:
              o8 = Exp10(Plus(Plus(Log10(Times(Power(Minus(1,ExtractByAttributes(Divide(Ac,rasPGA),"VALUE < 1")),2.335),Power(Divide(Ac,rasPGA),-1.478))),Times(0.424,rasM)),-2.710))
              Dn2 = gbd_rd + "\\J07_2_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o8, Dn2, "", "", "", "", "", "")        
            if JR07_3 == True:
              o9 = Exp10(Minus(Times(2.401,Log10(rasIa)),Plus(Times(3.481,Log10(Ac)),3.23)))
              Dn3 = gbd_rd + "\\J07_3_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o9, Dn3, "", "", "", "", "", "")
            if JR07_4 == True:
              o10 = Exp10(Minus(Times(0.561,Log10(rasIa)),Plus(Times(3.833,Log10(Divide(Ac,rasPGA))),1.474)))
              Dn4 = gbd_rd + "\\J07_4_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o10, Dn4, "", "", "", "", "", "")           
            if RS09 == True:
              o11 = Exp(Minus(Plus(Plus(4.89,Times(42.49,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Divide(Ac,rasPGA)))),Plus(Times(0.72,Ln(rasPGA)),Times(0.89,Minus(rasM,6)))),Plus(Plus(Times(4.85,Divide(Ac,rasPGA)),Times(19.64,Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))),Times(29.06,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))))))
              Dn5 = gbd_rd + "\\RS09_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o11, Dn5, "", "", "", "", "", "")
            if SR08_1 == True:
              o12 = Exp(Minus(Plus(Plus(5.52,Times(42.61,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Divide(Ac,rasPGA)))),Times(0.72,Ln(rasPGA))),Plus(Plus(Times(4.43,Divide(Ac,rasPGA)),Times(20.39,Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))),Times(28.74,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))))))
              Dn6 = gbd_rd + "\\SR08_1_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o12, Dn6, "", "", "", "", "", "")
            if SR08_2 == True:
              o13 = Exp(Minus(Plus(Plus(2.39,Times(42.01,Times(Divide(Ac,rasPGA),Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA))))),Times(1.38,Ln(rasIa))),Plus(Plus(Times(5.24,Divide(Ac,rasPGA)),Times(18.78,Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))),Plus(Times(29.15,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)))),Times(1.56,Ln(rasPGA))))))
              Dn7 = gbd_rd + "\\SR08_2_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o13, Dn7, "", "", "", "", "", "")
            if HL11 == True:
              o15 =Exp10(Minus(Plus(Plus(Times(0.847,Log10(rasIa)),Times(Times(6.587,Ac),Log10(rasIa))),1.84),Times(10.62,Ac)))
              Dn9 = gbd_rd + "\\HL11_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o15, Dn9, "", "", "", "", "", "")
            if BT07 == True:
              o16 =Exp(Minus(Plus(Plus(Times(Times(0.566,Ln(Ac)),Ln(rasPGA)),Times(3.04,Ln(rasPGA))),Times(0.278,Minus(rasM,7))),Plus(Plus(0.22,Times(2.83,Ln(Ac))),Plus(Times(0.333,Times(Ln(Ac),Ln(Ac))),Times(0.244,Times(Ln(rasPGA),Ln(rasPGA)))))))
              Dn10 = gbd_rd + "\\BT07_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o16, Dn10, "", "", "", "", "", "")
            if JL18 == True:
              o19=Exp(Minus(Plus(Plus(Times(0.0465,Log10(rasIa)),Times(Times(12.896,Ac),Log10(rasIa))),2.092),Times(22.201,Ac)))
              Dn13 = gbd_rd + "\\JL18_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o19, Dn13, "", "", "", "", "", "")
            if DJ20 == True:
              o20=Exp(Minus(Plus(Plus(1.416, Times(1.056,Log10(rasIa))),Times(20.421,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Divide(Ac,rasPGA)))),Plus(Plus(Times(0.279,Log10(rasPGA)),Times(13.303,Times(Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA)),Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA))))),Times(11.110,Times(Divide(Ac,rasPGA),Divide(Ac,rasPGA))))))
              Dn14 = gbd_rd + "\\DJ20_fi"+str(k)+"_c"+str(j)
              arcpy.CopyRaster_management(o20, Dn14, "", "", "", "", "", "")        
            j = j+40
          k = k+40