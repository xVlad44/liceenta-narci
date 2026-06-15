# -*- coding: utf-8 -*-
"""Tabel 2 - Evolutia vanzarilor si cotei BYD in UE (ACEA, 2024-2025). Stil FSEGA."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import textwrap
from pathlib import Path
plt.rcParams.update({"font.family":"DejaVu Sans"})
OUT=str(Path(__file__).resolve().parent)+"/"

head=["Anul fiscal","Autoturisme noi\nînmatriculate în UE (unități)","Cotă din piața\nauto a UE (%)","Variație\nanuală (%)"]
rows=[
 ["2024","39.303","0,4%","—"],
 ["2025","128.827","1,2%","+227,8%"],
]
xcol=[0.02,0.30,0.62,0.84]
fig,ax=plt.subplots(figsize=(10.4,3.5)); ax.axis("off")
ax.text(0.0,1.14,"Tabel 2.",fontsize=11,fontweight="bold",transform=ax.transAxes,va="bottom")
ax.text(0.105,1.14,"Evoluția vânzărilor și a cotei de piață BYD în Uniunea Europeană (2024–2025)",fontsize=11,fontweight="bold",transform=ax.transAxes,va="bottom")
ax.text(0.0,1.05,"Tabelul prezintă înmatriculările de autoturisme noi BYD și ponderea de piață în Uniunea Europeană.",fontsize=9.2,style="italic",color="#333333",transform=ax.transAxes,va="bottom")
top=0.86; rh=0.20
ax.plot([0,1],[top+0.09,top+0.09],color="#333333",lw=1.3,transform=ax.transAxes)
for j,h in enumerate(head):
    ax.text(xcol[j],top,h,fontsize=9.8,fontweight="bold",style="italic",transform=ax.transAxes,va="center")
ax.plot([0,1],[top-0.10,top-0.10],color="#333333",lw=0.9,transform=ax.transAxes)
y=top-0.10-rh
for r in rows:
    for j,c in enumerate(r):
        wt="bold" if (j>0 and any(ch.isdigit() for ch in c)) else "normal"
        ax.text(xcol[j],y+rh/2,c,fontsize=10.2,transform=ax.transAxes,va="center",fontweight=wt)
    y-=rh
ax.plot([0,1],[y+rh-0.001,y+rh-0.001],color="#333333",lw=1.3,transform=ax.transAxes)
ys=y+rh-0.11
ax.text(0.0,ys,"Sursa: ACEA (2026), New car registrations by manufacturer – European Union (ianuarie–decembrie 2025).",fontsize=8.8,color="#444444",transform=ax.transAxes,va="top")
nota="Notă: la nivelul Europei extinse (UE + AELS + Regatul Unit), BYD a înmatriculat 50.912 autoturisme în 2024 și 187.657 în 2025 (+268,6%). ACEA raportează volume individuale pentru marca BYD începând cu 2024; anterior, prezența pe piața UE era sub pragul de raportare pe marcă."
ax.text(0.0,ys-0.12,textwrap.fill(nota,150),fontsize=8.0,color="#666666",transform=ax.transAxes,va="top")
fig.savefig(OUT+"4-1_E_tabel2_byd_vanzari.png",bbox_inches="tight",facecolor="white",dpi=150); plt.close(fig); print("scris")
