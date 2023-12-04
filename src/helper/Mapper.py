'''
Function to return the month name.

Parameters:
  month: the number of the month.
Returns:
  The name of the month.
'''
def getMonthName(month):
  if month == "01" or month == "1":
    return "January"
  elif month == "02" or month == "2":
    return "February"
  elif month == "03" or month == "3":
    return "March"
  elif month == "04" or month == "4":
    return "April"
  elif month == "05" or month == "5":
    return "May"
  elif month == "06" or month == "6":
    return "June"
  elif month == "07" or month == "7":
    return "July"
  elif month == "08" or month == "8":
    return "August"
  elif month == "09" or month == "9":
    return "September"
  elif month == "10":
    return "October" 
  elif month == "11":
    return "November"
  elif month == "12":
    return "December"

'''
Function to mapper the population of each city.

Returns:
  A dictionary with the cities and population.
'''
def getCitiesPopulation():
  return {
    'BELO HORIZONTE': 2315560,
    'SAO LOURENCO': 44798,
    'NEPOMUCENO': 25018,
    'ELOI MENDES': 26336,
    'CRUZILIA': 15362,
    'UBA': 103365,
    'ARAGUARI': 117808,
    'MONTE SANTO DE MINAS': 20890,
    'UBERABA': 337836,
    'PARA DE MINAS': 97139,
    'PARAOPEBA': 24107,
    'PEDRO LEOPOLDO': 62580,
    'PRATA': 28342,
    'GOVERNADOR VALADARES': 257171,
    'ARCOS': 41416,
    'TRES MARIAS': 28895,
    'BARBACENA': 125317,
    'JAPARAIBA': 4506,
    'RIBEIRAO DAS NEVES': 329794,
    'JOAO MONLEVADE': 80187,
    'EXTREMA': 53482,
    'VARZEA DA PALMA': 33744,
    'ALFENAS': 78970,
    'VARGINHA': 136467,
    'BETIM': 411846,
    'OURO BRANCO': 38724,
    'IGARAPE': 45847,
    'DIVINOPOLIS': 231091,
    'JANAUBA': 70699,
    'SANTA LUZIA': 219132,
    'CONTAGEM': 621863,
    'NOVA LIMA': 111697,
    'MONTES CLAROS': 414240,
    'MANHUACU': 91886,
    'LAGOA DA PRATA': 51412,
    'SAO JOAO DEL REI': 90225,
    'BARROSO': 20080,
    'ALTEROSA': 13915,
    'PAPAGAIOS': 13920,
    'POUSO ALEGRE': 152217,
    'PARACATU': 94023,
    'ESMERALDAS': 85598,
    'SETE LAGOAS': 227397,
    'CARATINGA': 87360,
    'CONGONHAS': 52890,
    'ARCEBURGO': 9177,
    'MURIAE': 104108,
    'OURO PRETO': 74821,
    'CORONEL FABRICIANO': 104736,
    'PIRAPORA': 55606,
    'BOA ESPERANCA': 39848,
    'IBIRITE': 170537,
    'SABARA': 129380,
    'TURMALINA': 20000,
    'VIRGINIA': 8908,
    'CARBONITA': 8512,
    'LAVRAS': 104761,
    'CONSELHEIRO LAFAIETE': 131621,
    'CONCEICAO DO RIO VERDE': 12541,
    'MARIA DA FE': 14247,
    'BERTOPOLIS': 4451,
    'TEOFILO OTONI': 137418,
    'JAIBA': 37660,
    'ITUIUTABA': 102217,
    'ITANHANDU': 15236,
    'JANUARIA': 65150,
    'BRUMADINHO': 38915,
    'DIAMANTINA': 47702,
    'TRES CORACOES': 75485,
    'MARTINHO CAMPOS': 14003,
    'UBERLANDIA': 713224,
    'RESPLENDOR': 17226,
    'SAO JOSE DA LAPA': 26090,
    'LAGOA SANTA': 75145,
    'FELISBURGO': 6489,
    'PIUMHI': 36062,
    'CARANGOLA': 31240,
    'PIMENTA': 8563,
    'VICOSA': 76430,
    'MANHUMIRIM': 20613,
    'TIMOTEO': 81579,
    'JABOTICATUBAS': 20406,
    'JUIZ DE FORA': 540756,
    'JEQUERI': 12419,
    'PONTE NOVA': 57776,
    'MATOZINHOS': 37618,
    'ITURAMA': 38295,
    'JOAO PINHEIRO': 46801,
    'CARMOPOLIS DE MINAS': 18003,
    'MIRAI': 13633,
    'UNAI': 86619,
    'CAMPANHA': 15935,
    'CARMO DA CACHOEIRA': 11547,
    'CARRANCAS': 4049,
    'IPATINGA': 227731,
    'PATOS DE MINAS': 159235,
    'VESPASIANO': 129246,
    'ITABIRA': 113343,
    'PASSOS': 111939,
    'ARAXA': 111691,
    'NOVA SERRANA': 105552,
    'ITAUNA': 97669,
    'ITAJUBA': 93073,
    'SAO JOAO DEL REI': 90225,
    'PATROCINIO': 89826,
    'CURVELO': 80352,
    'SAO SEBASTIAO DO PARAISO': 71796,
    'FORMIGA': 68248,
    'CATAGUASES': 66261,
    'MARIANA': 61387,
    'FRUTAL': 58588,
    'TRES PONTAS': 55259,
    'ITABIRITO': 53282,
    'SAO FRANCISCO': 52762,
    'CAMPO BELO': 52277,
    'BOM DESPACHO': 51737,
    'LEOPOLDINA': 51145,
    'GUAXUPE': 50911,
    'BOCAIUVA': 48032,
    'MONTE CARMELO': 47689,
    'SANTANA DO PARAISO': 44800,
    'SANTOS DUMONT': 42406,
    'SAO GOTARGO': 40910,
    'SANTA RITA DO SAPUCAI': 40635,
    'ANDRADAS': 40548,
    'ALMENARA': 40364,
    'SALINAS': 40178,
    'CAPELINHA': 39624,
    'OLIVEIRA': 39262,
    'VISCONDE DO RIO BRANCO': 39160,
    'CAETE': 38776,
    'MATHEUS LEME': 37841,
    'MACHADO': 37684,
    'PORTEIRINHA': 37438,
    'SARZEDO': 36844,
    'NANUQUE': 35038,
    'SAO JOAQUIM DE BICAS': 34348,
    'ARACUAI': 34297,
    'TAIOBEIRAS': 33050,
    'ITAMARANDIBA': 32948,
    'GUANHAES': 32244,
    'OURO FINO': 32094,
    'BRASILIA DE MINAS': 32025,
    'POMPEU': 31047,
    'BARAO DE COCAIS': 30778,
    'ALEM PARAIBA': 30717,
    'JUATUBA': 30716,
    'SANTA BARBARA': 30466,
    'ESPINOSA': 30443,
    'CLAUDIO': 30159,
    'CAMBUI': 29536,
    'CARMO DO PARAINAIBA': 29011
  }