## Page 1

Lecture 13, 18 September 2025
Recursive definition of factorial
Add diagnostic print() to trace recursive calls
def fact(n):
    print("evaluating factorial of",n)
    if n == 0:
        return(1)
    else:
        return(n*fact(n-1))
fact(8)
evaluating factorial of 8
evaluating factorial of 7
evaluating factorial of 6
evaluating factorial of 5
evaluating factorial of 4
evaluating factorial of 3
evaluating factorial of 2
evaluating factorial of 1
evaluating factorial of 0
40320
A negative argument creates an unending sequence of recursive calls
Python has a built in recursion limit to abort such cases
This limit may deny some legitimate computation -- for instance factorial(3000) will also abort
We will see later that we can increase this limit
fact(-1)
In [1]:
In [2]:
Out[2]:
In [3]:

---

## Page 2

evaluating factorial of -1
evaluating factorial of -2
evaluating factorial of -3
evaluating factorial of -4
evaluating factorial of -5
evaluating factorial of -6
evaluating factorial of -7
evaluating factorial of -8
evaluating factorial of -9
evaluating factorial of -10
evaluating factorial of -11
evaluating factorial of -12
evaluating factorial of -13
evaluating factorial of -14
evaluating factorial of -15
evaluating factorial of -16
evaluating factorial of -17
evaluating factorial of -18
evaluating factorial of -19
evaluating factorial of -20
evaluating factorial of -21
evaluating factorial of -22
evaluating factorial of -23
evaluating factorial of -24
evaluating factorial of -25
evaluating factorial of -26
evaluating factorial of -27
evaluating factorial of -28
evaluating factorial of -29
evaluating factorial of -30
evaluating factorial of -31
evaluating factorial of -32
evaluating factorial of -33
evaluating factorial of -34
evaluating factorial of -35
evaluating factorial of -36
evaluating factorial of -37
evaluating factorial of -38
evaluating factorial of -39
evaluating factorial of -40
evaluating factorial of -41
evaluating factorial of -42
evaluating factorial of -43
evaluating factorial of -44
evaluating factorial of -45
evaluating factorial of -46
evaluating factorial of -47
evaluating factorial of -48
evaluating factorial of -49
evaluating factorial of -50
evaluating factorial of -51
evaluating factorial of -52
evaluating factorial of -53
evaluating factorial of -54
evaluating factorial of -55
evaluating factorial of -56
evaluating factorial of -57
evaluating factorial of -58
evaluating factorial of -59
evaluating factorial of -60
evaluating factorial of -61
evaluating factorial of -62
evaluating factorial of -63
evaluating factorial of -64
evaluating factorial of -65
evaluating factorial of -66
evaluating factorial of -67
evaluating factorial of -68
evaluating factorial of -69
evaluating factorial of -70
evaluating factorial of -71
evaluating factorial of -72
evaluating factorial of -73
evaluating factorial of -74
evaluating factorial of -75

---

## Page 3

evaluating factorial of -76
evaluating factorial of -77
evaluating factorial of -78
evaluating factorial of -79
evaluating factorial of -80
evaluating factorial of -81
evaluating factorial of -82
evaluating factorial of -83
evaluating factorial of -84
evaluating factorial of -85
evaluating factorial of -86
evaluating factorial of -87
evaluating factorial of -88
evaluating factorial of -89
evaluating factorial of -90
evaluating factorial of -91
evaluating factorial of -92
evaluating factorial of -93
evaluating factorial of -94
evaluating factorial of -95
evaluating factorial of -96
evaluating factorial of -97
evaluating factorial of -98
evaluating factorial of -99
evaluating factorial of -100
evaluating factorial of -101
evaluating factorial of -102
evaluating factorial of -103
evaluating factorial of -104
evaluating factorial of -105
evaluating factorial of -106
evaluating factorial of -107
evaluating factorial of -108
evaluating factorial of -109
evaluating factorial of -110
evaluating factorial of -111
evaluating factorial of -112
evaluating factorial of -113
evaluating factorial of -114
evaluating factorial of -115
evaluating factorial of -116
evaluating factorial of -117
evaluating factorial of -118
evaluating factorial of -119
evaluating factorial of -120
evaluating factorial of -121
evaluating factorial of -122
evaluating factorial of -123
evaluating factorial of -124
evaluating factorial of -125
evaluating factorial of -126
evaluating factorial of -127
evaluating factorial of -128
evaluating factorial of -129
evaluating factorial of -130
evaluating factorial of -131
evaluating factorial of -132
evaluating factorial of -133
evaluating factorial of -134
evaluating factorial of -135
evaluating factorial of -136
evaluating factorial of -137
evaluating factorial of -138
evaluating factorial of -139
evaluating factorial of -140
evaluating factorial of -141
evaluating factorial of -142
evaluating factorial of -143
evaluating factorial of -144
evaluating factorial of -145
evaluating factorial of -146
evaluating factorial of -147
evaluating factorial of -148
evaluating factorial of -149
evaluating factorial of -150

---

## Page 4

evaluating factorial of -151
evaluating factorial of -152
evaluating factorial of -153
evaluating factorial of -154
evaluating factorial of -155
evaluating factorial of -156
evaluating factorial of -157
evaluating factorial of -158
evaluating factorial of -159
evaluating factorial of -160
evaluating factorial of -161
evaluating factorial of -162
evaluating factorial of -163
evaluating factorial of -164
evaluating factorial of -165
evaluating factorial of -166
evaluating factorial of -167
evaluating factorial of -168
evaluating factorial of -169
evaluating factorial of -170
evaluating factorial of -171
evaluating factorial of -172
evaluating factorial of -173
evaluating factorial of -174
evaluating factorial of -175
evaluating factorial of -176
evaluating factorial of -177
evaluating factorial of -178
evaluating factorial of -179
evaluating factorial of -180
evaluating factorial of -181
evaluating factorial of -182
evaluating factorial of -183
evaluating factorial of -184
evaluating factorial of -185
evaluating factorial of -186
evaluating factorial of -187
evaluating factorial of -188
evaluating factorial of -189
evaluating factorial of -190
evaluating factorial of -191
evaluating factorial of -192
evaluating factorial of -193
evaluating factorial of -194
evaluating factorial of -195
evaluating factorial of -196
evaluating factorial of -197
evaluating factorial of -198
evaluating factorial of -199
evaluating factorial of -200
evaluating factorial of -201
evaluating factorial of -202
evaluating factorial of -203
evaluating factorial of -204
evaluating factorial of -205
evaluating factorial of -206
evaluating factorial of -207
evaluating factorial of -208
evaluating factorial of -209
evaluating factorial of -210
evaluating factorial of -211
evaluating factorial of -212
evaluating factorial of -213
evaluating factorial of -214
evaluating factorial of -215
evaluating factorial of -216
evaluating factorial of -217
evaluating factorial of -218
evaluating factorial of -219
evaluating factorial of -220
evaluating factorial of -221
evaluating factorial of -222
evaluating factorial of -223
evaluating factorial of -224
evaluating factorial of -225

---

## Page 5

evaluating factorial of -226
evaluating factorial of -227
evaluating factorial of -228
evaluating factorial of -229
evaluating factorial of -230
evaluating factorial of -231
evaluating factorial of -232
evaluating factorial of -233
evaluating factorial of -234
evaluating factorial of -235
evaluating factorial of -236
evaluating factorial of -237
evaluating factorial of -238
evaluating factorial of -239
evaluating factorial of -240
evaluating factorial of -241
evaluating factorial of -242
evaluating factorial of -243
evaluating factorial of -244
evaluating factorial of -245
evaluating factorial of -246
evaluating factorial of -247
evaluating factorial of -248
evaluating factorial of -249
evaluating factorial of -250
evaluating factorial of -251
evaluating factorial of -252
evaluating factorial of -253
evaluating factorial of -254
evaluating factorial of -255
evaluating factorial of -256
evaluating factorial of -257
evaluating factorial of -258
evaluating factorial of -259
evaluating factorial of -260
evaluating factorial of -261
evaluating factorial of -262
evaluating factorial of -263
evaluating factorial of -264
evaluating factorial of -265
evaluating factorial of -266
evaluating factorial of -267
evaluating factorial of -268
evaluating factorial of -269
evaluating factorial of -270
evaluating factorial of -271
evaluating factorial of -272
evaluating factorial of -273
evaluating factorial of -274
evaluating factorial of -275
evaluating factorial of -276
evaluating factorial of -277
evaluating factorial of -278
evaluating factorial of -279
evaluating factorial of -280
evaluating factorial of -281
evaluating factorial of -282
evaluating factorial of -283
evaluating factorial of -284
evaluating factorial of -285
evaluating factorial of -286
evaluating factorial of -287
evaluating factorial of -288
evaluating factorial of -289
evaluating factorial of -290
evaluating factorial of -291
evaluating factorial of -292
evaluating factorial of -293
evaluating factorial of -294
evaluating factorial of -295
evaluating factorial of -296
evaluating factorial of -297
evaluating factorial of -298
evaluating factorial of -299
evaluating factorial of -300

---

## Page 6

evaluating factorial of -301
evaluating factorial of -302
evaluating factorial of -303
evaluating factorial of -304
evaluating factorial of -305
evaluating factorial of -306
evaluating factorial of -307
evaluating factorial of -308
evaluating factorial of -309
evaluating factorial of -310
evaluating factorial of -311
evaluating factorial of -312
evaluating factorial of -313
evaluating factorial of -314
evaluating factorial of -315
evaluating factorial of -316
evaluating factorial of -317
evaluating factorial of -318
evaluating factorial of -319
evaluating factorial of -320
evaluating factorial of -321
evaluating factorial of -322
evaluating factorial of -323
evaluating factorial of -324
evaluating factorial of -325
evaluating factorial of -326
evaluating factorial of -327
evaluating factorial of -328
evaluating factorial of -329
evaluating factorial of -330
evaluating factorial of -331
evaluating factorial of -332
evaluating factorial of -333
evaluating factorial of -334
evaluating factorial of -335
evaluating factorial of -336
evaluating factorial of -337
evaluating factorial of -338
evaluating factorial of -339
evaluating factorial of -340
evaluating factorial of -341
evaluating factorial of -342
evaluating factorial of -343
evaluating factorial of -344
evaluating factorial of -345
evaluating factorial of -346
evaluating factorial of -347
evaluating factorial of -348
evaluating factorial of -349
evaluating factorial of -350
evaluating factorial of -351
evaluating factorial of -352
evaluating factorial of -353
evaluating factorial of -354
evaluating factorial of -355
evaluating factorial of -356
evaluating factorial of -357
evaluating factorial of -358
evaluating factorial of -359
evaluating factorial of -360
evaluating factorial of -361
evaluating factorial of -362
evaluating factorial of -363
evaluating factorial of -364
evaluating factorial of -365
evaluating factorial of -366
evaluating factorial of -367
evaluating factorial of -368
evaluating factorial of -369
evaluating factorial of -370
evaluating factorial of -371
evaluating factorial of -372
evaluating factorial of -373
evaluating factorial of -374
evaluating factorial of -375

---

## Page 7

