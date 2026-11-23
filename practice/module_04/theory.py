from dataclasses import dataclass


@dataclass
class EstateAgent:
    name: str
    phone: str
    sales: int = 0


kim = EstateAgent("Kim", "031-390 06 00")
same = EstateAgent("Kim", "031-390 06 00")
equal = kim == same

print(f"The agent:\n{kim}")
print(f"\nEqual to same:\n{equal}")