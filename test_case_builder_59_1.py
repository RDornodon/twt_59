def test(travel_list):
    travels = {}
    for x, line in enumerate(travel_list, start=1):
        departure, arrival, travel_time = line.split()
        travel_time = int(travel_time)
        if departure in travels:
            if arrival in travels[departure]:
                travels[departure][arrival] = min(travels[departure][arrival], (travel_time, x))
            else:
                travels[departure][arrival] = (travel_time, x)
        else:
            travels[departure] = dict({arrival: (travel_time, x)})
    cities = ['UK']
    routes = [['UK',0,[]]]
    while F := {*filter(cities.count, travels)}:
        DC = []
        for city in F:
            destinations = travels.pop(city)
            for d_city, d_params in destinations.items():
                for route, value, indices in routes:
                    if route[-2:] == city and d_city not in route:
                        R = [route + '>' + d_city, value + d_params[0], indices + [d_params[1]]]
                        routes.append(R)
                        DC += [d_city]
        cities = [*{*DC}]
    return len([route for route in routes if route[0][-2:] == 'DZ'])


if __name__ == '__main__':
    from random import randint, choice, choices
    countries = (\
        "AF LA AL LV DZ LB AD LS AO LR AG LY AR LI AM LT AU LU AT MK " +\
        "AZ MG BS MW BH MY BD MV BB ML BY MT BE MH BZ MR BJ MU BT MX " +\
        "BO FM BA MD BW MC BR MN BN MA BG MZ BF MM BI NA KH NR CM NP " +\
        "CA NL CV NZ CF NI TD NE CL NG CN NO CO OM KM PK CD PW CG PA " +\
        "CR PG CI PY HR PE CU PH CY PL CZ PT DK QA DJ PR DM RO DO RU " +\
        "TL RW EC KN SV LC GQ VC ER WS EE SM ET ST FJ SA FI SN FR CS " +\
        "GA SC GM SL GE SG DE SK GH SI GR SB GD SO GL ZA GT ES GN LK " +\
        "GW SD GY SR HT SZ HN SE HK CH HU SY IS TJ IN TZ ID TW IR TZ " +\
        "IQ TH IE TG IL TO IT TT JM TN JP TR JO TM KZ TV KE UG UA KP " +\
        "AE KR GB KW US KG UY UK").split()
    en_countries = [len(countries) if c == 'UK' else 1 for c in countries]
    ex_countries = [len(countries) if c == 'DZ' else 1 for c in countries]
    testcases = []
    testcases += [300]
    for x in range(300):
        transfers = [f"{choices(countries, weights=en_countries)[0]} {choice(countries)} {randint(1,30)*10}"for _ in range(20)]

        while test(transfers)<3:
            transfers += [f"{choice(countries)} {choices(countries, weights=ex_countries)[0]} {randint(1, 30) * 10}" for _ in range(5)]

        testcases += [len(transfers)]
        testcases += transfers

    print(*testcases, sep='\n')
