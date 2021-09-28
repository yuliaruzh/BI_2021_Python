print('Weight converter for units including kilograms(kg), grams(g),'
      ' stones(st), pounds(lb), ounces(oz), drams(dr) and grains(gr)')

in_weight = float(input('Enter the weight:'))
in_units = input('Enter the units to convert from:')
in_convert_units = input('Enter the units to convert to:')


def weight_convert(weight, units, convert_units):
    units_dict = {
        'kg': 1000,
        'g': 1,
        'st': 6350.2932,
        'lb': 453.5924,
        'oz': 28.3495,
        'dr': 1.7718,
        'gr': 0.0648
    }
    return weight * units_dict[units] / units_dict[convert_units]


print(weight_convert(in_weight, in_units, in_convert_units))