evaluating factorial of -376
evaluating factorial of -377
evaluating factorial of -378
evaluating factorial of -379
evaluating factorial of -380
evaluating factorial of -381
evaluating factorial of -382
evaluating factorial of -383
evaluating factorial of -384
evaluating factorial of -385
evaluating factorial of -386
evaluating factorial of -387
evaluating factorial of -388
evaluating factorial of -389
evaluating factorial of -390
evaluating factorial of -391
evaluating factorial of -392
evaluating factorial of -393
evaluating factorial of -394
evaluating factorial of -395
evaluating factorial of -396
evaluating factorial of -397
evaluating factorial of -398
evaluating factorial of -399
evaluating factorial of -400
evaluating factorial of -401
evaluating factorial of -402
evaluating factorial of -403
evaluating factorial of -404
evaluating factorial of -405
evaluating factorial of -406
evaluating factorial of -407
evaluating factorial of -408
evaluating factorial of -409
evaluating factorial of -410
evaluating factorial of -411
evaluating factorial of -412
evaluating factorial of -413
evaluating factorial of -414
evaluating factorial of -415
evaluating factorial of -416
evaluating factorial of -417
evaluating factorial of -418
evaluating factorial of -419
evaluating factorial of -420
evaluating factorial of -421
evaluating factorial of -422
evaluating factorial of -423
evaluating factorial of -424
evaluating factorial of -425
evaluating factorial of -426
evaluating factorial of -427
evaluating factorial of -428
evaluating factorial of -429
evaluating factorial of -430
evaluating factorial of -431
evaluating factorial of -432
evaluating factorial of -433
evaluating factorial of -434
evaluating factorial of -435
evaluating factorial of -436
evaluating factorial of -437
evaluating factorial of -438
evaluating factorial of -439
evaluating factorial of -440
evaluating factorial of -441
evaluating factorial of -442
evaluating factorial of -443
evaluating factorial of -444
evaluating factorial of -445
evaluating factorial of -446
evaluating factorial of -447
evaluating factorial of -448
evaluating factorial of -449
evaluating factorial of -450

---

## Page 8

evaluating factorial of -451
evaluating factorial of -452
evaluating factorial of -453
evaluating factorial of -454
evaluating factorial of -455
evaluating factorial of -456
evaluating factorial of -457
evaluating factorial of -458
evaluating factorial of -459
evaluating factorial of -460
evaluating factorial of -461
evaluating factorial of -462
evaluating factorial of -463
evaluating factorial of -464
evaluating factorial of -465
evaluating factorial of -466
evaluating factorial of -467
evaluating factorial of -468
evaluating factorial of -469
evaluating factorial of -470
evaluating factorial of -471
evaluating factorial of -472
evaluating factorial of -473
evaluating factorial of -474
evaluating factorial of -475
evaluating factorial of -476
evaluating factorial of -477
evaluating factorial of -478
evaluating factorial of -479
evaluating factorial of -480
evaluating factorial of -481
evaluating factorial of -482
evaluating factorial of -483
evaluating factorial of -484
evaluating factorial of -485
evaluating factorial of -486
evaluating factorial of -487
evaluating factorial of -488
evaluating factorial of -489
evaluating factorial of -490
evaluating factorial of -491
evaluating factorial of -492
evaluating factorial of -493
evaluating factorial of -494
evaluating factorial of -495
evaluating factorial of -496
evaluating factorial of -497
evaluating factorial of -498
evaluating factorial of -499
evaluating factorial of -500
evaluating factorial of -501
evaluating factorial of -502
evaluating factorial of -503
evaluating factorial of -504
evaluating factorial of -505
evaluating factorial of -506
evaluating factorial of -507
evaluating factorial of -508
evaluating factorial of -509
evaluating factorial of -510
evaluating factorial of -511
evaluating factorial of -512
evaluating factorial of -513
evaluating factorial of -514
evaluating factorial of -515
evaluating factorial of -516
evaluating factorial of -517
evaluating factorial of -518
evaluating factorial of -519
evaluating factorial of -520
evaluating factorial of -521
evaluating factorial of -522
evaluating factorial of -523
evaluating factorial of -524
evaluating factorial of -525

---

## Page 9

evaluating factorial of -526
evaluating factorial of -527
evaluating factorial of -528
evaluating factorial of -529
evaluating factorial of -530
evaluating factorial of -531
evaluating factorial of -532
evaluating factorial of -533
evaluating factorial of -534
evaluating factorial of -535
evaluating factorial of -536
evaluating factorial of -537
evaluating factorial of -538
evaluating factorial of -539
evaluating factorial of -540
evaluating factorial of -541
evaluating factorial of -542
evaluating factorial of -543
evaluating factorial of -544
evaluating factorial of -545
evaluating factorial of -546
evaluating factorial of -547
evaluating factorial of -548
evaluating factorial of -549
evaluating factorial of -550
evaluating factorial of -551
evaluating factorial of -552
evaluating factorial of -553
evaluating factorial of -554
evaluating factorial of -555
evaluating factorial of -556
evaluating factorial of -557
evaluating factorial of -558
evaluating factorial of -559
evaluating factorial of -560
evaluating factorial of -561
evaluating factorial of -562
evaluating factorial of -563
evaluating factorial of -564
evaluating factorial of -565
evaluating factorial of -566
evaluating factorial of -567
evaluating factorial of -568
evaluating factorial of -569
evaluating factorial of -570
evaluating factorial of -571
evaluating factorial of -572
evaluating factorial of -573
evaluating factorial of -574
evaluating factorial of -575
evaluating factorial of -576
evaluating factorial of -577
evaluating factorial of -578
evaluating factorial of -579
evaluating factorial of -580
evaluating factorial of -581
evaluating factorial of -582
evaluating factorial of -583
evaluating factorial of -584
evaluating factorial of -585
evaluating factorial of -586
evaluating factorial of -587
evaluating factorial of -588
evaluating factorial of -589
evaluating factorial of -590
evaluating factorial of -591
evaluating factorial of -592
evaluating factorial of -593
evaluating factorial of -594
evaluating factorial of -595
evaluating factorial of -596
evaluating factorial of -597
evaluating factorial of -598
evaluating factorial of -599
evaluating factorial of -600

---

## Page 10

evaluating factorial of -601
evaluating factorial of -602
evaluating factorial of -603
evaluating factorial of -604
evaluating factorial of -605
evaluating factorial of -606
evaluating factorial of -607
evaluating factorial of -608
evaluating factorial of -609
evaluating factorial of -610
evaluating factorial of -611
evaluating factorial of -612
evaluating factorial of -613
evaluating factorial of -614
evaluating factorial of -615
evaluating factorial of -616
evaluating factorial of -617
evaluating factorial of -618
evaluating factorial of -619
evaluating factorial of -620
evaluating factorial of -621
evaluating factorial of -622
evaluating factorial of -623
evaluating factorial of -624
evaluating factorial of -625
evaluating factorial of -626
evaluating factorial of -627
evaluating factorial of -628
evaluating factorial of -629
evaluating factorial of -630
evaluating factorial of -631
evaluating factorial of -632
evaluating factorial of -633
evaluating factorial of -634
evaluating factorial of -635
evaluating factorial of -636
evaluating factorial of -637
evaluating factorial of -638
evaluating factorial of -639
evaluating factorial of -640
evaluating factorial of -641
evaluating factorial of -642
evaluating factorial of -643
evaluating factorial of -644
evaluating factorial of -645
evaluating factorial of -646
evaluating factorial of -647
evaluating factorial of -648
evaluating factorial of -649
evaluating factorial of -650
evaluating factorial of -651
evaluating factorial of -652
evaluating factorial of -653
evaluating factorial of -654
evaluating factorial of -655
evaluating factorial of -656
evaluating factorial of -657
evaluating factorial of -658
evaluating factorial of -659
evaluating factorial of -660
evaluating factorial of -661
evaluating factorial of -662
evaluating factorial of -663
evaluating factorial of -664
evaluating factorial of -665
evaluating factorial of -666
evaluating factorial of -667
evaluating factorial of -668
evaluating factorial of -669
evaluating factorial of -670
evaluating factorial of -671
evaluating factorial of -672
evaluating factorial of -673
evaluating factorial of -674
evaluating factorial of -675

---

## Page 11

evaluating factorial of -676
evaluating factorial of -677
evaluating factorial of -678
evaluating factorial of -679
evaluating factorial of -680
evaluating factorial of -681
evaluating factorial of -682
evaluating factorial of -683
evaluating factorial of -684
evaluating factorial of -685
evaluating factorial of -686
evaluating factorial of -687
evaluating factorial of -688
evaluating factorial of -689
evaluating factorial of -690
evaluating factorial of -691
evaluating factorial of -692
evaluating factorial of -693
evaluating factorial of -694
evaluating factorial of -695
evaluating factorial of -696
evaluating factorial of -697
evaluating factorial of -698
evaluating factorial of -699
evaluating factorial of -700
evaluating factorial of -701
evaluating factorial of -702
evaluating factorial of -703
evaluating factorial of -704
evaluating factorial of -705
evaluating factorial of -706
evaluating factorial of -707
evaluating factorial of -708
evaluating factorial of -709
evaluating factorial of -710
evaluating factorial of -711
evaluating factorial of -712
evaluating factorial of -713
evaluating factorial of -714
evaluating factorial of -715
evaluating factorial of -716
evaluating factorial of -717
evaluating factorial of -718
evaluating factorial of -719
evaluating factorial of -720
evaluating factorial of -721
evaluating factorial of -722
evaluating factorial of -723
evaluating factorial of -724
evaluating factorial of -725
evaluating factorial of -726
evaluating factorial of -727
evaluating factorial of -728
evaluating factorial of -729
evaluating factorial of -730
evaluating factorial of -731
evaluating factorial of -732
evaluating factorial of -733
evaluating factorial of -734
evaluating factorial of -735
evaluating factorial of -736
evaluating factorial of -737
evaluating factorial of -738
evaluating factorial of -739
evaluating factorial of -740
evaluating factorial of -741
evaluating factorial of -742
evaluating factorial of -743
evaluating factorial of -744
evaluating factorial of -745
evaluating factorial of -746
evaluating factorial of -747
evaluating factorial of -748
evaluating factorial of -749
evaluating factorial of -750

---

## Page 12

evaluating factorial of -751
evaluating factorial of -752
evaluating factorial of -753
evaluating factorial of -754
evaluating factorial of -755
evaluating factorial of -756
evaluating factorial of -757
evaluating factorial of -758
evaluating factorial of -759
evaluating factorial of -760
evaluating factorial of -761
evaluating factorial of -762
evaluating factorial of -763
evaluating factorial of -764
evaluating factorial of -765
evaluating factorial of -766
evaluating factorial of -767
evaluating factorial of -768
evaluating factorial of -769
evaluating factorial of -770
evaluating factorial of -771
evaluating factorial of -772
evaluating factorial of -773
evaluating factorial of -774
evaluating factorial of -775
evaluating factorial of -776
evaluating factorial of -777
evaluating factorial of -778
evaluating factorial of -779
evaluating factorial of -780
evaluating factorial of -781
evaluating factorial of -782
evaluating factorial of -783
evaluating factorial of -784
evaluating factorial of -785
evaluating factorial of -786
evaluating factorial of -787
evaluating factorial of -788
evaluating factorial of -789
evaluating factorial of -790
evaluating factorial of -791
evaluating factorial of -792
evaluating factorial of -793
evaluating factorial of -794
evaluating factorial of -795
evaluating factorial of -796
evaluating factorial of -797
evaluating factorial of -798
evaluating factorial of -799
evaluating factorial of -800
evaluating factorial of -801
evaluating factorial of -802
evaluating factorial of -803
evaluating factorial of -804
evaluating factorial of -805
evaluating factorial of -806
evaluating factorial of -807
evaluating factorial of -808
evaluating factorial of -809
evaluating factorial of -810
evaluating factorial of -811
evaluating factorial of -812
evaluating factorial of -813
evaluating factorial of -814
evaluating factorial of -815
evaluating factorial of -816
evaluating factorial of -817
evaluating factorial of -818
evaluating factorial of -819
evaluating factorial of -820
evaluating factorial of -821
evaluating factorial of -822
evaluating factorial of -823
evaluating factorial of -824
evaluating factorial of -825

