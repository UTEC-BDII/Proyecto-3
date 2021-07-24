import face_recognition
from rtree import index

p = index.Property()
p.dimension = 128
p.buffering_capacity = 3
p.dat_extension = 'data'
p.idx_extension = 'index'

idx = index.Index('rtree', properties=p)
