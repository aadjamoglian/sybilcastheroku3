var data = ['SINGLE FAMILY DWELLING', 'STREET', 'OTHER PREMISE', 'PARKING LOT',
'SIDEWALK', 'MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)',
'RESTAURANT/FAST FOOD', 'BAR/COCKTAIL/NIGHTCLUB', 'HOTEL',
'OTHER BUSINESS', 'OTHER STORE',
'GOVERNMENT FACILITY (FEDERAL,STATE, COUNTY & CITY)',
'VEHICLE, PASSENGER/TRUCK',
'MUNICIPAL BUS LINE INCLUDES LADOT/DASH', 'PAWN SHOP',
'OTHER RESIDENCE', 'JEWELRY STORE', 'SPECIALTY SCHOOL/OTHER',
'CHURCH/CHAPEL (CHANGED 03-03 FROM CHURCH/TEMPLE)', 'ALLEY',
'OFFICE BUILDING/OFFICE', 'CONSTRUCTION SITE',
'PARKING UNDERGROUND/BUILDING', 'HOSPITAL', 'DRIVEWAY', 'BUS STOP',
'NIGHT CLUB (OPEN EVENINGS ONLY)', 'DRUG STORE', 'LIQUOR STORE',
'DEPARTMENT STORE', 'MARKET',
'TRAIN DEPOT/TERMINAL, OTHER THAN MTA', 'PUBLIC RESTROOM/OUTSIDE*',
'LIBRARY', 'SPORTS ARENA', 'ELEVATOR', 'CLOTHING STORE',
'HIGH SCHOOL', 'BUS DEPOT/TERMINAL, OTHER THAN MTA',
'POLICE FACILITY', 'OTHER/OUTSIDE', 'PARK/PLAYGROUND',
'GAS STATION', 'FREEWAY', 'THEATRE/MOVIE', 'BEAUTY/BARBER SHOP',
'MEDICAL/DENTAL OFFICES',
'TRAIN, OTHER THAN MTA (ALSO QUERY 809/810/811)',
'SHOPPING MALL (COMMON AREA)', 'AUTOMATED TELLER MACHINE (ATM)',
'HEALTH SPA/GYM', 'STAPLES CENTER *', 'MOTEL', 'GARAGE/CARPORT',
'CONDOMINIUM/TOWNHOUSE', 'PATIO*',
'PUBLIC RESTROOM(INDOORS-INSIDE)', 'WAREHOUSE',
'BUS-CHARTER/PRIVATE', 'CONVENTION CENTER', 'FACTORY', 'BANK',
'CREDIT UNION', 'PUBLIC STORAGE', 'YARD (RESIDENTIAL/BUSINESS)',
'TRADE SCHOOL (MEDICAL-TECHNICAL-BUSINESS)*', 'CLEANER/LAUNDROMAT',
'TERMINAL, OTHER THAN MTA', 'AMTRAK TRAIN',
'BUS STOP/LAYOVER (ALSO QUERY 124)', 'AUTO SALES LOT', 'MINI-MART',
'VACANT LOT', 'SWAP MEET', 'STAIRWELL*',
'TRANSPORTATION FACILITY (AIRPORT)', 'ELEMENTARY SCHOOL',
'MTA BUS', 'MANUFACTURING COMPANY', 'BEAUTY SUPPLY STORE',
'PORCH, RESIDENTIAL', 'BAR/SPORTS BAR (OPEN DAY & NIGHT)',
'STORAGE SHED', 'FINANCE COMPANY',
'COLLEGE/JUNIOR COLLEGE/UNIVERSITY', 'TRUCK, COMMERICAL',
'ENTERTAINMENT/COMEDY CLUB (OTHER)', 'TAXI', 'PAY PHONE',
'NURSING/CONVALESCENT/RETIREMENT HOME', 'HIGH-RISE BUILDING',
'REDLINE ENTRANCE/EXIT', 'SKATEBOARD FACILITY/SKATEBOARD PARK*',
'CHECK CASHING*', 'JUNIOR HIGH SCHOOL',
'FOSTER HOME BOYS OR GIRLS*', 'LAUNDROMAT',
'ARCADE,GAME ROOM/VIDEO GAMES (EXAMPLE CHUCKIE CHEESE)*',
'VIDEO RENTAL STORE', 'ABANDONED BUILDING ABANDONED HOUSE',
'POOL-PUBLIC/OUTDOOR OR INDOOR*',
'PHARMACY INSIDE STORE OR SUPERMARKET*', 'GROUP HOME',
'HARDWARE/BUILDING SUPPLY', 'FRAT HOUSE/SORORITY/DORMITORY',
'AUTO REPAIR SHOP', 'REDLINE SUBWAY PLATFORM',
'MEDICAL MARIJUANA FACILITIES/BUSINESSES', 'NAIL SALON',
'TV/RADIO/APPLIANCE', 'PRIVATE SCHOOL/PRESCHOOL',
'PROJECT/TENEMENT/PUBLIC HOUSING', 'POST OFFICE',
'PEDESTRIAN OVERCROSSING', 'DAY CARE/ADULTS*',
'GUN/SPORTING GOODS', 'BUS, SCHOOL, CHURCH',
"SEX ORIENTED/BOOK STORE/STRIP CLUB/GENTLEMAN'S CLUB",
'MEMBERSHIP STORE (COSTCO,SAMS CLUB)*', 'TATTOO PARLOR*',
'TOW YARD*', 'COLISEUM', 'AUTO SUPPLY STORE*',
'SLIPS/DOCK/MARINA/BOAT', 'OTHER PLACE OF WORSHIP',
'REDLINE SUBWAY RAIL CAR (INSIDE TRAIN)',
'RETIRED (DUPLICATE) DO NOT USE THIS CODE', 'UNDERPASS/BRIDGE*',
'Unknown', 'VISION CARE FACILITY*',
"MOBILE HOME/TRAILERS/CONSTRUCTION TRAILERS/RV'S/MOTORHOME",
'MTA PROPERTY OR PARKING LOT',
'RECORD-CD MUSIC/COMPUTER GAME STORE', 'DRIVE THRU*', 'BALCONY*',
'BEACH', 'DAY CARE/CHILDREN*', 'SYNAGOGUE/TEMPLE', 'GOLF COURSE*',
'FIRE STATION',
'DELIVERY SERVICE (FED EX, UPS, COURIERS,COURIER SERVICE)*',
'CEMETARY*', 'MASSAGE PARLOR',
'BLUE LINE (ABOVE GROUND SURFACE TRAIN)', 'OIL REFINERY',
'CELL PHONE STORE', 'ABORTION CLINIC/ABORTION FACILITY*',
'MAIL BOX', 'RIVER BED*',
'OPTICAL OFFICE INSIDE STORE OR SUPERMARKET*', 'BOWLING ALLEY*',
'SPORTS VENUE, OTHER', 'TOOL SHED*', 'AIRCRAFT', 'DODGER STADIUM',
'AMUSEMENT PARK*', 'GARMENT MANUFACTURER',
'BANKING INSIDE MARKET-STORE *', 'MASS GATHERING LOCATION',
'MOSQUE*', 'GREYHOUND OR INTERSTATE BUS', 'METROLINK TRAIN',
'HORSE RACING/SANTA ANITA PARK*', 'SAVINGS & LOAN', 'TOBACCO SHOP',
'CHEMICAL STORAGE/MANUFACTURING PLANT', 'EQUIPMENT RENTAL',
'DRIVE THRU BANKING (WINDOW)*',
'TELECOMMUNICATION FACILITY/LOCATION', 'TRAIN TRACKS',
'REDLINE SUBWAY TUNNEL', 'TUNNEL', 'CAR WASH', 'WEBSITE',
'OTHER RR TRAIN (UNION PAC, SANTE FE ETC', 'CYBERSPACE',
'PET STORE', 'RECYCLING CENTER',
'DISCOUNT STORE (99 CENT,DOLLAR,ETC.',
"DIY CENTER (LOWE'S,HOME DEPOT,OSH,CONTRACTORS WAREHOUSE)",
'NURSERY/FLOWER SHOP', 'COMPUTER SERVICES/REPAIRS/SALES',
'ORANGE LINE PARKING LOT', 'OTHER INTERSTATE, CHARTER BUS',
'SKATING RINK*', 'ABATEMENT LOCATION', 'DAM/RESERVOIR',
'ENERGY PLANT/FACILITY', 'TRASH CAN/TRASH DUMPSTER',
'TRAM/STREETCAR(BOXLIKE WAG ON RAILS)*', 'HOSPICE',
'CULTURAL SIGNIFICANCE/MONUMENT', 'WATER FACILITY', 'ESCALATOR*',
'MISSIONS/SHELTERS', 'CATERING/ICE CREAM TRUCK',
'REDLINE (SUBWAY TRAIN)', 'METHADONE CLINIC',
'DETENTION/JAIL FACILITY', 'VALET',
'GREEN LINE (I-105 FWY LEVEL TRAIN)',
"COFFEE SHOP (STARBUCKS, COFFEE BEAN, PEET'S, ETC.)",
'HOCKEY RINK/ICE HOCKEY', 'REDLINE SUBWAY MEZZANINE',
'APARTMENT/CONDO COMMON LAUNDRY ROOM',
'AUTO DEALERSHIP (CHEVY, FORD, BMW, MERCEDES, ETC.)', 'MORTUARY',
'ELECTRONICS STORE (IE:RADIO SHACK, ETC.)', 'MUSEUM',
'FURNITURE STORE', "SINGLE RESIDENCE OCCUPANCY (SRO'S) LOCATIONS",
'VETERINARIAN/ANIMAL HOSPITAL', 'TACTICAL SIGNIFICANCE',
'BOOK STORE', 'MTA - GREEN LINE - AVIATION/LAX',
'BANK DROP BOX/MONEY DROP-OUTSIDE OF BANK*',
'MTA - ORANGE LINE - WOODLEY',
'MTA - RED LINE - 7TH AND METRO CENTER',
'TRANSITIONAL HOUSING/HALFWAY HOUSE',
"VEHICLE STORAGE LOT (CARS, TRUCKS, RV'S, BOATS, TRAILERS, ETC.)",
'NUCLEAR FACILITY', 'STUDIO (FILM/PHOTOGRAPHIC/MUSIC)',
'DEPT OF DEFENSE FACILITY', 'TRANSIENT ENCAMPMENT',
'MTA - RED LINE - UNION STATION', 'THE GROVE',
'THE BEVERLY CENTER', 'THE BEVERLY CONNECTION',
'MTA - RED LINE - HOLLYWOOD/VINE',
'MTA - RED LINE - WESTLAKE/MACARTHUR PARK',
'MTA - GREEN LINE - HARBOR FWY', 'SEWAGE FACILITY/PIPE',
'MTA - RED LINE - PERSHING SQUARE',
'MTA - RED LINE - VERMONT/BEVERLY',
'LA UNION STATION (NOT LINE SPECIFIC)',
'MTA - RED LINE - VERMONT/SANTA MONICA',
'MTA - RED LINE - NORTH HOLLYWOOD', 'MTA - BLUE LINE - WASHINGTON',
'MTA - EXPO LINE - PICO', 'MTA - EXPO LINE - EXPO/WESTERN',
'7TH AND METRO CENTER (NOT LINE SPECIFIC)',
'MTA - BLUE LINE - 7TH AND METRO CENTER',
'MTA - RED LINE - VERMONT/SUNSET',
'MTA - SILVER LINE - HARBOR GATEWAY TRANSIT CTR',
'MTA - EXPO LINE - EXPO/CRENSHAW',
'MTA - EXPO LINE - EXPO/VERMONT',
'MTA - GOLD LINE - LITTLE TOKYO/ARTS DISTRICT',
'MTA - EXPO LINE - FARMDALE', 'MTA - EXPO LINE - EXPO/BUNDY',
'MTA - EXPO LINE - 7TH AND METRO CENTER',
'MTA - PURPLE LINE - CIVIC CENTER/GRAND PARK',
'MTA - GOLD LINE - HIGHLAND PARK',
'MTA - PURPLE LINE - WILSHIRE/WESTERN',
'MTA - PURPLE LINE - UNION STATION',
'MTA - GOLD LINE - UNION STATION',
'MTA - RED LINE - HOLLYWOOD/HIGHLAND',
'MTA - RED LINE - UNIVERSAL CITY/STUDIO CITY',
'MTA - SILVER LINE - UNION STATION',
'MTA - GOLD LINE - MARIACHI PLAZA',
'MTA - EXPO LINE - EXPO PARK/USC',
'MTA - RED LINE - WILSHIRE/VERMONT',
'MTA - EXPO LINE - EXPO/LA BREA',
'MTA - RED LINE - CIVIC CENTER/GRAND PARK',
'MTA - BLUE LINE - PICO', 'MTA - GOLD LINE - CHINATOWN',
'MTA - ORANGE LINE - CHATSWORTH',
'MTA - EXPO LINE - EXPO/SEPULVEDA',
'MTA - EXPO LINE - JEFFERSON/USC', 'MTA - GOLD LINE - SOTO',
'MTA - EXPO LINE - LATTC/ORTHO INSTITUTE',
'MTA - ORANGE LINE - NORTH HOLLYWOOD',
'MTA - ORANGE LINE - SEPULVEDA', 'MTA - GREEN LINE - AVALON',
'MTA - BLUE LINE - 103RD/WATTS TOWERS',
'MTA - ORANGE LINE - VAN NUYS', 'MTA - GOLD LINE - INDIANA',
'MTA - EXPO LINE - WESTWOOD/RANCHO PARK',
'MTA - EXPO LINE - LA CIENEGA/JEFFERSON',
'MTA - RED LINE - HOLLYWOOD/WESTERN', 'MTA - ORANGE LINE - RESEDA',
'MTA - ORANGE LINE - LAUREL CANYON', 'SHORT-TERM VACATION RENTAL',
'MTA - ORANGE LINE - VALLEY COLLEGE', 'MTA - ORANGE LINE - CANOGA',
'MTA - ORANGE LINE - BALBOA', 'MTA - GOLD LINE - PICO/ALISO',
'MTA - BLUE LINE - VERNON', 'MTA - EXPO LINE - PALMS',
'MTA - PURPLE LINE - PERSHING SQUARE',
'MTA - BLUE LINE - SAN PEDRO',
'MTA - PURPLE LINE - WESTLAKE/MACARTHUR PARK',
'MTA - SILVER LINE - DOWNTOWN STREET STOPS',
'MTA - ORANGE LINE - WOODMAN', 'BASKETBALL COURTS',
'MTA - GOLD LINE - HERITAGE SQ', 'SURPLUS SURVIVAL STORE',
'MTA - ORANGE LINE - WARNER CTR', 'MTA - SILVER LINE - SLAUSON',
'MTA - PURPLE LINE - WILSHIRE/VERMONT',
'MTA - PURPLE LINE - 7TH AND METRO CENTER',
'MTA - SILVER LINE - MANCHESTER', 'MTA - ORANGE LINE - TAMPA',
'MTA - ORANGE LINE - PIERCE COLLEGE',
'MTA - SILVER LINE - PACIFIC COAST HWY',
'MTA - PURPLE LINE - WILSHIRE/NORMANDIE',
'MTA - GOLD LINE - LINCOLN/CYPRESS',
'MTA - SILVER LINE - HARBOR FWY', 'MUSCLE BEACH',
'MTA - BLUE LINE - GRAND/LATTC',
'MTA - GOLD LINE - SOUTHWEST MUSEUM',
'MTA - SILVER LINE - ROSECRANS', 'MTA - ORANGE LINE - SHERMAN WAY',
'MTA - SILVER LINE - CAL STATE LA',
'HARBOR FRWY STATION (NOT LINE SPECIFIC)',
'MTA - SILVER LINE - 37TH ST/USC', 'MTA - ORANGE LINE - DE SOTO',
'HANDBALL COURTS', 'MTA - ORANGE LINE - ROSCOE',
'MTA - SILVER LINE - SAN PEDRO STREET STOPS',
'MTA - ORANGE LINE - NORDHOFF']

// Append the Premise Descriptions, but append "Select" for the first value
d3.select('#js-search')
    .selectAll('option')
    .data(data)
    .enter()
    .append('option')
    .text(function(d) {return d})

