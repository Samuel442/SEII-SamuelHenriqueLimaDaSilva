#Aula 11

import chunk


with open('bronx.jpeg', 'rb') as rf:
    with open('bronx_copy.jpeg', 'wb') as wf:
         chunk_size = 4096
         rf_chunk = rf.read(chunk_size)
         while len(rf_chunk) > 0:
             wf.write(rf_chunk)
             rf_chunk = rf.read(chunk_size)