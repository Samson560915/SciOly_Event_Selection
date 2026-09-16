from utils import dot_product, avr_lists

# File is copy/pasted from Claude
# These values for each vector should be HEAVILY reviewed
# Format: [biology, chemistry, physics, logic/reasoning, test/lab/build]

# Life, Personal & Social Science
anatomy = [0.9, 0.1, 0.3, 0.1, 0.3]
botany = [0.9, 0.2, 0.1, 0.2, 0.6]
designer_genes = [0.9, 0.3, 0.1, 0.6, 0.5]
disease_detectives = [0.7, 0.1, 0.1, 0.8, 0.3]
water_quality = [0.6, 0.7, 0.2, 0.3, 0.6]

# Earth and Space Science
astronomy = [0.1, 0.1, 0.8, 0.4, 0.5]
dynamic_planet = [0.1, 0.3, 0.5, 0.4, 0.6]
remote_sensing = [0.1, 0.1, 0.6, 0.7, 0.6]
rocks_and_minerals = [0.05, 0.7, 0.3, 0.3, 0.7]

# Physical Science & Chemistry
chemistry_lab = [0.05, 1.0, 0.2, 0.3, 0.9]
circuit_lab = [0.0, 0.1, 0.9, 0.5, 0.8]
forensics = [0.3, 0.8, 0.2, 0.6, 0.7]
hovercraft = [0.0, 0.1, 0.8, 0.3, 1.0]
protein_modeling = [0.6, 0.7, 0.1, 0.3, 0.9]
thermodynamics = [0.0, 0.4, 0.9, 0.4, 0.9]

# Technology & Engineering
boomilever = [0.0, 0.0, 0.8, 0.4, 1.0]
electric_vehicle = [0.0, 0.1, 0.8, 0.4, 1.0]
mission_possible = [0.0, 0.1, 0.7, 0.5, 1.0]
wright_stuff = [0.0, 0.0, 0.8, 0.3, 1.0]

# Inquiry & Nature of Science
codebusters = [0.0, 0.0, 0.0, 1.0, 0.3]
engineering_cad = [0.0, 0.0, 0.6, 0.6, 0.8]
experimental_design = [0.3, 0.3, 0.3, 0.9, 0.7]
ping_pong_parachute = [0.0, 0.0, 0.7, 0.3, 1.0]

# Optional: collect into one dict for easy iteration/analysis
events = {
    "Anatomy and Physiology": anatomy,
    "Botany": botany,
    "Designer Genes": designer_genes,
    "Disease Detectives": disease_detectives,
    "Water Quality": water_quality,
    "Astronomy": astronomy,
    "Dynamic Planet": dynamic_planet,
    "Remote Sensing": remote_sensing,
    "Rocks and Minerals": rocks_and_minerals,
    "Chemistry Lab": chemistry_lab,
    "Circuit Lab": circuit_lab,
    "Forensics": forensics,
    "Hovercraft": hovercraft,
    "Protein Modeling": protein_modeling,
    "Thermodynamics": thermodynamics,
    "Boomilever": boomilever,
    "Electric Vehicle": electric_vehicle,
    "Mission Possible": mission_possible,
    "Wright Stuff": wright_stuff,
    "Codebusters": codebusters,
    "Engineering CAD": engineering_cad,
    "Experimental Design": experimental_design,
    "Ping-Pong Parachute": ping_pong_parachute,
}

