# -*- coding: utf-8 -*-
"""3.3 – C-D si transfer de tehnologie. Grafice cu O SINGURA moneda: EUR."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#555555",
    "axes.linewidth":0.8,"axes.grid":True,"grid.color":"#E2E2E2","grid.linewidth":0.7,
    "axes.axisbelow":True,"figure.dpi":150})
OUT="/sessions/friendly-beautiful-babbage/mnt/liceenta bixi/research/chapter3/charts/"
C_EU="#003399"; C_US="#C8102E"; C_ACC="#2E8B57"; C_GOLD="#FFB000"
CNY={2019:7.735491,2020:7.874697,2021:7.628231,2022:7.078800,2023:7.660022,2024:7.787470}
def save(fig,name): fig.savefig(OUT+name,bbox_inches="tight",facecolor="white"); plt.close(fig); print("scris:",name)
def note(ax,txt): ax.text(0.0,-0.17,txt,transform=ax.transAxes,fontsize=8.2,color="#666666",va="top",ha="left")
def ro(x,d=1): return f"{x:,.{d}f}".replace(",","§").replace(".",",").replace("§",".")

# L) Cheltuieli R&D Shenzhen 2019-2024 (EUR) + intensitate (% PIB)
yrs=[2019,2020,2021,2022,2023,2024]
rmb_mld=[132.8,151.081,168.215,188.049,223.661,245.307]   # mld RMB
eur=[rmb_mld[i]/CNY[yrs[i]] for i in range(6)]
inten=[4.93,5.46,5.49,5.81,6.46,6.67]
fig,ax=plt.subplots(figsize=(9.4,5.3)); x=np.arange(6)
ax.bar(x,eur,color=C_EU,width=0.58,label="Cheltuieli R&D (mld EUR)")
for i in range(6): ax.text(x[i],eur[i]-1.6,ro(eur[i],1),ha="center",fontsize=9.2,fontweight="bold",color="white")
ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel("Cheltuieli R&D (miliarde EUR)"); ax.set_ylim(0,38)
ax2=ax.twinx(); ax2.plot(x,inten,color=C_GOLD,marker="o",lw=2.4,label="Intensitate R&D (% din PIB)")
for i in range(6): ax2.text(x[i],inten[i]+0.18,ro(inten[i],2)+"%",ha="center",fontsize=8.6,color="#9a6b00",fontweight="bold")
ax2.set_ylabel("Intensitate R&D (% din PIB local)"); ax2.set_ylim(0,8); ax2.grid(False)
ax.set_title("Cheltuielile de cercetare-dezvoltare ale Shenzhenului, 2019–2024",fontsize=12.5,fontweight="bold")
l1,la1=ax.get_legend_handles_labels(); l2,la2=ax2.get_legend_handles_labels()
ax.legend(l1+l2,la1+la2,loc="upper left",frameon=False,fontsize=9)
note(ax,"Sursă: Biroul Municipal de Statistică Shenzhen / Guvernul Shenzhen, Comunicatele privind investiția în C-D 2019–2024 (2022: Comunicatul provincial Guangdong). 2019 = valoare preliminară. Conversie EUR la cursul mediu anual de referință BCE.")
save(fig,"3-3_L_rd_total_intensitate.png")

# M) R&D Shenzhen pe tip de activitate (2021) – EUR
fig,ax=plt.subplots(figsize=(7.8,5.8))
tip=["Dezvoltare experimentală","Cercetare aplicată","Cercetare fundamentală"]
share=[83.6,9.1,7.3]; eurv=[140.707/CNY[2021],15.306/CNY[2021],12.202/CNY[2021]]
cols=[C_EU,"#5B7FB9","#A9C0E0"]
ax.pie(share,colors=cols,startangle=90,counterclock=False,wedgeprops=dict(edgecolor="white",linewidth=1.5))
ax.legend([f"{tip[i]}: {ro(share[i],1)}%  ({ro(eurv[i],1)} mld EUR)" for i in range(3)],
          loc="lower center",bbox_to_anchor=(0.5,-0.24),frameon=False,fontsize=9.4)
ax.set_title("Structura cheltuielilor R&D ale Shenzhenului pe tip de activitate (2021)",fontsize=12.5,fontweight="bold")
ax.text(0,-1.30,"Sursă: Biroul Municipal de Statistică Shenzhen, Comunicatul privind investiția în C-D 2021. Defalcarea pe tip nu este\ncomparabilă între ani (revizuire metodologică a cercetării fundamentale). Conversie EUR la cursul mediu anual BCE 2021.",
        ha="center",fontsize=7.8,color="#666666")
save(fig,"3-3_M_rd_pe_tip_2021.png")

# N) Publicari de brevete pe destinatie (2024) – numar (fara moneda)
fig,ax=plt.subplots(figsize=(8.4,5.0))
dest=["Total publicări\nîn străinătate","SUA","Europa","din care: acordate\nîn Europa"]
val=[76440,18106,10737,3386]; cols=["#7A7A7A",C_US,C_EU,"#6699CC"]
ax.bar(dest,val,color=cols,width=0.6)
for i,v in enumerate(val): ax.text(i,v+900,f"{v:,}".replace(",","."),ha="center",fontsize=9.5,fontweight="bold")
ax.set_ylabel("Număr de brevete"); ax.set_ylim(0,85000)
ax.set_title("Publicările de brevete ale Shenzhenului în străinătate pe destinație (2024)",fontsize=12.5,fontweight="bold")
note(ax,"Sursă: Administrația pentru Reglementarea Pieței Shenzhen, Raportul de analiză statistică a datelor de brevete 2024. Instantaneu pentru anul 2024.")
save(fig,"3-3_N_brevete_destinatie.png")

# O) Cooperarea programatica UE-China pe teme (calitativ)
fig,ax=plt.subplots(figsize=(9.6,5.4)); ax.axis("off")
ax.set_title("Cooperarea programatică UE–China în cercetare, pe teme și perioade",
             fontsize=12.5,fontweight="bold",pad=16)
rows=[("Horizon 2020\n(2016)","Inițiativă-flagship UE–China în aviație –\n4 acțiuni comune de cercetare (2016)","#EEF3FA",C_EU),
      ("Horizon Europe\n(din 2021)","Două inițiative-flagship încurajate: (1) Alimentație, agricultură\nși biosoluții; (2) Schimbări climatice și biodiversitate","#E8F3EC",C_ACC),
      ("Mecanism de\ncofinanțare (2021–2024)","Aranjament administrativ (apr. 2022): Ministerul chinez al Științei\ncofinanțează participarea entităților din China la cele două flagship-uri","#FFF6E5",C_GOLD)]
y=0.74
for tag,txt,bg,ec in rows:
    ax.add_patch(plt.Rectangle((0.03,y-0.13),0.22,0.16,transform=ax.transAxes,color=bg,ec=ec,lw=1.4))
    ax.text(0.14,y-0.05,tag,ha="center",va="center",fontsize=9.6,fontweight="bold",transform=ax.transAxes)
    ax.add_patch(plt.Rectangle((0.28,y-0.13),0.69,0.16,transform=ax.transAxes,color=bg,ec=ec,lw=1.0))
    ax.text(0.295,y-0.05,txt,ha="left",va="center",fontsize=9.0,transform=ax.transAxes)
    y-=0.22
ax.text(0.5,0.02,"Sursă: Comisia Europeană – International cooperation with China in research and innovation.",
        ha="center",fontsize=8.4,color="#666666",transform=ax.transAxes)
save(fig,"3-3_O_cooperare_teme.png")
print("=== 3.3 gata (EUR) ===")