---

## Page 13

evaluating factorial of -826
evaluating factorial of -827
evaluating factorial of -828
evaluating factorial of -829
evaluating factorial of -830
evaluating factorial of -831
evaluating factorial of -832
evaluating factorial of -833
evaluating factorial of -834
evaluating factorial of -835
evaluating factorial of -836
evaluating factorial of -837
evaluating factorial of -838
evaluating factorial of -839
evaluating factorial of -840
evaluating factorial of -841
evaluating factorial of -842
evaluating factorial of -843
evaluating factorial of -844
evaluating factorial of -845
evaluating factorial of -846
evaluating factorial of -847
evaluating factorial of -848
evaluating factorial of -849
evaluating factorial of -850
evaluating factorial of -851
evaluating factorial of -852
evaluating factorial of -853
evaluating factorial of -854
evaluating factorial of -855
evaluating factorial of -856
evaluating factorial of -857
evaluating factorial of -858
evaluating factorial of -859
evaluating factorial of -860
evaluating factorial of -861
evaluating factorial of -862
evaluating factorial of -863
evaluating factorial of -864
evaluating factorial of -865
evaluating factorial of -866
evaluating factorial of -867
evaluating factorial of -868
evaluating factorial of -869
evaluating factorial of -870
evaluating factorial of -871
evaluating factorial of -872
evaluating factorial of -873
evaluating factorial of -874
evaluating factorial of -875
evaluating factorial of -876
evaluating factorial of -877
evaluating factorial of -878
evaluating factorial of -879
evaluating factorial of -880
evaluating factorial of -881
evaluating factorial of -882
evaluating factorial of -883
evaluating factorial of -884
evaluating factorial of -885
evaluating factorial of -886
evaluating factorial of -887
evaluating factorial of -888
evaluating factorial of -889
evaluating factorial of -890
evaluating factorial of -891
evaluating factorial of -892
evaluating factorial of -893
evaluating factorial of -894
evaluating factorial of -895
evaluating factorial of -896
evaluating factorial of -897
evaluating factorial of -898
evaluating factorial of -899
evaluating factorial of -900

---

## Page 14

evaluating factorial of -901
evaluating factorial of -902
evaluating factorial of -903
evaluating factorial of -904
evaluating factorial of -905
evaluating factorial of -906
evaluating factorial of -907
evaluating factorial of -908
evaluating factorial of -909
evaluating factorial of -910
evaluating factorial of -911
evaluating factorial of -912
evaluating factorial of -913
evaluating factorial of -914
evaluating factorial of -915
evaluating factorial of -916
evaluating factorial of -917
evaluating factorial of -918
evaluating factorial of -919
evaluating factorial of -920
evaluating factorial of -921
evaluating factorial of -922
evaluating factorial of -923
evaluating factorial of -924
evaluating factorial of -925
evaluating factorial of -926
evaluating factorial of -927
evaluating factorial of -928
evaluating factorial of -929
evaluating factorial of -930
evaluating factorial of -931
evaluating factorial of -932
evaluating factorial of -933
evaluating factorial of -934
evaluating factorial of -935
evaluating factorial of -936
evaluating factorial of -937
evaluating factorial of -938
evaluating factorial of -939
evaluating factorial of -940
evaluating factorial of -941
evaluating factorial of -942
evaluating factorial of -943
evaluating factorial of -944
evaluating factorial of -945
evaluating factorial of -946
evaluating factorial of -947
evaluating factorial of -948
evaluating factorial of -949
evaluating factorial of -950
evaluating factorial of -951
evaluating factorial of -952
evaluating factorial of -953
evaluating factorial of -954
evaluating factorial of -955
evaluating factorial of -956
evaluating factorial of -957
evaluating factorial of -958
evaluating factorial of -959
evaluating factorial of -960
evaluating factorial of -961
evaluating factorial of -962
evaluating factorial of -963
evaluating factorial of -964
evaluating factorial of -965
evaluating factorial of -966
evaluating factorial of -967
evaluating factorial of -968
evaluating factorial of -969
evaluating factorial of -970
evaluating factorial of -971
evaluating factorial of -972
evaluating factorial of -973
evaluating factorial of -974
evaluating factorial of -975

---

## Page 15

evaluating factorial of -976
evaluating factorial of -977
evaluating factorial of -978
evaluating factorial of -979
evaluating factorial of -980
evaluating factorial of -981
evaluating factorial of -982
evaluating factorial of -983
evaluating factorial of -984
evaluating factorial of -985
evaluating factorial of -986
evaluating factorial of -987
evaluating factorial of -988
evaluating factorial of -989
evaluating factorial of -990
evaluating factorial of -991
evaluating factorial of -992
evaluating factorial of -993
evaluating factorial of -994
evaluating factorial of -995
evaluating factorial of -996
evaluating factorial of -997
evaluating factorial of -998
evaluating factorial of -999
evaluating factorial of -1000
evaluating factorial of -1001
evaluating factorial of -1002
evaluating factorial of -1003
evaluating factorial of -1004
evaluating factorial of -1005
evaluating factorial of -1006
evaluating factorial of -1007
evaluating factorial of -1008
evaluating factorial of -1009
evaluating factorial of -1010
evaluating factorial of -1011
evaluating factorial of -1012
evaluating factorial of -1013
evaluating factorial of -1014
evaluating factorial of -1015
evaluating factorial of -1016
evaluating factorial of -1017
evaluating factorial of -1018
evaluating factorial of -1019
evaluating factorial of -1020
evaluating factorial of -1021
evaluating factorial of -1022
evaluating factorial of -1023
evaluating factorial of -1024
evaluating factorial of -1025
evaluating factorial of -1026
evaluating factorial of -1027
evaluating factorial of -1028
evaluating factorial of -1029
evaluating factorial of -1030
evaluating factorial of -1031
evaluating factorial of -1032
evaluating factorial of -1033
evaluating factorial of -1034
evaluating factorial of -1035
evaluating factorial of -1036
evaluating factorial of -1037
evaluating factorial of -1038
evaluating factorial of -1039
evaluating factorial of -1040
evaluating factorial of -1041
evaluating factorial of -1042
evaluating factorial of -1043
evaluating factorial of -1044
evaluating factorial of -1045
evaluating factorial of -1046
evaluating factorial of -1047
evaluating factorial of -1048
evaluating factorial of -1049
evaluating factorial of -1050

---

## Page 16

evaluating factorial of -1051
evaluating factorial of -1052
evaluating factorial of -1053
evaluating factorial of -1054
evaluating factorial of -1055
evaluating factorial of -1056
evaluating factorial of -1057
evaluating factorial of -1058
evaluating factorial of -1059
evaluating factorial of -1060
evaluating factorial of -1061
evaluating factorial of -1062
evaluating factorial of -1063
evaluating factorial of -1064
evaluating factorial of -1065
evaluating factorial of -1066
evaluating factorial of -1067
evaluating factorial of -1068
evaluating factorial of -1069
evaluating factorial of -1070
evaluating factorial of -1071
evaluating factorial of -1072
evaluating factorial of -1073
evaluating factorial of -1074
evaluating factorial of -1075
evaluating factorial of -1076
evaluating factorial of -1077
evaluating factorial of -1078
evaluating factorial of -1079
evaluating factorial of -1080
evaluating factorial of -1081
evaluating factorial of -1082
evaluating factorial of -1083
evaluating factorial of -1084
evaluating factorial of -1085
evaluating factorial of -1086
evaluating factorial of -1087
evaluating factorial of -1088
evaluating factorial of -1089
evaluating factorial of -1090
evaluating factorial of -1091
evaluating factorial of -1092
evaluating factorial of -1093
evaluating factorial of -1094
evaluating factorial of -1095
evaluating factorial of -1096
evaluating factorial of -1097
evaluating factorial of -1098
evaluating factorial of -1099
evaluating factorial of -1100
evaluating factorial of -1101
evaluating factorial of -1102
evaluating factorial of -1103
evaluating factorial of -1104
evaluating factorial of -1105
evaluating factorial of -1106
evaluating factorial of -1107
evaluating factorial of -1108
evaluating factorial of -1109
evaluating factorial of -1110
evaluating factorial of -1111
evaluating factorial of -1112
evaluating factorial of -1113
evaluating factorial of -1114
evaluating factorial of -1115
evaluating factorial of -1116
evaluating factorial of -1117
evaluating factorial of -1118
evaluating factorial of -1119
evaluating factorial of -1120
evaluating factorial of -1121
evaluating factorial of -1122
evaluating factorial of -1123
evaluating factorial of -1124
evaluating factorial of -1125

---

## Page 17

evaluating factorial of -1126
evaluating factorial of -1127
evaluating factorial of -1128
evaluating factorial of -1129
evaluating factorial of -1130
evaluating factorial of -1131
evaluating factorial of -1132
evaluating factorial of -1133
evaluating factorial of -1134
evaluating factorial of -1135
evaluating factorial of -1136
evaluating factorial of -1137
evaluating factorial of -1138
evaluating factorial of -1139
evaluating factorial of -1140
evaluating factorial of -1141
evaluating factorial of -1142
evaluating factorial of -1143
evaluating factorial of -1144
evaluating factorial of -1145
evaluating factorial of -1146
evaluating factorial of -1147
evaluating factorial of -1148
evaluating factorial of -1149
evaluating factorial of -1150
evaluating factorial of -1151
evaluating factorial of -1152
evaluating factorial of -1153
evaluating factorial of -1154
evaluating factorial of -1155
evaluating factorial of -1156
evaluating factorial of -1157
evaluating factorial of -1158
evaluating factorial of -1159
evaluating factorial of -1160
evaluating factorial of -1161
evaluating factorial of -1162
evaluating factorial of -1163
evaluating factorial of -1164
evaluating factorial of -1165
evaluating factorial of -1166
evaluating factorial of -1167
evaluating factorial of -1168
evaluating factorial of -1169
evaluating factorial of -1170
evaluating factorial of -1171
evaluating factorial of -1172
evaluating factorial of -1173
evaluating factorial of -1174
evaluating factorial of -1175
evaluating factorial of -1176
evaluating factorial of -1177
evaluating factorial of -1178
evaluating factorial of -1179
evaluating factorial of -1180
evaluating factorial of -1181
evaluating factorial of -1182
evaluating factorial of -1183
evaluating factorial of -1184
evaluating factorial of -1185
evaluating factorial of -1186
evaluating factorial of -1187
evaluating factorial of -1188
evaluating factorial of -1189
evaluating factorial of -1190
evaluating factorial of -1191
evaluating factorial of -1192
evaluating factorial of -1193
evaluating factorial of -1194
evaluating factorial of -1195
evaluating factorial of -1196
evaluating factorial of -1197
evaluating factorial of -1198
evaluating factorial of -1199
evaluating factorial of -1200

---

## Page 18

