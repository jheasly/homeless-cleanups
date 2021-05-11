import pdfplumber
import pprint
import re

from os import listdir

pdf_files = listdir('pdf')
pdf_files = pdf_files[:3]

for file_name in pdf_files:
    
    with pdfplumber.open('pdf/{}'.format(file_name)) as pdf:
        
        p0 = pdf.pages[0]

        lines = p0.extract_text()
        
        lines = enumerate(lines.split('\n'))
        iter_lines = iter(lines)

        for line_id, line in iter_lines:
            # get Work Order ID
            if line.startswith('Work Order ID'):
                work_order_id_plus = line.split('Work Order ID: ')[1]
                work_order_id = work_order_id_plus.split(' Work Order Date: ')[0]
    #             print(work_order_id)

            # get Service Code
            if line.startswith('Service Code'):
                service_code, = re.findall(r'\[([^\]]*)\]', line)
                
            # get Service Address
            if line.startswith('Service Address'):
                index, service_address = next(iter_lines)
                print('>>> service address:', service_address)

            print(line_id, line)
                
        print(work_order_id, service_code, service_address, '\n\n')
        
        

#     tables = p0.extract_tables()
#     for table in tables:
#         pprint.pprint(table)
    
#     im = p0.to_image()
#     im.debug_tablefinder()
#     im.save('/Users/jpheasly/Development/homeless-cleanups/foo.png', format="PNG")
    