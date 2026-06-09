# -*- coding: utf-8 -*-
"""3.1 - grafice suplimentare (parteneri, pondere, tip de comert, sectoare). EUR."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import textwrap
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#555555",
    "axes.linewidth":0.8,"axes.grid":True,"grid.color":"#E2E2E2","grid.linewidth":0.7,
    "axes.axisbelow":True,"figure.dpi":150})
OUT="/sessions/friendly-beautiful-babbage/mnt/liceenta bixi/research/chapter3/charts/"
C_EU="#003399"; C_CN="#C8102E"
def save(fig,name): fig.savefig(OUT+name,bbox_inches="tight",facecolor="white"); plt.close(fig); print("scris:",name)
def note(ax,txt): ax.text(0.0,-0.17,txt,transform=ax.transAxes,fontsize=8.0,color="#666666",va="top",ha="left")
def footer(fig,ax,shz,src,width=110):
    fh=fig.get_size_inches()[1]; per=(8/72)/fh*1.5
    sh=textwrap.fill(shz,width); sr=textwrap.fill(src,width); n=sh.count("\n")+1
    ax.text(0.0,-0.16,sh,transform=ax.transAxes,fontsize=8.0,color="#333333",va="top",ha="left")
    ax.text(0.0,-0.16-per*n-0.010,sr,transform=ax.transAxes,fontsize=8.0,color="#666666",va="top",ha="left")
def ro(x,d=1): return f"{x:,.{d}f}".replace(",","§").replace(".",",").replace("§",".")

# ===== Punct 1: Top 3 state membre UE in comertul cu China (2024) =====
fig,(axL,axR)=plt.subplots(1,2,figsize=(11.0,5.2))
axL.bar(["Țările de Jos","Germania","Italia"],[109,96,50],color=C_CN,width=0.6)
for i,v in enumerate([109,96,50]): axL.text(i,v+1.5,ro(v,0),ha="center",fontsize=10,fontweight="bold")
axL.set_title("Top 3 importatori din China",fontsize=11,fontweight="bold")
axL.set_ylabel("Miliarde EUR"); axL.set_ylim(0,125); axL.grid(axis="y")
axR.bar(["Germania","Franța","Țările de Jos"],[90,24,24],color=C_EU,width=0.6)
for i,v in enumerate([90,24,24]): axR.text(i,v+1.5,ro(v,0),ha="center",fontsize=10,fontweight="bold")
axR.set_title("Top 3 exportatori către China",fontsize=11,fontweight="bold")
axR.set_ylabel("Miliarde EUR"); axR.set_ylim(0,125); axR.grid(axis="y")
fig.suptitle("Principalele state membre UE în comerțul de bunuri cu China (2024)",fontsize=13,fontweight="bold",y=1.00)
fig.text(0.0,-0.04,"Sursă: Eurostat (comunicat 04-03-2025). În 2019 clasamentul era similar: Țările de Jos – cel mai mare importator (88 mld EUR), Germania – cel mai mare exportator (96 mld EUR). Țările de Jos sunt supraevaluate (efectul Rotterdam).",fontsize=8.0,color="#666666")
fig.tight_layout()
save(fig,"3-1_C_parteneri_state_membre.png")

# ===== Punct 2a: Ponderea Chinei in comertul extra-UE 2019-2024 =====
yrs=[2019,2020,2021,2022,2023,2024]
imp_share=[18.7,22.4,22.2,20.9,20.6,21.3]
exp_share=[9.3,10.5,10.2,9.0,8.7,8.3]
fig,ax=plt.subplots(figsize=(9.4,5.2)); x=np.arange(6)
ax.plot(x,imp_share,marker="o",lw=2.6,color=C_CN,label="China în importurile extra-UE")
ax.plot(x,exp_share,marker="s",lw=2.6,color=C_EU,label="China în exporturile extra-UE")
for i in range(6):
    ax.text(x[i],imp_share[i]+0.5,ro(imp_share[i],1)+"%",ha="center",fontsize=8.6,color=C_CN,fontweight="bold")
    ax.text(x[i],exp_share[i]-1.0,ro(exp_share[i],1)+"%",ha="center",fontsize=8.6,color=C_EU,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylabel("% din comerțul extra-UE"); ax.set_ylim(0,26)
ax.set_title("Ponderea Chinei în comerțul extra-UE de bunuri, 2019–2024",fontsize=12.5,fontweight="bold")
ax.legend(loc="center left",frameon=False)
note(ax,"Sursă: Comisia Europeană, DG Comerț / Eurostat COMEXT. China = cel mai mare furnizor de importuri al UE și al 3-lea partener pentru exporturi.")
save(fig,"3-1_D_pondere_china_extraUE.png")

# ===== Punct 2b: Structura comertului extra-UE pe parteneri 2024 =====
fig,ax=plt.subplots(figsize=(8.6,6.0))
part=["Statele Unite","China","Regatul Unit","Elveția","Turcia","Alți parteneri"]
shr=[17.3,14.6,10.1,6.5,4.2,47.3]
cols=["#88A0C8",C_CN,"#9FB4D6","#C3D0E6","#DCE4F0","#E9E9E9"]
ax.pie(shr,labels=part,colors=cols,explode=[0,0.08,0,0,0,0],autopct=lambda p:ro(p,1)+"%",
       startangle=90,counterclock=False,pctdistance=0.78,
       textprops=dict(fontsize=9.5),wedgeprops=dict(edgecolor="white",linewidth=1.2))
ax.set_title("Structura comerțului extra-UE de bunuri pe parteneri (2024)",fontsize=12.5,fontweight="bold")
ax.text(0,-1.30,"Din comerțul UE–China (732 mld EUR în 2024), zona Shenzhen reprezintă ≈ 7,8%\n(≈ 57 mld EUR), adică ≈ 1,1% din comerțul extra-UE.",ha="center",fontsize=8.3,color="#333333")
ax.text(0,-1.60,"Sursă: Comisia Europeană, DG Comerț / Eurostat COMEXT (2024).\nPondere Shenzhen calculată din datele Vamei Shenzhen 2024.",ha="center",fontsize=7.8,color="#666666")
save(fig,"3-1_E_structura_parteneri_2024.png")

# ===== Punct 3: Tipul de comert care predomina - importuri UE din China pe categorii SITC =====
yrs4=[2021,2022,2023,2024]
masini=[263.291,334.979,298.693,287.059]
divmanuf=[108.524,134.514,107.867,114.331]
manufmat=[55.011,72.939,54.874,59.592]
chimice=[34.522,66.496,43.660,44.007]
total=[472.491,627.766,520.447,519.007]
fig,ax=plt.subplots(figsize=(9.6,5.8)); x=np.arange(4); w=0.62
ax.bar(x,masini,w,label="Mașini și echipamente de transport",color=C_EU)
ax.bar(x,divmanuf,w,bottom=masini,label="Articole manufacturate diverse",color="#5B7FB9")
ax.bar(x,manufmat,w,bottom=np.array(masini)+np.array(divmanuf),label="Produse manufacturate după material",color="#9FB4D6")
ax.bar(x,chimice,w,bottom=np.array(masini)+np.array(divmanuf)+np.array(manufmat),label="Produse chimice",color="#FFB000")
for i in range(4):
    sh=masini[i]/total[i]*100
    ax.text(x[i],masini[i]/2,f"{ro(masini[i],0)}\n({ro(sh,0)}%)",ha="center",va="center",fontsize=8.6,color="white",fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(yrs4); ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,690)
ax.set_title("Tipul de comerț care predomină: importurile UE din China pe categorii, 2021–2024",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper center",ncol=2,frameon=False,fontsize=8.8)
footer(fig,ax,"Ponderea Shenzhenului: produsele electromecanice = ≈71% din exporturile totale ale Shenzhenului (2024) și 72,3% din exporturile Shenzhen→UE (ian.–feb. 2024) — categoria care domină importurile UE din China.","Sursă: Comisia Europeană, DG Comerț / Eurostat COMEXT (SITC); Vama Shenzhen 2024 (ponderea Shenzhenului).")
save(fig,"3-1_G_tip_comert_importuri.png")

# ===== Punct 4: Top 3 sectoare ale exporturilor UE catre China =====
masini_e=[116.214,120.167,114.479,109.416]
chimice_e=[32.977,37.769,39.635,35.627]
divmanuf_e=[26.308,27.573,28.067,28.178]
fig,ax=plt.subplots(figsize=(9.6,5.6)); x=np.arange(4); w=0.26
ax.bar(x-w,masini_e,w,label="Mașini și echipamente de transport",color=C_EU)
ax.bar(x,chimice_e,w,label="Produse chimice",color="#FFB000")
ax.bar(x+w,divmanuf_e,w,label="Articole manufacturate diverse",color="#2E8B57")
for i in range(4):
    ax.text(x[i]-w,masini_e[i]+1.5,ro(masini_e[i],0),ha="center",fontsize=8.2,fontweight="bold")
    ax.text(x[i],chimice_e[i]+1.5,ro(chimice_e[i],0),ha="center",fontsize=8.2,fontweight="bold")
    ax.text(x[i]+w,divmanuf_e[i]+1.5,ro(divmanuf_e[i],0),ha="center",fontsize=8.2,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(yrs4); ax.set_ylabel("Miliarde EUR"); ax.set_ylim(0,140)
ax.set_title("Top 3 sectoare ale fluxurilor UE → China (exporturi), 2021–2024",fontsize=12.5,fontweight="bold")
ax.legend(loc="upper right",frameon=False,fontsize=8.8)
footer(fig,ax,"Ponderea Shenzhenului: importurile Shenzhenului din UE sunt concentrate în echipamente de fabricație a semiconductorilor, circuite integrate și produse farmaceutice (54,1% produse electromecanice, ian.–feb. 2024).","Sursă: Comisia Europeană, DG Comerț / Eurostat COMEXT (SITC); Vama Shenzhen 2024 (ponderea Shenzhenului).")
save(fig,"3-1_H_top3_sectoare_export.png")
print("gata 3.1 suplimentar")
