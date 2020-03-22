def predict_person(person_age, person_genderName, person_descentName, person_premisName, person_lat, person_lon, person_areaName, person_seasonName, person_dayNightName):
    '''
    This function takes a person's attributes and returns a dictionary of the most probable crimes that would happen to that person if that person was to be a victim of a crime
    Inputs: Age, Sex, Descent, Premise Description, Latitude, Longitude, Area Name, Season, Day or Night
    Output: Dictionary with the top 5 most probable crimes and their respective probabilities
    '''

    import pandas as pd
    import numpy as np

    dummy_cols=['Vict Age',
    'NEWlat',
    'NEWlon',
    'NEW_Z',
    'AREA NAME_77th Street',
    'AREA NAME_Central',
    'AREA NAME_Devonshire',
    'AREA NAME_Foothill',
    'AREA NAME_Harbor',
    'AREA NAME_Hollenbeck',
    'AREA NAME_Hollywood',
    'AREA NAME_Mission',
    'AREA NAME_N Hollywood',
    'AREA NAME_Newton',
    'AREA NAME_Northeast',
    'AREA NAME_Olympic',
    'AREA NAME_Pacific',
    'AREA NAME_Rampart',
    'AREA NAME_Southeast',
    'AREA NAME_Southwest',
    'AREA NAME_Topanga',
    'AREA NAME_Van Nuys',
    'AREA NAME_West LA',
    'AREA NAME_West Valley',
    'AREA NAME_Wilshire',
    'Vict Sex_F',
    'Vict Sex_M',
    'Vict Sex_X',
    'Vict Descent_A',
    'Vict Descent_B',
    'Vict Descent_C',
    'Vict Descent_D',
    'Vict Descent_F',
    'Vict Descent_G',
    'Vict Descent_H',
    'Vict Descent_I',
    'Vict Descent_J',
    'Vict Descent_K',
    'Vict Descent_L',
    'Vict Descent_O',
    'Vict Descent_P',
    'Vict Descent_S',
    'Vict Descent_U',
    'Vict Descent_V',
    'Vict Descent_W',
    'Vict Descent_X',
    'Vict Descent_Z',
    'Premis Desc_7TH AND METRO CENTER (NOT LINE SPECIFIC)',
    'Premis Desc_ABANDONED BUILDING ABANDONED HOUSE',
    'Premis Desc_ABATEMENT LOCATION',
    'Premis Desc_ABORTION CLINIC/ABORTION FACILITY*',
    'Premis Desc_AIRCRAFT',
    'Premis Desc_ALLEY',
    'Premis Desc_AMTRAK TRAIN',
    'Premis Desc_AMUSEMENT PARK*',
    'Premis Desc_APARTMENT/CONDO COMMON LAUNDRY ROOM',
    'Premis Desc_ARCADE,GAME ROOM/VIDEO GAMES (EXAMPLE CHUCKIE CHEESE)*',
    'Premis Desc_AUTO DEALERSHIP (CHEVY, FORD, BMW, MERCEDES, ETC.)',
    'Premis Desc_AUTO REPAIR SHOP',
    'Premis Desc_AUTO SALES LOT',
    'Premis Desc_AUTO SUPPLY STORE*',
    'Premis Desc_AUTOMATED TELLER MACHINE (ATM)',
    'Premis Desc_BALCONY*',
    'Premis Desc_BANK',
    'Premis Desc_BANK DROP BOX/MONEY DROP-OUTSIDE OF BANK*',
    'Premis Desc_BANKING INSIDE MARKET-STORE *',
    'Premis Desc_BAR/COCKTAIL/NIGHTCLUB',
    'Premis Desc_BAR/SPORTS BAR (OPEN DAY & NIGHT)',
    'Premis Desc_BASKETBALL COURTS',
    'Premis Desc_BEACH',
    'Premis Desc_BEAUTY SUPPLY STORE',
    'Premis Desc_BEAUTY/BARBER SHOP',
    'Premis Desc_BLUE LINE (ABOVE GROUND SURFACE TRAIN)',
    'Premis Desc_BOOK STORE',
    'Premis Desc_BOWLING ALLEY*',
    'Premis Desc_BUS DEPOT/TERMINAL, OTHER THAN MTA',
    'Premis Desc_BUS STOP',
    'Premis Desc_BUS STOP/LAYOVER (ALSO QUERY 124)',
    'Premis Desc_BUS, SCHOOL, CHURCH',
    'Premis Desc_BUS-CHARTER/PRIVATE',
    'Premis Desc_CAR WASH',
    'Premis Desc_CATERING/ICE CREAM TRUCK',
    'Premis Desc_CELL PHONE STORE',
    'Premis Desc_CEMETARY*',
    'Premis Desc_CHECK CASHING*',
    'Premis Desc_CHEMICAL STORAGE/MANUFACTURING PLANT',
    'Premis Desc_CHURCH/CHAPEL (CHANGED 03-03 FROM CHURCH/TEMPLE)',
    'Premis Desc_CLEANER/LAUNDROMAT',
    'Premis Desc_CLOTHING STORE',
    "Premis Desc_COFFEE SHOP (STARBUCKS, COFFEE BEAN, PEET'S, ETC.)",
    'Premis Desc_COLISEUM',
    'Premis Desc_COLLEGE/JUNIOR COLLEGE/UNIVERSITY',
    'Premis Desc_COMPUTER SERVICES/REPAIRS/SALES',
    'Premis Desc_CONDOMINIUM/TOWNHOUSE',
    'Premis Desc_CONSTRUCTION SITE',
    'Premis Desc_CONVENTION CENTER',
    'Premis Desc_CREDIT UNION',
    'Premis Desc_CULTURAL SIGNIFICANCE/MONUMENT',
    'Premis Desc_CYBERSPACE',
    'Premis Desc_DAM/RESERVOIR',
    'Premis Desc_DAY CARE/ADULTS*',
    'Premis Desc_DAY CARE/CHILDREN*',
    'Premis Desc_DELIVERY SERVICE (FED EX, UPS, COURIERS,COURIER SERVICE)*',
    'Premis Desc_DEPARTMENT STORE',
    'Premis Desc_DEPT OF DEFENSE FACILITY',
    'Premis Desc_DETENTION/JAIL FACILITY',
    'Premis Desc_DISCOUNT STORE (99 CENT,DOLLAR,ETC.',
    "Premis Desc_DIY CENTER (LOWE'S,HOME DEPOT,OSH,CONTRACTORS WAREHOUSE)",
    'Premis Desc_DODGER STADIUM',
    'Premis Desc_DRIVE THRU BANKING (WINDOW)*',
    'Premis Desc_DRIVE THRU*',
    'Premis Desc_DRIVEWAY',
    'Premis Desc_DRUG STORE',
    'Premis Desc_ELECTRONICS STORE (IE:RADIO SHACK, ETC.)',
    'Premis Desc_ELEMENTARY SCHOOL',
    'Premis Desc_ELEVATOR',
    'Premis Desc_ENERGY PLANT/FACILITY',
    'Premis Desc_ENTERTAINMENT/COMEDY CLUB (OTHER)',
    'Premis Desc_EQUIPMENT RENTAL',
    'Premis Desc_ESCALATOR*',
    'Premis Desc_FACTORY',
    'Premis Desc_FINANCE COMPANY',
    'Premis Desc_FIRE STATION',
    'Premis Desc_FOSTER HOME BOYS OR GIRLS*',
    'Premis Desc_FRAT HOUSE/SORORITY/DORMITORY',
    'Premis Desc_FREEWAY',
    'Premis Desc_FURNITURE STORE',
    'Premis Desc_GARAGE/CARPORT',
    'Premis Desc_GARMENT MANUFACTURER',
    'Premis Desc_GAS STATION',
    'Premis Desc_GOLF COURSE*',
    'Premis Desc_GOVERNMENT FACILITY (FEDERAL,STATE, COUNTY & CITY)',
    'Premis Desc_GREEN LINE (I-105 FWY LEVEL TRAIN)',
    'Premis Desc_GREYHOUND OR INTERSTATE BUS',
    'Premis Desc_GROUP HOME',
    'Premis Desc_GUN/SPORTING GOODS',
    'Premis Desc_HANDBALL COURTS',
    'Premis Desc_HARBOR FRWY STATION (NOT LINE SPECIFIC)',
    'Premis Desc_HARDWARE/BUILDING SUPPLY',
    'Premis Desc_HEALTH SPA/GYM',
    'Premis Desc_HIGH SCHOOL',
    'Premis Desc_HIGH-RISE BUILDING',
    'Premis Desc_HOCKEY RINK/ICE HOCKEY',
    'Premis Desc_HORSE RACING/SANTA ANITA PARK*',
    'Premis Desc_HOSPICE',
    'Premis Desc_HOSPITAL',
    'Premis Desc_HOTEL',
    'Premis Desc_JEWELRY STORE',
    'Premis Desc_JUNIOR HIGH SCHOOL',
    'Premis Desc_LA UNION STATION (NOT LINE SPECIFIC)',
    'Premis Desc_LAUNDROMAT',
    'Premis Desc_LIBRARY',
    'Premis Desc_LIQUOR STORE',
    'Premis Desc_MAIL BOX',
    'Premis Desc_MANUFACTURING COMPANY',
    'Premis Desc_MARKET',
    'Premis Desc_MASS GATHERING LOCATION',
    'Premis Desc_MASSAGE PARLOR',
    'Premis Desc_MEDICAL MARIJUANA FACILITIES/BUSINESSES',
    'Premis Desc_MEDICAL/DENTAL OFFICES',
    'Premis Desc_MEMBERSHIP STORE (COSTCO,SAMS CLUB)*',
    'Premis Desc_METHADONE CLINIC',
    'Premis Desc_METROLINK TRAIN',
    'Premis Desc_MINI-MART',
    'Premis Desc_MISSIONS/SHELTERS',
    "Premis Desc_MOBILE HOME/TRAILERS/CONSTRUCTION TRAILERS/RV'S/MOTORHOME",
    'Premis Desc_MORTUARY',
    'Premis Desc_MOSQUE*',
    'Premis Desc_MOTEL',
    'Premis Desc_MTA - BLUE LINE - 103RD/WATTS TOWERS',
    'Premis Desc_MTA - BLUE LINE - 7TH AND METRO CENTER',
    'Premis Desc_MTA - BLUE LINE - GRAND/LATTC',
    'Premis Desc_MTA - BLUE LINE - PICO',
    'Premis Desc_MTA - BLUE LINE - SAN PEDRO',
    'Premis Desc_MTA - BLUE LINE - VERNON',
    'Premis Desc_MTA - BLUE LINE - WASHINGTON',
    'Premis Desc_MTA - EXPO LINE - 7TH AND METRO CENTER',
    'Premis Desc_MTA - EXPO LINE - EXPO PARK/USC',
    'Premis Desc_MTA - EXPO LINE - EXPO/BUNDY',
    'Premis Desc_MTA - EXPO LINE - EXPO/CRENSHAW',
    'Premis Desc_MTA - EXPO LINE - EXPO/LA BREA',
    'Premis Desc_MTA - EXPO LINE - EXPO/SEPULVEDA',
    'Premis Desc_MTA - EXPO LINE - EXPO/VERMONT',
    'Premis Desc_MTA - EXPO LINE - EXPO/WESTERN',
    'Premis Desc_MTA - EXPO LINE - FARMDALE',
    'Premis Desc_MTA - EXPO LINE - JEFFERSON/USC',
    'Premis Desc_MTA - EXPO LINE - LA CIENEGA/JEFFERSON',
    'Premis Desc_MTA - EXPO LINE - LATTC/ORTHO INSTITUTE',
    'Premis Desc_MTA - EXPO LINE - PALMS',
    'Premis Desc_MTA - EXPO LINE - PICO',
    'Premis Desc_MTA - EXPO LINE - WESTWOOD/RANCHO PARK',
    'Premis Desc_MTA - GOLD LINE - CHINATOWN',
    'Premis Desc_MTA - GOLD LINE - HERITAGE SQ',
    'Premis Desc_MTA - GOLD LINE - HIGHLAND PARK',
    'Premis Desc_MTA - GOLD LINE - INDIANA',
    'Premis Desc_MTA - GOLD LINE - LINCOLN/CYPRESS',
    'Premis Desc_MTA - GOLD LINE - LITTLE TOKYO/ARTS DISTRICT',
    'Premis Desc_MTA - GOLD LINE - MARIACHI PLAZA',
    'Premis Desc_MTA - GOLD LINE - PICO/ALISO',
    'Premis Desc_MTA - GOLD LINE - SOTO',
    'Premis Desc_MTA - GOLD LINE - SOUTHWEST MUSEUM',
    'Premis Desc_MTA - GOLD LINE - UNION STATION',
    'Premis Desc_MTA - GREEN LINE - AVALON',
    'Premis Desc_MTA - GREEN LINE - AVIATION/LAX',
    'Premis Desc_MTA - GREEN LINE - HARBOR FWY',
    'Premis Desc_MTA - ORANGE LINE - BALBOA',
    'Premis Desc_MTA - ORANGE LINE - CANOGA',
    'Premis Desc_MTA - ORANGE LINE - CHATSWORTH',
    'Premis Desc_MTA - ORANGE LINE - DE SOTO',
    'Premis Desc_MTA - ORANGE LINE - LAUREL CANYON',
    'Premis Desc_MTA - ORANGE LINE - NORDHOFF',
    'Premis Desc_MTA - ORANGE LINE - NORTH HOLLYWOOD',
    'Premis Desc_MTA - ORANGE LINE - PIERCE COLLEGE',
    'Premis Desc_MTA - ORANGE LINE - RESEDA',
    'Premis Desc_MTA - ORANGE LINE - ROSCOE',
    'Premis Desc_MTA - ORANGE LINE - SEPULVEDA',
    'Premis Desc_MTA - ORANGE LINE - SHERMAN WAY',
    'Premis Desc_MTA - ORANGE LINE - TAMPA',
    'Premis Desc_MTA - ORANGE LINE - VALLEY COLLEGE',
    'Premis Desc_MTA - ORANGE LINE - VAN NUYS',
    'Premis Desc_MTA - ORANGE LINE - WARNER CTR',
    'Premis Desc_MTA - ORANGE LINE - WOODLEY',
    'Premis Desc_MTA - ORANGE LINE - WOODMAN',
    'Premis Desc_MTA - PURPLE LINE - 7TH AND METRO CENTER',
    'Premis Desc_MTA - PURPLE LINE - CIVIC CENTER/GRAND PARK',
    'Premis Desc_MTA - PURPLE LINE - PERSHING SQUARE',
    'Premis Desc_MTA - PURPLE LINE - UNION STATION',
    'Premis Desc_MTA - PURPLE LINE - WESTLAKE/MACARTHUR PARK',
    'Premis Desc_MTA - PURPLE LINE - WILSHIRE/NORMANDIE',
    'Premis Desc_MTA - PURPLE LINE - WILSHIRE/VERMONT',
    'Premis Desc_MTA - PURPLE LINE - WILSHIRE/WESTERN',
    'Premis Desc_MTA - RED LINE - 7TH AND METRO CENTER',
    'Premis Desc_MTA - RED LINE - CIVIC CENTER/GRAND PARK',
    'Premis Desc_MTA - RED LINE - HOLLYWOOD/HIGHLAND',
    'Premis Desc_MTA - RED LINE - HOLLYWOOD/VINE',
    'Premis Desc_MTA - RED LINE - HOLLYWOOD/WESTERN',
    'Premis Desc_MTA - RED LINE - NORTH HOLLYWOOD',
    'Premis Desc_MTA - RED LINE - PERSHING SQUARE',
    'Premis Desc_MTA - RED LINE - UNION STATION',
    'Premis Desc_MTA - RED LINE - UNIVERSAL CITY/STUDIO CITY',
    'Premis Desc_MTA - RED LINE - VERMONT/BEVERLY',
    'Premis Desc_MTA - RED LINE - VERMONT/SANTA MONICA',
    'Premis Desc_MTA - RED LINE - VERMONT/SUNSET',
    'Premis Desc_MTA - RED LINE - WESTLAKE/MACARTHUR PARK',
    'Premis Desc_MTA - RED LINE - WILSHIRE/VERMONT',
    'Premis Desc_MTA - SILVER LINE - 37TH ST/USC',
    'Premis Desc_MTA - SILVER LINE - CAL STATE LA',
    'Premis Desc_MTA - SILVER LINE - DOWNTOWN STREET STOPS',
    'Premis Desc_MTA - SILVER LINE - HARBOR FWY',
    'Premis Desc_MTA - SILVER LINE - HARBOR GATEWAY TRANSIT CTR',
    'Premis Desc_MTA - SILVER LINE - MANCHESTER',
    'Premis Desc_MTA - SILVER LINE - PACIFIC COAST HWY',
    'Premis Desc_MTA - SILVER LINE - ROSECRANS',
    'Premis Desc_MTA - SILVER LINE - SAN PEDRO STREET STOPS',
    'Premis Desc_MTA - SILVER LINE - SLAUSON',
    'Premis Desc_MTA - SILVER LINE - UNION STATION',
    'Premis Desc_MTA BUS',
    'Premis Desc_MTA PROPERTY OR PARKING LOT',
    'Premis Desc_MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)',
    'Premis Desc_MUNICIPAL BUS LINE INCLUDES LADOT/DASH',
    'Premis Desc_MUSCLE BEACH',
    'Premis Desc_MUSEUM',
    'Premis Desc_NAIL SALON',
    'Premis Desc_NIGHT CLUB (OPEN EVENINGS ONLY)',
    'Premis Desc_NUCLEAR FACILITY',
    'Premis Desc_NURSERY/FLOWER SHOP',
    'Premis Desc_NURSING/CONVALESCENT/RETIREMENT HOME',
    'Premis Desc_OFFICE BUILDING/OFFICE',
    'Premis Desc_OIL REFINERY',
    'Premis Desc_OPTICAL OFFICE INSIDE STORE OR SUPERMARKET*',
    'Premis Desc_ORANGE LINE PARKING LOT',
    'Premis Desc_OTHER BUSINESS',
    'Premis Desc_OTHER INTERSTATE, CHARTER BUS',
    'Premis Desc_OTHER PLACE OF WORSHIP',
    'Premis Desc_OTHER PREMISE',
    'Premis Desc_OTHER RESIDENCE',
    'Premis Desc_OTHER RR TRAIN (UNION PAC, SANTE FE ETC',
    'Premis Desc_OTHER STORE',
    'Premis Desc_OTHER/OUTSIDE',
    'Premis Desc_PARK/PLAYGROUND',
    'Premis Desc_PARKING LOT',
    'Premis Desc_PARKING UNDERGROUND/BUILDING',
    'Premis Desc_PATIO*',
    'Premis Desc_PAWN SHOP',
    'Premis Desc_PAY PHONE',
    'Premis Desc_PEDESTRIAN OVERCROSSING',
    'Premis Desc_PET STORE',
    'Premis Desc_PHARMACY INSIDE STORE OR SUPERMARKET*',
    'Premis Desc_POLICE FACILITY',
    'Premis Desc_POOL-PUBLIC/OUTDOOR OR INDOOR*',
    'Premis Desc_PORCH, RESIDENTIAL',
    'Premis Desc_POST OFFICE',
    'Premis Desc_PRIVATE SCHOOL/PRESCHOOL',
    'Premis Desc_PROJECT/TENEMENT/PUBLIC HOUSING',
    'Premis Desc_PUBLIC RESTROOM(INDOORS-INSIDE)',
    'Premis Desc_PUBLIC RESTROOM/OUTSIDE*',
    'Premis Desc_PUBLIC STORAGE',
    'Premis Desc_RECORD-CD MUSIC/COMPUTER GAME STORE',
    'Premis Desc_RECYCLING CENTER',
    'Premis Desc_REDLINE (SUBWAY TRAIN)',
    'Premis Desc_REDLINE ENTRANCE/EXIT',
    'Premis Desc_REDLINE SUBWAY MEZZANINE',
    'Premis Desc_REDLINE SUBWAY PLATFORM',
    'Premis Desc_REDLINE SUBWAY RAIL CAR (INSIDE TRAIN)',
    'Premis Desc_REDLINE SUBWAY TUNNEL',
    'Premis Desc_RESTAURANT/FAST FOOD',
    'Premis Desc_RETIRED (DUPLICATE) DO NOT USE THIS CODE',
    'Premis Desc_RIVER BED*',
    'Premis Desc_SAVINGS & LOAN',
    'Premis Desc_SEWAGE FACILITY/PIPE',
    "Premis Desc_SEX ORIENTED/BOOK STORE/STRIP CLUB/GENTLEMAN'S CLUB",
    'Premis Desc_SHOPPING MALL (COMMON AREA)',
    'Premis Desc_SHORT-TERM VACATION RENTAL',
    'Premis Desc_SIDEWALK',
    'Premis Desc_SINGLE FAMILY DWELLING',
    "Premis Desc_SINGLE RESIDENCE OCCUPANCY (SRO'S) LOCATIONS",
    'Premis Desc_SKATEBOARD FACILITY/SKATEBOARD PARK*',
    'Premis Desc_SKATING RINK*',
    'Premis Desc_SLIPS/DOCK/MARINA/BOAT',
    'Premis Desc_SPECIALTY SCHOOL/OTHER',
    'Premis Desc_SPORTS ARENA',
    'Premis Desc_SPORTS VENUE, OTHER',
    'Premis Desc_STAIRWELL*',
    'Premis Desc_STAPLES CENTER *',
    'Premis Desc_STORAGE SHED',
    'Premis Desc_STREET',
    'Premis Desc_STUDIO (FILM/PHOTOGRAPHIC/MUSIC)',
    'Premis Desc_SURPLUS SURVIVAL STORE',
    'Premis Desc_SWAP MEET',
    'Premis Desc_SYNAGOGUE/TEMPLE',
    'Premis Desc_TACTICAL SIGNIFICANCE',
    'Premis Desc_TATTOO PARLOR*',
    'Premis Desc_TAXI',
    'Premis Desc_TELECOMMUNICATION FACILITY/LOCATION',
    'Premis Desc_TERMINAL, OTHER THAN MTA',
    'Premis Desc_THE BEVERLY CENTER',
    'Premis Desc_THE BEVERLY CONNECTION',
    'Premis Desc_THE GROVE',
    'Premis Desc_THEATRE/MOVIE',
    'Premis Desc_TOBACCO SHOP',
    'Premis Desc_TOOL SHED*',
    'Premis Desc_TOW YARD*',
    'Premis Desc_TRADE SCHOOL (MEDICAL-TECHNICAL-BUSINESS)*',
    'Premis Desc_TRAIN DEPOT/TERMINAL, OTHER THAN MTA',
    'Premis Desc_TRAIN TRACKS',
    'Premis Desc_TRAIN, OTHER THAN MTA (ALSO QUERY 809/810/811)',
    'Premis Desc_TRAM/STREETCAR(BOXLIKE WAG ON RAILS)*',
    'Premis Desc_TRANSIENT ENCAMPMENT',
    'Premis Desc_TRANSITIONAL HOUSING/HALFWAY HOUSE',
    'Premis Desc_TRANSPORTATION FACILITY (AIRPORT)',
    'Premis Desc_TRASH CAN/TRASH DUMPSTER',
    'Premis Desc_TRUCK, COMMERICAL',
    'Premis Desc_TUNNEL',
    'Premis Desc_TV/RADIO/APPLIANCE',
    'Premis Desc_UNDERPASS/BRIDGE*',
    'Premis Desc_Unknown',
    'Premis Desc_VACANT LOT',
    'Premis Desc_VALET',
    "Premis Desc_VEHICLE STORAGE LOT (CARS, TRUCKS, RV'S, BOATS, TRAILERS, ETC.)",
    'Premis Desc_VEHICLE, PASSENGER/TRUCK',
    'Premis Desc_VETERINARIAN/ANIMAL HOSPITAL',
    'Premis Desc_VIDEO RENTAL STORE',
    'Premis Desc_VISION CARE FACILITY*',
    'Premis Desc_WAREHOUSE',
    'Premis Desc_WATER FACILITY',
    'Premis Desc_WEBSITE',
    'Premis Desc_YARD (RESIDENTIAL/BUSINESS)',
    'SEASON_fall',
    'SEASON_spring',
    'SEASON_summer',
    'SEASON_winter',
    'day_night_day',
    'day_night_night']

    person = pd.DataFrame(np.zeros((1, 373)), columns = dummy_cols)

    # Populate the respective dummy columns based on the inputs
    # (1) AREA  (EX: person_areaName = 'Van Nuys')
    person_area = 'AREA NAME_' + person_areaName
    person[person_area] = 1
    area_cols = [col for col in person.columns if 'AREA NAME' in col]
    area_cols.remove(person_area)
    person[area_cols] = 0

    # (2) GENDER/SEX  (EX: person_genderName = 'M')
    sex_cols = [col for col in person.columns if 'Vict Sex' in col]
    person_sex = 'Vict Sex_'+person_genderName
    person[person_sex]=1
    sex_cols.remove(person_sex)
    person[sex_cols]=0

    # (3) DESCENT (EX: person_descentName = 'H')
    descent_cols = [col for col in person.columns if 'Vict Descent' in col]
    person_descent = 'Vict Descent_'+person_descentName
    person[person_descent]=1
    descent_cols.remove(person_descent)
    person[descent_cols]=0

    # (4) PREMISE DESCRIPTION (EX: person_premisName = 'LIBRARY')
    premis_cols = [col for col in person.columns if 'Premis Desc' in col]
    person_premis = 'Premis Desc_'+person_premisName
    person[person_premis]=1
    premis_cols.remove(person_premis)
    person[premis_cols]=0

    # (5) SEASON (EX: person_seasonName = 'fall')
    season_cols = [col for col in person.columns if 'SEASON' in col]
    person_season = 'SEASON_'+person_seasonName
    person[person_season]=1
    season_cols.remove(person_season)
    person[season_cols]=0

    # (6) DAY/NIGHT (EX: # person_dayNightName = 'night')
    dayNight_cols = [col for col in person.columns if 'day_night' in col]
    person_dayNight = 'day_night_'+person_dayNightName
    person[person_dayNight]=1
    dayNight_cols.remove(person_dayNight)
    person[dayNight_cols]=0

    # (7) LAT, LON, Z
    person['NEWlat'] = person_lat**2
    person['NEWlon'] = person_lon**2
    person['NEW_Z'] = person_lat*person_lon

    # (8) AGE
    person['Vict Age'] = person_age

    # Load the model
    import joblib
    model2 = joblib.load('crime-model-v2.sav')

    X_scaler_desc = joblib.load('std_scaler.bin')
    # Scale the data for the person data
    person_scaled = X_scaler_desc.transform(person)

    # Make the prediction using the model
    person_pred = model2.predict([person_scaled[0]])

    # Predict the probabilities of the crimes for that person
    list2 = []
    for i in zip(model2.classes_, model2.predict_proba([person_scaled[0]])[0]):
        list2.append(i)

    # Sort them in ascending order based on the probability
    list2.sort(key = lambda x: x[1])

    # Reverse so it shows the most probable crime first
    list2.reverse()

    # Get the top 5 most probable crimes if a crime was to happen to the person
    top5 = list2[0:5]

    # Create a dictionary of the top 5 most probable crimes and their probabilities
    top5_dict = {}
    for i in top5:
        top5_dict[i[0]]=round(i[1]*100,2)
    # TO get the crime names in the returned dictionary: top5_dict.keys()
    # To get the probabilities of the crimes in the returned dictionary: top5_dict.values()
    return top5_dict 