# twt_59_1.py

for _ in '*' * int(input()):
    travels = {}
    for x in range(1, 1 + int(input())):
        departure, arrival, travel_time=input().split()
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
    R, *routes = [route for route in routes if route[0][-2:] == 'DZ']
    for route in routes:
        if route[1] < R[1] or (route[1] == R[1] and len(route[2]) < len(R[2])):
            R = route
    print(*R[2])
