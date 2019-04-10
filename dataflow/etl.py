import csv
from astropy.table import row
from astropy.extern.bundled.six import next

widget_id=0
customer_id=0
supplier_id=0
inventory_id=0
warehouse_id=0
record_id=0

line_count=0
with open('widgets.tsv') as tsvfile:

  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    if line_count<1:
          
    else:   
        line_count +=1 
    
        (widget,\
         packaging,\
         customer,\
         price, \
         supplier, \
         cost,\
         warehouse,\
         qty,\
         min_qty)=row
    
    
    
        widget_item=widget+"\t"+packaging  
        print (widget_item)
    