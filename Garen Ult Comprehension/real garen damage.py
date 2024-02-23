#real garen damage

'''
This code will output at which point various targets would die based on the WHOLE Garen ultimate damage.
Taking into account both the base damage and the missing health damage

Display format:
Original HP the target had
The actual HP it had before being killable with the ultimate
The percentage of it's total hp it had before being killabe with the ultimate
'''

from math import floor

TD=[[150, 0.25], [300, 0.3], [450, 0.35]]

OV=700
#original/first victim

line= '_'*32+'\n'

for rank in range(3):
    print(f'{line*3}{"RANK "+str(rank+1):_^32}\n{line*3}')
    for i in range(67):
        ah=oh=OV+(50*i)
        while ah>=0:
            if ah-(TD[rank][0]+(oh-ah)*TD[rank][1])<=0:
                print(f'Original HP: {oh}\n'
                      f'Actual HP: {ah}\n'
                      f'Percentage: {floor((ah/oh)*100)}%HP\n'
                      f'{line}')
                break
            ah-=1

        

'''
pegar hp
mata? não ent
menos hp, mais missing h
matou?
reseta interação
'''




'''
OUTPUT:

________________________________
________________________________
________________________________
_____________RANK 1_____________
________________________________
________________________________
________________________________

Original HP: 700
Actual HP: 260
Percentage: 37%HP
________________________________

Original HP: 750
Actual HP: 270
Percentage: 36%HP
________________________________

Original HP: 800
Actual HP: 280
Percentage: 35%HP
________________________________

Original HP: 850
Actual HP: 290
Percentage: 34%HP
________________________________

Original HP: 900
Actual HP: 300
Percentage: 33%HP
________________________________

Original HP: 950
Actual HP: 310
Percentage: 32%HP
________________________________

Original HP: 1000
Actual HP: 320
Percentage: 32%HP
________________________________

Original HP: 1050
Actual HP: 330
Percentage: 31%HP
________________________________

Original HP: 1100
Actual HP: 340
Percentage: 30%HP
________________________________

Original HP: 1150
Actual HP: 350
Percentage: 30%HP
________________________________

Original HP: 1200
Actual HP: 360
Percentage: 30%HP
________________________________

Original HP: 1250
Actual HP: 370
Percentage: 29%HP
________________________________

Original HP: 1300
Actual HP: 380
Percentage: 29%HP
________________________________

Original HP: 1350
Actual HP: 390
Percentage: 28%HP
________________________________

Original HP: 1400
Actual HP: 400
Percentage: 28%HP
________________________________

Original HP: 1450
Actual HP: 410
Percentage: 28%HP
________________________________

Original HP: 1500
Actual HP: 420
Percentage: 28%HP
________________________________

Original HP: 1550
Actual HP: 430
Percentage: 27%HP
________________________________

Original HP: 1600
Actual HP: 440
Percentage: 27%HP
________________________________

Original HP: 1650
Actual HP: 450
Percentage: 27%HP
________________________________

Original HP: 1700
Actual HP: 460
Percentage: 27%HP
________________________________

Original HP: 1750
Actual HP: 470
Percentage: 26%HP
________________________________

Original HP: 1800
Actual HP: 480
Percentage: 26%HP
________________________________

Original HP: 1850
Actual HP: 490
Percentage: 26%HP
________________________________

Original HP: 1900
Actual HP: 500
Percentage: 26%HP
________________________________

Original HP: 1950
Actual HP: 510
Percentage: 26%HP
________________________________

Original HP: 2000
Actual HP: 520
Percentage: 26%HP
________________________________

Original HP: 2050
Actual HP: 530
Percentage: 25%HP
________________________________

Original HP: 2100
Actual HP: 540
Percentage: 25%HP
________________________________

Original HP: 2150
Actual HP: 550
Percentage: 25%HP
________________________________

Original HP: 2200
Actual HP: 560
Percentage: 25%HP
________________________________

Original HP: 2250
Actual HP: 570
Percentage: 25%HP
________________________________

Original HP: 2300
Actual HP: 580
Percentage: 25%HP
________________________________

Original HP: 2350
Actual HP: 590
Percentage: 25%HP
________________________________

Original HP: 2400
Actual HP: 600
Percentage: 25%HP
________________________________

Original HP: 2450
Actual HP: 610
Percentage: 24%HP
________________________________

Original HP: 2500
Actual HP: 620
Percentage: 24%HP
________________________________

Original HP: 2550
Actual HP: 630
Percentage: 24%HP
________________________________

Original HP: 2600
Actual HP: 640
Percentage: 24%HP
________________________________

Original HP: 2650
Actual HP: 650
Percentage: 24%HP
________________________________

Original HP: 2700
Actual HP: 660
Percentage: 24%HP
________________________________

Original HP: 2750
Actual HP: 670
Percentage: 24%HP
________________________________

Original HP: 2800
Actual HP: 680
Percentage: 24%HP
________________________________

Original HP: 2850
Actual HP: 690
Percentage: 24%HP
________________________________

Original HP: 2900
Actual HP: 700
Percentage: 24%HP
________________________________

Original HP: 2950
Actual HP: 710
Percentage: 24%HP
________________________________

Original HP: 3000
Actual HP: 720
Percentage: 24%HP
________________________________

Original HP: 3050
Actual HP: 730
Percentage: 23%HP
________________________________

Original HP: 3100
Actual HP: 740
Percentage: 23%HP
________________________________

Original HP: 3150
Actual HP: 750
Percentage: 23%HP
________________________________

Original HP: 3200
Actual HP: 760
Percentage: 23%HP
________________________________

Original HP: 3250
Actual HP: 770
Percentage: 23%HP
________________________________

Original HP: 3300
Actual HP: 780
Percentage: 23%HP
________________________________

Original HP: 3350
Actual HP: 790
Percentage: 23%HP
________________________________

Original HP: 3400
Actual HP: 800
Percentage: 23%HP
________________________________

Original HP: 3450
Actual HP: 810
Percentage: 23%HP
________________________________

Original HP: 3500
Actual HP: 820
Percentage: 23%HP
________________________________

Original HP: 3550
Actual HP: 830
Percentage: 23%HP
________________________________

Original HP: 3600
Actual HP: 840
Percentage: 23%HP
________________________________

Original HP: 3650
Actual HP: 850
Percentage: 23%HP
________________________________

Original HP: 3700
Actual HP: 860
Percentage: 23%HP
________________________________

Original HP: 3750
Actual HP: 870
Percentage: 23%HP
________________________________

Original HP: 3800
Actual HP: 880
Percentage: 23%HP
________________________________

Original HP: 3850
Actual HP: 890
Percentage: 23%HP
________________________________

Original HP: 3900
Actual HP: 900
Percentage: 23%HP
________________________________

Original HP: 3950
Actual HP: 910
Percentage: 23%HP
________________________________

Original HP: 4000
Actual HP: 920
Percentage: 23%HP
________________________________

________________________________
________________________________
________________________________
_____________RANK 2_____________
________________________________
________________________________
________________________________

Original HP: 700
Actual HP: 392
Percentage: 56%HP
________________________________

Original HP: 750
Actual HP: 403
Percentage: 53%HP
________________________________

Original HP: 800
Actual HP: 415
Percentage: 51%HP
________________________________

Original HP: 850
Actual HP: 426
Percentage: 50%HP
________________________________

Original HP: 900
Actual HP: 438
Percentage: 48%HP
________________________________

Original HP: 950
Actual HP: 450
Percentage: 47%HP
________________________________

Original HP: 1000
Actual HP: 461
Percentage: 46%HP
________________________________

Original HP: 1050
Actual HP: 473
Percentage: 45%HP
________________________________

Original HP: 1100
Actual HP: 484
Percentage: 44%HP
________________________________

Original HP: 1150
Actual HP: 496
Percentage: 43%HP
________________________________

Original HP: 1200
Actual HP: 507
Percentage: 42%HP
________________________________

Original HP: 1250
Actual HP: 519
Percentage: 41%HP
________________________________

Original HP: 1300
Actual HP: 530
Percentage: 40%HP
________________________________

Original HP: 1350
Actual HP: 542
Percentage: 40%HP
________________________________

Original HP: 1400
Actual HP: 553
Percentage: 39%HP
________________________________

Original HP: 1450
Actual HP: 565
Percentage: 38%HP
________________________________

Original HP: 1500
Actual HP: 576
Percentage: 38%HP
________________________________

Original HP: 1550
Actual HP: 588
Percentage: 37%HP
________________________________

Original HP: 1600
Actual HP: 600
Percentage: 37%HP
________________________________

Original HP: 1650
Actual HP: 611
Percentage: 37%HP
________________________________

Original HP: 1700
Actual HP: 623
Percentage: 36%HP
________________________________

Original HP: 1750
Actual HP: 634
Percentage: 36%HP
________________________________

Original HP: 1800
Actual HP: 646
Percentage: 35%HP
________________________________

Original HP: 1850
Actual HP: 657
Percentage: 35%HP
________________________________

Original HP: 1900
Actual HP: 669
Percentage: 35%HP
________________________________

Original HP: 1950
Actual HP: 680
Percentage: 34%HP
________________________________

Original HP: 2000
Actual HP: 692
Percentage: 34%HP
________________________________

Original HP: 2050
Actual HP: 703
Percentage: 34%HP
________________________________

Original HP: 2100
Actual HP: 715
Percentage: 34%HP
________________________________

Original HP: 2150
Actual HP: 726
Percentage: 33%HP
________________________________

Original HP: 2200
Actual HP: 738
Percentage: 33%HP
________________________________

Original HP: 2250
Actual HP: 750
Percentage: 33%HP
________________________________

Original HP: 2300
Actual HP: 761
Percentage: 33%HP
________________________________

Original HP: 2350
Actual HP: 773
Percentage: 32%HP
________________________________

Original HP: 2400
Actual HP: 784
Percentage: 32%HP
________________________________

Original HP: 2450
Actual HP: 796
Percentage: 32%HP
________________________________

Original HP: 2500
Actual HP: 807
Percentage: 32%HP
________________________________

Original HP: 2550
Actual HP: 819
Percentage: 32%HP
________________________________

Original HP: 2600
Actual HP: 830
Percentage: 31%HP
________________________________

Original HP: 2650
Actual HP: 842
Percentage: 31%HP
________________________________

Original HP: 2700
Actual HP: 853
Percentage: 31%HP
________________________________

Original HP: 2750
Actual HP: 865
Percentage: 31%HP
________________________________

Original HP: 2800
Actual HP: 876
Percentage: 31%HP
________________________________

Original HP: 2850
Actual HP: 888
Percentage: 31%HP
________________________________

Original HP: 2900
Actual HP: 900
Percentage: 31%HP
________________________________

Original HP: 2950
Actual HP: 911
Percentage: 30%HP
________________________________

Original HP: 3000
Actual HP: 923
Percentage: 30%HP
________________________________

Original HP: 3050
Actual HP: 934
Percentage: 30%HP
________________________________

Original HP: 3100
Actual HP: 946
Percentage: 30%HP
________________________________

Original HP: 3150
Actual HP: 957
Percentage: 30%HP
________________________________

Original HP: 3200
Actual HP: 969
Percentage: 30%HP
________________________________

Original HP: 3250
Actual HP: 980
Percentage: 30%HP
________________________________

Original HP: 3300
Actual HP: 992
Percentage: 30%HP
________________________________

Original HP: 3350
Actual HP: 1003
Percentage: 29%HP
________________________________

Original HP: 3400
Actual HP: 1015
Percentage: 29%HP
________________________________

Original HP: 3450
Actual HP: 1026
Percentage: 29%HP
________________________________

Original HP: 3500
Actual HP: 1038
Percentage: 29%HP
________________________________

Original HP: 3550
Actual HP: 1050
Percentage: 29%HP
________________________________

Original HP: 3600
Actual HP: 1061
Percentage: 29%HP
________________________________

Original HP: 3650
Actual HP: 1073
Percentage: 29%HP
________________________________

Original HP: 3700
Actual HP: 1084
Percentage: 29%HP
________________________________

Original HP: 3750
Actual HP: 1096
Percentage: 29%HP
________________________________

Original HP: 3800
Actual HP: 1107
Percentage: 29%HP
________________________________

Original HP: 3850
Actual HP: 1119
Percentage: 29%HP
________________________________

Original HP: 3900
Actual HP: 1130
Percentage: 28%HP
________________________________

Original HP: 3950
Actual HP: 1142
Percentage: 28%HP
________________________________

Original HP: 4000
Actual HP: 1153
Percentage: 28%HP
________________________________

________________________________
________________________________
________________________________
_____________RANK 3_____________
________________________________
________________________________
________________________________

Original HP: 700
Actual HP: 514
Percentage: 73%HP
________________________________

Original HP: 750
Actual HP: 527
Percentage: 70%HP
________________________________

Original HP: 800
Actual HP: 540
Percentage: 67%HP
________________________________

Original HP: 850
Actual HP: 553
Percentage: 65%HP
________________________________

Original HP: 900
Actual HP: 566
Percentage: 62%HP
________________________________

Original HP: 950
Actual HP: 579
Percentage: 60%HP
________________________________

Original HP: 1000
Actual HP: 592
Percentage: 59%HP
________________________________

Original HP: 1050
Actual HP: 605
Percentage: 57%HP
________________________________

Original HP: 1100
Actual HP: 618
Percentage: 56%HP
________________________________

Original HP: 1150
Actual HP: 631
Percentage: 54%HP
________________________________

Original HP: 1200
Actual HP: 644
Percentage: 53%HP
________________________________

Original HP: 1250
Actual HP: 657
Percentage: 52%HP
________________________________

Original HP: 1300
Actual HP: 670
Percentage: 51%HP
________________________________

Original HP: 1350
Actual HP: 683
Percentage: 50%HP
________________________________

Original HP: 1400
Actual HP: 696
Percentage: 49%HP
________________________________

Original HP: 1450
Actual HP: 709
Percentage: 48%HP
________________________________

Original HP: 1500
Actual HP: 722
Percentage: 48%HP
________________________________

Original HP: 1550
Actual HP: 735
Percentage: 47%HP
________________________________

Original HP: 1600
Actual HP: 748
Percentage: 46%HP
________________________________

Original HP: 1650
Actual HP: 761
Percentage: 46%HP
________________________________

Original HP: 1700
Actual HP: 774
Percentage: 45%HP
________________________________

Original HP: 1750
Actual HP: 787
Percentage: 44%HP
________________________________

Original HP: 1800
Actual HP: 800
Percentage: 44%HP
________________________________

Original HP: 1850
Actual HP: 812
Percentage: 43%HP
________________________________

Original HP: 1900
Actual HP: 825
Percentage: 43%HP
________________________________

Original HP: 1950
Actual HP: 838
Percentage: 42%HP
________________________________

Original HP: 2000
Actual HP: 851
Percentage: 42%HP
________________________________

Original HP: 2050
Actual HP: 864
Percentage: 42%HP
________________________________

Original HP: 2100
Actual HP: 877
Percentage: 41%HP
________________________________

Original HP: 2150
Actual HP: 890
Percentage: 41%HP
________________________________

Original HP: 2200
Actual HP: 903
Percentage: 41%HP
________________________________

Original HP: 2250
Actual HP: 916
Percentage: 40%HP
________________________________

Original HP: 2300
Actual HP: 929
Percentage: 40%HP
________________________________

Original HP: 2350
Actual HP: 942
Percentage: 40%HP
________________________________

Original HP: 2400
Actual HP: 955
Percentage: 39%HP
________________________________

Original HP: 2450
Actual HP: 968
Percentage: 39%HP
________________________________

Original HP: 2500
Actual HP: 981
Percentage: 39%HP
________________________________

Original HP: 2550
Actual HP: 994
Percentage: 38%HP
________________________________

Original HP: 2600
Actual HP: 1007
Percentage: 38%HP
________________________________

Original HP: 2650
Actual HP: 1020
Percentage: 38%HP
________________________________

Original HP: 2700
Actual HP: 1033
Percentage: 38%HP
________________________________

Original HP: 2750
Actual HP: 1046
Percentage: 38%HP
________________________________

Original HP: 2800
Actual HP: 1059
Percentage: 37%HP
________________________________

Original HP: 2850
Actual HP: 1072
Percentage: 37%HP
________________________________

Original HP: 2900
Actual HP: 1085
Percentage: 37%HP
________________________________

Original HP: 2950
Actual HP: 1098
Percentage: 37%HP
________________________________

Original HP: 3000
Actual HP: 1111
Percentage: 37%HP
________________________________

Original HP: 3050
Actual HP: 1124
Percentage: 36%HP
________________________________

Original HP: 3100
Actual HP: 1137
Percentage: 36%HP
________________________________

Original HP: 3150
Actual HP: 1150
Percentage: 36%HP
________________________________

Original HP: 3200
Actual HP: 1162
Percentage: 36%HP
________________________________

Original HP: 3250
Actual HP: 1175
Percentage: 36%HP
________________________________

Original HP: 3300
Actual HP: 1188
Percentage: 36%HP
________________________________

Original HP: 3350
Actual HP: 1201
Percentage: 35%HP
________________________________

Original HP: 3400
Actual HP: 1214
Percentage: 35%HP
________________________________

Original HP: 3450
Actual HP: 1227
Percentage: 35%HP
________________________________

Original HP: 3500
Actual HP: 1240
Percentage: 35%HP
________________________________

Original HP: 3550
Actual HP: 1253
Percentage: 35%HP
________________________________

Original HP: 3600
Actual HP: 1266
Percentage: 35%HP
________________________________

Original HP: 3650
Actual HP: 1279
Percentage: 35%HP
________________________________

Original HP: 3700
Actual HP: 1292
Percentage: 34%HP
________________________________

Original HP: 3750
Actual HP: 1305
Percentage: 34%HP
________________________________

Original HP: 3800
Actual HP: 1318
Percentage: 34%HP
________________________________

Original HP: 3850
Actual HP: 1331
Percentage: 34%HP
________________________________

Original HP: 3900
Actual HP: 1344
Percentage: 34%HP
________________________________

Original HP: 3950
Actual HP: 1357
Percentage: 34%HP
________________________________

Original HP: 4000
Actual HP: 1370
Percentage: 34%HP
________________________________

'''
