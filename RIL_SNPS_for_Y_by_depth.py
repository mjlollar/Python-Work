# Current depth is filtered to n = 10, adjust where noted if you wish to adjust depth threshold


import sys
import re
import json

FR_Y_vcf = input("Enter the name of the France Y Chromosome vcf file:/n")

data = open("FR_ChrY_filtered.csv", 'w')

with open(FR_Y_vcf, 'w') as dpfilter:
        for line in dpfilter:
            line1 = re.split("\t", line[:-1])
            cov1 = line1[7]
            if "DP=" in cov1:
                cov2 = re.split(r";", cov1)
                for info in cov2:
                    name = re.split(r'=', info)
# Change number following ">=" to adjust depth filter                    
                    if "DP" == name[0]:
                        if int(name[1]) >= 10:
                            data.write(line)
                            print(line)
                        else:
                            pass

data.close()

ZI_Y_vcf = input("Enter the name of the Zambia Y Chromsome vdf file:"/n)

data = open("ZI_ChrY_filtered.csv", 'w')

with open(ZI_Y_vcf, 'w') as dpfilter:
        for line in dpfilter:
            line1 = re.split("\t", line[:-1])
            cov1 = line1[7]
            if "DP=" in cov1:
                cov2 = re.split(r";", cov1)
                for info in cov2:
                    name = re.split(r'=', info)
                    if "DP" == name[0]:
# Change number following ">=" to adjust depth filter                        
                        if int(name[1]) >= 10:
                            data.write(line)
                            print(line)
                        else:
                            pass

data.close()

dict_FR = {}

with open("FR_ChrY_filtered.txt", 'r') as frdata:
    for line in frdata:
        line1 = re.split('\t', line)
        key = line1[1]
        dict_FR[key] = line1[3]
    print("France Dictionary created")

dict_ZI = {}

with open("ZI_ChrY_filtered.txt", 'r') as zidata:
    for line in zidata:
        line1 = re.split('\t', line)
        key = line1[1]
        dict_ZI[key] = line1[3]
    print("Zambia Dictionary created")

dict_combined = {}

for key, value1 in dict_FR.items():
    dict_combined.setdefault(key, [value1]).extend(
        value2 for interval, value2 in dict_ZI.items() if key in interval)

output_name = input("Enter the output file for your SNPs:"/n)

with open(output_name, 'w') as comb:
    json.dump(dict_combined, comb, indent=4)
    comb.close()
