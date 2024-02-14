
from PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    def test_save_random(self): # Experimental
        self.fetch_tiktok()
        self.iterate_through_batches_save_random()
        time.sleep(10)

experimental_audit = TiktokAudit()

for i in range(2):
    print(f"=========== SAVING EXPERIMENT RUN #{i} ===========")
    experimental_audit.test_save_random()
    
    

    
# should create 10 csv files
    # 5 csv files of saved video data (for 5 "batches")
    # 5 csv files of all video data (for 5 "batches")