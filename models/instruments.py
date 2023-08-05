class Instrument:
    def __init__(self, name, ins_type, displayName, 
                    pipLocation, tradeUnitsPrecision, marginRate, displayPrecision):
        self.name = name
        self.ins_type = ins_type #type is a keyword
        self.displayName = displayName
        self.pipLocation = pow(10, pipLocation) #pips are usually 10^-4 but can vary
        self.tradeUnitsPrecision = tradeUnitsPrecision
        self.marginRate = float(marginRate)
        self.displayPrecision = displayPrecision

    #Representation of dictionary, properties of class
    def __repr__(self):
        return str(vars(self))
    
    #Used to actually create an instance from the API object
    @classmethod 
    def FromApiObject(cls, obj):
        return Instrument(
            obj['name'],
            obj['type'],
            obj['displayName'],
            obj['pipLocation'],
            obj['tradeUnitsPrecision'],
            obj['marginRate'],
            obj['displayPrecision']
        )