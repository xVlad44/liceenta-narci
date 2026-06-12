# -*- coding: utf-8 -*-
"""Capitolul 4 - Studiu de caz BYD. Date verificate in surse primare."""
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
C_EU="#003399"; C_CN="#C8102E"; C_GOLD="#FFB000"; C_GREEN="#2E8B57"; C_GRAY="#7A7A7A"
def save(fig,name): fig.savefig(OUT+name,bbox_inches="tight",facecolor="white"); plt.close(fig); print("scris:",name)
def note(ax,txt): ax.text(0.0,-0.16,txt,transform=ax.transAxes,fontsize=8.2,color="#666666",va="top",ha="left")
def footer(fig,ax,top,src,width=112,y0=-0.15):
    fh=fig.get_size_inches()[1]; per=(8/72)/fh*1.5
    t=textwrap.fill(top,width); s=textwrap.fill(src,width); n=t.count("\n")+1
    ax.text(0.0,y0,t,transform=ax.transAxes,fontsize=8.0,color="#333333",va="top",ha="left")
    ax.text(0.0,y0-per*n-0.010,s,transform=ax.transAxes,fontsize=8.0,color="#666666",va="top",ha="left")
def ro(x,d=1): return f"{x:,.{d}f}".replace(",","§").replace(".",",").replace("§",".")

