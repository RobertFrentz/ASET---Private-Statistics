from Builder import ConcreteBuilder1
from Director import Director

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

print("Standard basic protocol: ")
director.build_minimal_viable_protocol()
builder.protocol.list_parts()

print("\n")

print("Standard full featured protocol: ")
director.build_full_featured_product()
builder.protocol.list_parts()

print("\n")

print("Custom protocol: ")
builder.produce_part_init()
builder.produce_part_encryption()
builder.protocol.list_parts()
