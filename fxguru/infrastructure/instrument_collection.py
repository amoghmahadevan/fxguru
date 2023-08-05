import json
from models.instruments import Instrument
from db.db import DataDB
class InstrumentCollection:
   FILENAME = "instruments.json"
   API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 
         'displayPrecision', 'tradeUnitsPrecision', 'marginRate']

   def __init__(self):
    self.instruments_dict = {}
#Loads elements by adding them to dictionary (our collection) from instruments.json
   def LoadInstruments(self, path):
        self.instruments_dict = {}
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, "r") as f:
            data = json.loads(f.read())
            for k, v in data.items():
                self.instruments_dict[k] = Instrument.FromApiObject(v)

   def LoadInstrumentsDB(self):
         self.instruments_dict = {}
         data = DataDB().query_single(DataDB.INSTRUMENT_COL)
         for k, v in data.items():
            self.instruments_dict[k] = Instrument.FromApiObject(v)
         
#Writes instruments.json file
   def CreateFile(self, data, path):
      if data is None:
         print("Instrument File Creation Failed")
         return
      
      instruments_dict = {}
      for i in data:
         key = i['name']
         instruments_dict[key] = {k: i[k] for k in self.API_KEYS}

      fileName = f"{path}/{self.FILENAME}"
      with open(fileName, "w") as f:
         f.write(json.dumps(instruments_dict, indent = 2))

   def CreateDB(self, data):
      if data is None:
         print("Instrument File Creation Failed")
         return
      #One document in the collection, so to modify we delete, and add back modified version
      instruments_dict = {}
      for i in data:
         key = i['name']
         instruments_dict[key] = {k: i[k] for k in self.API_KEYS}

      database = DataDB()
      database.delete_many(DataDB.INSTRUMENT_COL)
      database.add_one(DataDB.INSTRUMENT_COL, instruments_dict)
   #Prints our collection (Not instruments.json file but created dictionary from instruments.json) 
   def PrintInstruments(self):
      [print(k,v) for k,v in self.instruments_dict.items()]
      print(len(self.instruments_dict.keys()), "instruments")
    
#Reference to instruments
instrumentCollection = InstrumentCollection()