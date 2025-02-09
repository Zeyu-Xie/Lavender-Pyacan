import pandas as pd
from io import StringIO

csv_str = """Name,Flag,Country Code,Capital,State,Telephone Area Code,Internet Domain
Russia,🇷🇺,RU,Moscow,Europe,7,ru
Antarctica,🇦🇶,AQ,,Antarctica,672,aq
Canada,🇨🇦,CA,Ottawa,North America,1,ca
China,🇨🇳,CN,Beijing,Asia,86,cn
United States,🇺🇸,US,Washington,North America,1,us
Brazil,🇧🇷,BR,Brasília,South America,55,br
Australia,🇦🇺,AU,Canberra,Oceania,61,au
India,🇮🇳,IN,New Delhi,Asia,91,in
Argentina,🇦🇷,AR,Buenos Aires,South America,54,ar
Kazakhstan,🇰🇿,KZ,Nur-Sultan,Asia,7,kz
Algeria,🇩🇿,DZ,Algiers,Africa,213,dz
Democratic Republic of the Congo,🇨🇩,CD,Kinshasa,Africa,243,cd
Kingdom of Denmark,🇩🇰,DK,Copenhagen,Europe,45,dk
Greenland (Denmark),🇬🇱,GL,Nuuk,North America,299,gl
Saudi Arabia,🇸🇦,SA,Riyadh,Asia,966,sa
Mexico,🇲🇽,MX,Mexico City,North America,52,mx
Indonesia,🇮🇩,ID,Jakarta,Asia,62,id
Sudan,🇸🇩,SD,Khartoum,Africa,249,sd
Libya,🇱🇾,LY,Tripoli,Africa,218,ly
Iran,🇮🇷,IR,Tehran,Asia,98,ir
Mongolia,🇲🇳,MN,Ulaanbaatar,Asia,976,mn
Peru,🇵🇪,PE,Lima,South America,51,pe
Chad,🇹🇩,TD,N'Djamena,Africa,235,td
Niger,🇳🇪,NE,Niamey,Africa,227,ne
Angola,🇦🇴,AO,Luanda,Africa,244,ao
Mali,🇲🇱,ML,Bamako,Africa,223,ml
South Africa,🇿🇦,ZA,Pretoria,Africa,27,za
Colombia,🇨🇴,CO,Bogotá,South America,57,co
Ethiopia,🇪🇹,ET,Addis Ababa,Africa,251,et
Bolivia,🇧🇴,BO,Sucre,South America,591,bo
Mauritania,🇲🇷,MR,Nouakchott,Africa,222,mr
Egypt,🇪🇬,EG,Cairo,Africa,20,eg
Tanzania,🇹🇿,TZ,Dodoma,Africa,255,tz
Nigeria,🇳🇬,NG,Abuja,Africa,234,ng
Venezuela,🇻🇪,VE,Caracas,South America,58,ve
Pakistan,🇵🇰,PK,Islamabad,Asia,92,pk
Namibia,🇳🇦,NA,Windhoek,Africa,264,na
Mozambique,🇲🇿,MZ,Maputo,Africa,258,mz
Turkey,🇹🇷,TR,Ankara,Asia,90,tr
Chile,🇨🇱,CL,Santiago,South America,56,cl
Zambia,🇿🇲,ZM,Lusaka,Africa,260,zm
Myanmar,🇲🇲,MM,Naypyidaw,Asia,95,mm
Afghanistan,🇦🇫,AF,Kabul,Asia,93,af
South Sudan,🇸🇸,SS,Juba,Africa,211,ss
France,🇫🇷,FR,Paris,Europe,33,fr
Somalia,🇸🇴,SO,Mogadishu,Africa,252,so
Central African Republic,🇨🇫,CF,Bangui,Africa,236,cf
Ukraine,🇺🇦,UA,Kiev,Europe,380,ua
Madagascar,🇲🇬,MG,Antananarivo,Africa,261,mg
Botswana,🇧🇼,BW,Gaborone,Africa,267,bw
Kenya,🇰🇪,KE,Nairobi,Africa,254,ke
France (metropolitan),,,,Europe,33,fr
Thailand,🇹🇭,TH,Bangkok,Asia,66,th
Spain,🇪🇸,ES,Madrid,Europe,34,es
Turkmenistan,🇹🇲,TM,Ashgabat,Asia,993,tm
Cameroon,🇨🇲,CM,Yaoundé,Africa,237,cm
Papua New Guinea,🇵🇬,PG,Port Moresby,Oceania,675,pg
Yemen,🇾🇪,YE,Sana'a,Asia,967,ye
Sweden,🇸🇪,SE,Stockholm,Europe,46,se
Uzbekistan,🇺🇿,UZ,Tashkent,Asia,998,uz
Morocco,🇲🇦,MA,Rabat,Africa,212,ma
Iraq,🇮🇶,IQ,Baghdad,Asia,964,iq
Paraguay,🇵🇾,PY,Asunción,South America,595,py
Zimbabwe,🇿🇼,ZW,Harare,Africa,263,zw
Norway (mainland),🇳🇴,NO,Oslo,Europe,47,no
Japan,🇯🇵,JP,Tokyo,Asia,81,jp
Germany,🇩🇪,DE,Berlin,Europe,49,de
Republic of the Congo,🇨🇬,CG,Brazzaville,Africa,242,cg
Finland,🇫🇮,FI,Helsinki,Europe,358,fi
Vietnam,🇻🇳,VN,Hanoi,Asia,84,vn
Malaysia,🇲🇾,MY,Kuala Lumpur,Asia,60,my
Ivory Coast,🇨🇮,CI,Yamoussoukro,Africa,225,ci
Poland,🇵🇱,PL,Warsaw,Europe,48,pl
Oman,🇴🇲,OM,Muscat,Asia,968,om
Italy,🇮🇹,IT,Rome,Europe,39,it
Philippines,🇵🇭,PH,Manila,Asia,63,ph
Ecuador,🇪🇨,EC,Quito,South America,593,ec
Burkina Faso,🇧🇫,BF,Ouagadougou,Africa,226,bf
New Zealand,🇳🇿,NZ,Wellington,Oceania,64,nz
Gabon,🇬🇦,GA,Libreville,Africa,241,ga
Western Sahara,🇪🇭,EH,El Aaiún,Africa,212,eh
Guinea,🇬🇳,GN,Conakry,Africa,224,gn
United Kingdom,🇬🇧,GB,London,Europe,44,uk
Uganda,🇺🇬,UG,Kampala,Africa,256,ug
Ghana,🇬🇭,GH,Accra,Africa,233,gh
Romania,🇷🇴,RO,Bucharest,Europe,40,ro
Laos,🇱🇦,LA,Vientiane,Asia,856,la
Guyana,🇬🇾,GY,Georgetown,South America,592,gy
Belarus,🇧🇾,BY,Minsk,Europe,375,by
Kyrgyzstan,🇰🇬,KG,Bishkek,Asia,996,kg
Senegal,🇸🇳,SN,Dakar,Africa,221,sn
Syria,🇸🇾,SY,Damascus,Asia,963,sy
Cambodia,🇰🇭,KH,Phnom Penh,Asia,855,kh
Somaliland,🇸🇴,SO,Hargeisa,Africa,252,so
Uruguay,🇺🇾,UY,Montevideo,South America,598,uy
Suriname,🇸🇷,SR,Paramaribo,South America,597,sr
Tunisia,🇹🇳,TN,Tunis,Africa,216,tn
Bangladesh,🇧🇩,BD,Dhaka,Asia,880,bd
Nepal,🇳🇵,NP,Kathmandu,Asia,977,np
Tajikistan,🇹🇯,TJ,Dushanbe,Asia,992,tj
Greece,🇬🇷,GR,Athens,Europe,30,gr
Nicaragua,🇳🇮,NI,Managua,North America,505,ni
North Korea,🇰🇵,KP,Pyongyang,Asia,850,kp
Malawi,🇲🇼,MW,Lilongwe,Africa,265,mw
Eritrea,🇪🇷,ER,Asmara,Africa,291,er
Benin,🇧🇯,BJ,Porto-Novo,Africa,229,bj
Honduras,🇭🇳,HN,Tegucigalpa,North America,504,hn
Liberia,🇱🇷,LR,Monrovia,Africa,231,lr
Bulgaria,🇧🇬,BG,Sofia,Europe,359,bg
Cuba,🇨🇺,CU,Havana,North America,53,cu
Guatemala,🇬🇹,GT,Guatemala City,North America,502,gt
Iceland,🇮🇸,IS,Rey,,,
South Korea,🇰🇷,KR,Seoul,Asia,82,kr
Hungary,🇭🇺,HU,Budapest,Europe,36,hu
Portugal,🇵🇹,PT,Lisbon,Europe,351,pt
Jordan,🇯🇴,JO,Amman,Asia,962,jo
Serbia,🇷🇸,RS,Belgrade,Europe,381,rs
Azerbaijan,🇦🇿,AZ,Baku,Asia,994,az
Austria,🇦🇹,AT,Vienna,Europe,43,at
United Arab Emirates,🇦🇪,AE,Abu Dhabi,Asia,971,ae
Czech Republic,🇨🇿,CZ,Prague,Europe,420,cz
Panama,🇵🇦,PA,Panama City,North America,507,pa
Sierra Leone,🇸🇱,SL,Freetown,Africa,232,sl
Ireland,🇮🇪,IE,Dublin,Europe,353,ie
Georgia,🇬🇪,GE,Tbilisi,Asia,995,ge
Sri Lanka,🇱🇰,LK,Colombo,Asia,94,lk
Lithuania,🇱🇹,LT,Vilnius,Europe,370,lt
Latvia,🇱🇻,LV,Riga,Europe,371,lv
Svalbard (Norway),,SJ,Longyearbyen,Europe,47,sj
Togo,🇹🇬,TG,Lomé,Africa,228,tg
Croatia,🇭🇷,HR,Zagreb,Europe,385,hr
Bosnia and Herzegovina,🇧🇦,BA,Sarajevo,Europe,387,ba
Costa Rica,🇨🇷,CR,San José,North America,506,cr
Slovakia,🇸🇰,SK,Bratislava,Europe,421,sk
Dominican Republic,🇩🇴,DO,Santo Domingo,North America,1,do
Estonia,🇪🇪,EE,Tallinn,Europe,372,ee
Denmark (mainland),🇩🇰,DK,Copenhagen,Europe,45,dk
Netherlands,🇳🇱,NL,Amsterdam,Europe,31,nl
Switzerland,🇨🇭,CH,Bern,Europe,41,ch
Bhutan,🇧🇹,BT,Thimphu,Asia,975,bt
Guinea-Bissau,🇬🇼,GW,Bissau,Africa,245,gw
Taiwan,🇹🇼,TW,Taipei,Asia,886,tw
Moldova,🇲🇩,MD,Chisinau,Europe,373,md
Belgium,🇧🇪,BE,Brussels,Europe,32,be
Lesotho,🇱🇸,LS,Maseru,Africa,266,ls
Armenia,🇦🇲,AM,Yerevan,Asia,374,am
Solomon Islands,🇸🇧,SB,Honiara,Oceania,677,sb
Albania,🇦🇱,AL,Tirana,Europe,355,al
Equatorial Guinea,🇬🇶,GQ,Malabo,Africa,240,gq
Burundi,🇧🇮,BI,Gitega,Africa,257,bi
Haiti,🇭🇹,HT,Port-au-Prince,North America,509,ht
Rwanda,🇷🇼,RW,Kigali,Africa,250,rw
North Macedonia,🇲🇰,MK,Skopje,Europe,389,mk
Djibouti,🇩🇯,DJ,Djibouti,Africa,253,dj
Belize,🇧🇿,BZ,Belmopan,North America,501,bz
Israel,🇮🇱,IL,Jerusalem,Asia,972,il
El Salvador,🇸🇻,SV,San Salvador,North America,503,sv
Slovenia,🇸🇮,SI,Ljubljana,Europe,386,si
New Caledonia (France),🇳🇨,NC,Nouméa,Oceania,687,nc
Fiji,🇫🇯,FJ,Suva,Oceania,679,fj
Kuwait,🇰🇼,KW,Kuwait City,Asia,965,kw
Eswatini,🇸🇿,SZ,Mbabane,Africa,268,sz
East Timor,🇹🇱,TL,Dili,Asia,670,tl
Bahamas,🇧🇸,BS,Nassau,North America,242,bs
Montenegro,🇲🇪,ME,Podgorica,Europe,382,me
Vanuatu,🇻🇺,VU,Port Vila,Oceania,678,vu
Falkland Islands (UK),🇫🇰,FK,Stanley,South America,500,fk
Qatar,🇶🇦,QA,Doha,Asia,974,qa
Gambia,🇬🇲,GM,Banjul,Africa,220,gm
Jamaica,🇯🇲,JM,Kingston,North America,1,jm
Kosovo,🇽🇰,XK,Pristina,Europe,383,xk
Lebanon,🇱🇧,LB,Beirut,Asia,961,lb
Cyprus,🇨🇾,CY,Nicosia,Europe,357,cy
Puerto Rico (US),🇵🇷,PR,San Juan,North America,1,pr
Abkhazia,🇦🇹,GE,Sukhumi,Asia,995,ge
French Southern Territories (France),🇹🇫,TF,Port-aux-Français,Africa,262,tf
Palestine,🇵🇸,PS,Ramallah,Asia,970,ps
Brunei,🇧🇳,BN,Bandar Seri Begawan,Asia,673,bn
Trinidad and Tobago,🇹🇹,TT,Port of Spain,North America,1,tt
French Polynesia (France),🇵🇫,PF,Papeete,Oceania,689,pf
Transnistria,🇹🇩,MD,Tiraspol,Europe,373,md
Cape Verde,🇨🇻,CV,Praia,Africa,238,cv
South Georgia and the South Sandwich Islands (UK),🇬🇸,GS,King Edward Point,South America,500,gs
South Ossetia,🇬🇪,GE,Tskhinvali,Asia,995,ge
Northern Cyprus,🇨🇾,CY,Nicosia,Europe,357,cy
Samoa,🇼🇸,WS,Apia,Oceania,685,ws
Luxembourg,🇱🇺,LU,Luxembourg,Europe,352,lu
Bir Tawil (terra nullius),,,,Africa,,
Mauritius,🇲🇺,MU,Port Louis,Africa,230,mu
Comoros,🇰🇲,KM,Moroni,Africa,269,km
Åland (Finland),🇦🇽,AX,Mariehamn,Europe,358,ax
Faroe Islands (Denmark),🇫🇴,FO,Tórshavn,Europe,298,fo
Hong Kong (China),🇭🇰,HK,Hong Kong,Asia,852,hk
São Tomé and Príncipe,🇸🇹,ST,São Tomé,Africa,239,st
Turks and Caicos Islands (UK),🇹🇨,TC,Cockburn Town,North America,649,tc
Kiribati,🇰🇮,KI,South Tarawa,Oceania,686,ki
Bahrain,🇧🇭,BH,Manama,Asia,973,bh
Dominica,🇩🇲,DM,Roseau,North America,1,dm
Tonga,🇹🇴,TO,Nukuʻalofa,Oceania,676,to
Singapore,🇸🇬,SG,Singapore,Asia,65,sg
Micronesia,🇫🇲,FM,Palikir,Oceania,691,fm
Saint Lucia,🇱🇨,LC,Castries,North America,1,lc
Isle of Man (UK),🇮🇲,IM,Douglas,Europe,44,im
Guam (US),🇬🇺,GU,Hagåtña,Oceania,1,gu
Andorra,🇦🇩,AD,Andorra la Vella,Europe,376,ad
Palau,🇵🇼,PW,Ngerulmud,Oceania,680,pw
Northern Mariana Islands (US),🇲🇵,MP,Saipan,Oceania,1,mp
Seychelles,🇸🇨,SC,Victoria,Africa,248,sc
Curaçao (Netherlands),🇨🇼,CW,Willemstad,North America,599,cw
Antigua and Barbuda,🇦🇬,AG,St John's,North America,1,ag
Barbados,🇧🇧,BB,Bridgetown,North America,1,bb
Heard Island and McDonald Islands (Australia),,HM,,Antarctica,672,hm
"Saint Helena, Ascension and Tristan da Cunha (UK)",🇸🇭,SH,Jamestown,Africa,290,sh
Saint Vincent and the Grenadines,🇻🇨,VC,Kingstown,North America,1,vc
Jan Mayen (Norway),🇯🇲,,,Europe,47,sj
US Virgin Islands (US),🇻🇮,VI,Charlotte Amalie,North America,1,vi
Grenada,🇬🇩,GD,St George's,North America,1,gd
Malta,🇲🇹,MT,Valletta,Europe,356,mt
Maldives,🇲🇻,MV,Malé,Asia,960,mv
Bonaire (Netherlands),🇧🇶,BQ,Kralendijk,North America,599,bq
Cayman Islands (UK),🇰🇾,KY,George Town,North America,1,ky
Saint Kitts and Nevis,🇰🇳,KN,Basseterre,North America,1,kn
Niue (New Zealand),🇳🇺,NU,Alofi,Oceania,683,nu
Akrotiri and Dhekelia (UK),,,Episkopi Cantonment,Europe,357,ax
Saint Pierre and Miquelon (France),🇵🇲,PM,Saint-Pierre,North America,508,pm
Cook Islands,🇨🇰,CK,Avarua,Oceania,682,ck
American Samoa (US),🇦🇸,AS,Pago Pago,Oceania,1,as
Marshall Islands,🇲🇭,MH,Majuro,Oceania,692,mh
Aruba (Netherlands),🇦🇼,AW,Oranjestad,North America,297,aw
Easter Island (Chile),,,Hanga Roa,South America,56,cl
Liechtenstein,🇱🇮,LI,Vaduz,Europe,423,li
British Virgin Islands (UK),🇻🇬,VG,Road Town,North America,1,vg
Wallis and Futuna (France),🇼🇫,WF,Mata-Utu,Oceania,681,wf
Christmas Island (Australia),🇨🇽,CX,Flying Fish Cove,Oceania,61,cx
Jersey (UK),🇯🇪,JE,Saint Helier,Europe,44,je
Montserrat (UK),🇲🇸,MS,Plymouth,North America,1,ms
Anguilla (UK),🇦🇮,AI,The Valley,North America,1,ai
Guernsey (UK),🇬🇬,GG,St Peter Port,Europe,44,gg
San Marino,🇸🇲,SM,San Marino,Europe,378,sm
British Indian Ocean Territory (UK),🇮🇴,IO,Diego Garcia,Africa,246,io
Bermuda (UK),🇧🇲,BM,Hamilton,North America,1,bm
Saint Martin (France),,MF,Marigot,North America,590,mf
Bouvet Island (Norway),,BV,,Antarctica,47,bv
Pitcairn Islands (UK),🇵🇳,PN,Adamstown,Oceania,64,pn
Norfolk Island (Australia),🇳🇫,NF,Kingston,Oceania,672,nf
Sint Maarten (Netherlands),🇸🇽,SX,Philipsburg,North America,1,sx
US Minor Outlying Islands (US),,UM,,North America,1,us
Macau (China),🇲🇴,MO,Macau,Asia,853,mo
Tuvalu,🇹🇻,TV,Funafuti,Oceania,688,tv
Saint Barthélemy (France),🇧🇱,BL,Gustavia,North America,590,bl
Nauru,🇳🇷,NR,Yaren,Oceania,674,nr
Sint Eustatius (Netherlands),🇧🇶,BQ,Oranjestad,North America,599,bq
Cocos (Keeling) Islands (Australia),🇨🇨,CC,West Island,Oceania,61,cc
Saba (Netherlands),🇧🇶,BQ,The Bottom,North America,599,bq
Tokelau (New Zealand),🇹🇰,TK,Nukunonu,Oceania,690,tk
Gibraltar (UK),🇬🇮,GI,Gibraltar,Europe,350,gi
Clipperton Island (France),🇨🇵,CP,Port Jaouen,North America,262,cp
Ashmore and Cartier Islands (Australia),🇦🇨,,,Oceania,61,ac
Coral Sea Islands (Australia),🇨🇽,,,Oceania,61,cs
Spratly Islands (disputed),,,,Asia,,
Monaco,🇲🇨,MC,Monaco,Europe,377,mc
Vatican City,🇻🇦,VA,Vatican City,Europe,379,va"""

df = pd.read_csv(StringIO(csv_str), dtype={"Telephone Area Code": str})


class Region:
    def __init__(self, name):
        index_list = df[df["Name"] == name].index
        if len(index_list) == 0:
            raise ValueError(f"No region found with name '{name}'")
        self.index = index_list[0]
        self.name = name
        self.flag = df.iloc[self.index]["Flag"]
        self.country_code = df.iloc[self.index]["Country Code"]
        self.capital = df.iloc[self.index]["Capital"]
        self.state = df.iloc[self.index]["State"]
        self.telephone_area_code = df.iloc[self.index]["Telephone Area Code"]
        self.internet_domain = df.iloc[self.index]["Internet Domain"]

    def __str__(self):
        str = f"""Name: {self.name}
Flag: {self.flag}
Country Code: {self.country_code}
Capital: {self.capital}
State: {self.state}
Telephone Area Code: {self.telephone_area_code}
Internet Domain: {self.internet_domain}"""
        return str