# ===== 4-1_A: Tarife compensatorii UE (provizorii vs definitive) =====
cat=["BYD","Geely","SAIC","Alți\ncooperanți","Necooperanți"]
prov=[17.4,19.9,37.6,20.8,37.6]; defi=[17.0,18.8,35.3,20.7,35.3]
fig,ax=plt.subplots(figsize=(9.6,5.4)); x=np.arange(5); w=0.38
ax.bar(x-w/2,prov,w,label="Provizorii (iul. 2024)",color=C_GOLD)
ax.bar(x+w/2,defi,w,label="Definitive (oct. 2024)",color=C_CN)
for i in range(5):
    ax.text(x[i]-w/2,prov[i]+0.4,ro(prov[i],1)+"%",ha="center",fontsize=8.6,fontweight="bold")
    ax.text(x[i]+w/2,defi[i]+0.4,ro(defi[i],1)+"%",ha="center",fontsize=8.6,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(cat); ax.set_ylabel("Taxă compensatorie (%)"); ax.set_ylim(0,42)
ax.set_title("Taxele compensatorii ale UE asupra vehiculelor electrice din China",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper left",frameon=False)
footer(fig,ax,"Tesla (Shanghai), după examinare individuală: 7,8% (definitiv). Taxele se aplică suplimentar față de taxa vamală standard de 10% pentru autoturisme.","Sursă: Comisia Europeană — Reg. de punere în aplicare (UE) 2024/1866 (provizorii) și (UE) 2024/2754 (definitive).")
save(fig,"4-1_A_tarife_compensatorii.png")

# ===== 4-1_B: Cresterea BYD in Europa (ian.-sept. 2024 vs 2025) =====
fig,ax=plt.subplots(figsize=(8.2,5.4))
vol=[29579,119085]; lab=["ian.–sept. 2024","ian.–sept. 2025"]
b=ax.bar(lab,vol,color=[C_GRAY,C_CN],width=0.55)
for i,v in enumerate(vol): ax.text(i,v+2500,f"{v:,}".replace(",","."),ha="center",fontsize=11,fontweight="bold")
ax.text(0,vol[0]*0.5,"cotă 1,4%",ha="center",color="white",fontsize=10,fontweight="bold")
ax.text(1,vol[1]*0.5,"cotă 4,4%",ha="center",color="white",fontsize=10,fontweight="bold")
ax.set_ylabel("Vehicule electrice înmatriculate (BEV+PHEV)"); ax.set_ylim(0,140000)
ax.set_title("Vânzările BYD pe piața europeană de vehicule electrice (+302,6%)",fontsize=12,fontweight="bold")
footer(fig,ax,"În T3 2025 cota BYD a urcat la 4,8% (de la 1,8% în T3 2024). Modelul Seal U (PHEV) a fost cel mai vândut plug-in din Europa în primele 9 luni (45.837 unități).","Sursă: Autovista24 / EV Volumes (noiembrie 2025).",y0=-0.17)
save(fig,"4-1_B_byd_crestere_cota.png")

# ===== 4-1_C: Clasamentul marcilor EV in Europa (ian.-sept. 2025) =====
fig,ax=plt.subplots(figsize=(9.4,5.6))
br=["Volkswagen","BMW","Mercedes-Benz","Tesla","Audi","Volvo","Škoda","BYD"]
vv=[305746,245276,185230,172582,151005,147339,145385,119085]
cols=[C_GRAY]*7+[C_CN]
ax.barh(br[::-1],vv[::-1],color=cols[::-1],height=0.66)
for i,v in enumerate(vv[::-1]): ax.text(v+3000,i,f"{v:,}".replace(",","."),va="center",fontsize=9,fontweight="bold")
ax.set_xlabel("Vehicule electrice înmatriculate (BEV+PHEV)"); ax.set_xlim(0,360000)
ax.set_title("BYD în top 10 mărci de vehicule electrice din Europa (ian.–sept. 2025)",fontsize=12,fontweight="bold")
note(ax,"Sursă: Autovista24 / EV Volumes (noiembrie 2025). BYD = locul 8, cu cea mai mare creștere din top 10 (+302,6%).")
save(fig,"4-1_C_byd_clasament_marci.png")

# ===== 4-1_D: Lant valoric integrat BYD vs constructori UE =====
fig,ax=plt.subplots(figsize=(9.6,5.4)); ax.axis("off")
ax.set_title("Lanțul valoric: integrare verticală BYD vs. constructorii europeni",fontsize=12.5,fontweight="bold",pad=14)
comp=["Baterii","Motoare electrice","Controlere electronice","Semiconductori"]
ax.text(0.46,0.90,"BYD",ha="center",fontsize=12,fontweight="bold",color=C_CN,transform=ax.transAxes)
ax.text(0.78,0.90,"Constructori UE",ha="center",fontsize=12,fontweight="bold",color=C_EU,transform=ax.transAxes)
for i,c in enumerate(comp):
    y=0.76-i*0.16
    ax.text(0.02,y,c,ha="left",va="center",fontsize=10.5,transform=ax.transAxes)
    ax.add_patch(plt.Rectangle((0.34,y-0.055),0.24,0.11,transform=ax.transAxes,color="#E8F3EC",ec=C_GREEN))
    ax.text(0.46,y,"producție internă",ha="center",va="center",fontsize=9.2,color=C_GREEN,fontweight="bold",transform=ax.transAxes)
    ax.add_patch(plt.Rectangle((0.66,y-0.055),0.24,0.11,transform=ax.transAxes,color="#FBE9EC",ec=C_CN))
    ax.text(0.78,y,"furnizori externi",ha="center",va="center",fontsize=9.2,color=C_CN,fontweight="bold",transform=ax.transAxes)
ax.text(0.0,0.04,textwrap.fill("UE asigură doar ~7% din producția globală de baterii; peste 20% din cererea europeană de baterii este acoperită din importuri, iar China și SUA dețin 87% din capacitatea globală de producție upstream.",118),
        ha="left",va="top",fontsize=8.2,color="#333333",transform=ax.transAxes)
ax.text(0.0,-0.10,"Sursă: ACEA (2025), Fact sheet: EU battery supply chain and import reliance; BYD (2022).",ha="left",fontsize=8.0,color="#666666",transform=ax.transAxes)
save(fig,"4-1_D_lant_valoric.png")

# ===== 4-3_A: Mix energetic China vs UE (2024) =====
reg=["China","Uniunea Europeană"]
carbune=[58,10]; gaz=[3,19]; regen=[34,47]; nuclear=[5,24]
fig,ax=plt.subplots(figsize=(9.4,4.6)); yps=[1,0]
ax.barh(yps,carbune,color="#4D4D4D",label="Cărbune")
ax.barh(yps,gaz,left=carbune,color=C_GOLD,label="Gaz și alți combustibili fosili")
ax.barh(yps,regen,left=np.array(carbune)+np.array(gaz),color=C_GREEN,label="Regenerabile (hidro, eolian, solar, bio)")
ax.barh(yps,nuclear,left=np.array(carbune)+np.array(gaz)+np.array(regen),color=C_EU,label="Nuclear")
for j in range(2):
    seg=[(carbune[j],0),(gaz[j],carbune[j]),(regen[j],carbune[j]+gaz[j]),(nuclear[j],carbune[j]+gaz[j]+regen[j])]
    for val,left in seg:
        if val>=4: ax.text(left+val/2,yps[j],f"{val}%",ha="center",va="center",fontsize=9,color="white",fontweight="bold")
ax.set_yticks(yps); ax.set_yticklabels(reg,fontsize=11); ax.set_xlim(0,100); ax.set_xlabel("% din producția de electricitate (2024)")
ax.set_title("Mixul de producție a electricității: China vs. UE (2024)",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.18),ncol=2,frameon=False,fontsize=8.8)
ax.text(0.0,-0.46,"Sursă: Ember, Global/European Electricity Review 2025 (date 2024). Provincia Guangdong (sediul BYD) rămâne mai dependentă de cărbune decât media națională.",transform=ax.transAxes,fontsize=8.0,color="#666666",va="top")
save(fig,"4-3_A_mix_energetic.png")

# ===== 4-3_B: Emisii CO2 pe ciclu de viata BEV vs benzina (UE) =====
fig,ax=plt.subplots(figsize=(7.6,5.2))
v=[63,235]; labs=["Vehicul electric\ncu baterie (BEV)","Vehicul cu motor\ncu ardere (benzină)"]
ax.bar(labs,v,color=[C_GREEN,C_GRAY],width=0.55)
for i,val in enumerate(v): ax.text(i,val+5,str(val)+" g",ha="center",fontsize=12,fontweight="bold")
ax.annotate("−73%",xy=(0,63),xytext=(0.5,150),fontsize=13,fontweight="bold",color=C_CN,ha="center")
ax.set_ylabel("Emisii CO₂e pe ciclu de viață (g/km)"); ax.set_ylim(0,260)
ax.set_title("Emisiile de CO₂ pe ciclu de viață: BEV vs. benzină în UE (2025)",fontsize=12,fontweight="bold")
note(ax,"Sursă: ICCT (2025), Life-cycle greenhouse gas emissions from passenger cars in the European Union. Valori pentru rețeaua electrică medie a UE.")
save(fig,"4-3_B_co2_km.png")
print("gata cap.4")
