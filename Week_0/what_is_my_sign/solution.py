"""
    Aries: 21 March – 20 April
    Taurus: 21 April – 21 May
    Gemini: 22 May – 21 June
    Cancer: 22 June – 22 July
    Leo: 23 July – 22 August
    Virgo: 23 August – 23 September
    Libra: 24 September – 23 October
    Scorpio: 24 October – 22 November
    Sagittarius: 23 November – 21 December
    Capricorn: 22 December – 20 January
    Aquarius: 21 January – 19 February
    Pisces: 20 February – 20 March
"""

signs = {
	'Aries': {'from': (3,21), 'to': (4,20)},
	'Taurus': {'from': (4,21), 'to': (5,21)},
	'Gemini': {'from': (5,22), 'to': (6,21)},
	'Cancer': {'from': (6,22), 'to': (7,22)},
	'Leo': {'from': (7,23), 'to': (8,22)},
	'Virgo': {'from': (8,23), 'to': (9,23)},
	'Libra': {'from': (9,24), 'to': (10,23)},
	'Scorpio': {'from': (10,24), 'to': (11,22)},
	'Sagittarius': {'from': (11,23), 'to': (12,21)},
	'Capricorn': {'from': (12,22), 'to': (1,20)},
	'Aquarius': {'from': (1,21), 'to': (2,19)},
	'Pisces': {'from': (2,20), 'to': (3,20)},
}

def what_is_my_sign(day, month):
	date = (month, day)	
	for sign in signs:
		if sign != 'Capricorn' and signs[sign]['from'] <= date <= signs[sign]['to']:
			return sign
	return 'Capricorn'

def main():
	print(what_is_my_sign(5, 8))
	print(what_is_my_sign(29, 1))
	print(what_is_my_sign(30, 6))
	print(what_is_my_sign(31, 5))
	print(what_is_my_sign(2, 2))
	print(what_is_my_sign(8, 5))
	print(what_is_my_sign(9, 1))

if __name__ == '__main__':
	main()