evaluating factorial of -1201
evaluating factorial of -1202
evaluating factorial of -1203
evaluating factorial of -1204
evaluating factorial of -1205
evaluating factorial of -1206
evaluating factorial of -1207
evaluating factorial of -1208
evaluating factorial of -1209
evaluating factorial of -1210
evaluating factorial of -1211
evaluating factorial of -1212
evaluating factorial of -1213
evaluating factorial of -1214
evaluating factorial of -1215
evaluating factorial of -1216
evaluating factorial of -1217
evaluating factorial of -1218
evaluating factorial of -1219
evaluating factorial of -1220
evaluating factorial of -1221
evaluating factorial of -1222
evaluating factorial of -1223
evaluating factorial of -1224
evaluating factorial of -1225
evaluating factorial of -1226
evaluating factorial of -1227
evaluating factorial of -1228
evaluating factorial of -1229
evaluating factorial of -1230
evaluating factorial of -1231
evaluating factorial of -1232
evaluating factorial of -1233
evaluating factorial of -1234
evaluating factorial of -1235
evaluating factorial of -1236
evaluating factorial of -1237
evaluating factorial of -1238
evaluating factorial of -1239
evaluating factorial of -1240
evaluating factorial of -1241
evaluating factorial of -1242
evaluating factorial of -1243
evaluating factorial of -1244
evaluating factorial of -1245
evaluating factorial of -1246
evaluating factorial of -1247
evaluating factorial of -1248
evaluating factorial of -1249
evaluating factorial of -1250
evaluating factorial of -1251
evaluating factorial of -1252
evaluating factorial of -1253
evaluating factorial of -1254
evaluating factorial of -1255
evaluating factorial of -1256
evaluating factorial of -1257
evaluating factorial of -1258
evaluating factorial of -1259
evaluating factorial of -1260
evaluating factorial of -1261
evaluating factorial of -1262
evaluating factorial of -1263
evaluating factorial of -1264
evaluating factorial of -1265
evaluating factorial of -1266
evaluating factorial of -1267
evaluating factorial of -1268
evaluating factorial of -1269
evaluating factorial of -1270
evaluating factorial of -1271
evaluating factorial of -1272
evaluating factorial of -1273
evaluating factorial of -1274
evaluating factorial of -1275

---

## Page 19

evaluating factorial of -1276
evaluating factorial of -1277
evaluating factorial of -1278
evaluating factorial of -1279
evaluating factorial of -1280
evaluating factorial of -1281
evaluating factorial of -1282
evaluating factorial of -1283
evaluating factorial of -1284
evaluating factorial of -1285
evaluating factorial of -1286
evaluating factorial of -1287
evaluating factorial of -1288
evaluating factorial of -1289
evaluating factorial of -1290
evaluating factorial of -1291
evaluating factorial of -1292
evaluating factorial of -1293
evaluating factorial of -1294
evaluating factorial of -1295
evaluating factorial of -1296
evaluating factorial of -1297
evaluating factorial of -1298
evaluating factorial of -1299
evaluating factorial of -1300
evaluating factorial of -1301
evaluating factorial of -1302
evaluating factorial of -1303
evaluating factorial of -1304
evaluating factorial of -1305
evaluating factorial of -1306
evaluating factorial of -1307
evaluating factorial of -1308
evaluating factorial of -1309
evaluating factorial of -1310
evaluating factorial of -1311
evaluating factorial of -1312
evaluating factorial of -1313
evaluating factorial of -1314
evaluating factorial of -1315
evaluating factorial of -1316
evaluating factorial of -1317
evaluating factorial of -1318
evaluating factorial of -1319
evaluating factorial of -1320
evaluating factorial of -1321
evaluating factorial of -1322
evaluating factorial of -1323
evaluating factorial of -1324
evaluating factorial of -1325
evaluating factorial of -1326
evaluating factorial of -1327
evaluating factorial of -1328
evaluating factorial of -1329
evaluating factorial of -1330
evaluating factorial of -1331
evaluating factorial of -1332
evaluating factorial of -1333
evaluating factorial of -1334
evaluating factorial of -1335
evaluating factorial of -1336
evaluating factorial of -1337
evaluating factorial of -1338
evaluating factorial of -1339
evaluating factorial of -1340
evaluating factorial of -1341
evaluating factorial of -1342
evaluating factorial of -1343
evaluating factorial of -1344
evaluating factorial of -1345
evaluating factorial of -1346
evaluating factorial of -1347
evaluating factorial of -1348
evaluating factorial of -1349
evaluating factorial of -1350

---

## Page 20

evaluating factorial of -1351
evaluating factorial of -1352
evaluating factorial of -1353
evaluating factorial of -1354
evaluating factorial of -1355
evaluating factorial of -1356
evaluating factorial of -1357
evaluating factorial of -1358
evaluating factorial of -1359
evaluating factorial of -1360
evaluating factorial of -1361
evaluating factorial of -1362
evaluating factorial of -1363
evaluating factorial of -1364
evaluating factorial of -1365
evaluating factorial of -1366
evaluating factorial of -1367
evaluating factorial of -1368
evaluating factorial of -1369
evaluating factorial of -1370
evaluating factorial of -1371
evaluating factorial of -1372
evaluating factorial of -1373
evaluating factorial of -1374
evaluating factorial of -1375
evaluating factorial of -1376
evaluating factorial of -1377
evaluating factorial of -1378
evaluating factorial of -1379
evaluating factorial of -1380
evaluating factorial of -1381
evaluating factorial of -1382
evaluating factorial of -1383
evaluating factorial of -1384
evaluating factorial of -1385
evaluating factorial of -1386
evaluating factorial of -1387
evaluating factorial of -1388
evaluating factorial of -1389
evaluating factorial of -1390
evaluating factorial of -1391
evaluating factorial of -1392
evaluating factorial of -1393
evaluating factorial of -1394
evaluating factorial of -1395
evaluating factorial of -1396
evaluating factorial of -1397
evaluating factorial of -1398
evaluating factorial of -1399
evaluating factorial of -1400
evaluating factorial of -1401
evaluating factorial of -1402
evaluating factorial of -1403
evaluating factorial of -1404
evaluating factorial of -1405
evaluating factorial of -1406
evaluating factorial of -1407
evaluating factorial of -1408
evaluating factorial of -1409
evaluating factorial of -1410
evaluating factorial of -1411
evaluating factorial of -1412
evaluating factorial of -1413
evaluating factorial of -1414
evaluating factorial of -1415
evaluating factorial of -1416
evaluating factorial of -1417
evaluating factorial of -1418
evaluating factorial of -1419
evaluating factorial of -1420
evaluating factorial of -1421
evaluating factorial of -1422
evaluating factorial of -1423
evaluating factorial of -1424
evaluating factorial of -1425

---

## Page 21

evaluating factorial of -1426
evaluating factorial of -1427
evaluating factorial of -1428
evaluating factorial of -1429
evaluating factorial of -1430
evaluating factorial of -1431
evaluating factorial of -1432
evaluating factorial of -1433
evaluating factorial of -1434
evaluating factorial of -1435
evaluating factorial of -1436
evaluating factorial of -1437
evaluating factorial of -1438
evaluating factorial of -1439
evaluating factorial of -1440
evaluating factorial of -1441
evaluating factorial of -1442
evaluating factorial of -1443
evaluating factorial of -1444
evaluating factorial of -1445
evaluating factorial of -1446
evaluating factorial of -1447
evaluating factorial of -1448
evaluating factorial of -1449
evaluating factorial of -1450
evaluating factorial of -1451
evaluating factorial of -1452
evaluating factorial of -1453
evaluating factorial of -1454
evaluating factorial of -1455
evaluating factorial of -1456
evaluating factorial of -1457
evaluating factorial of -1458
evaluating factorial of -1459
evaluating factorial of -1460
evaluating factorial of -1461
evaluating factorial of -1462
evaluating factorial of -1463
evaluating factorial of -1464
evaluating factorial of -1465
evaluating factorial of -1466
evaluating factorial of -1467
evaluating factorial of -1468
evaluating factorial of -1469
evaluating factorial of -1470
evaluating factorial of -1471
evaluating factorial of -1472
evaluating factorial of -1473
evaluating factorial of -1474
evaluating factorial of -1475
evaluating factorial of -1476
evaluating factorial of -1477
evaluating factorial of -1478
evaluating factorial of -1479
evaluating factorial of -1480
evaluating factorial of -1481
evaluating factorial of -1482
evaluating factorial of -1483
evaluating factorial of -1484
evaluating factorial of -1485
evaluating factorial of -1486
evaluating factorial of -1487
evaluating factorial of -1488
evaluating factorial of -1489
evaluating factorial of -1490
evaluating factorial of -1491
evaluating factorial of -1492
evaluating factorial of -1493
evaluating factorial of -1494
evaluating factorial of -1495
evaluating factorial of -1496
evaluating factorial of -1497
evaluating factorial of -1498
evaluating factorial of -1499
evaluating factorial of -1500

---

## Page 22

evaluating factorial of -1501
evaluating factorial of -1502
evaluating factorial of -1503
evaluating factorial of -1504
evaluating factorial of -1505
evaluating factorial of -1506
evaluating factorial of -1507
evaluating factorial of -1508
evaluating factorial of -1509
evaluating factorial of -1510
evaluating factorial of -1511
evaluating factorial of -1512
evaluating factorial of -1513
evaluating factorial of -1514
evaluating factorial of -1515
evaluating factorial of -1516
evaluating factorial of -1517
evaluating factorial of -1518
evaluating factorial of -1519
evaluating factorial of -1520
evaluating factorial of -1521
evaluating factorial of -1522
evaluating factorial of -1523
evaluating factorial of -1524
evaluating factorial of -1525
evaluating factorial of -1526
evaluating factorial of -1527
evaluating factorial of -1528
evaluating factorial of -1529
evaluating factorial of -1530
evaluating factorial of -1531
evaluating factorial of -1532
evaluating factorial of -1533
evaluating factorial of -1534
evaluating factorial of -1535
evaluating factorial of -1536
evaluating factorial of -1537
evaluating factorial of -1538
evaluating factorial of -1539
evaluating factorial of -1540
evaluating factorial of -1541
evaluating factorial of -1542
evaluating factorial of -1543
evaluating factorial of -1544
evaluating factorial of -1545
evaluating factorial of -1546
evaluating factorial of -1547
evaluating factorial of -1548
evaluating factorial of -1549
evaluating factorial of -1550
evaluating factorial of -1551
evaluating factorial of -1552
evaluating factorial of -1553
evaluating factorial of -1554
evaluating factorial of -1555
evaluating factorial of -1556
evaluating factorial of -1557
evaluating factorial of -1558
evaluating factorial of -1559
evaluating factorial of -1560
evaluating factorial of -1561
evaluating factorial of -1562
evaluating factorial of -1563
evaluating factorial of -1564
evaluating factorial of -1565
evaluating factorial of -1566
evaluating factorial of -1567
evaluating factorial of -1568
evaluating factorial of -1569
evaluating factorial of -1570
evaluating factorial of -1571
evaluating factorial of -1572
evaluating factorial of -1573
evaluating factorial of -1574
evaluating factorial of -1575

---

## Page 23

