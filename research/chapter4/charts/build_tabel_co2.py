# -*- coding: utf-8 -*-
"""Tabel CO2 pe cap de locuitor: China (reper Shenzhen) vs UE-27. EDGAR/JRC. Stil FSEGA."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.family":"DejaVu Sans"})
OUT=str(Path(__file__).resolve().parent)+"/"
C_CN="#C8102E"; C_EU="#003399"; C_LINE="#333333"

head=["Indicator (pe cap de locuitor)","China\n(reper Shenzhen)","UE-27","Raport\nChina / UE"]
rows=[
 ["Emisii de CO₂ fosil, 2023 (t/loc.)","9,24","5,66","≈ 1,6×"],
 ["Emisii totale de GES, 2024 (t CO₂e/loc.)","10,8","7,1","≈ 1,5×"],
]
cx=[0.015,0.45,0.705,0.865]
fig,ax=plt.subplots(figsize=(11.0,3.1)); ax.axis("off")
ax.text(0.0,1.13,"Emisii de CO₂ pe cap de locuitor: China (reper pentru Shenzhen) vs. UE-27",fontsize=11.5,fontweight="bold",transform=ax.transAxes,va="bottom")
Y0=0.92; hh=0.16; rh=0.26
ax.plot([0,1],[Y0,Y0],color=C_LINE,lw=1.4,transform=ax.transAxes)
for j,h in enumerate(head):
    col=C_CN if j==1 else (C_EU if j==2 else "#000000")
    ax.text(cx[j],Y0-hh/2,h,fontsize=9.8,fontweight="bold",style="italic",transform=ax.transAxes,va="center",color=col)
ax.plot([0,1],[Y0-hh,Y0-hh],color=C_LINE,lw=0.8,transform=ax.transAxes)
yb=Y0-hh
for i,r in enumerate(rows):
    yc=yb-rh*i-rh/2
    ax.text(cx[0],yc,r[0],fontsize=9.6,transform=ax.transAxes,va="center")
    ax.text(cx[1],yc,r[1],fontsize=10.2,transform=ax.transAxes,va="center",fontweight="bold",color=C_CN)
    ax.text(cx[2],yc,r[2],fontsize=10.2,transform=ax.transAxes,va="center",fontweight="bold",color=C_EU)
    ax.text(cx[3],yc,r[3],fontsize=9.8,transform=ax.transAxes,va="center")
ax.plot([0,1],[yb-rh*len(rows),yb-rh*len(rows)],color=C_LINE,lw=1.4,transform=ax.transAxes)
fig.savefig(OUT+"4-3_E_tabel_co2_capita.png",bbox_inches="tight",facecolor="white",dpi=150); plt.close(fig); print("scris")
