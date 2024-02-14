
from page_objects.PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    
    def test_control(self): # Control 
        self.fetch_tiktok()
        self.iterate_through_batches_control()
        time.sleep(10)

control_audit = TiktokAudit()

for i in range(1):
    print(f"=========== CONTROL EXPERIMENT RUN #{i} ===========")
    control_audit.test_control()
    
# should create 5 csv files of all the videos (for 5 "batches")