evaluating factorial of -1576
evaluating factorial of -1577
evaluating factorial of -1578
evaluating factorial of -1579
evaluating factorial of -1580
evaluating factorial of -1581
evaluating factorial of -1582
evaluating factorial of -1583
evaluating factorial of -1584
evaluating factorial of -1585
evaluating factorial of -1586
evaluating factorial of -1587
evaluating factorial of -1588
evaluating factorial of -1589
evaluating factorial of -1590
evaluating factorial of -1591
evaluating factorial of -1592
evaluating factorial of -1593
evaluating factorial of -1594
evaluating factorial of -1595
evaluating factorial of -1596
evaluating factorial of -1597
evaluating factorial of -1598
evaluating factorial of -1599
evaluating factorial of -1600
evaluating factorial of -1601
evaluating factorial of -1602
evaluating factorial of -1603
evaluating factorial of -1604
evaluating factorial of -1605
evaluating factorial of -1606
evaluating factorial of -1607
evaluating factorial of -1608
evaluating factorial of -1609
evaluating factorial of -1610
evaluating factorial of -1611
evaluating factorial of -1612
evaluating factorial of -1613
evaluating factorial of -1614
evaluating factorial of -1615
evaluating factorial of -1616
evaluating factorial of -1617
evaluating factorial of -1618
evaluating factorial of -1619
evaluating factorial of -1620
evaluating factorial of -1621
evaluating factorial of -1622
evaluating factorial of -1623
evaluating factorial of -1624
evaluating factorial of -1625
evaluating factorial of -1626
evaluating factorial of -1627
evaluating factorial of -1628
evaluating factorial of -1629
evaluating factorial of -1630
evaluating factorial of -1631
evaluating factorial of -1632
evaluating factorial of -1633
evaluating factorial of -1634
evaluating factorial of -1635
evaluating factorial of -1636
evaluating factorial of -1637
evaluating factorial of -1638
evaluating factorial of -1639
evaluating factorial of -1640
evaluating factorial of -1641
evaluating factorial of -1642
evaluating factorial of -1643
evaluating factorial of -1644
evaluating factorial of -1645
evaluating factorial of -1646
evaluating factorial of -1647
evaluating factorial of -1648
evaluating factorial of -1649
evaluating factorial of -1650

---

## Page 24

evaluating factorial of -1651
evaluating factorial of -1652
evaluating factorial of -1653
evaluating factorial of -1654
evaluating factorial of -1655
evaluating factorial of -1656
evaluating factorial of -1657
evaluating factorial of -1658
evaluating factorial of -1659
evaluating factorial of -1660
evaluating factorial of -1661
evaluating factorial of -1662
evaluating factorial of -1663
evaluating factorial of -1664
evaluating factorial of -1665
evaluating factorial of -1666
evaluating factorial of -1667
evaluating factorial of -1668
evaluating factorial of -1669
evaluating factorial of -1670
evaluating factorial of -1671
evaluating factorial of -1672
evaluating factorial of -1673
evaluating factorial of -1674
evaluating factorial of -1675
evaluating factorial of -1676
evaluating factorial of -1677
evaluating factorial of -1678
evaluating factorial of -1679
evaluating factorial of -1680
evaluating factorial of -1681
evaluating factorial of -1682
evaluating factorial of -1683
evaluating factorial of -1684
evaluating factorial of -1685
evaluating factorial of -1686
evaluating factorial of -1687
evaluating factorial of -1688
evaluating factorial of -1689
evaluating factorial of -1690
evaluating factorial of -1691
evaluating factorial of -1692
evaluating factorial of -1693
evaluating factorial of -1694
evaluating factorial of -1695
evaluating factorial of -1696
evaluating factorial of -1697
evaluating factorial of -1698
evaluating factorial of -1699
evaluating factorial of -1700
evaluating factorial of -1701
evaluating factorial of -1702
evaluating factorial of -1703
evaluating factorial of -1704
evaluating factorial of -1705
evaluating factorial of -1706
evaluating factorial of -1707
evaluating factorial of -1708
evaluating factorial of -1709
evaluating factorial of -1710
evaluating factorial of -1711
evaluating factorial of -1712
evaluating factorial of -1713
evaluating factorial of -1714
evaluating factorial of -1715
evaluating factorial of -1716
evaluating factorial of -1717
evaluating factorial of -1718
evaluating factorial of -1719
evaluating factorial of -1720
evaluating factorial of -1721
evaluating factorial of -1722
evaluating factorial of -1723
evaluating factorial of -1724
evaluating factorial of -1725

---

## Page 25

evaluating factorial of -1726
evaluating factorial of -1727
evaluating factorial of -1728
evaluating factorial of -1729
evaluating factorial of -1730
evaluating factorial of -1731
evaluating factorial of -1732
evaluating factorial of -1733
evaluating factorial of -1734
evaluating factorial of -1735
evaluating factorial of -1736
evaluating factorial of -1737
evaluating factorial of -1738
evaluating factorial of -1739
evaluating factorial of -1740
evaluating factorial of -1741
evaluating factorial of -1742
evaluating factorial of -1743
evaluating factorial of -1744
evaluating factorial of -1745
evaluating factorial of -1746
evaluating factorial of -1747
evaluating factorial of -1748
evaluating factorial of -1749
evaluating factorial of -1750
evaluating factorial of -1751
evaluating factorial of -1752
evaluating factorial of -1753
evaluating factorial of -1754
evaluating factorial of -1755
evaluating factorial of -1756
evaluating factorial of -1757
evaluating factorial of -1758
evaluating factorial of -1759
evaluating factorial of -1760
evaluating factorial of -1761
evaluating factorial of -1762
evaluating factorial of -1763
evaluating factorial of -1764
evaluating factorial of -1765
evaluating factorial of -1766
evaluating factorial of -1767
evaluating factorial of -1768
evaluating factorial of -1769
evaluating factorial of -1770
evaluating factorial of -1771
evaluating factorial of -1772
evaluating factorial of -1773
evaluating factorial of -1774
evaluating factorial of -1775
evaluating factorial of -1776
evaluating factorial of -1777
evaluating factorial of -1778
evaluating factorial of -1779
evaluating factorial of -1780
evaluating factorial of -1781
evaluating factorial of -1782
evaluating factorial of -1783
evaluating factorial of -1784
evaluating factorial of -1785
evaluating factorial of -1786
evaluating factorial of -1787
evaluating factorial of -1788
evaluating factorial of -1789
evaluating factorial of -1790
evaluating factorial of -1791
evaluating factorial of -1792
evaluating factorial of -1793
evaluating factorial of -1794
evaluating factorial of -1795
evaluating factorial of -1796
evaluating factorial of -1797
evaluating factorial of -1798
evaluating factorial of -1799
evaluating factorial of -1800

---

## Page 26

evaluating factorial of -1801
evaluating factorial of -1802
evaluating factorial of -1803
evaluating factorial of -1804
evaluating factorial of -1805
evaluating factorial of -1806
evaluating factorial of -1807
evaluating factorial of -1808
evaluating factorial of -1809
evaluating factorial of -1810
evaluating factorial of -1811
evaluating factorial of -1812
evaluating factorial of -1813
evaluating factorial of -1814
evaluating factorial of -1815
evaluating factorial of -1816
evaluating factorial of -1817
evaluating factorial of -1818
evaluating factorial of -1819
evaluating factorial of -1820
evaluating factorial of -1821
evaluating factorial of -1822
evaluating factorial of -1823
evaluating factorial of -1824
evaluating factorial of -1825
evaluating factorial of -1826
evaluating factorial of -1827
evaluating factorial of -1828
evaluating factorial of -1829
evaluating factorial of -1830
evaluating factorial of -1831
evaluating factorial of -1832
evaluating factorial of -1833
evaluating factorial of -1834
evaluating factorial of -1835
evaluating factorial of -1836
evaluating factorial of -1837
evaluating factorial of -1838
evaluating factorial of -1839
evaluating factorial of -1840
evaluating factorial of -1841
evaluating factorial of -1842
evaluating factorial of -1843
evaluating factorial of -1844
evaluating factorial of -1845
evaluating factorial of -1846
evaluating factorial of -1847
evaluating factorial of -1848
evaluating factorial of -1849
evaluating factorial of -1850
evaluating factorial of -1851
evaluating factorial of -1852
evaluating factorial of -1853
evaluating factorial of -1854
evaluating factorial of -1855
evaluating factorial of -1856
evaluating factorial of -1857
evaluating factorial of -1858
evaluating factorial of -1859
evaluating factorial of -1860
evaluating factorial of -1861
evaluating factorial of -1862
evaluating factorial of -1863
evaluating factorial of -1864
evaluating factorial of -1865
evaluating factorial of -1866
evaluating factorial of -1867
evaluating factorial of -1868
evaluating factorial of -1869
evaluating factorial of -1870
evaluating factorial of -1871
evaluating factorial of -1872
evaluating factorial of -1873
evaluating factorial of -1874
evaluating factorial of -1875

---

## Page 27

evaluating factorial of -1876
evaluating factorial of -1877
evaluating factorial of -1878
evaluating factorial of -1879
evaluating factorial of -1880
evaluating factorial of -1881
evaluating factorial of -1882
evaluating factorial of -1883
evaluating factorial of -1884
evaluating factorial of -1885
evaluating factorial of -1886
evaluating factorial of -1887
evaluating factorial of -1888
evaluating factorial of -1889
evaluating factorial of -1890
evaluating factorial of -1891
evaluating factorial of -1892
evaluating factorial of -1893
evaluating factorial of -1894
evaluating factorial of -1895
evaluating factorial of -1896
evaluating factorial of -1897
evaluating factorial of -1898
evaluating factorial of -1899
evaluating factorial of -1900
evaluating factorial of -1901
evaluating factorial of -1902
evaluating factorial of -1903
evaluating factorial of -1904
evaluating factorial of -1905
evaluating factorial of -1906
evaluating factorial of -1907
evaluating factorial of -1908
evaluating factorial of -1909
evaluating factorial of -1910
evaluating factorial of -1911
evaluating factorial of -1912
evaluating factorial of -1913
evaluating factorial of -1914
evaluating factorial of -1915
evaluating factorial of -1916
evaluating factorial of -1917
evaluating factorial of -1918
evaluating factorial of -1919
evaluating factorial of -1920
evaluating factorial of -1921
evaluating factorial of -1922
evaluating factorial of -1923
evaluating factorial of -1924
evaluating factorial of -1925
evaluating factorial of -1926
evaluating factorial of -1927
evaluating factorial of -1928
evaluating factorial of -1929
evaluating factorial of -1930
evaluating factorial of -1931
evaluating factorial of -1932
evaluating factorial of -1933
evaluating factorial of -1934
evaluating factorial of -1935
evaluating factorial of -1936
evaluating factorial of -1937
evaluating factorial of -1938
evaluating factorial of -1939
evaluating factorial of -1940
evaluating factorial of -1941
evaluating factorial of -1942
evaluating factorial of -1943
evaluating factorial of -1944
evaluating factorial of -1945
evaluating factorial of -1946
evaluating factorial of -1947
evaluating factorial of -1948
evaluating factorial of -1949
evaluating factorial of -1950

---

## Page 28

