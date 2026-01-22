# Driver that interfaces with the thermocouple lookup tables
# Temperature (°C) <-> Voltage (mV)

class ThermoTable:
    def __init__(self, THERMO_TYPE):
        fpath = "./tables/tc_"+THERMO_TYPE
        self.dict = self.load_lookup_table(fpath)
        self.type = THERMO_TYPE
        self.max_temp = max(self.dict)
        self.min_temp = min(self.dict)

    def load_lookup_table(self, file_path):
        lookup_table = {}
    
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines[1:]:
            parts = line.split()
            if not parts:
                continue
            
            base_temp = int(parts[0])
        
            values = parts[1:]
        
            for offset, val in enumerate(values):
                exact_temp = base_temp + offset
                lookup_table[exact_temp] = float(val)
            
        return lookup_table

    def voltage(self, temperature):
        val = self.dict.get(temperature)
        if isinstance(val, (float, int)):
            return val
        raise ValueError(f"Temperature {temperature} °C not found in lookup table for Thermocouple Type {self.type}")

    def temperature(self, voltage):
        max_temp = self.max_temp
        min_temp = self.min_temp
        range = max_temp - min_temp

        temperature = None
        done = False
        while not done:
            midpoint = round(max_temp - range/2)
            temperature = midpoint
            #print(f"Max: {max_temp}")
            #print(f"Min: {min_temp}")
            #print(f"Mid: {midpoint}")
            midpoint_voltage = self.dict.get(midpoint)
            #print(f"Voltage: {midpoint_voltage}\n")
            if midpoint_voltage == voltage:
                done = True
            elif voltage < midpoint_voltage:
                max_temp = round(max_temp - range/2)
            else:
                min_temp = round(min_temp + range/2)
            range = max_temp - min_temp
            if range <= 1:
                done = True
        
        if temperature == None:
            raise ValueError(f"There was a problem performing a reverse lookup on the thermocouple type {self.type} dictionary")
        return temperature

if __name__ == "__main__":
    tt = ThermoTable("e")
    temp = -30
    voltage = 0.058
    print(f"At {temp} °C the thermocouple has {tt.voltage(temp)} mV across it")
    print(f"At {voltage} mV the thermocouple is {tt.temperature(voltage)} °C")