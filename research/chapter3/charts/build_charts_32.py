# -*- coding: utf-8 -*-
"""3.2 - ISD, SERIE ANUALA 2019-2024 + cheltuieli R&D UE. EUR."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import textwrap
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#555555",
    "axes.linewidth":0.8,"axes.grid":True,"grid.color":"#E2E2E2","grid.linewidth":0.7,
    "axes.axisbelow":True,"figure.dpi":150})
OUT="/sessions/friendly-beautiful-babbage/mnt/liceenta bixi/research/chapter3/charts/"
C_CN="#C8102E"; C_EU="#003399"; C_ACC="#2E8B57"; C_GOLD="#FFB000"
CNY={2023:7.660022,2024:7.787470}; USD={2019:1.119475,2020:1.142196,2021:1.182740,2022:1.053049}
def save(fig,name): fig.savefig(OUT+name,bbox_inches="tight",facecolor="white"); plt.close(fig); print("scris:",name)
def note(ax,txt): ax.text(0.0,-0.16,txt,transform=ax.transAxes,fontsize=8.2,color="#666666",va="top",ha="left")
def footer(fig,ax,top,src,width=112):
    fh=fig.get_size_inches()[1]; per=(8/72)/fh*1.5
    t=textwrap.fill(top,width); s=textwrap.fill(src,width); n=t.count("\n")+1
    ax.text(0.0,-0.15,t,transform=ax.transAxes,fontsize=8.0,color="#333333",va="top",ha="left")
    ax.text(0.0,-0.15-per*n-0.010,s,transform=ax.transAxes,fontsize=8.0,color="#666666",va="top",ha="left")
def ro(x,d=1): return f"{x:,.{d}f}".replace(",","§").replace(".",",").replace("§",".")

yrs=[2019,2020,2021,2022,2023,2024]

# G) Proiecte noi de ISD in Shenzhen 2019-2024 (numar) + pondere UE
fig,ax=plt.subplots(figsize=(9.2,5.2))
proj=[5867,4434,5788,4289,8002,9738]
ax.bar([str(y) for y in yrs],proj,color=C_ACC,width=0.6)
for i,v in enumerate(proj): ax.text(i,v+150,f"{v:,}".replace(",","."),ha="center",fontsize=9.5,fontweight="bold")
ax.set_ylabel("Număr de proiecte"); ax.set_ylim(0,11000)
ax.set_title("Proiecte noi de investiții străine directe în Shenzhen, 2019–2024",fontsize=12.5,fontweight="bold")
footer(fig,ax,"Ponderea UE: Shenzhen nu publică ISD pe țări de origine (capital majoritar din Hong Kong). La nivel China, stocul ISD al UE în China = 239,3 mld EUR în 2024, ≈ 7% din stocul total de ISD intrate în China (≈ 3.660 mld USD).","Sursă: Biroul Municipal de Statistică Shenzhen, Comunicatele 2019–2024; DG Comerț 2024 și UNCTAD WIR 2024 (ponderea UE). Definiția proiectelor ajustată în 2023.")
save(fig,"3-2_G_proiecte_isd_shenzhen.png")

# H) ISD efectiv utilizata in Shenzhen 2019-2024 (EUR)
fig,ax=plt.subplots(figsize=(9.2,5.2))
eur=[7.809/USD[2019],8.683/USD[2020],10.965/USD[2021],10.97/USD[2022],62.62/CNY[2023],44.142/CNY[2024]]
ax.bar([str(y) for y in yrs],eur,color=C_EU,width=0.6)
for i,v in enumerate(eur): ax.text(i,v+0.15,ro(v,2),ha="center",fontsize=9.3,fontweight="bold")
ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,12)
ax.set_title("ISD efectiv utilizată în Shenzhen, 2019–2024 (miliarde EUR)",fontsize=12.5,fontweight="bold")
note(ax,"Sursă: Biroul Municipal de Statistică Shenzhen, Comunicatele statistice anuale 2019–2024. Notă: sursa raportează 2019–2022 în USD și 2023–2024 în RMB; conversie EUR la cursul mediu anual de referință BCE (comparabilitate orientativă).")
save(fig,"3-2_H_isd_efectiv_shenzhen.png")

# I) Stocuri ISD UE-China 2024 (EUR)
fig,ax=plt.subplots(figsize=(7.6,5.0))
val=[239.3,79.8]
ax.bar(["Stoc ISD al UE\nîn China","Stoc ISD al Chinei\nîn UE"],val,color=[C_EU,C_CN],width=0.55)
for i,v in enumerate(val): ax.text(i,v+4,ro(v,1)+" mld EUR",ha="center",fontsize=10,fontweight="bold")
ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,270)
ax.set_title("Stocurile de ISD UE–China, 2024",fontsize=12.5,fontweight="bold")
note(ax,"Sursă: Comisia Europeană, DG Comerț — pagina „EU trade relations with China” (facts & figures, 2024).")
save(fig,"3-2_I_stocuri_isd.png")

# J) Fluxuri ISD UE-China 2023 (EUR)
fig,ax=plt.subplots(figsize=(7.6,5.0))
val=[10.1,6.4]
ax.bar(["Flux ISD\nUE → China","Flux ISD\nChina → UE"],val,color=[C_EU,C_CN],width=0.55)
for i,v in enumerate(val): ax.text(i,v+0.2,ro(v,1)+" mld EUR",ha="center",fontsize=10,fontweight="bold")
ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,12)
ax.set_title("Fluxurile anuale de ISD UE–China, 2023",fontsize=12.5,fontweight="bold")
note(ax,"Sursă: Comisia Europeană, DG Comerț — pagina „EU trade relations with China” (facts & figures, 2023).")
save(fig,"3-2_J_fluxuri_isd.png")

# K) Tipologia sectoriala (calitativ)
fig,ax=plt.subplots(figsize=(9.6,5.2)); ax.axis("off")
ax.set_title("Tipologia sectorială a ISD UE–China (orientări recente)",fontsize=12.5,fontweight="bold",pad=18)
eu_sect=["Automobile","Farmaceutice și biotehnologie","Materiale de bază"]
cn_sect=["Automobile","Divertisment, media și educație","Energie și materiale de bază"]
ax.text(0.25,0.86,"ISD ale UE în China",ha="center",fontsize=12,fontweight="bold",color=C_EU,transform=ax.transAxes)
ax.text(0.75,0.86,"ISD ale Chinei în UE",ha="center",fontsize=12,fontweight="bold",color=C_CN,transform=ax.transAxes)
for i,s in enumerate(eu_sect):
    ax.add_patch(plt.Rectangle((0.04,0.62-i*0.16),0.42,0.12,transform=ax.transAxes,color="#E8EDF7",ec=C_EU))
    ax.text(0.25,0.68-i*0.16,s,ha="center",va="center",fontsize=10.5,transform=ax.transAxes)
for i,s in enumerate(cn_sect):
    ax.add_patch(plt.Rectangle((0.54,0.62-i*0.16),0.42,0.12,transform=ax.transAxes,color="#FBE9EC",ec=C_CN))
    ax.text(0.75,0.68-i*0.16,s,ha="center",va="center",fontsize=10.5,transform=ax.transAxes)
ax.text(0.5,0.04,"Sursă: Comisia Europeană, DG Comerț — pagina „EU trade relations with China” (orientarea sectorială recentă a investițiilor).",
        ha="center",fontsize=8.4,color="#666666",transform=ax.transAxes)
save(fig,"3-2_K_tipologie_sectoriala.png")

# L) Cheltuieli totale de R&D ale UE 2019-2024 (EUR) + intensitate (% PIB)
gerd=[311.657,309.444,331.032,359.342,389.184,403.270]
inten=[2.21,2.28,2.24,2.22,2.26,2.24]
fig,ax=plt.subplots(figsize=(9.4,5.3)); x=np.arange(6)
ax.bar(x,gerd,color=C_EU,width=0.58,label="Cheltuieli R&D UE (mld EUR)")
for i in range(6): ax.text(x[i],gerd[i]-22,ro(gerd[i],0),ha="center",fontsize=9.0,fontweight="bold",color="white")
ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel("Cheltuieli R&D (miliarde EUR)"); ax.set_ylim(0,470)
ax2=ax.twinx(); ax2.plot(x,inten,color=C_GOLD,marker="o",lw=2.4,label="Intensitate R&D (% din PIB)")
for i in range(6): ax2.text(x[i],inten[i]+0.06,ro(inten[i],2)+"%",ha="center",fontsize=8.6,color="#9a6b00",fontweight="bold")
ax2.set_ylabel("Intensitate R&D (% din PIB)"); ax2.set_ylim(0,3.3); ax2.grid(False)
ax.set_title("Cheltuielile totale de cercetare-dezvoltare ale UE, 2019–2024",fontsize=12.5,fontweight="bold")
l1,la1=ax.get_legend_handles_labels(); l2,la2=ax2.get_legend_handles_labels()
ax.legend(l1+l2,la1+la2,loc="upper left",frameon=False,fontsize=9)
note(ax,"Sursă: Eurostat, „Gross domestic expenditure on R&D (GERD)”, set de date rd_e_gerdtot (DOI 10.2908/RD_E_GERDTOT), UE-27.")
save(fig,"3-2_L_cheltuieli_rd_ue.png")
print("gata 3.2")