evaluating factorial of -1951
evaluating factorial of -1952
evaluating factorial of -1953
evaluating factorial of -1954
evaluating factorial of -1955
evaluating factorial of -1956
evaluating factorial of -1957
evaluating factorial of -1958
evaluating factorial of -1959
evaluating factorial of -1960
evaluating factorial of -1961
evaluating factorial of -1962
evaluating factorial of -1963
evaluating factorial of -1964
evaluating factorial of -1965
evaluating factorial of -1966
evaluating factorial of -1967
evaluating factorial of -1968
evaluating factorial of -1969
evaluating factorial of -1970
evaluating factorial of -1971
evaluating factorial of -1972
evaluating factorial of -1973
evaluating factorial of -1974
evaluating factorial of -1975
evaluating factorial of -1976
evaluating factorial of -1977
evaluating factorial of -1978
evaluating factorial of -1979
evaluating factorial of -1980
evaluating factorial of -1981
evaluating factorial of -1982
evaluating factorial of -1983
evaluating factorial of -1984
evaluating factorial of -1985
evaluating factorial of -1986
evaluating factorial of -1987
evaluating factorial of -1988
evaluating factorial of -1989
evaluating factorial of -1990
evaluating factorial of -1991
evaluating factorial of -1992
evaluating factorial of -1993
evaluating factorial of -1994
evaluating factorial of -1995
evaluating factorial of -1996
evaluating factorial of -1997
evaluating factorial of -1998
evaluating factorial of -1999
evaluating factorial of -2000
evaluating factorial of -2001
evaluating factorial of -2002
evaluating factorial of -2003
evaluating factorial of -2004
evaluating factorial of -2005
evaluating factorial of -2006
evaluating factorial of -2007
evaluating factorial of -2008
evaluating factorial of -2009
evaluating factorial of -2010
evaluating factorial of -2011
evaluating factorial of -2012
evaluating factorial of -2013
evaluating factorial of -2014
evaluating factorial of -2015
evaluating factorial of -2016
evaluating factorial of -2017
evaluating factorial of -2018
evaluating factorial of -2019
evaluating factorial of -2020
evaluating factorial of -2021
evaluating factorial of -2022
evaluating factorial of -2023
evaluating factorial of -2024
evaluating factorial of -2025

---

## Page 29

evaluating factorial of -2026
evaluating factorial of -2027
evaluating factorial of -2028
evaluating factorial of -2029
evaluating factorial of -2030
evaluating factorial of -2031
evaluating factorial of -2032
evaluating factorial of -2033
evaluating factorial of -2034
evaluating factorial of -2035
evaluating factorial of -2036
evaluating factorial of -2037
evaluating factorial of -2038
evaluating factorial of -2039
evaluating factorial of -2040
evaluating factorial of -2041
evaluating factorial of -2042
evaluating factorial of -2043
evaluating factorial of -2044
evaluating factorial of -2045
evaluating factorial of -2046
evaluating factorial of -2047
evaluating factorial of -2048
evaluating factorial of -2049
evaluating factorial of -2050
evaluating factorial of -2051
evaluating factorial of -2052
evaluating factorial of -2053
evaluating factorial of -2054
evaluating factorial of -2055
evaluating factorial of -2056
evaluating factorial of -2057
evaluating factorial of -2058
evaluating factorial of -2059
evaluating factorial of -2060
evaluating factorial of -2061
evaluating factorial of -2062
evaluating factorial of -2063
evaluating factorial of -2064
evaluating factorial of -2065
evaluating factorial of -2066
evaluating factorial of -2067
evaluating factorial of -2068
evaluating factorial of -2069
evaluating factorial of -2070
evaluating factorial of -2071
evaluating factorial of -2072
evaluating factorial of -2073
evaluating factorial of -2074
evaluating factorial of -2075
evaluating factorial of -2076
evaluating factorial of -2077
evaluating factorial of -2078
evaluating factorial of -2079
evaluating factorial of -2080
evaluating factorial of -2081
evaluating factorial of -2082
evaluating factorial of -2083
evaluating factorial of -2084
evaluating factorial of -2085
evaluating factorial of -2086
evaluating factorial of -2087
evaluating factorial of -2088
evaluating factorial of -2089
evaluating factorial of -2090
evaluating factorial of -2091
evaluating factorial of -2092
evaluating factorial of -2093
evaluating factorial of -2094
evaluating factorial of -2095
evaluating factorial of -2096
evaluating factorial of -2097
evaluating factorial of -2098
evaluating factorial of -2099
evaluating factorial of -2100

---

## Page 30

evaluating factorial of -2101
evaluating factorial of -2102
evaluating factorial of -2103
evaluating factorial of -2104
evaluating factorial of -2105
evaluating factorial of -2106
evaluating factorial of -2107
evaluating factorial of -2108
evaluating factorial of -2109
evaluating factorial of -2110
evaluating factorial of -2111
evaluating factorial of -2112
evaluating factorial of -2113
evaluating factorial of -2114
evaluating factorial of -2115
evaluating factorial of -2116
evaluating factorial of -2117
evaluating factorial of -2118
evaluating factorial of -2119
evaluating factorial of -2120
evaluating factorial of -2121
evaluating factorial of -2122
evaluating factorial of -2123
evaluating factorial of -2124
evaluating factorial of -2125
evaluating factorial of -2126
evaluating factorial of -2127
evaluating factorial of -2128
evaluating factorial of -2129
evaluating factorial of -2130
evaluating factorial of -2131
evaluating factorial of -2132
evaluating factorial of -2133
evaluating factorial of -2134
evaluating factorial of -2135
evaluating factorial of -2136
evaluating factorial of -2137
evaluating factorial of -2138
evaluating factorial of -2139
evaluating factorial of -2140
evaluating factorial of -2141
evaluating factorial of -2142
evaluating factorial of -2143
evaluating factorial of -2144
evaluating factorial of -2145
evaluating factorial of -2146
evaluating factorial of -2147
evaluating factorial of -2148
evaluating factorial of -2149
evaluating factorial of -2150
evaluating factorial of -2151
evaluating factorial of -2152
evaluating factorial of -2153
evaluating factorial of -2154
evaluating factorial of -2155
evaluating factorial of -2156
evaluating factorial of -2157
evaluating factorial of -2158
evaluating factorial of -2159
evaluating factorial of -2160
evaluating factorial of -2161
evaluating factorial of -2162
evaluating factorial of -2163
evaluating factorial of -2164
evaluating factorial of -2165
evaluating factorial of -2166
evaluating factorial of -2167
evaluating factorial of -2168
evaluating factorial of -2169
evaluating factorial of -2170
evaluating factorial of -2171
evaluating factorial of -2172
evaluating factorial of -2173
evaluating factorial of -2174
evaluating factorial of -2175

---

## Page 31

evaluating factorial of -2176
evaluating factorial of -2177
evaluating factorial of -2178
evaluating factorial of -2179
evaluating factorial of -2180
evaluating factorial of -2181
evaluating factorial of -2182
evaluating factorial of -2183
evaluating factorial of -2184
evaluating factorial of -2185
evaluating factorial of -2186
evaluating factorial of -2187
evaluating factorial of -2188
evaluating factorial of -2189
evaluating factorial of -2190
evaluating factorial of -2191
evaluating factorial of -2192
evaluating factorial of -2193
evaluating factorial of -2194
evaluating factorial of -2195
evaluating factorial of -2196
evaluating factorial of -2197
evaluating factorial of -2198
evaluating factorial of -2199
evaluating factorial of -2200
evaluating factorial of -2201
evaluating factorial of -2202
evaluating factorial of -2203
evaluating factorial of -2204
evaluating factorial of -2205
evaluating factorial of -2206
evaluating factorial of -2207
evaluating factorial of -2208
evaluating factorial of -2209
evaluating factorial of -2210
evaluating factorial of -2211
evaluating factorial of -2212
evaluating factorial of -2213
evaluating factorial of -2214
evaluating factorial of -2215
evaluating factorial of -2216
evaluating factorial of -2217
evaluating factorial of -2218
evaluating factorial of -2219
evaluating factorial of -2220
evaluating factorial of -2221
evaluating factorial of -2222
evaluating factorial of -2223
evaluating factorial of -2224
evaluating factorial of -2225
evaluating factorial of -2226
evaluating factorial of -2227
evaluating factorial of -2228
evaluating factorial of -2229
evaluating factorial of -2230
evaluating factorial of -2231
evaluating factorial of -2232
evaluating factorial of -2233
evaluating factorial of -2234
evaluating factorial of -2235
evaluating factorial of -2236
evaluating factorial of -2237
evaluating factorial of -2238
evaluating factorial of -2239
evaluating factorial of -2240
evaluating factorial of -2241
evaluating factorial of -2242
evaluating factorial of -2243
evaluating factorial of -2244
evaluating factorial of -2245
evaluating factorial of -2246
evaluating factorial of -2247
evaluating factorial of -2248
evaluating factorial of -2249
evaluating factorial of -2250

---

## Page 32

evaluating factorial of -2251
evaluating factorial of -2252
evaluating factorial of -2253
evaluating factorial of -2254
evaluating factorial of -2255
evaluating factorial of -2256
evaluating factorial of -2257
evaluating factorial of -2258
evaluating factorial of -2259
evaluating factorial of -2260
evaluating factorial of -2261
evaluating factorial of -2262
evaluating factorial of -2263
evaluating factorial of -2264
evaluating factorial of -2265
evaluating factorial of -2266
evaluating factorial of -2267
evaluating factorial of -2268
evaluating factorial of -2269
evaluating factorial of -2270
evaluating factorial of -2271
evaluating factorial of -2272
evaluating factorial of -2273
evaluating factorial of -2274
evaluating factorial of -2275
evaluating factorial of -2276
evaluating factorial of -2277
evaluating factorial of -2278
evaluating factorial of -2279
evaluating factorial of -2280
evaluating factorial of -2281
evaluating factorial of -2282
evaluating factorial of -2283
evaluating factorial of -2284
evaluating factorial of -2285
evaluating factorial of -2286
evaluating factorial of -2287
evaluating factorial of -2288
evaluating factorial of -2289
evaluating factorial of -2290
evaluating factorial of -2291
evaluating factorial of -2292
evaluating factorial of -2293
evaluating factorial of -2294
evaluating factorial of -2295
evaluating factorial of -2296
evaluating factorial of -2297
evaluating factorial of -2298
evaluating factorial of -2299
evaluating factorial of -2300
evaluating factorial of -2301
evaluating factorial of -2302
evaluating factorial of -2303
evaluating factorial of -2304
evaluating factorial of -2305
evaluating factorial of -2306
evaluating factorial of -2307
evaluating factorial of -2308
evaluating factorial of -2309
evaluating factorial of -2310
evaluating factorial of -2311
evaluating factorial of -2312
evaluating factorial of -2313
evaluating factorial of -2314
evaluating factorial of -2315
evaluating factorial of -2316
evaluating factorial of -2317
evaluating factorial of -2318
evaluating factorial of -2319
evaluating factorial of -2320
evaluating factorial of -2321
evaluating factorial of -2322
evaluating factorial of -2323
evaluating factorial of -2324
evaluating factorial of -2325

---

## Page 33

