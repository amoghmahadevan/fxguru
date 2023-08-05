from simulation.ema_macd import run_pair
from infrastructure.instrument_collection import instrumentCollection

if __name__ == '__main__':
    instrumentCollection.LoadInstrumentsDB()
    run_pair("EUR_USD")