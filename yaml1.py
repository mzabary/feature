import yaml
print(yaml.load("""
name: Vorlin Laruknuzum
sex: Male
class: Priest
title: Acolyte
hp: [32, 71]
sp: [1, 13]
gold: 423
inventory:
    - a Holy Book of Prayers (Words of Wisdom)
    - an Azure Potion of Cure Light Wounds
    - a Silver Wand of Wonder """))
print(yaml.dump({'hp': [32, 71], 'title': 'Acolyte', 'sex': 'Male', 'name': 'Vorlin Laruknuzum', 'class':
    'Priest', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)', 'an Azure Potion of Cure Light Wounds',
                            'a Silver Wand of Wonder'], 'gold': 423, 'sp': [1, 13]}))

print(yaml.load("""
invoice: 34843
date   : 2001-01-23
bill-to: &id001
    given  : Chris
    family : Dumars
    address:
        lines: |
            458 Walkman Dr.
            Suite #292
        city    : Royal Oak
        state   : MI
        postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments:
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338"""))

data="""
invoice: 34843
date   : 2001-01-23
bill-to: &id001
    given  : Chris
    family : Dumars
    address:
        lines: |
            458 Walkman Dr.
            Suite #292
        city    : Royal Oak
        state   : MI
        postal  : 48046
ship-to: *id001
product:
    - sku         : BL394D
      quantity    : 4
      description : Basketball
      price       : 450.00
    - sku         : BL4438H
      quantity    : 1
      description : Super Hoop
      price       : 2392.00
tax  : 251.42
total: 4443.52
comments:
    Late afternoon is best.
    Backup contact is Nancy
    Billsmer @ 338-4338"""

#default_flow_style=False
print(yaml.dump(data,default_flow_style=False))