neda_jantzen         = [designer_genes, rocks_and_minerals, forensics, boomilever, experimental_design]
evelyn_leng          =  [designer_genes, disease_detectives, experimental_design]
everett_mcglothlin   =  [astronomy, codebusters, engineering_cad]
samson_ou            =  [protein_modeling, thermodynamics, codebusters]
yunes_adjerid        =  [anatomy, disease_detectives, water_quality, circuit_lab, protein_modeling] 
milo_tao_lin         =  [circuit_lab, protein_modeling, thermodynamics] 
rey_han              =  [botany, circuit_lab, hovercraft] 
pam_kampanya         =  [anatomy, circuit_lab, hovercraft] 
clara_cook           =  [anatomy, disease_detectives, experimental_design] 
moses_park           =  [astronomy, circuit_lab, thermodynamics] 
siena_marr           =  [astronomy, chemistry_lab, experimental_design] 
hadley_teaster       =  [anatomy, designer_genes, protein_modeling] 
jeannette_wang       =  [anatomy, designer_genes, protein_modeling] 
ethan_zhu            =  [circuit_lab, hovercraft, electric_vehicle] 
david_hicks          =  [botany, astronomy, dynamic_planet] 
kora_pence           =  [botany, designer_genes, disease_detectives] 
meera_nair           =  [anatomy, forensics] 
ozan_tural           =  [anatomy, water_quality, dynamic_planet, protein_modeling, thermodynamics] 
sophia_warren        =  [designer_genes, chemistry_lab, protein_modeling] 
jenny_li             =  [designer_genes, forensics, codebusters] 
giang_nguyen         =  [botany, remote_sensing, hovercraft, boomilever, wright_stuff, codebusters] 
sadie_zhang          =  [remote_sensing, forensics, ping_pong_parachute] 
nathan_chen          =  [astronomy, chemistry_lab, circuit_lab, thermodynamics, codebusters, experimental_design] 
andrew_hou           =  [anatomy, chemistry_lab, protein_modeling] 
braulio_escalante    =  [botany, water_quality, rocks_and_minerals] 
emma_hungate         =  [boomilever, electric_vehicle, mission_possible, wright_stuff, engineering_cad, experimental_design, ping_pong_parachute] 
garrett_butler       =  [astronomy, hovercraft, electric_vehicle] 
owen_fotinos         =  [chemistry_lab, protein_modeling, thermodynamics, boomilever] 
grace_li             =  [anatomy, designer_genes, water_quality] 
elisabeth_emmett     =  [anatomy, designer_genes, disease_detectives] 
mirabella_garza      =  [anatomy, remote_sensing, chemistry_lab] 
mack_strahm          =  [chemistry_lab, protein_modeling, electric_vehicle] 
evan_weng            =  [water_quality, dynamic_planet, remote_sensing, thermodynamics, wright_stuff, ping_pong_parachute] 
sailor_long          =  [astronomy, chemistry_lab, forensics] 
sofia_mariani        =  [electric_vehicle, mission_possible] 
atiksh_ajit          =  [anatomy, astronomy, hovercraft, electric_vehicle, codebusters, ping_pong_parachute]   # kept: 6-event submission
henry_vikesland      =  [chemistry_lab, electric_vehicle, ping_pong_parachute] 
adi_ali              =  [anatomy, chemistry_lab, protein_modeling]   # kept: 3-event submission
zoe_zhang            =  [dynamic_planet, wright_stuff, ping_pong_parachute] 
nyala_smith          =  [anatomy, chemistry_lab, wright_stuff] 
margaret_martin      =  [chemistry_lab, wright_stuff, codebusters] 
dennis_zhao          =  [anatomy, dynamic_planet, protein_modeling] 
rose_delong          =  [anatomy, botany, astronomy, rocks_and_minerals, chemistry_lab, protein_modeling] 
maeve_holland        =  [anatomy, protein_modeling, codebusters] 
stephen_duncan       =  [circuit_lab, electric_vehicle, ping_pong_parachute] 
simon_jaworski       =  [astronomy, chemistry_lab, ping_pong_parachute] 
hari_kumar           =  [astronomy, chemistry_lab, ping_pong_parachute] 
isabella_baisden     =  [anatomy, disease_detectives, forensics, thermodynamics, experimental_design] 
mira_davison         =  [anatomy, disease_detectives, forensics, thermodynamics, experimental_design] 
natalia_migan_gandonou  =  [anatomy, chemistry_lab, forensics] 
sophie_zhang         =  [botany, disease_detectives, astronomy, dynamic_planet, chemistry_lab, protein_modeling, boomilever, ping_pong_parachute] 
faiyaz_kabir         =  [anatomy, protein_modeling, experimental_design] 
joshua_byun          =  [anatomy, astronomy, chemistry_lab] 