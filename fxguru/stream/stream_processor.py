import copy
import random
import threading
import time
from queue import Queue
from stream.stream_base import StreamBase

class PriceProcessor(StreamBase):

    def __init__(self, shared_prices, price_lock: threading.Lock, price_events, logname, pair, work_queue: Queue):
        super().__init__(shared_prices, price_lock, price_events, logname)
        self.pair = pair
        self.work_queue = work_queue

    def process_price(self):
        
        price = None

        try: 
            self.price_lock.acquire()
            price = copy.deepcopy(self.shared_prices[self.pair])
        except Exception as error:
            self.log_message(f"Program Crash: {error}", error=True)
        finally:
            self.price_lock.release()

        if price is None:
            self.log_message(f"NO PRICE", error=True)
        else:
            self.log_message(f"Found Price: {price}")
            time.sleep(random.randint(2,5))
            self.log_message(f"Completed processing price: {price}")
            if random.randint(0,5) == 3:
                self.log_message(f"Adding work: {price}")
                self.work_queue.put(price)
    
    def run(self):

        while True:
             self.price_events[self.pair].wait()
             self.process_price()
             self.price_events[self.pair].clear()