evaluating factorial of -2326
evaluating factorial of -2327
evaluating factorial of -2328
evaluating factorial of -2329
evaluating factorial of -2330
evaluating factorial of -2331
evaluating factorial of -2332
evaluating factorial of -2333
evaluating factorial of -2334
evaluating factorial of -2335
evaluating factorial of -2336
evaluating factorial of -2337
evaluating factorial of -2338
evaluating factorial of -2339
evaluating factorial of -2340
evaluating factorial of -2341
evaluating factorial of -2342
evaluating factorial of -2343
evaluating factorial of -2344
evaluating factorial of -2345
evaluating factorial of -2346
evaluating factorial of -2347
evaluating factorial of -2348
evaluating factorial of -2349
evaluating factorial of -2350
evaluating factorial of -2351
evaluating factorial of -2352
evaluating factorial of -2353
evaluating factorial of -2354
evaluating factorial of -2355
evaluating factorial of -2356
evaluating factorial of -2357
evaluating factorial of -2358
evaluating factorial of -2359
evaluating factorial of -2360
evaluating factorial of -2361
evaluating factorial of -2362
evaluating factorial of -2363
evaluating factorial of -2364
evaluating factorial of -2365
evaluating factorial of -2366
evaluating factorial of -2367
evaluating factorial of -2368
evaluating factorial of -2369
evaluating factorial of -2370
evaluating factorial of -2371
evaluating factorial of -2372
evaluating factorial of -2373
evaluating factorial of -2374
evaluating factorial of -2375
evaluating factorial of -2376
evaluating factorial of -2377
evaluating factorial of -2378
evaluating factorial of -2379
evaluating factorial of -2380
evaluating factorial of -2381
evaluating factorial of -2382
evaluating factorial of -2383
evaluating factorial of -2384
evaluating factorial of -2385
evaluating factorial of -2386
evaluating factorial of -2387
evaluating factorial of -2388
evaluating factorial of -2389
evaluating factorial of -2390
evaluating factorial of -2391
evaluating factorial of -2392
evaluating factorial of -2393
evaluating factorial of -2394
evaluating factorial of -2395
evaluating factorial of -2396
evaluating factorial of -2397
evaluating factorial of -2398
evaluating factorial of -2399
evaluating factorial of -2400

---

## Page 34

evaluating factorial of -2401
evaluating factorial of -2402
evaluating factorial of -2403
evaluating factorial of -2404
evaluating factorial of -2405
evaluating factorial of -2406
evaluating factorial of -2407
evaluating factorial of -2408
evaluating factorial of -2409
evaluating factorial of -2410
evaluating factorial of -2411
evaluating factorial of -2412
evaluating factorial of -2413
evaluating factorial of -2414
evaluating factorial of -2415
evaluating factorial of -2416
evaluating factorial of -2417
evaluating factorial of -2418
evaluating factorial of -2419
evaluating factorial of -2420
evaluating factorial of -2421
evaluating factorial of -2422
evaluating factorial of -2423
evaluating factorial of -2424
evaluating factorial of -2425
evaluating factorial of -2426
evaluating factorial of -2427
evaluating factorial of -2428
evaluating factorial of -2429
evaluating factorial of -2430
evaluating factorial of -2431
evaluating factorial of -2432
evaluating factorial of -2433
evaluating factorial of -2434
evaluating factorial of -2435
evaluating factorial of -2436
evaluating factorial of -2437
evaluating factorial of -2438
evaluating factorial of -2439
evaluating factorial of -2440
evaluating factorial of -2441
evaluating factorial of -2442
evaluating factorial of -2443
evaluating factorial of -2444
evaluating factorial of -2445
evaluating factorial of -2446
evaluating factorial of -2447
evaluating factorial of -2448
evaluating factorial of -2449
evaluating factorial of -2450
evaluating factorial of -2451
evaluating factorial of -2452
evaluating factorial of -2453
evaluating factorial of -2454
evaluating factorial of -2455
evaluating factorial of -2456
evaluating factorial of -2457
evaluating factorial of -2458
evaluating factorial of -2459
evaluating factorial of -2460
evaluating factorial of -2461
evaluating factorial of -2462
evaluating factorial of -2463
evaluating factorial of -2464
evaluating factorial of -2465
evaluating factorial of -2466
evaluating factorial of -2467
evaluating factorial of -2468
evaluating factorial of -2469
evaluating factorial of -2470
evaluating factorial of -2471
evaluating factorial of -2472
evaluating factorial of -2473
evaluating factorial of -2474
evaluating factorial of -2475

---

## Page 35

evaluating factorial of -2476
evaluating factorial of -2477
evaluating factorial of -2478
evaluating factorial of -2479
evaluating factorial of -2480
evaluating factorial of -2481
evaluating factorial of -2482
evaluating factorial of -2483
evaluating factorial of -2484
evaluating factorial of -2485
evaluating factorial of -2486
evaluating factorial of -2487
evaluating factorial of -2488
evaluating factorial of -2489
evaluating factorial of -2490
evaluating factorial of -2491
evaluating factorial of -2492
evaluating factorial of -2493
evaluating factorial of -2494
evaluating factorial of -2495
evaluating factorial of -2496
evaluating factorial of -2497
evaluating factorial of -2498
evaluating factorial of -2499
evaluating factorial of -2500
evaluating factorial of -2501
evaluating factorial of -2502
evaluating factorial of -2503
evaluating factorial of -2504
evaluating factorial of -2505
evaluating factorial of -2506
evaluating factorial of -2507
evaluating factorial of -2508
evaluating factorial of -2509
evaluating factorial of -2510
evaluating factorial of -2511
evaluating factorial of -2512
evaluating factorial of -2513
evaluating factorial of -2514
evaluating factorial of -2515
evaluating factorial of -2516
evaluating factorial of -2517
evaluating factorial of -2518
evaluating factorial of -2519
evaluating factorial of -2520
evaluating factorial of -2521
evaluating factorial of -2522
evaluating factorial of -2523
evaluating factorial of -2524
evaluating factorial of -2525
evaluating factorial of -2526
evaluating factorial of -2527
evaluating factorial of -2528
evaluating factorial of -2529
evaluating factorial of -2530
evaluating factorial of -2531
evaluating factorial of -2532
evaluating factorial of -2533
evaluating factorial of -2534
evaluating factorial of -2535
evaluating factorial of -2536
evaluating factorial of -2537
evaluating factorial of -2538
evaluating factorial of -2539
evaluating factorial of -2540
evaluating factorial of -2541
evaluating factorial of -2542
evaluating factorial of -2543
evaluating factorial of -2544
evaluating factorial of -2545
evaluating factorial of -2546
evaluating factorial of -2547
evaluating factorial of -2548
evaluating factorial of -2549
evaluating factorial of -2550

---

## Page 36

evaluating factorial of -2551
evaluating factorial of -2552
evaluating factorial of -2553
evaluating factorial of -2554
evaluating factorial of -2555
evaluating factorial of -2556
evaluating factorial of -2557
evaluating factorial of -2558
evaluating factorial of -2559
evaluating factorial of -2560
evaluating factorial of -2561
evaluating factorial of -2562
evaluating factorial of -2563
evaluating factorial of -2564
evaluating factorial of -2565
evaluating factorial of -2566
evaluating factorial of -2567
evaluating factorial of -2568
evaluating factorial of -2569
evaluating factorial of -2570
evaluating factorial of -2571
evaluating factorial of -2572
evaluating factorial of -2573
evaluating factorial of -2574
evaluating factorial of -2575
evaluating factorial of -2576
evaluating factorial of -2577
evaluating factorial of -2578
evaluating factorial of -2579
evaluating factorial of -2580
evaluating factorial of -2581
evaluating factorial of -2582
evaluating factorial of -2583
evaluating factorial of -2584
evaluating factorial of -2585
evaluating factorial of -2586
evaluating factorial of -2587
evaluating factorial of -2588
evaluating factorial of -2589
evaluating factorial of -2590
evaluating factorial of -2591
evaluating factorial of -2592
evaluating factorial of -2593
evaluating factorial of -2594
evaluating factorial of -2595
evaluating factorial of -2596
evaluating factorial of -2597
evaluating factorial of -2598
evaluating factorial of -2599
evaluating factorial of -2600
evaluating factorial of -2601
evaluating factorial of -2602
evaluating factorial of -2603
evaluating factorial of -2604
evaluating factorial of -2605
evaluating factorial of -2606
evaluating factorial of -2607
evaluating factorial of -2608
evaluating factorial of -2609
evaluating factorial of -2610
evaluating factorial of -2611
evaluating factorial of -2612
evaluating factorial of -2613
evaluating factorial of -2614
evaluating factorial of -2615
evaluating factorial of -2616
evaluating factorial of -2617
evaluating factorial of -2618
evaluating factorial of -2619
evaluating factorial of -2620
evaluating factorial of -2621
evaluating factorial of -2622
evaluating factorial of -2623
evaluating factorial of -2624
evaluating factorial of -2625

---

## Page 37

evaluating factorial of -2626
evaluating factorial of -2627
evaluating factorial of -2628
evaluating factorial of -2629
evaluating factorial of -2630
evaluating factorial of -2631
evaluating factorial of -2632
evaluating factorial of -2633
evaluating factorial of -2634
evaluating factorial of -2635
evaluating factorial of -2636
evaluating factorial of -2637
evaluating factorial of -2638
evaluating factorial of -2639
evaluating factorial of -2640
evaluating factorial of -2641
evaluating factorial of -2642
evaluating factorial of -2643
evaluating factorial of -2644
evaluating factorial of -2645
evaluating factorial of -2646
evaluating factorial of -2647
evaluating factorial of -2648
evaluating factorial of -2649
evaluating factorial of -2650
evaluating factorial of -2651
evaluating factorial of -2652
evaluating factorial of -2653
evaluating factorial of -2654
evaluating factorial of -2655
evaluating factorial of -2656
evaluating factorial of -2657
evaluating factorial of -2658
evaluating factorial of -2659
evaluating factorial of -2660
evaluating factorial of -2661
evaluating factorial of -2662
evaluating factorial of -2663
evaluating factorial of -2664
evaluating factorial of -2665
evaluating factorial of -2666
evaluating factorial of -2667
evaluating factorial of -2668
evaluating factorial of -2669
evaluating factorial of -2670
evaluating factorial of -2671
evaluating factorial of -2672
evaluating factorial of -2673
evaluating factorial of -2674
evaluating factorial of -2675
evaluating factorial of -2676
evaluating factorial of -2677
evaluating factorial of -2678
evaluating factorial of -2679
evaluating factorial of -2680
evaluating factorial of -2681
evaluating factorial of -2682
evaluating factorial of -2683
evaluating factorial of -2684
evaluating factorial of -2685
evaluating factorial of -2686
evaluating factorial of -2687
evaluating factorial of -2688
evaluating factorial of -2689
evaluating factorial of -2690
evaluating factorial of -2691
evaluating factorial of -2692
evaluating factorial of -2693
evaluating factorial of -2694
evaluating factorial of -2695
evaluating factorial of -2696
evaluating factorial of -2697
evaluating factorial of -2698
evaluating factorial of -2699
evaluating factorial of -2700

---

## Page 38

