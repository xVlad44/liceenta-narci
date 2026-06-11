# -*- coding: utf-8 -*-
"""3.1 - Fluxuri comerciale, SERIE ANUALA 2019-2024. EUR."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from pathlib import Path
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#555555",
    "axes.linewidth":0.8,"axes.grid":True,"grid.color":"#E2E2E2","grid.linewidth":0.7,
    "axes.axisbelow":True,"figure.dpi":150})
OUT=str(Path(__file__).resolve().parent)+"/"
C_EXP="#003399"; C_IMP="#FFB000"; C_EU="#003399"; C_CN="#C8102E"
CNY={2019:7.735491,2020:7.874697,2021:7.628231,2022:7.078800,2023:7.660022,2024:7.787470}
def save(fig,name): fig.savefig(OUT+name,bbox_inches="tight",facecolor="white"); plt.close(fig); print("scris:",name)
def note(ax,txt): ax.text(0.0,-0.16,txt,transform=ax.transAxes,fontsize=8.2,color="#666666",va="top",ha="left")
def footer(fig,ax,shz,src,width=110):
    fh=fig.get_size_inches()[1]; per=(8/72)/fh*1.5
    sh=textwrap.fill(shz,width); sr=textwrap.fill(src,width); n=sh.count("\n")+1
    ax.text(0.0,-0.15,sh,transform=ax.transAxes,fontsize=8.0,color="#333333",va="top",ha="left")
    ax.text(0.0,-0.15-per*n-0.010,sr,transform=ax.transAxes,fontsize=8.0,color="#666666",va="top",ha="left")
def ro(x,d=0): return f"{x:,.{d}f}".replace(",","§").replace(".",",").replace("§",".")

yrs=[2019,2020,2021,2022,2023,2024]
exp_yi=[16708.95,16972.66,19263.41,21944.80,24552.0,28122.0]
imp_yi=[13064.92,13529.86,16172.16,14792.72,14159.0,16926.0]
exp=[exp_yi[i]/10/CNY[yrs[i]] for i in range(6)]
imp=[imp_yi[i]/10/CNY[yrs[i]] for i in range(6)]
fig,ax=plt.subplots(figsize=(9.6,5.2)); x=np.arange(6); w=0.40
ax.bar(x-w/2,exp,w,label="Exporturi",color=C_EXP); ax.bar(x+w/2,imp,w,label="Importuri",color=C_IMP)
for i in range(6):
    ax.text(x[i]-w/2,exp[i]+4,ro(exp[i]),ha="center",va="bottom",fontsize=8.6,fontweight="bold")
    ax.text(x[i]+w/2,imp[i]+4,ro(imp[i]),ha="center",va="bottom",fontsize=8.6,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,400)
ax.set_title("Comerțul exterior de bunuri al Shenzhenului, 2019–2024",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper left",frameon=False)
note(ax,"Sursă: Biroul Municipal de Statistică Shenzhen, Comunicatele statistice anuale 2019–2024. Conversie EUR la cursul mediu anual de referință BCE.")
save(fig,"3-1_A_comert_total_shenzhen.png")

imp_cn=[363.472,384.970,472.491,627.766,520.447,519.007]
exp_cn=[198.486,202.786,223.458,230.402,223.436,213.219]
fig,ax=plt.subplots(figsize=(9.6,5.4)); x=np.arange(6)
ax.plot(x,imp_cn,marker="o",lw=2.6,color=C_CN,label="Importuri UE din China")
ax.plot(x,exp_cn,marker="s",lw=2.6,color=C_EU,label="Exporturi UE către China")
for i in range(6):
    ax.text(x[i],imp_cn[i]+14,ro(imp_cn[i]),ha="center",fontsize=8.6,color=C_CN,fontweight="bold")
    ax.text(x[i],exp_cn[i]-26,ro(exp_cn[i]),ha="center",fontsize=8.6,color=C_EU,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,700)
ax.set_title("Comerțul bilateral de bunuri UE–China, 2019–2024 (miliarde EUR)",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper left",frameon=False)
footer(fig,ax,"Ponderea Shenzhenului: din comerțul UE–China, zona Shenzhen reprezintă ≈ 7,8% (≈ 57 mld EUR în 2024); UE = al 5-lea partener comercial al Shenzhenului, cu 9,9%.","Sursă: Comisia Europeană, DG Comerț / Eurostat COMEXT (nivel UE–China); Vama Shenzhen, analiza anuală 2024 (ponderea Shenzhenului).")
save(fig,"3-1_B_comert_china_ue.png")

fig,ax=plt.subplots(figsize=(7.0,5.6))
ax.pie([9.9,90.1],colors=[C_EU,"#D9D9D9"],startangle=90,counterclock=False,wedgeprops=dict(width=0.42,edgecolor="white"))
ax.text(0,0.12,"9,9%",ha="center",fontsize=26,fontweight="bold",color=C_EU)
ax.text(0,-0.16,"UE în comerțul\ntotal al Shenzhenului",ha="center",fontsize=10)
ax.set_title("UE – al 5-lea partener comercial al Shenzhenului (2024)",fontsize=12,fontweight="bold")
ax.text(0,-1.35,"Sursă: Vama Shenzhen, 2025 (analiza anuală 2024). Conversie EUR la cursul mediu anual de referință BCE 2024.",ha="center",fontsize=7.8,color="#666666")
save(fig,"3-1_F_pozitie_UE.png")

# I) Relatii comerciale UE-China 2000-2010 (mld EUR)
yrs_hist=list(range(2000,2011))
exp_hist=[25.8,30.6,35.0,41.4,48.3,51.8,63.7,71.9,78.4,82.4,113.1]
imp_hist=[74.6,82.0,90.1,106.2,128.5,160.3,194.9,232.6,247.9,214.1,281.9]
bal_hist=[-48.7,-51.3,-55.0,-64.7,-80.2,-108.5,-131.1,-160.7,-169.5,-131.7,-168.6]
fig,ax=plt.subplots(figsize=(11.0,5.4)); x=np.arange(11); w=0.24
ax.bar(x-w,exp_hist,w,label="Exporturi UE către China",color=C_EXP)
ax.bar(x,imp_hist,w,label="Importuri UE din China",color=C_IMP)
ax.bar(x+w,bal_hist,w,label="Sold comercial",color=C_CN)
ax.axhline(0,color="#555555",linewidth=0.9,zorder=3)
ax.set_xticks(x); ax.set_xticklabels(yrs_hist); ax.set_ylabel("Miliarde EUR")
ax.set_ylim(-200,320)
ax.set_title("Relațiile comerciale UE–China, 2000–2010 (miliarde EUR)",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper left",frameon=False,fontsize=9)
note(ax,"Sursă: Parlamentul European (Europarl).")
save(fig,"3-1_I_comert_china_ue_2000_2010.png")
print("gata 3.1 baza")
