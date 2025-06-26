from time import sleep
while True:
    try:
        print("\t\t\n\nEnter 'e' to quit anytime! ")
        sleep(1.5)
        #Date
        date = input("Enter the Date: ")
        if date == 'e':
            break
        Date = int(date) 
        #Month
        month = input("Enter the month: ")
        if month == 'e' :
            break
        Month = int(month)
        #Year
        year = input("Enter the Year: ")
        if year == 'e' :
            break
        Year = int(year)
        # leap = None


        """For leap  Year"""
        """                                                           """

        if Year%4 == 0:
            Year = Year-1 
            # quotient = Year//400
            # zero_oddday_years = quotient*400
            odd_day_years = Year%400
            # print(zero_oddday_years)
            # print(odd_day_years)
            leap_years = odd_day_years//4
            ordinary_years = odd_day_years - leap_years
            odd_days = leap_years*2+ordinary_years*1 
            pr_odd_days = odd_days%7
            jan = 31%7
            feb = 29%7
            mar = 31%7
            apr = 30%7
            may = 31%7
            jun = 30%7
            jul = 31%7
            aug = 31%7
            sep = 30%7
            octo = 31%7
            nov = 30%7
            dec = 31%7
            if Month == 1:
                if Date<=31:
                    odd_jan = (Date%7 + pr_odd_days)%7
                    if odd_jan == 0:
                        print("Sunday")
                    elif odd_jan == 1:
                        print("Monday")
                    elif odd_jan == 2:
                        print("Tuesday")
                    elif odd_jan == 3:
                        print("Wednesday")
                    elif odd_jan == 4:
                        print("Thursday")
                    elif odd_jan == 5:
                        print("Friday")
                    elif odd_jan == 6:
                        print("Saturday")
            if Month == 2:
                if Date<=29:
                    odd_feb = (Date%7 + pr_odd_days+jan)%7
                    if odd_feb == 0:
                        print("Sunday")
                    elif odd_feb == 1:
                        print("Monday")
                    elif odd_feb == 2:
                        print("Tuesday")
                    elif odd_feb == 3:
                        print("Wednesday")
                    elif odd_feb == 4:
                        print("Thursday")
                    elif odd_feb == 5:
                        print("Friday")
                    elif odd_feb == 6:
                        print("Saturday")

            """For March month"""
            if Month == 3:
                if Date<=31:
                    odd_mar = (Date%7 + pr_odd_days+jan+feb)%7
                    if odd_mar == 0:
                        print("Sunday")
                    elif odd_mar == 1:
                        print("Monday")
                    elif odd_mar == 2:
                        print("Tuesday")
                    elif odd_mar == 3:
                        print("Wednesday")
                    elif odd_mar == 4:
                        print("Thursday")
                    elif odd_mar == 5:
                        print("Friday")
                    elif odd_mar == 6:
                        print("Saturday")
            """For April month"""            
            if Month == 4:
                if Date<=30:
                    odd_apr = (Date%7 + pr_odd_days+jan+feb+mar)%7
                    if odd_apr == 0:
                        print("Sunday")
                    elif odd_apr == 1:
                        print("Monday")
                    elif odd_apr == 2:
                        print("Tuesday")
                    elif odd_apr == 3:
                        print("Wednesday")
                    elif odd_apr == 4:
                        print("Thursday")
                    elif odd_apr == 5:
                        print("Friday")
                    elif odd_apr == 6:
                        print("Saturday")
            """For May month"""
            if Month == 5:
                if Date<=31:
                    odd_may = (Date%7 + pr_odd_days+jan+feb+mar+apr)%7
                    if odd_may == 0:
                        print("Sunday")
                    elif odd_may == 1:
                        print("Monday")
                    elif odd_may == 2:
                        print("Tuesday")
                    elif odd_may == 3:
                        print("Wednesday")
                    elif odd_may == 4:
                        print("Thursday")
                    elif odd_may == 5:
                        print("Friday")
                    elif odd_may == 6:
                        print("Saturday")
            
            """For June month"""
            if Month == 6:
                if Date<=30:
                    odd_jun = (Date%7 + pr_odd_days+jan+feb+mar+apr+may)%7
                    if odd_jun == 0:
                        print("Sunday")
                    elif odd_jun == 1:
                        print("Monday")
                    elif odd_jun == 2:
                        print("Tuesday")
                    elif odd_jun == 3:
                        print("Wednesday")
                    elif odd_jun == 4:
                        print("Thursday")
                    elif odd_jun == 5:
                        print("Friday")
                    elif odd_jun == 6:
                        print("Saturday")
            
            """For July month"""
            if Month == 7:
                if Date<=31:
                    odd_jul = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun)%7
                    if odd_jul == 0:
                        print("Sunday")
                    elif odd_jul == 1:
                        print("Monday")
                    elif odd_jul == 2:
                        print("Tuesday")
                    elif odd_jul == 3:
                        print("Wednesday")
                    elif odd_jul == 4:
                        print("Thursday")
                    elif odd_jul == 5:
                        print("Friday")
                    elif odd_jul == 6:
                        print("Saturday")
            
            """For August month"""
            if Month ==8 :
                if Date<=31:
                    odd_aug = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul)%7
                    if odd_aug == 0:
                        print("Sunday")
                    elif odd_aug == 1:
                        print("Monday")
                    elif odd_aug == 2:
                        print("Tuesday")
                    elif odd_aug == 3:
                        print("Wednesday")
                    elif odd_aug == 4:
                        print("Thursday")
                    elif odd_aug == 5:
                        print("Friday")
                    elif odd_aug == 6:
                        print("Saturday")

            """For September month"""
            if Month == 9:
                if Date<=30:
                    odd_sept = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug)%7
                    if odd_sept == 0:
                        print("Sunday")
                    elif odd_sept == 1:
                        print("Monday")
                    elif odd_sept == 2:
                        print("Tuesday")
                    elif odd_sept == 3:
                        print("Wednesday")
                    elif odd_sept == 4:
                        print("Thursday")
                    elif odd_sept == 5:
                        print("Friday")
                    elif odd_sept == 6:
                        print("Saturday")

            """For October month"""
            if Month == 10:
                if Date<=31:
                    odd_oct = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep)%7
                    if odd_oct == 0:
                        print("Sunday")
                    elif odd_oct == 1:
                        print("Monday")
                    elif odd_oct == 2:
                        print("Tuesday")
                    elif odd_oct == 3:
                        print("Wednesday")
                    elif odd_oct == 4:
                        print("Thursday")
                    elif odd_oct == 5:
                        print("Friday")
                    elif odd_oct == 6:
                        print("Saturday")

            """For November month"""
            if Month == 11:
                if Date<=30:
                    odd_nov = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep+octo)%7
                    if odd_nov == 0:
                        print("Sunday")
                    elif odd_nov == 1:
                        print("Monday")
                    elif odd_nov == 2:
                        print("Tuesday")
                    elif odd_nov == 3:
                        print("Wednesday")
                    elif odd_nov == 4:
                        print("Thursday")
                    elif odd_nov == 5:
                        print("Friday")
                    elif odd_nov == 6:
                        print("Saturday")

            """For December month"""
            if Month == 12:
                if Date<=31:
                    odd_dec = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep+octo+nov)%7
                    if odd_dec == 0:
                        print("Sunday")
                    elif odd_dec == 1:
                        print("Monday")
                    elif odd_dec == 2:
                        print("Tuesday")
                    elif odd_dec == 3:
                        print("Wednesday")
                    elif odd_dec == 4:
                        print("Thursday")
                    elif odd_dec == 5:
                        print("Friday")
                    elif odd_dec == 6:
                        print("Saturday")
        elif Year%4 != 0:
            Year = Year-1 
            # quotient = Year//400
            # zero_oddday_years = quotient*400
            odd_day_years = Year%400
            # print(zero_oddday_years)
            # print(odd_day_years)
            leap_years = odd_day_years//4
            ordinary_years = odd_day_years - leap_years
            odd_days = leap_years*2+ordinary_years*1 
            pr_odd_days = odd_days%7
            jan = 31%7
            feb = 28%7
            mar = 31%7
            apr = 30%7
            may = 31%7
            jun = 30%7
            jul = 31%7
            aug = 31%7
            sep = 30%7
            octo = 31%7
            nov = 30%7
            dec = 31%7
            if Month == 1:
                if Date<=31:
                    odd_jan = (Date%7 + pr_odd_days)%7
                    if odd_jan == 0:
                        print("Sunday")
                    elif odd_jan == 1:
                        print("Monday")
                    elif odd_jan == 2:
                        print("Tuesday")
                    elif odd_jan == 3:
                        print("Wednesday")
                    elif odd_jan == 4:
                        print("Thursday")
                    elif odd_jan == 5:
                        print("Friday")
                    elif odd_jan == 6:
                        print("Saturday")
            if Month == 2:
                if Date<=28:
                    odd_feb = (Date%7 + pr_odd_days+jan)%7
                    if odd_feb == 0:
                        print("Sunday")
                    elif odd_feb == 1:
                        print("Monday")
                    elif odd_feb == 2:
                        print("Tuesday")
                    elif odd_feb == 3:
                        print("Wednesday")
                    elif odd_feb == 4:
                        print("Thursday")
                    elif odd_feb == 5:
                        print("Friday")
                    elif odd_feb == 6:
                        print("Saturday")

            """For March month"""
            if Month == 3:
                if Date<=31:
                    odd_mar = (Date%7 + pr_odd_days+jan+feb)%7
                    if odd_mar == 0:
                        print("Sunday")
                    elif odd_mar == 1:
                        print("Monday")
                    elif odd_mar == 2:
                        print("Tuesday")
                    elif odd_mar == 3:
                        print("Wednesday")
                    elif odd_mar == 4:
                        print("Thursday")
                    elif odd_mar == 5:
                        print("Friday")
                    elif odd_mar == 6:
                        print("Saturday")
            """For April month"""            
            if Month == 4:
                if Date<=30:
                    odd_apr = (Date%7 + pr_odd_days+jan+feb+mar)%7
                    if odd_apr == 0:
                        print("Sunday")
                    elif odd_apr == 1:
                        print("Monday")
                    elif odd_apr == 2:
                        print("Tuesday")
                    elif odd_apr == 3:
                        print("Wednesday")
                    elif odd_apr == 4:
                        print("Thursday")
                    elif odd_apr == 5:
                        print("Friday")
                    elif odd_apr == 6:
                        print("Saturday")
            """For May month"""
            if Month == 5:
                if Date<=31:
                    odd_may = (Date%7 + pr_odd_days+jan+feb+mar+apr)%7
                    if odd_may == 0:
                        print("Sunday")
                    elif odd_may == 1:
                        print("Monday")
                    elif odd_may == 2:
                        print("Tuesday")
                    elif odd_may == 3:
                        print("Wednesday")
                    elif odd_may == 4:
                        print("Thursday")
                    elif odd_may == 5:
                        print("Friday")
                    elif odd_may == 6:
                        print("Saturday")
            
            """For June month"""
            if Month == 6:
                if Date<=30:
                    odd_jun = (Date%7 + pr_odd_days+jan+feb+mar+apr+may)%7
                    if odd_jun == 0:
                        print("Sunday")
                    elif odd_jun == 1:
                        print("Monday")
                    elif odd_jun == 2:
                        print("Tuesday")
                    elif odd_jun == 3:
                        print("Wednesday")
                    elif odd_jun == 4:
                        print("Thursday")
                    elif odd_jun == 5:
                        print("Friday")
                    elif odd_jun == 6:
                        print("Saturday")
            
            """For July month"""
            if Month == 7:
                if Date<=31:
                    odd_jul = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun)%7
                    if odd_jul == 0:
                        print("Sunday")
                    elif odd_jul == 1:
                        print("Monday")
                    elif odd_jul == 2:
                        print("Tuesday")
                    elif odd_jul == 3:
                        print("Wednesday")
                    elif odd_jul == 4:
                        print("Thursday")
                    elif odd_jul == 5:
                        print("Friday")
                    elif odd_jul == 6:
                        print("Saturday")
            
            """For August month"""
            if Month ==8 :
                if Date<=31:
                    odd_aug = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul)%7
                    if odd_aug == 0:
                        print("Sunday")
                    elif odd_aug == 1:
                        print("Monday")
                    elif odd_aug == 2:
                        print("Tuesday")
                    elif odd_aug == 3:
                        print("Wednesday")
                    elif odd_aug == 4:
                        print("Thursday")
                    elif odd_aug == 5:
                        print("Friday")
                    elif odd_aug == 6:
                        print("Saturday")

            """For September month"""
            if Month == 9:
                if Date<=30:
                    odd_sept = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug)%7
                    if odd_sept == 0:
                        print("Sunday")
                    elif odd_sept == 1:
                        print("Monday")
                    elif odd_sept == 2:
                        print("Tuesday")
                    elif odd_sept == 3:
                        print("Wednesday")
                    elif odd_sept == 4:
                        print("Thursday")
                    elif odd_sept == 5:
                        print("Friday")
                    elif odd_sept == 6:
                        print("Saturday")

            """For October month"""
            if Month == 10:
                if Date<=31:
                    odd_oct = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep)%7
                    if odd_oct == 0:
                        print("Sunday")
                    elif odd_oct == 1:
                        print("Monday")
                    elif odd_oct == 2:
                        print("Tuesday")
                    elif odd_oct == 3:
                        print("Wednesday")
                    elif odd_oct == 4:
                        print("Thursday")
                    elif odd_oct == 5:
                        print("Friday")
                    elif odd_oct == 6:
                        print("Saturday")

            """For November month"""
            if Month == 11:
                if Date<=30:
                    odd_nov = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep+octo)%7
                    if odd_nov == 0:
                        print("Sunday")
                    elif odd_nov == 1:
                        print("Monday")
                    elif odd_nov == 2:
                        print("Tuesday")
                    elif odd_nov == 3:
                        print("Wednesday")
                    elif odd_nov == 4:
                        print("Thursday")
                    elif odd_nov == 5:
                        print("Friday")
                    elif odd_nov == 6:
                        print("Saturday")

            """For December month"""
            if Month == 12:
                if Date<=31:
                    odd_dec = (Date%7 + pr_odd_days+jan+feb+mar+apr+may+jun+jul+aug+sep+octo+nov)%7
                    if odd_dec == 0:
                        print("Sunday")
                    elif odd_dec == 1:
                        print("Monday")
                    elif odd_dec == 2:
                        print("Tuesday")
                    elif odd_dec == 3:
                        print("Wednesday")
                    elif odd_dec == 4:
                        print("Thursday")
                    elif odd_dec == 5:
                        print("Friday")
                    elif odd_dec == 6:
                        print("Saturday")
    except Exception:
        print("Please enter the values of date,month and year IN NUMERICAL FORMS ONLY....!")
print("Thanks for choosing us!")
print("\t\t\t\n\nDeveloped By: NANOBEING (nanobeing.org)")
sleep(60)
"""        OK Tested       """
""" No bug found 🤘👊👌👍👌🤘🤘👍👍🤙💪💪🤳"""