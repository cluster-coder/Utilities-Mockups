#garen true damage

#This code will output the point at which a range of victims would die based solely on their missing HP
#Made to give myself some notion about it.

from math import ceil

victimsHP=[700,900,950,1000,1200,1400,1800,2000,2500,3000,4000,5000]

TD=[0.25,0.30,0.35]         #percentage of missing health as true damage

for originalHP in victimsHP:
    print(f'\n\n\n{originalHP} health champ:')
    HP=originalHP
    for level in range(3):
        losthealth=0
        while HP>0:
            if HP-(TD[level]*losthealth)<=0:
                #print(f'{originalHP} Health champion has died on {HP} HP, {losthealth} missing health')
                print(f'level {level+1}: {HP} HP\n'
                      f'Kill: {ceil((HP/originalHP)*100)}% HP\n\n')
                break
            HP-=1
            losthealth+=1
        HP=originalHP
        

'''
OUTPUT:




700 health champ:
level 1: 140 HP
Kill: 20% HP


level 2: 161 HP
Kill: 23% HP


level 3: 181 HP
Kill: 26% HP





900 health champ:
level 1: 180 HP
Kill: 20% HP


level 2: 207 HP
Kill: 23% HP


level 3: 233 HP
Kill: 26% HP





950 health champ:
level 1: 190 HP
Kill: 20% HP


level 2: 219 HP
Kill: 24% HP


level 3: 246 HP
Kill: 26% HP





1000 health champ:
level 1: 200 HP
Kill: 20% HP


level 2: 230 HP
Kill: 23% HP


level 3: 259 HP
Kill: 26% HP





1200 health champ:
level 1: 240 HP
Kill: 20% HP


level 2: 276 HP
Kill: 23% HP


level 3: 311 HP
Kill: 26% HP





1400 health champ:
level 1: 280 HP
Kill: 20% HP


level 2: 323 HP
Kill: 24% HP


level 3: 362 HP
Kill: 26% HP





1800 health champ:
level 1: 360 HP
Kill: 20% HP


level 2: 415 HP
Kill: 24% HP


level 3: 466 HP
Kill: 26% HP





2000 health champ:
level 1: 400 HP
Kill: 20% HP


level 2: 461 HP
Kill: 24% HP


level 3: 518 HP
Kill: 26% HP





2500 health champ:
level 1: 500 HP
Kill: 20% HP


level 2: 576 HP
Kill: 24% HP


level 3: 648 HP
Kill: 26% HP





3000 health champ:
level 1: 600 HP
Kill: 20% HP


level 2: 692 HP
Kill: 24% HP


level 3: 777 HP
Kill: 26% HP





4000 health champ:
level 1: 800 HP
Kill: 20% HP


level 2: 923 HP
Kill: 24% HP


level 3: 1037 HP
Kill: 26% HP





5000 health champ:
level 1: 1000 HP
Kill: 20% HP


level 2: 1153 HP
Kill: 24% HP


level 3: 1296 HP
Kill: 26% HP

'''
