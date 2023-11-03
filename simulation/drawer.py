# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:45:39 2023

@author: Akahaoua David BROU
"""

#Les Importations
import os
import numpy as np    #bibliothèque pour la programmation scientique vectorielle
import pandas as pd   #bibliothèque pour la lecture de fichier excel

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt   #pour la représentation grphique
#from mpl_toolkits.mplot3d import Axes3D
import copy
import time


def main_draw(timp_param,nbEclosion_param,typeVegetation_param,simulation_name):
    ##### allumage dynamique ########
    #recuperer l'indice de la valeur correspondante  j=coorx.tolist().index(xEclosion[i])
    def allumage(siteEnFeu,cotéAllumé,longueurEclosion,nbEclosion,coorx,coory,\
                varN,varS,varW,varE,varC,timeAllumage,timeCombustion,ieclo,jeclo,\
                directionDuVent,deltax,deltay,veg,temperatureSite,temperatureAllumage):
        import numpy as np
        for i in np.arange(nbEclosion):
            if longueurEclosion[i] < 0.:
                break
    #mise a feu frontière nord
            if cotéAllumé[i]=="nord":
                if varN[i]*deltax<=longueurEclosion[i]:
                    if coorx[ieclo[i]]==coorx[0] or \
                        abs(coorx[ieclo[i]]-coorx[0])<abs(coorx[ieclo[i]]-coorx[-1]):
                            coef=1
                    if coorx[ieclo[i]]==coorx[-1] or \
                        abs(coorx[ieclo[i]]-coorx[0])>abs(coorx[ieclo[i]]-coorx[-1]):
                            coef=-1
                    #siteEnFeu.append([coorx[ieclo[i]+coef*varN[i]],coory[-1],\
                    #                  timeCombustion[veg[ieclo[i]+varN[i],-1]]]) 
                    siteEnFeu.append([ieclo[i]+coef*varN[i],-1,\
                                    timeCombustion[veg[ieclo[i]+varN[i],-1]]])
                    temperatureSite[ieclo[i]+coef*varN[i],-1]=temperatureAllumage
    # mise à feu frontière sud
            if cotéAllumé[i]=="sud":
                if varS[i]*deltax<=longueurEclosion[i]:
                    if coorx[ieclo[i]]==coorx[0] or \
                        abs(coorx[ieclo[i]]-coorx[0])<abs(coorx[ieclo[i]]-coorx[-1]):
                            coef=1
                    if coorx[ieclo[i]]==coorx[-1] or \
                        abs(coorx[ieclo[i]]-coorx[0])>abs(coorx[ieclo[i]]-coorx[-1]):
                            coef=-1
                    #siteEnFeu.append([coorx[ieclo[i]+coef*varS[i]],coory[0],\
                    #                  timeCombustion[veg[ieclo[i]+varS[i],0]]])
                    siteEnFeu.append([ieclo[i]+coef*varS[i],0,\
                                    timeCombustion[veg[ieclo[i]+varS[i],0]]])
                    temperatureSite[ieclo[i]+coef*varS[i],0]=temperatureAllumage  
    # mise à feu frontière ouest
            if cotéAllumé[i]=="ouest":
                if varW[i]*deltay<=longueurEclosion[i]:
                    if coory[ieclo[i]]==coory[0] or \
                        abs(coory[jeclo[i]]-coory[0])<abs(coory[jeclo[i]]-coory[-1]):
                            coef=1
                    if coory[ieclo[i]]==coory[-1] or \
                        abs(coory[jeclo[i]]-coory[0])>abs(coory[jeclo[i]]-coory[-1]):
                            coef=-1
                    #siteEnFeu.append([coorx[0],coory[jeclo[i]+varW[i]],\
                    #                  timeCombustion[veg[0,jeclo[i]+varW]]])
                    siteEnFeu.append([0,jeclo[i]+varW[i],\
                                    timeCombustion[veg[0,jeclo[i]+varW[i]]]])
                    temperatureSite[0,jeclo[i]+varW[i]]=temperatureAllumage
    # mise à feu frontière est
            if cotéAllumé[i]=="est":
                if varE[i]*deltay<=longueurEclosion[i]:
                    if coory[ieclo[i]]==coory[0] or \
                        abs(coory[jeclo[i]]-coory[0])<abs(coory[jeclo[i]]-coory[-1]):
                            coef=1
                    if coory[ieclo[i]]==coory[-1] or \
                        abs(coory[jeclo[i]]-coory[0])>abs(coory[jeclo[i]]-coory[-1]):
                            coef=-1
                    #siteEnFeu.append([coorx[-1],coory[jeclo[i]+varE[i]],\
                    #                  timeCombustion[veg[-1,jeclo[i]+varE[i]]]]) 
                    siteEnFeu.append([-1,jeclo[i]+varE[i],\
                                    timeCombustion[veg[-1,jeclo[i]+varE[i]]]])
                    temperatureSite[-1,jeclo[i]+varE[i]]=temperatureAllumage
    # allumage centré
            coefx=0; coefy=0
            if cotéAllumé[i]=="centre":
                if varC[i]*(deltax+deltay)*0.5<=longueurEclosion[i]/2.:
                    if coory[jeclo[i]]==coory[0] or coory[jeclo[i]]==coory[-1]:
                        coefx=1
                    if coorx[ieclo[i]]==coorx[0] or coorx[ieclo[i]]==coorx[-1]:
                        coefy=1 
                    siteEnFeu.append([ieclo[i]+coefx*varC[i],jeclo[i]+coefy*varC[i],\
                                    timeCombustion[veg[ieclo[i]+coefx*varC[i],jeclo[i]+coefy*varC[i]]]])
                    temperatureSite[ieclo[i]+coefx*varC[i],jeclo[i]+coefy*varC[i]]=temperatureAllumage
                    siteEnFeu.append([ieclo[i]-coefx*varC[i],jeclo[i]-coefy*varC[i],\
                                    timeCombustion[veg[ieclo[i]-coefx*varC[i],jeclo[i]-coefy*varC[i]]]])
                    temperatureSite[ieclo[i]-coefx*varC[i],jeclo[i]-coefy*varC[i]]=temperatureAllumage
        return siteEnFeu,temperatureSite
    ##############################fin allumage dynamique##########################
    #################programme principal###################

    #from numpy import linalg as la
    start=time.time()
    #on vide la mémoire de tous les graphiques
    #plt.close("all")
    #**LES CONSTANTES DU MODELE***
    pesanteur=9.81
    chaleurVap=2.25e6 #CHALEUR LATENTE D'EVAPORATION
    sigmaRay=5.67e-8
    prandtl=0.71
    coefxDomInter=2.
    coefyDomInter=3.
    ############### lecture du fichier des données#################
    timp=timp_param
    # print("lecture fichier des données")
    typeVegetation=typeVegetation_param
    nbreVegetation=typeVegetation  #on conserve le nombre initial de vegetation
    ##création de vecteurs
    x1veg=np.zeros(nbreVegetation)
    x2veg=np.zeros(nbreVegetation)
    y1veg=np.zeros(nbreVegetation)
    y2veg=np.zeros(nbreVegetation)
    teneurEnEau=np.zeros(nbreVegetation)
    hauteurFuelBed=np.zeros(nbreVegetation)
    emissiviteFuelBed=np.zeros(nbreVegetation)
    absorptionFuelBed=np.zeros(nbreVegetation)
    fractionVolumiq=np.zeros(nbreVegetation)
    densitéFuelBed=np.zeros(nbreVegetation)
    surfaceSpec=np.zeros(nbreVegetation)
    diametreFuelBed=np.zeros(nbreVegetation)
    chaleurSpecFeulBed=np.zeros(nbreVegetation)
    chargeSurface=np.zeros(nbreVegetation)
    hauteurFlamme=np.zeros(nbreVegetation)
    timeCombustion=np.zeros(nbreVegetation)
    #
    siteEnFeu=[]
    siteVoisin=[]   
    siteBrule=[]

    #NOTE : path of right xlsx file
    file_vegetation = os.path.join('media', simulation_name,'vegetation.csv')
    file_climat = os.path.join('media', simulation_name,'climat.csv')
    file_eclosion = os.path.join('media', simulation_name,'eclosion.csv')

    vegetation=pd.read_csv(file_vegetation,usecols=[0,1])   #,usecols=(0,1)
    climat=pd.read_csv(file_climat,usecols=[0,1])   #,usecols=(0,1)
    eclosion=pd.read_csv(file_eclosion,usecols=[0,1])   #,usecols=(0,1)

    ##print(vegetation)
    veget1=vegetation['valeurs'].to_numpy()  #choix de la colonne pour lecture
    x1veg[0]=float(veget1[0])
    x2veg[0]=float(veget1[1])
    y1veg[0]=float(veget1[2])
    y2veg[0]=float(veget1[3])
    hauteurFlamme[0]=float(veget1[4])
    hauteurFuelBed[0]=float(veget1[5])
    diametreFuelBed[0]=float(veget1[6])
    densitéFuelBed[0]=float(veget1[7])
    chargeSurface[0]=float(veget1[8])
    teneurEnEau[0]=float(veget1[9])
    timeCombustion[0]=float(veget1[10])
    chaleurSpecFeulBed[0]=float(veget1[11])
    absorptionFuelBed[0]=float(veget1[12])
    emissiviteFuelBed[0]=float(veget1[13])
    typeVegetation-=1    # incrémentation pour lecture des colonnes jusqu'a 0
    if typeVegetation>0:
        veget2=vegetation['vegetation2'].to_numpy()
        x1veg[1]=float(veget2[0])
        x2veg[1]=float(veget2[1])
        y1veg[1]=float(veget2[2])
        y2veg[1]=float(veget2[3])
        hauteurFlamme[1]=float(veget2[4])
        hauteurFuelBed[1]=float(veget2[5])
        diametreFuelBed[1]=float(veget2[6])
        densitéFuelBed[1]=float(veget2[7])
        chargeSurface[1]=float(veget2[8])
        teneurEnEau[1]=float(veget2[9])
        timeCombustion[1]=float(veget2[10])
        chaleurSpecFeulBed[1]=float(veget2[11])
        absorptionFuelBed[1]=float(veget2[12])
        emissiviteFuelBed[1]=float(veget2[13])
    typeVegetation-=1
    if typeVegetation>0:
        veget3=vegetation['vegetation3'].to_numpy()
        x1veg[2]=float(veget3[0])
        x2veg[2]=float(veget3[1])
        y1veg[2]=float(veget3[2])
        y2veg[2]=float(veget3[3])
        hauteurFlamme[2]=float(veget3[4])
        hauteurFuelBed[2]=float(veget3[5])
        diametreFuelBed[2]=float(veget3[6])
        densitéFuelBed[2]=float(veget3[7])
        chargeSurface[2]=float(veget3[8])
        teneurEnEau[2]=float(veget3[9])
        timeCombustion[2]=float(veget3[10])
        chaleurSpecFeulBed[2]=float(veget3[11])
        absorptionFuelBed[2]=float(veget3[12])
        emissiviteFuelBed[2]=float(veget3[13])
    typeVegetation-=1
    if typeVegetation>0:
        veget4=vegetation['vegetation4'].to_numpy()
        x1veg[3]=float(veget4[0])
        x2veg[3]=float(veget4[1])
        y1veg[3]=float(veget4[2])
        y2veg[3]=float(veget4[3])
        hauteurFlamme[3]=float(veget4[4])
        hauteurFuelBed[3]=float(veget4[5])
        diametreFuelBed[3]=float(veget4[6])
        densitéFuelBed[3]=float(veget4[7])
        chargeSurface[3]=float(veget4[8])
        teneurEnEau[3]=float(veget4[9])
        timeCombustion[3]=float(veget4[10])
        chaleurSpecFeulBed[3]=float(veget4[11])
        absorptionFuelBed[3]=float(veget4[12])
        emissiviteFuelBed[3]=float(veget4[13])

    #lecture de la second feuille de donnees
    # climat=pd.read_excel(file_climat,usecols=[1])    
    ##print(climat)
    clim=climat['valeurs'].to_numpy()    

    timeMax=float(clim[0])
    deltat=float(clim[1])
    deltax=float(clim[2])
    deltay=float(clim[3])
    xDebut=float(clim[4])
    xFin=float(clim[5])
    yDebut=float(clim[6])
    yFin=float(clim[7])
    temperatureAir=float(clim[8])
    vitesseDuVent=float(clim[9])
    directionDuVent=float(clim[10])
    pentex=float(clim[11])
    pentey=float(clim[12])
    temperatureFlamme=float(clim[13])
    temperatureAllumage=float(clim[14])
    temperatureBraise=float(clim[15])
    emissiviteBraise=float(clim[16])
    conductiviteBraise=float(clim[17])
    conductiviteFlamme=float(clim[18])
    viscositeAirChaud=float(clim[19])
    #lecture de la troisieme feuille
    ##print(eclosion)
    nbEclosion=nbEclosion_param
    nbreDepartFeu=nbEclosion
    # eclosion=pd.read_excel(file_eclosion,usecols=[1])

    eclos1=eclosion['valeurs'].to_numpy()

    xEclosion=np.zeros(nbEclosion)
    yEclosion=np.zeros(nbEclosion)
    ieclo=np.zeros(nbEclosion,"int")
    jeclo=np.zeros(nbEclosion,"int")
    # des variables entieres pour l'allumage dynamique
    varN=np.ones(nbEclosion,"int")
    varS=np.ones(nbEclosion,"int")
    varW=np.ones(nbEclosion,"int")
    varE=np.ones(nbEclosion,"int")
    varC=np.ones(nbEclosion,"int")
    cotéAllumé=[]
    timeAllumage=np.zeros(nbEclosion)
    longueurEclosion=np.zeros(nbEclosion)
    xEclosion[0]=float(eclos1[0])
    yEclosion[0]=float(eclos1[1])
    cotéAllumé.append(str(eclos1[2]))
    longueurEclosion[0]=float(eclos1[3])
    timeAllumage[0]=float(eclos1[4])
    xenreg=float(eclos1[5])
    yenreg=float(eclos1[6])
    nbreDepartFeu-=1
    if nbreDepartFeu>0:
        eclos2=eclosion['depart2'].to_numpy()
        xEclosion[1]=float(eclos2[0])
        yEclosion[1]=float(eclos2[1])
        cotéAllumé.append(str(eclos2[2]))
        longueurEclosion[1]=float(eclos2[3])
        timeAllumage[1]=float(eclos2[4])
    nbreDepartFeu-=1
    if nbreDepartFeu>0:
        eclos3=eclosion['depart3'].to_numpy()
        xEclosion[2]=float(eclos3[0])
        yEclosion[2]=float(eclos3[1])
        cotéAllumé.append(str(eclos3[2]))
        longueurEclosion[2]=float(eclos3[3])
        timeAllumage[2]=float(eclos1[4])
    # maillage de la zone de calcul
    coorx=np.arange(xDebut,xFin+deltax,deltax)
    coory=np.arange(yDebut,yFin+deltay,deltay)
    coorz=np.zeros((len(coorx),len(coory)))
    xnormaleCell=np.zeros((len(coorx),len(coory)))
    ynormaleCell=np.zeros((len(coorx),len(coory)))
    znormaleCell=np.zeros((len(coorx),len(coory)))
    #++++++++++++++++++++++++++++++++++++++++
    #for j in np.arange(len()):
    #    for i in np.arange(xDebut,xFin,rapport):
    #        pentexmnt[i,j]=(z[i+1,j]-z[i,j])/(coorx[i+1]-coorx[i])
    #        penteymnt[i,j]=(z[i+1,j]-z[i,j])/(coory[j+1]-coory[j])
    veg=np.zeros((len(coorx),len(coory)),'int')
    proportionEnEau=np.zeros((len(coorx),len(coory)))
    temperatureSite=np.zeros((len(coorx),len(coory)))
    temperatureSite=np.full((len(coorx),len(coory)),temperatureAir,float)
    #distribution de la végétation
    for i in np.arange(len(coorx)):
        for j in np.arange(len(coory)):
            for k in np.arange(nbreVegetation):
                if x1veg[k]<=coorx[i]<=x2veg[k] and\
                    y1veg[k]<=coory[j]<=y2veg[k]:
                        veg[i,j]=k
                        proportionEnEau[i,j]=teneurEnEau[veg[i,j]]
            if timeCombustion[veg[i,j]]==0.:
                temperatureSite[i,j]=-2.
    #reperage des points d'eclosion
    for i in list(range(nbEclosion)):
        ieclo[i]=int(abs(xEclosion[i]-xDebut)//deltax)
        jeclo[i]=int(abs(yEclosion[i]-yDebut)//deltay)
        if ieclo[i]<=max(list(range(len(coorx)))) and \
            jeclo[i]<=max(list(range(len(coory)))):
                if timeCombustion[veg[ieclo[i],jeclo[i]]]==0.:
                    continue
                #siteEnFeu.append([coorx[ieclo[i]],coory[jeclo[i]], \
                #                  timeCombustion[veg[ieclo[i],jeclo[i]]]])
                siteEnFeu.append([ieclo[i],jeclo[i], \
                                timeCombustion[veg[ieclo[i],jeclo[i]]]])
                temperatureSite[ieclo[i],jeclo[i]]=temperatureAllumage
        else:
            print("site en fue n°",i," hors de la zone")
            #break
    print("siteEnFeu=",siteEnFeu)
    #calcul de l'effet des pentes
    #++++Calcul du vecteur normal à la cellule++++
    for i in np.arange(len(coorx)):
        for j in np.arange(len(coory)):
            gamax=float(pentex*np.pi/180.)
            gamay=float(pentey*np.pi/180.)
            xnormaleCell[i,j]=-np.sin(pentex)
            ynormaleCell[i,j]=-np.cos(pentex)*np.sin(pentey)
            znormaleCell[i,j]=np.cos(pentex)*np.cos(pentey)
            #coorx[i]=coorx[i]*np.cos(gamax)-coory[j]*np.sin(gamax)*np.sin(gamay)
            #coory[j]=coory[j]*np.cos(gamay)
            coorz[i,j]=coorx[i]*np.sin(gamax)+coory[j]*np.cos(gamax)*np.sin(gamay)
            normC=float(np.sqrt(xnormaleCell[i,j]**2+ \
                ynormaleCell[i,j]**2+znormaleCell[i,j]**2))
            xnormaleCell[i,j]=float(xnormaleCell[i,j]/normC)
            ynormaleCell[i,j]=float(ynormaleCell[i,j]/normC)
            znormaleCell[i,j]=float(znormaleCell[i,j]/normC)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    print("coordonnées x debut=",coorx[0],"","fin =",coorx[-1])
    print("coordonnées y debut=",coory[0],"","fin =",coory[-1])
    print("coordonnées z debut=",coorz[0,0],"","fin =",coorz[-1,-1])
    #
    for m in np.arange(nbreVegetation):
        if timeCombustion[m]==0.:
            continue
        fractionVolumiq[m]=(chargeSurface[m]/(densitéFuelBed[m]* \
                                            hauteurFuelBed[m]))
        surfaceSpec[m]=(4.*fractionVolumiq[m]/diametreFuelBed[m])
    idistmax=np.zeros(int(timeMax//deltat)+1)
    tempEnreg=np.zeros(int(timeMax//deltat)+1)
    temps=np.zeros(int(timeMax//deltat)+1)
    ienreg=int((xenreg-coorx[0])//deltax)
    jenreg=int((yenreg-coory[0])//deltay)
    ########## Calcul du facteur de forme une fois avant itération temporelle######
    # maillage de la flamme cylindrique                            
    pasAngle=0.1
    pasHauteur=0.1
    diametreFlam=float((deltax+deltay)/2.)    
    Nangle=int(2.*np.pi//pasAngle)+1
    Nhauteur=int(hauteurFlamme.max()//pasHauteur)+1
    NxdomInter=np.zeros(nbreVegetation)
    NydomInter=np.zeros(nbreVegetation)
    #maillage de la circonférence 
    gama=np.arange(0.,2.*np.pi,pasAngle)    
    #maillage de la hauteur
    zprime=np.arange(0.,hauteurFlamme.max()+pasHauteur,pasHauteur)   
    xfl=np.zeros((len(gama),len(zprime)))
    yfl=np.zeros((len(gama),len(zprime)))
    zfl=np.zeros((len(gama),len(zprime)))
    normx=np.zeros((len(gama),len(zprime)))
    normy=np.zeros((len(gama),len(zprime)))
    normz=np.zeros((len(gama),len(zprime)))
    inclinFlamme=np.arctan(1.4*vitesseDuVent/ \
                    np.sqrt(pesanteur*float(hauteurFlamme.max())))
    #coordonnées de la flamme dans le repère du vent 
    for i in np.arange(len(gama)):
        for j in np.arange(len(zprime)):
            xfl[i,j]=0.5*diametreFlam*np.cos(gama[i])    
            yfl[i,j]=0.5*diametreFlam*np.sin(gama[i]) + \
            zprime[j]*np.sin(inclinFlamme)  
            zfl[i,j]=zprime[j]*np.cos(inclinFlamme)

    NxdomInter=int(coefxDomInter*float(hauteurFlamme.max())//deltax) +1
    NydomInter=int(coefyDomInter*float(hauteurFlamme.max())//deltay)+1
    facform=np.zeros((int(2.*NxdomInter)+1,int(NxdomInter+NydomInter)+1))
    for jd in np.arange(-NxdomInter,NxdomInter+1):
        for kd in np.arange(-NxdomInter,NydomInter+1):
            #conversion des indices négatifs en indices positifs
            q1=NxdomInter+jd; q2=kd+NxdomInter
            #indice du centre de la flamme cylindrique
            #pifl=int(NxdomInter[nf]);pjfl=int(NxdomInter[nf])  
            if jd==0 and kd==0:
                continue   
            sizeFlamme=np.pi*(deltax+deltay)*0.5*hauteurFlamme.max() #2.*            
    # la distance cellule flamme - cellule vegetation
            for i in np.arange(len(gama)):
                for j in np.arange(len(zprime)):
                    #la normale à l'élément de surface
                    if i<len(gama)-1:
                        ux=xfl[i+1,j]-xfl[i,j]
                        uy=yfl[i+1,j]-yfl[i,j]
                        uz=zfl[i+1,j]-zfl[i,j]
                    else:
                        ux=(xfl[i,j]-xfl[i-1,j])
                        uy=(yfl[i,j]-yfl[i-1,j])
                        uz=(zfl[i,j]-zfl[i-1,j])
                    norme1=float(np.sqrt(ux**2+uy**2+uz**2))
                    ux=float(ux/norme1)
                    uy=float(uy/norme1)
                    uz=float(uz/norme1)
                    if j<len(zprime)-1:
                        vx=xfl[i,j+1]-xfl[i,j]
                        vy=yfl[i,j+1]-yfl[i,j]
                        vz=zfl[i,j+1]-zfl[i,j]
                    else:
                        vx=(xfl[i,j]-xfl[i,j-1])
                        vy=(yfl[i,j]-yfl[i,j-1])
                        vz=(zfl[i,j]-zfl[i,j-1])
                    norme2=float(np.sqrt(vx**2+vy**2+vz**2))
                    vx=float(vx/norme2)
                    vy=float(vy/norme2)
                    vz=float(vz/norme2)
                    #les coordonnées du vecteur normale
                    normx[i,j]=uy*vz-uz*vy
                    normy[i,j]=uz*vx-ux*vz
                    normz[i,j]=ux*vy-uy*vx
                    norme=float(np.sqrt(normx[i,j]**2+normy[i,j]**2+normz[i,j]**2))
                    if norme==0.:
                        continue
                    normx[i,j]=float(normx[i,j]/norme)
                    normy[i,j]=float(normy[i,j]/norme)
                    normz[i,j]=float(normz[i,j]/norme)
                    xdist=jd*deltax-xfl[i,j]   
                    ydist=kd*deltay-yfl[i,j]                                      
                    zdist=-zfl[i,j]
                    #zdist=coorz[q1,q2]-zfl[i,j]   # a vérifier
                    normCiblFla=float(np.sqrt(xdist**2+ydist**2+zdist**2))
                    xdistN=float(xdist/normCiblFla)
                    ydistN=float(ydist/normCiblFla)
                    zdistN=float(zdist/normCiblFla)
    #calcul des cosinus pour le positionnement
                    #cosTetaCell=xnormaleCell[i,j]*(-xdistN)+ \
                    #ynormaleCell[i,j]*(-ydistN)+ \
                    #znormaleCell[i,j]*(-zdistN)
                    cosTetaCell=-zdistN
                    cosTetaFlam=normx[i,j]*xdistN+normy[i,j]*ydistN+normz[i,j]*zdistN  
    #calcul du facteur de forme dans le quadrant positif
                    if cosTetaCell>0. and cosTetaFlam>0.:
                        facform[q1,q2]+=float(cosTetaCell*cosTetaFlam* \
                                    deltax*deltay*pasAngle*pasHauteur/ \
                                    (np.pi*sizeFlamme*normCiblFla**2))      
                        
    '''                    
    #===représentation 3d
    fig=plt.figure()
    ax=fig.add_subplot(projection='3d')
    ax.quiver(xfl,yfl,zfl,normx,normy,normz,length=0.1,label='Flamme cylindrique')
    plt.legend()
    plt.show()
    #===représentation facteur de forme
    x=np.arange(-NxdomInter*deltax,NxdomInter*deltax+deltax,deltax)
    y=np.arange(-NxdomInter*deltay,NydomInter*deltay+deltay,deltay)
    plt.pcolormesh(x,y,facform.T,cmap="jet")
    plt.colorbar()
    plt.axis('equal')
    plt.title('facteur de forme 2d')
    plt.show()
    '''

    ################### debut de la boucle en temps###########################

    #NOTE: create simulation_dir for all png
    simulation_dir = os.path.join('media', simulation_name,'images')
    os.makedirs(simulation_dir, exist_ok=True)

    with open(f"media/{simulation_name}/contour.txt","r") as fichier1:   #, open("Surface.txt","w") as fichier2: 
        for IT in list(range(1,int(timeMax//deltat)+1)):
            temps[IT]=IT*deltat
    #Calcul de la propagation ##
            DwRad=float(directionDuVent*np.pi/180.)
            for i in np.arange(len(siteEnFeu)):
                dxp=0.;dyp=0.;dx=0.;dy=0.
                ifl=int(siteEnFeu[i][0])   
                jfl=int(siteEnFeu[i][1])
            #determination des sites voisins une fois en debut d'itération
                if float(siteEnFeu[i][2])>=timeCombustion[veg[ifl,jfl]]:
                    #siteVoisin.append([coorx[ifl],coory[jfl]])
                    siteVoisin.append([ifl,jfl])
                    inclinaisonFlamme=np.arctan(1.4*vitesseDuVent/ \
                        np.sqrt(pesanteur*hauteurFlamme[veg[ifl,jfl]]))
                    idebut=int(ifl-int(NxdomInter))   
                    ifin=int(ifl+int(NxdomInter))     
                    jdebut=int(jfl-int(NxdomInter))   
                    jfin=int(jfl+int(NydomInter))     
                    #start=time.time()
                    for jj in list(range(max(jdebut,0),\
                        min(jfin,len(coory)))):
                        for ii in list(range(max(idebut,0),\
                            min(ifin,len(coorx)))):
                            if jj==jfl and ii==ifl:
                                continue
                            if int(timeCombustion[veg[ii,jj]])!=0:
                                dx=(ii-ifl)*deltax
                                dy=(jj-jfl)*deltay
                                dxp=float(-dx*np.cos(DwRad)+dy*np.sin(DwRad))
                                dyp=float(-dx*np.sin(DwRad)-dy*np.cos(DwRad))
                                if dyp<=0.:
                                    dsite=float(np.sqrt((dxp/float(NxdomInter))**2\
                                                        +(dyp/float(NxdomInter))**2))
                                if dyp>0.:
                                    dsite=float(np.sqrt((dxp/float(NxdomInter))**2\
                                                        +(dyp/float(NydomInter))**2))
                                ##if dsite<=float(coefDomInter*hauteurFlamme[veg[ifl,jfl]]):
                                if dsite<=1.:
                                    #siteVoisin[i].append([coorx[ii],coory[jj]])
                                    siteVoisin[i].append([ii,jj])
                #print(time.time()-start)
                dxp=0.;dyp=0.;dx=0.;dy=0.
                siteEnFeu[i][2]-=deltat
                ipl1=ifl+1; imo1=ifl-1; jpl1=jfl+1; jmo1=jfl-1
                if ipl1 in np.arange(len(coorx)) and imo1 in np.arange(len(coorx))\
                    and jpl1 in np.arange(len(coory)) and jmo1 in np.arange(len(coory)):
                        if temperatureSite[ifl,jpl1]>=temperatureAllumage and\
                        temperatureSite[ifl,jmo1]>=temperatureAllumage and\
                        temperatureSite[ipl1,jfl]>=temperatureAllumage and\
                        temperatureSite[imo1,jfl]>=temperatureAllumage and\
                        temperatureSite[ipl1,jpl1]>=temperatureAllumage and\
                        temperatureSite[ipl1,jmo1]>=temperatureAllumage and\
                        temperatureSite[imo1,jpl1]>=temperatureAllumage and\
                        temperatureSite[imo1,jmo1]>=temperatureAllumage:
                            siteEnFeu[i][2]=-0.1                
                if float(siteEnFeu[i][2])<=0.:
                    temperatureSite[ifl,jfl]=-1.
                for j in np.arange(2,len(siteVoisin[i])):
                    #iv=coorx.tolist().index(siteVoisin[i][j][0])
                    #jv=coory.tolist().index(siteVoisin[i][j][1])
                    iv=siteVoisin[i][j][0]
                    jv=siteVoisin[i][j][1]
                    if temperatureSite[iv,jv]>=temperatureAllumage \
                        or temperatureSite[iv,jv]<=0.:
                        continue
                    dx=(iv-ifl)*deltax
                    dy=(jv-jfl)*deltay
                    ##dx=siteVoisin[i][j][0]-siteEnFeu[i][0]
                    ##dy=siteVoisin[i][j][1]-siteEnFeu[i][1]                
                    dxp=float(-dx*np.cos(DwRad)+dy*np.sin(DwRad))
                    dyp=float(-dx*np.sin(DwRad)-dy*np.cos(DwRad))
                    iff=int(dxp//deltax); jff=int(dyp//deltay)
                    q1=NxdomInter+iff; q2=jff+NxdomInter
                    if abs(dxp)<=1.e-10:
                        dxp==0.
                    if abs(dyp)<=1.e-10:
                        dyp==0.
                    DIST=np.sqrt(dxp**2+dyp**2)
                    if dyp>=0.:
                        UW=vitesseDuVent*(dyp/DIST)
                    else:
                        UW=0.
                    inclinaisonFlamme=np.arctan(1.4*vitesseDuVent/ \
                            np.sqrt(pesanteur*hauteurFlamme[veg[ifl,jfl]]))
                    HFL=hauteurFlamme[veg[ifl,jfl]]
                    PHI=fractionVolumiq[veg[iv,jv]]
                    SSP=surfaceSpec[veg[iv,jv]]
                    rocp=chaleurSpecFeulBed[veg[iv,jv]]*PHI* \
                        densitéFuelBed[veg[iv,jv]]
                    rohvap=chaleurVap*PHI*densitéFuelBed[veg[iv,jv]] 
                    FF=facform[q1,q2]
    ######## Calcul des flux #############
                    somme=0.;K1RK=0.;K2RK=0.;K3RK=0.;K4RK=0.
                    QSR=0.;QSR1=0.;QSC=0.;QSC1=0.;QIR=0.;QIR1=0.
                    emissivitéFlamme=1.-np.exp(-0.6*HFL)
                    efl=emissivitéFlamme*sigmaRay*temperatureFlamme**4
                    QSR1=(absorptionFuelBed[veg[iv,jv]]*efl)/ \
                        hauteurFuelBed[veg[iv,jv]]
                    ebraise=emissiviteBraise*sigmaRay*temperatureBraise**4
                    QIR1=0.25*SSP*ebraise
                    QRL1=emissiviteFuelBed[veg[iv,jv]]*sigmaRay/ \
                        hauteurFuelBed[veg[iv,jv]]
            # rayonnement de la flamme
                    QSR=QSR1*FF
            # Convection de surface
                    ReyFl=UW*DIST/viscositeAirChaud
                    KRPfl=0.565*conductiviteFlamme*(ReyFl**0.5)*(prandtl**0.5)
                    QSC1=(KRPfl/(DIST*hauteurFuelBed[veg[iv,jv]]))* \
                        np.exp(-0.3*DIST/HFL)
            # convection interne
                    ReyD=(1.-PHI)*UW*diametreFuelBed[veg[iv,jv]]/viscositeAirChaud
                    ReyD1=ReyD**0.385
                    PR1=prandtl**0.3333
                    KRPB=0.911*SSP*conductiviteBraise*ReyD1*PR1
                    QIC1=(KRPB/diametreFuelBed[veg[iv,jv]])*np.exp(-0.25*SSP*DIST)
            #fin des flux
                    VART=temperatureSite[iv,jv]
                    QIR=QIR1*np.exp(-0.25*SSP*DIST)
                    QRL=-QRL1*(VART**4-temperatureAir**4)
                    QSC=QSC1*(temperatureFlamme-VART)
                    QIC=QIC1*(temperatureBraise-VART)
                    K1RK=float((QSR+QIR+QRL+QSC+QIC)/rocp)
                    K1RKVAP=float((QSR+QIR+QRL+QSC+QIC)/rohvap)
                    VART=copy.deepcopy(temperatureSite[iv,jv]+K1RK*deltat*0.5)
                    QIR=QIR1*np.exp(-0.25*SSP*DIST)
                    QRL=-QRL1*(VART**4-temperatureAir**4)
                    QSC=QSC1*(temperatureFlamme-VART)
                    QIC=QIC1*(temperatureBraise-VART)
                    K2RK=float((QSR+QIR+QRL+QSC+QIC)/rocp)
                    VART=copy.deepcopy(temperatureSite[iv,jv]+K2RK*deltat*0.5)
                    QIR=QIR1*np.exp(-0.25*SSP*DIST)
                    QRL=-QRL1*(VART**4-temperatureAir**4)
                    QSC=QSC1*(temperatureFlamme-VART)
                    QIC=QIC1*(temperatureBraise-VART)
                    K3RK=float((QSR+QIR+QRL+QSC+QIC)/rocp)
                    VART=copy.deepcopy(temperatureSite[iv,jv]+K3RK*deltat)
                    QIR=QIR1*np.exp(-0.25*SSP*DIST)
                    QRL=-QRL1*(VART**4-temperatureAir**4)
                    QSC=QSC1*(temperatureFlamme-VART)
                    QIC=QIC1*(temperatureBraise-VART)
                    K4RK=float((QSR+QIR+QRL+QSC+QIC)/rocp)
                    SOMME=deltat*(K1RK+2.*K2RK+2.*K3RK+K4RK)/6.
                    if proportionEnEau[iv,jv]>0. and temperatureSite[iv,jv]>=373.:
                        proportionEnEau[iv,jv]-=deltat*K1RKVAP
                        SOMME=0.
                    if SOMME<1.e-10:
                        SOMME=0.
                    temperatureSite[iv,jv]+=SOMME
                    if temperatureSite[iv,jv]>=temperatureAllumage:
                        #siteEnFeu.append([coorx[iv],coory[jv],timeCombustion[veg[iv,jv]]])
                        siteEnFeu.append([iv,jv,timeCombustion[veg[iv,jv]]])
                        ###temperatureSite[iv,jv]=temperatureFlamme

            for n1 in np.arange(len(siteEnFeu)):              
                if n1>=len(siteEnFeu):
                    continue
                ipyr=int(siteEnFeu[n1][0]);jpyr=int(siteEnFeu[n1][1])
                xpyr=(coorx[ipyr]-coorx[ieclo[0]])*np.sin(DwRad)
                ypyr=-(coory[jpyr]-coory[jeclo[0]])*np.cos(DwRad)
                idistmax[IT]=max(idistmax[IT],np.sqrt(xpyr**2+ypyr**2))
                if float(siteEnFeu[n1][2])<=0.:
                    siteBrule.append(siteEnFeu[n1])
                    #ib=coorx.tolist().index(siteEnFeu[n1][0])
                    #jb=coory.tolist().index(siteEnFeu[n1][1])
                    #temperatureSite[ib,jb]=1500.
                    temperatureSite[ipyr,jpyr]=-1.
                    del siteEnFeu[n1]    #à revoir apres analyse
                    del siteVoisin[n1]
            print("temps de simulation =",temps[IT],"site en feu=",len(siteEnFeu),\
                "surface brûlés(ha)=",float(len(siteBrule)*deltax*deltay/1000.))
            if temps[IT]%timp==0:
                #fichier1.write(f"ZONE I= {len(siteEnFeu)} F=POINT\n")
                for k in list(range(len(siteEnFeu))):
                    #fichier1.write(f"{float(siteEnFeu[k][0])} {float(siteEnFeu[k][1])}\n")
                    imp=int(siteEnFeu[k][0]);jmp=int(siteEnFeu[k][1])
                    #fichier1.write(f"{coorx[imp]:7.3f} {coory[jmp]:7.3f}\n")
            ##fichier2.write(f"ZONE I= {len(coorx)} J= {len(coory)}\n")
            ##for js in list(range(len(coorx))):
            ##    for ks in list(range(len(coory))):
                    ##fichier2.write(f"{float(coorx[js])} {float(coory[ks])} \
                    ##              {float(temperatureSite[js,ks])}\n")
                    
            #affichage contour de feu
            if temps[IT]%timp==0:
                #plt.subplot(1,2,1)
                fig=plt.figure(figsize=(12,8),dpi=92)
                plt.pcolormesh(coorx,coory,temperatureSite.T,cmap="jet")  
                plt.colorbar()
                plt.title("time(s)="+str(temps[IT]) +\
                        "  and ROS(m/s)="+ str(idistmax[IT]/temps[IT]))
                plt.axis('equal')
                #plt.xlim([coorx[0],coorx[-1]])
                #plt.ylim([coory[0],coory[-1]])


                #NOTE: save on simulation_dir the png item
                file_name = f'simulation_{IT}.png'
                file_path = os.path.join(simulation_dir, file_name)
                plt.savefig(file_path)


                #plt.show()
                plt.close()
            ##if IT%10==0:
            ##    print('vitesse instantanée=',float(idistmax[IT]/temps[IT]))
    ####### Allumage dynamique########
            allumage(siteEnFeu,cotéAllumé,longueurEclosion,nbEclosion,coorx,coory,\
                    varN,varS,varW,varE,varC,timeAllumage,timeCombustion,ieclo,jeclo,\
                    directionDuVent,deltax,deltay,veg,temperatureSite,temperatureAllumage)
            for L in np.arange(nbEclosion):
                varC[L]+=int(longueurEclosion[L]*deltat//timeAllumage[L])
                varN[L]+=int(longueurEclosion[L]*deltat//timeAllumage[L])
                varS[L]+=int(longueurEclosion[L]*deltat//timeAllumage[L])
                varW[L]+=int(longueurEclosion[L]*deltat//timeAllumage[L])
                varE[L]+=int(longueurEclosion[L]*deltat//timeAllumage[L])
            if len(siteEnFeu)<=0:
                break
    print(time.time()-start)      
    #################################fin programme principal######################                  
