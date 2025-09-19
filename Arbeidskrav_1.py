# -*- coding: utf-8 -*-
"""ARBEIDSKRAV 1"""

"""

Oppgavetekst: 

Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, 
og du ønsker å sammenlikne de årlige kostnadene ved elbil 
sammenliknet med bensinbil.

Lag et Python-program som beregner 
og presenterer (i konsollen) de årlige totalkostnadene 
for elbil og for bensinbil samt årlig kostnadsdifferanse"


"""


"""BEREGNING AV ÅRLIGE TOTALKOSTNADER FOR ELBIL"""

# VARIABLER og VERDIER 
km_pr_år = 10000 # antall kjørte kilometer kjørt pr år
dager_i_året = 365
elbilforsikring = 5000 # forsikring pr år/kr
trafikkforsikringsavgift = 8.38 # trafikkforsikringsavgift kr/pr dag for elbil og bensinbil
kwh_pr_km = 0.2 # kWh per kilometer
kr_pr_kWh = 2.00 # kroner pr kWh
e_bomavgift_kr_pr_km = 0.1 

# 1. Årlig kWH
e_total_kWh = km_pr_år * kwh_pr_km
#print("Elbilens årlige kWH forbruk er beregnet til å være", e_total_kWh)

# 2. Årlige kostnader for kWH/drivstoff
e_total_kost_kWh = e_total_kWh * kr_pr_kWh
#print("Elbilens årlige kostander for kWh er:", e_total_kost_kWh)

# 3. Årlige kostnader for trafikkforsikringsavgift
forsikringsavgift_prår = trafikkforsikringsavgift * dager_i_året
#print("Forsikringsavgift pr år er:", forsikringsavgift_prår)

# 4. Årlige kostnader av bomavgift
e_total_bomavgift_pr_år = km_pr_år * e_bomavgift_kr_pr_km
#print("Elbilens årlige kostnader for bomavgift pr år er:", e_total_bomavgift_pr_år)

# 5. Elbilens årlige totalekostnader 
elbil_årlig_kost = e_total_kost_kWh + forsikringsavgift_prår + e_total_bomavgift_pr_år + elbilforsikring
print("Årlige totalkostnader for elbil er", (int(elbil_årlig_kost)), "kroner.")



"""BEREGNING AV ÅRLIGE TOTALKOSTNADER FOR BENSINBIL"""

# VARIABLER
bensinbilforsikring = 7500 # forsikring pr år/kr
trafikkforsikringsavgift = 8.38 # trafikkforsikringsavgift kr/pr dag for elbil og bensinbil
drivstoffbruk_kr_pr_km = 1.00
b_bomavgift_kr_pr_km = 0.3 

# 1. Årlige kostnader for trafikkforsikringsavgift
forsikringsavgift_prår = trafikkforsikringsavgift * dager_i_året
#print("Forsikringsavgift pr år er:", forsikringsavgift_prår)

# 2. Årlige kostnader for drivstoff
b_total_kost_drivstoff = km_pr_år * drivstoffbruk_kr_pr_km
#print("Bensinbilense årlige drivstoffkostnader er", b_total_kost_drivstoff)

# 3. Årlige kostnader av bomavgift
b_total_bomavgift_pr_år = km_pr_år * b_bomavgift_kr_pr_km
#print("Bensinbilens årlige kostnader for bomavgift er pr år:", b_total_bomavgift_pr_år)

# 4. Bensibilens årlige totalkostnader
bensinbil_årlig_kost = b_total_kost_drivstoff + b_total_bomavgift_pr_år + bensinbilforsikring + forsikringsavgift_prår + bensinbilforsikring
print("Årlige kostnader for bensinbil er", (int(bensinbil_årlig_kost)), "kroner.")


"""ÅRLIG KOSTNADSDIFFERANSE"""
årlig_diff = bensinbil_årlig_kost - elbil_årlig_kost
print("Årlig kostnadsdifferanse mellom elbil og bensinbil er", (int(årlig_diff)), "kroner.")


 


















