from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from api.web_options import get_options


if __name__ == "__main__":
    instrumentCollection.LoadInstrumentsDB()
    api = OandaApi()

    print("\nweb options:")
    print(get_options())

    print("\nget_account_summary():")
    print(api.get_account_summary())
    
    
    print("\nget_candles_df():")
    print(api.get_candles_df(pair_name="EUR_USD", count=20))
