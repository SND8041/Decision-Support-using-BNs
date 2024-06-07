def getSEI2(scenario):
    sei = []
    s = scenario.socioeconomic_impact
    t = scenario.recovery_time
    d = scenario.social_discount_rate
    sei.append(s)  # first value
    for i in range(t - 1):
        y = sei[i] / pow((1 + d), i + 1)
        sei.append(y + sei[i])
        print(sei[i])
    return sei

#the function is used with FuncFormatter with Matplotlib to change the y-axis labels to millions
def millions(x, pos):
    if x < 10000e6:
        return '%1.0fM' % (x * 1e-6)    #'The two args are the value and tick position'
    else:
        return '%1.0fB' % (x * 1e-9)


# this function calculates the sei of the recently added scenario. The function returns sei in
# millions of dollars
# the following seems to be the true only for MNA recovery method
def getSEI(scenario):#this function looks good for MNA recovery method
    Vs = scenario.compensation_amount
    Vn = 1.0 #cost of unit damage = $1.0
    Qpt = scenario.quantity_of_oil  # quantity of oil in US gallons
    Yn = scenario.recovery_time  # service recovery time
    r = scenario.social_discount_rate
    d = scenario.rate_of_biodegradation
    sei = []
    s = 0
    sei.append(scenario.socioeconomic_impact)
    print("Karlo dada 2")
    print(sei[0])

    Qpt = Qpt * (1-0.3)#due to mechanical recovery of oil at, assuming, 30% remediation in the first year
    print("Value of Qpt: ", Qpt)
    for year in range(scenario.recovery_time - 1):
        b = Qpt * Yn
        s = Vn*(b * (1 + r)) / (r + d) #this is Eq. 9, on page 9 of Mawuli's multiperiod paper
        sei.append((sei[year] + s))
        Yn = Yn - 1  # every passing year should be subtracted
        Qpt = Qpt * (1 - d)
        print(sei[year])

    return sei