evaluating factorial of -2701
evaluating factorial of -2702
evaluating factorial of -2703
evaluating factorial of -2704
evaluating factorial of -2705
evaluating factorial of -2706
evaluating factorial of -2707
evaluating factorial of -2708
evaluating factorial of -2709
evaluating factorial of -2710
evaluating factorial of -2711
evaluating factorial of -2712
evaluating factorial of -2713
evaluating factorial of -2714
evaluating factorial of -2715
evaluating factorial of -2716
evaluating factorial of -2717
evaluating factorial of -2718
evaluating factorial of -2719
evaluating factorial of -2720
evaluating factorial of -2721
evaluating factorial of -2722
evaluating factorial of -2723
evaluating factorial of -2724
evaluating factorial of -2725
evaluating factorial of -2726
evaluating factorial of -2727
evaluating factorial of -2728
evaluating factorial of -2729
evaluating factorial of -2730
evaluating factorial of -2731
evaluating factorial of -2732
evaluating factorial of -2733
evaluating factorial of -2734
evaluating factorial of -2735
evaluating factorial of -2736
evaluating factorial of -2737
evaluating factorial of -2738
evaluating factorial of -2739
evaluating factorial of -2740
evaluating factorial of -2741
evaluating factorial of -2742
evaluating factorial of -2743
evaluating factorial of -2744
evaluating factorial of -2745
evaluating factorial of -2746
evaluating factorial of -2747
evaluating factorial of -2748
evaluating factorial of -2749
evaluating factorial of -2750
evaluating factorial of -2751
evaluating factorial of -2752
evaluating factorial of -2753
evaluating factorial of -2754
evaluating factorial of -2755
evaluating factorial of -2756
evaluating factorial of -2757
evaluating factorial of -2758
evaluating factorial of -2759
evaluating factorial of -2760
evaluating factorial of -2761
evaluating factorial of -2762
evaluating factorial of -2763
evaluating factorial of -2764
evaluating factorial of -2765
evaluating factorial of -2766
evaluating factorial of -2767
evaluating factorial of -2768
evaluating factorial of -2769
evaluating factorial of -2770
evaluating factorial of -2771
evaluating factorial of -2772
evaluating factorial of -2773
evaluating factorial of -2774
evaluating factorial of -2775

---

## Page 39

evaluating factorial of -2776
evaluating factorial of -2777
evaluating factorial of -2778
evaluating factorial of -2779
evaluating factorial of -2780
evaluating factorial of -2781
evaluating factorial of -2782
evaluating factorial of -2783
evaluating factorial of -2784
evaluating factorial of -2785
evaluating factorial of -2786
evaluating factorial of -2787
evaluating factorial of -2788
evaluating factorial of -2789
evaluating factorial of -2790
evaluating factorial of -2791
evaluating factorial of -2792
evaluating factorial of -2793
evaluating factorial of -2794
evaluating factorial of -2795
evaluating factorial of -2796
evaluating factorial of -2797
evaluating factorial of -2798
evaluating factorial of -2799
evaluating factorial of -2800
evaluating factorial of -2801
evaluating factorial of -2802
evaluating factorial of -2803
evaluating factorial of -2804
evaluating factorial of -2805
evaluating factorial of -2806
evaluating factorial of -2807
evaluating factorial of -2808
evaluating factorial of -2809
evaluating factorial of -2810
evaluating factorial of -2811
evaluating factorial of -2812
evaluating factorial of -2813
evaluating factorial of -2814
evaluating factorial of -2815
evaluating factorial of -2816
evaluating factorial of -2817
evaluating factorial of -2818
evaluating factorial of -2819
evaluating factorial of -2820
evaluating factorial of -2821
evaluating factorial of -2822
evaluating factorial of -2823
evaluating factorial of -2824
evaluating factorial of -2825
evaluating factorial of -2826
evaluating factorial of -2827
evaluating factorial of -2828
evaluating factorial of -2829
evaluating factorial of -2830
evaluating factorial of -2831
evaluating factorial of -2832
evaluating factorial of -2833
evaluating factorial of -2834
evaluating factorial of -2835
evaluating factorial of -2836
evaluating factorial of -2837
evaluating factorial of -2838
evaluating factorial of -2839
evaluating factorial of -2840
evaluating factorial of -2841
evaluating factorial of -2842
evaluating factorial of -2843
evaluating factorial of -2844
evaluating factorial of -2845
evaluating factorial of -2846
evaluating factorial of -2847
evaluating factorial of -2848
evaluating factorial of -2849
evaluating factorial of -2850

---

## Page 40

evaluating factorial of -2851
evaluating factorial of -2852
evaluating factorial of -2853
evaluating factorial of -2854
evaluating factorial of -2855
evaluating factorial of -2856
evaluating factorial of -2857
evaluating factorial of -2858
evaluating factorial of -2859
evaluating factorial of -2860
evaluating factorial of -2861
evaluating factorial of -2862
evaluating factorial of -2863
evaluating factorial of -2864
evaluating factorial of -2865
evaluating factorial of -2866
evaluating factorial of -2867
evaluating factorial of -2868
evaluating factorial of -2869
evaluating factorial of -2870
evaluating factorial of -2871
evaluating factorial of -2872
evaluating factorial of -2873
evaluating factorial of -2874
evaluating factorial of -2875
evaluating factorial of -2876
evaluating factorial of -2877
evaluating factorial of -2878
evaluating factorial of -2879
evaluating factorial of -2880
evaluating factorial of -2881
evaluating factorial of -2882
evaluating factorial of -2883
evaluating factorial of -2884
evaluating factorial of -2885
evaluating factorial of -2886
evaluating factorial of -2887
evaluating factorial of -2888
evaluating factorial of -2889
evaluating factorial of -2890
evaluating factorial of -2891
evaluating factorial of -2892
evaluating factorial of -2893
evaluating factorial of -2894
evaluating factorial of -2895
evaluating factorial of -2896
evaluating factorial of -2897
evaluating factorial of -2898
evaluating factorial of -2899
evaluating factorial of -2900
evaluating factorial of -2901
evaluating factorial of -2902
evaluating factorial of -2903
evaluating factorial of -2904
evaluating factorial of -2905
evaluating factorial of -2906
evaluating factorial of -2907
evaluating factorial of -2908
evaluating factorial of -2909
evaluating factorial of -2910
evaluating factorial of -2911
evaluating factorial of -2912
evaluating factorial of -2913
evaluating factorial of -2914
evaluating factorial of -2915
evaluating factorial of -2916
evaluating factorial of -2917
evaluating factorial of -2918
evaluating factorial of -2919
evaluating factorial of -2920
evaluating factorial of -2921
evaluating factorial of -2922
evaluating factorial of -2923
evaluating factorial of -2924
evaluating factorial of -2925

---

## Page 41

evaluating factorial of -2926
evaluating factorial of -2927
evaluating factorial of -2928
evaluating factorial of -2929
evaluating factorial of -2930
evaluating factorial of -2931
evaluating factorial of -2932
evaluating factorial of -2933
evaluating factorial of -2934
evaluating factorial of -2935
evaluating factorial of -2936
evaluating factorial of -2937
evaluating factorial of -2938
evaluating factorial of -2939
evaluating factorial of -2940
evaluating factorial of -2941
evaluating factorial of -2942
evaluating factorial of -2943
evaluating factorial of -2944
evaluating factorial of -2945
evaluating factorial of -2946
evaluating factorial of -2947
evaluating factorial of -2948
evaluating factorial of -2949
evaluating factorial of -2950
evaluating factorial of -2951
evaluating factorial of -2952
evaluating factorial of -2953
evaluating factorial of -2954
evaluating factorial of -2955
evaluating factorial of -2956
evaluating factorial of -2957
evaluating factorial of -2958
evaluating factorial of -2959
evaluating factorial of -2960
evaluating factorial of -2961
evaluating factorial of -2962
evaluating factorial of -2963
evaluating factorial of -2964
evaluating factorial of -2965
evaluating factorial of -2966
evaluating factorial of -2967
evaluating factorial of -2968
evaluating factorial of -2969
evaluating factorial of -2970
evaluating factorial of -2971
evaluating factorial of -2972
evaluating factorial of -2973
evaluating factorial of

---

## Page 42

---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[3], line 1
----> 1 fact(-1)
Cell In[1], line 6, in fact(n)
     4     return(1)
     5 else:
----> 6     return(n*fact(n-1))
Cell In[1], line 6, in fact(n)
     4     return(1)
     5 else:
----> 6     return(n*fact(n-1))
   [... skipping similar frames: fact at line 6 (2970 times)]
Cell In[1], line 6, in fact(n)
     4     return(1)
     5 else:
----> 6     return(n*fact(n-1))
Cell In[1], line 2, in fact(n)
     1 def fact(n):
----> 2     print("evaluating factorial of",n)
     3     if n == 0:
     4         return(1)
File ~/python-venv/lib/python3.13/site-packages/IPython/core/interactiveshell.py:3056, in Intera
ctiveShell._tee.<locals>.write(data, *args, **kwargs)
  3054 if not data:
  3055     return result
-> 3056 execution_count = self.execution_count
  3057 output_stream = None
  3058 outputs_by_counter = self.history_manager.outputs
File ~/python-venv/lib/python3.13/site-packages/traitlets/traitlets.py:687, in TraitType.__get__
(self, obj, cls)
   685     return self
   686 else:
--> 687     return t.cast(G, self.get(obj, cls))
File ~/python-venv/lib/python3.13/site-packages/traitlets/traitlets.py:666, in TraitType.get(sel
f, obj, cls)
   664     raise TraitError("Unexpected error in TraitType: default value not set properly") fr
om e
   665 else:
--> 666     return t.cast(G, value)
RecursionError: maximum recursion depth exceeded
We can also induct on the structure of a datastructure
We can break up a list into the first element (the head) and the rest (the tail) as a smaller list
Here is a recursive definition of len()
def mylen(l):
    print("Call with",l)
    if l == []:
        return(0)
    else:
        return(1+mylen(l[1:]))
mylen([7,18,2,-1,3])
Call with [7, 18, 2, -1, 3]
Call with [18, 2, -1, 3]
Call with [2, -1, 3]
Call with [-1, 3]
Call with [3]
Call with []

In [4]:
In [5]:
Out[5]:

---

## Page 43

A similar definition for sum()
def mysum(l):
    print("Call with",l)
    if l == []:
        return(0)
    else:
        return(l[0]+mysum(l[1:]))
mysum([7,18,2,-1,3])
Call with [7, 18, 2, -1, 3]
Call with [18, 2, -1, 3]
Call with [2, -1, 3]
Call with [-1, 3]
Call with [3]
Call with []

Insert a value v into a list l sorted in ascending order
def sortedinsert(v,l):
    if l == []:
        return([v])
    if v <= l[0]:
        return([v]+l)
    else:
        return(l[:1] + sortedinsert(v,l[1:]))
sortedinsert(14,list(range(1,20,2)))
[1, 3, 5, 7, 9, 11, 13, 14, 15, 17, 19]
The built in recursion limit causes this function to fail on moderate size lists
sortedinsert(3000,list(range(3000)))
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
Cell In[10], line 1
----> 1 sortedinsert(3000,list(range(3000)))
Cell In[8], line 7, in sortedinsert(v, l)
     5     return([v]+l)
     6 else:
----> 7     return(l[:1] + sortedinsert(v,l[1:]))
Cell In[8], line 7, in sortedinsert(v, l)
     5     return([v]+l)
     6 else:
----> 7     return(l[:1] + sortedinsert(v,l[1:]))
   [... skipping similar frames: sortedinsert at line 7 (2974 times)]
Cell In[8], line 7, in sortedinsert(v, l)
     5     return([v]+l)
     6 else:
----> 7     return(l[:1] + sortedinsert(v,l[1:]))
RecursionError: maximum recursion depth exceeded
Can manually increase the recursion limit
Maximum is
, the largest int value that can be stored in 32 bits
import sys
sys.setrecursionlimit(2**31-1)
len(sortedinsert(3000,list(range(3000))))
In [6]:
In [7]:
Out[7]:
In [8]:
In [9]:
Out[9]:
In [10]:
231 −1
In [11]:
In [12]: