
Filter way
#form
"""
create this four form tobe filled used by user

fields_level1 = {
        "entry_condtions",
        "exit_condtions",
        'trails',
        'risk_managment'}
"""

#if all forms values in {} are to be from dropdown


"""
========== Form1 ==============

entry_condtions form
by default there will be 1 row, user can add / update / delete row as per his need

There will be 5 column in form

column 1 field : {            # Multiple      (Add multiple column with same fields)
                    "time",         # pvpfi
                    "day",          # hntze
                    "MA_Cross",     # shfyk
                    "BB",           # ekvlm
                    "ST",           # wlgiy
                    "MACD",         # vfwla
                    "pattern_no"    # xyxib
                }

column 2 : This column is to set specific para based on selected column 2

    time : field = {"present_time"}

    day : field = {"present_day"}

    MA_Cross : field = {
                "short",            # vzlvj
                    short : {"1","2","3",..."10"}
                "long"              # vydln
                    long : {"1","2","3",..."10"}
            }

    BB : field = {
                "length",           # fcxvh
                    length : {"1","2","3",..."5"}
                "mult"              # gqnzb
                    mult : {"3","4","5",..."9"}
            }

    ST : field = {
                "length",
                    length : {"1","2","3",..."20"}
                "factor"            # crzda
                    factor : {"3","4","5",..."15"}
            }

    MACD : field = {
                "fastl",            # qzzaa
                    fastl : {"1","2","3",..."8"}
                "slowl",            # qaypa
                    slowl : {"3","4","5",..."8"}
                "source"            # qckeq
                    source : {"open","high","low","close"}
                }



    pattern_no field = {"1","2","3"}


column 3 :

    field = {
                "less_than_equal_to",       # urupf
                "less_than",                # hejou
                "equal_to",                 # educn
                "greater_than",             # knxqu
                "greater_than_equal_to"     # iavct
            }

column 4 :
    this will be based on selected column 1 (not on 2 or 3)

    if column1 is - time :
        field = {"9:15","9:16","9:17"......."15:30"}    # ozmgz
    if column1 is -  day :
        field = {"monday","tuesday",....."friday"}      # injzo
    if column1 is -  MA_Cross :
        field = {"upcross", "downcross"}                # owbsi
    if column1 is -  BB :
        field = {"1","2",....."6"}                      # ruvcf
    if column1 is -  ST :
        field = {"upcross","downcross"}                 # owbsi
    if column1 is -  MACD :
        field = {"upcross","downcross"}                 # owbsi


// To be included after add more conditionsfunction
column 4 : field = {"and","or"}                         # rnapi
"""

"""
========== Form2 ==============
exit form : similar to entry_conditions form
"""




"""
========== Form3 ==============
trail condition form
field : want_to_trail : {
                            "yes",      # rpcyp
                            "No
                    }

if yes :
    its similar to entry form with 5 column to set conditions, with following addition

    column 1 :
        trail_start_condition field : {
                    "time",
                    "day",
                    "MA_Cross",
                    "BB",
                    "ST",
                    "MACD",
                    "profit",               # fkkyc
                    "risk_value"            # yiriz
                }

            "time","day", "MA_Cross","BB","ST","MACD" = {same as in form 1}
            profit : {-100 % to 100 %}
            risk_value : { 0,0.1, 0.2, .........up to 1   }

    column 2 : same as form 1
    column 3 : same as form 1
    column 4 : same as form 1
    column 5 : same as form 1


"""

"""
========== Form4 ==============
risk_managment form
user to add required row and select field

column 1 field : {"max_long","max_short", "max_total","max_loss"}
column 2
        max_long : {"1","2","3",...,"5"}            # gxvgo
        max_total : {"1","2","3",...,"10"}          # hteil
        max_short : {"1","2","3",...,"5"}           # qlige
        max_loss : {
                    "absolute",                    # keves
                        if selected is "absolute", fields are {"-10000,-5000,0,5000,10000"}
                    "percentage"                   # xpegc
                        if selected is "percentage", fields are {"-1,-0.5,0,5,1"}
                }
"""
