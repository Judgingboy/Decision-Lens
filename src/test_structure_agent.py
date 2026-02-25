from agents.structure_agent import structure_decision

user_input = """
I want to buy a laptop.
Performance matters most, then price.
Laptop A is very fast but expensive.
Laptop B is balanced.
Laptop C is cheap with great battery life.
"""

structured = structure_decision(user_input)
print(structured)