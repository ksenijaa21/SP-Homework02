class Vehicle():

    def __init__(self, company, model, year_of_production, reg_number, engine_power, color):
        self.company = company
        self.model = model
        self.year_of_production = year_of_production
        self.reg_number = reg_number
        self.engine_power = engine_power
        self.color = color

    def __str__(self):
        return "{0} {1} {2} [REGISTRATION NUMBER: {3} POWER: {4}KW, COLOR: {5}]".format(self.company,self.model,self.year_of_production,self.reg_number,self.engine_power,self.color)

    def cost_of_registration(self):

        if int(self.year_of_production) < 1990:
            fee = 100
        elif int(self.year_of_production) > 1990 and int(self.year_of_production) < 2000:
            fee = 200
        elif int(self.year_of_production) > 2000 and int(self.year_of_production) < 2010:
            fee = 300
        else:
            fee = 400

        registration_fee = fee + (int(self.engine_power) * 2)

        return registration_fee


class Bus(Vehicle):

    def __init__(self, company, model, year_of_production, reg_number, engine_power, color, number_of_seats, bus_company):
        Vehicle.__init__(self, company, model, year_of_production, reg_number, engine_power, color)
        self.number_of_seats = number_of_seats
        self.bus_company = bus_company

    def __str__(self):
        return "AUTOBUS {0} {1} {2} '{3}' - BROJ MJESTA {4}".format(self.company,self.model,self.year_of_production,self.bus_company,self.number_of_seats)

    def cost_of_registration(self):
        Vehicle.cost_of_registration(self)
        number_of_seats_fee = int(self.number_of_seats) * 1
        bus_reg_fee = int(Vehicle.cost_of_registration(self)) + int(number_of_seats_fee)
        return bus_reg_fee




auto = Vehicle("Ford", "Fiesta", "2013", "23456789", "60", "white")
print(auto)
print("Vehicle registration fee is: " + str(Vehicle.cost_of_registration(auto)))

autobus = Bus("Mercedes", "Benz", "2000", "203743240987", "100", "Black", "50", "Pavicevic")
print(autobus)
print("Bus registration fee is: " + str(Bus.cost_of_registration(autobus)))
