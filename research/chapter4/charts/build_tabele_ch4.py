# -*- coding: utf-8 -*-
"""Tabel 1 (LFP vs NMC) si Tabel 2 (matrice de risc) - stil FSEGA, fara note gri."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import textwrap
from pathlib import Path
plt.rcParams.update({"font.family":"DejaVu Sans"})
OUT=str(Path(__file__).resolve().parent)+"/"
C_RED="#C8102E"; C_ORG="#B8860B"; C_GREEN="#2E8B57"; C_LINE="#333333"

# ===================== TABEL 1: LFP vs NMC =====================
head1=["Indicator","BYD Blade (LFP)","Baterii tradiționale (NCM)"]
rows1=[
 ["Chimia celulelor","Litiu–fier–fosfat (LiFePO₄), fără cobalt","Nichel–cobalt–mangan (NCM)"],
 ["Materiale / toxicitate","Materiale mai sustenabile (fier și fosfat)","Cobalt și nichel (resurse limitate)"],
 ["Siguranță (test penetrare cui)","Trece testul fără fum sau flăcări","Risc de incendiu în condiții extreme"],
 ["Stabilitate termică","Temp. de suprafață 30–60 °C","Thermal runaway posibil peste 200 °C"],
 ["Emisii de oxigen","Fără emisii","Eliberare de oxigen la supraîncălzire"],
 ["Durata de viață","Peste 5.000 de cicluri de încărcare","~1.000–2.000 cicluri"],
 ["Degradare în timp","Foarte lentă","Mai rapidă după 3–5 ani"],
 ["Eficiență spațială","+50% față de pachetele tradiționale","Standard"],
]
colx=[0.015,0.340,0.700]
fig,ax=plt.subplots(figsize=(11.4,5.4)); ax.axis("off")
ax.text(0.0,1.085,"Evaluarea comparativă a indicatorilor tehnico-ambientali pe ciclul de viață (LFP vs. NMC)",fontsize=11,fontweight="bold",transform=ax.transAxes,va="bottom")
Y0=0.92; hh=0.085; rh=0.099
ax.plot([0,1],[Y0,Y0],color=C_LINE,lw=1.4,transform=ax.transAxes)
for j,h in enumerate(head1):
    ax.text(colx[j],Y0-hh/2,h,fontsize=10,fontweight="bold",style="italic",transform=ax.transAxes,va="center")
ax.plot([0,1],[Y0-hh,Y0-hh],color=C_LINE,lw=0.8,transform=ax.transAxes)
yb=Y0-hh
for i,r in enumerate(rows1):
    yc=yb-rh*i-rh/2
    ax.text(colx[0],yc,r[0],fontsize=9.4,transform=ax.transAxes,va="center")
    ax.text(colx[1],yc,r[1],fontsize=9.4,transform=ax.transAxes,va="center",color=C_GREEN)
    ax.text(colx[2],yc,r[2],fontsize=9.4,transform=ax.transAxes,va="center",color=C_RED)
ax.plot([0,1],[yb-rh*len(rows1),yb-rh*len(rows1)],color=C_LINE,lw=1.4,transform=ax.transAxes)
fig.savefig(OUT+"4-3_C_tabel_LCA_LFP_NMC.png",bbox_inches="tight",facecolor="white",dpi=150); plt.close(fig); print("scris t1")

# ===================== TABEL 2: Matricea de risc =====================
rows2=[
 ["Exploatarea muncii\n(materii prime)","~70% din cobaltul global provine din RD Congo, cu muncă a copiilor și condiții periculoase documentate în sector.","Ridicat",C_RED,"Amnesty (2024);\nReg. (UE) 2023/1542"],
 ["Guvernanța muncii\nîn fabrici","Lanț valoric integrat vertical (control intern), dar fără audituri sociale independente publice.","Mediu",C_ORG,"BYD (2025)"],
 ["Trasabilitatea /\nîncrederea furnizorilor","Lacună în UE privind verificarea încrederii furnizorilor de componente critice; Cyber Resilience Act abia până la finalul lui 2027.","Ridicat",C_RED,"MERICS (2025)"],
 ["Protecția datelor\npersonale (GDPR)","Localizare, VIN și plăcuțele = date personale; necesită DPIA (art. 35); risc ridicat la transferul în afara vehiculului.","Ridicat",C_RED,"EDPS –\nTechDispatch #3"],
 ["Guvernanța datelor /\ntransfer transfrontalier","Cadru UE fragmentat; datele ne-personale necuprinse; firmele chineze obligate să furnizeze date statului (National Intelligence Law).","Ridicat",C_RED,"MERICS (2025)"],
 ["Conformitate cu\nData Act","Reg. (UE) 2023/2854 aplicabil din 12 sept. 2025; control al utilizatorului asupra datelor de vehicul; BYD a publicat o notificare Data Act.","Mediu /\nîn tranziție",C_ORG,"Comisia Europeană;\nBYD Data Act Notice"],
 ["Pregătirea pentru\npașaportul bateriei","Pașaport digital obligatoriu din 18 feb. 2027 (acumulatori ≥ 2 kWh): trasabilitate, compoziție, amprentă de carbon.","Mediu /\nîn pregătire",C_ORG,"Reg. (UE) 2023/1542"],
]
cx=[0.010,0.225,0.660,0.815]
fig,ax=plt.subplots(figsize=(13.4,7.0)); ax.axis("off")
ax.text(0.0,1.06,"Matricea de risc social, etic și de transparență a lanțului de aprovizionare BYD/EV",fontsize=11,fontweight="bold",transform=ax.transAxes,va="bottom")
head2=["Dimensiune de risc","Constatare-cheie","Nivel de risc","Sursă"]
Y0=0.94; hh=0.075; rh=0.124
ax.plot([0,1],[Y0,Y0],color=C_LINE,lw=1.4,transform=ax.transAxes)
for j,h in enumerate(head2):
    ax.text(cx[j],Y0-hh/2,h,fontsize=9.8,fontweight="bold",style="italic",transform=ax.transAxes,va="center")
ax.plot([0,1],[Y0-hh,Y0-hh],color=C_LINE,lw=0.8,transform=ax.transAxes)
yb=Y0-hh
for i,r in enumerate(rows2):
    yc=yb-rh*i-rh/2
    ax.text(cx[0],yc,r[0],fontsize=8.9,transform=ax.transAxes,va="center",fontweight="bold")
    ax.text(cx[1],yc,textwrap.fill(r[1],58),fontsize=8.5,transform=ax.transAxes,va="center")
    ax.text(cx[2],yc,r[2],fontsize=9.0,transform=ax.transAxes,va="center",fontweight="bold",color=r[3])
    ax.text(cx[3],yc,r[4],fontsize=8.4,transform=ax.transAxes,va="center",color="#444444")
ax.plot([0,1],[yb-rh*len(rows2),yb-rh*len(rows2)],color=C_LINE,lw=1.4,transform=ax.transAxes)
fig.savefig(OUT+"4-3_D_tabel_matrice_risc.png",bbox_inches="tight",facecolor="white",dpi=150); plt.close(fig); print("scris t2")
