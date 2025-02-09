import pandas as pd
from io import StringIO

csv_str = """Name,Flag,Country Code,Capital,State,Telephone Area Code,Internet Domain
Abkhazia,🇦🇹,GE,Sukhumi,Asia,995,ge
Afghanistan,🇦🇫,AF,Kabul,Asia,93,af
Akrotiri and Dhekelia (UK),,,Episkopi Cantonment,Europe,357,ax
Åland (Finland),🇦🇽,AX,Mariehamn,Europe,358,ax
Albania,🇦🇱,AL,Tirana,Europe,355,al
Algeria,🇩🇿,DZ,Algiers,Africa,213,dz
American Samoa (US),🇦🇸,AS,Pago Pago,Oceania,1,as
Andorra,🇦🇩,AD,Andorra la Vella,Europe,376,ad
Angola,🇦🇴,AO,Luanda,Africa,244,ao
Anguilla (UK),🇦🇮,AI,The Valley,North America,1,ai
Antarctica,🇦🇶,AQ,,Antarctica,672,aq
Antigua and Barbuda,🇦🇬,AG,St John's,North America,1,ag
Argentina,🇦🇷,AR,Buenos Aires,South America,54,ar
Armenia,🇦🇲,AM,Yerevan,Asia,374,am
Aruba (Netherlands),🇦🇼,AW,Oranjestad,North America,297,aw
Ashmore and Cartier Islands (Australia),🇦🇨,,,Oceania,61,ac
Australia,🇦🇺,AU,Canberra,Oceania,61,au
Austria,🇦🇹,AT,Vienna,Europe,43,at
Azerbaijan,🇦🇿,AZ,Baku,Asia,994,az
Bahamas,🇧🇸,BS,Nassau,North America,242,bs
Bahrain,🇧🇭,BH,Manama,Asia,973,bh
Bangladesh,🇧🇩,BD,Dhaka,Asia,880,bd
Barbados,🇧🇧,BB,Bridgetown,North America,1,bb
Belarus,🇧🇾,BY,Minsk,Europe,375,by
Belgium,🇧🇪,BE,Brussels,Europe,32,be
Belize,🇧🇿,BZ,Belmopan,North America,501,bz
Benin,🇧🇯,BJ,Porto-Novo,Africa,229,bj
Bermuda (UK),🇧🇲,BM,Hamilton,North America,1,bm
Bhutan,🇧🇹,BT,Thimphu,Asia,975,bt
Bir Tawil (terra nullius),,,,Africa,,
Bolivia,🇧🇴,BO,Sucre,South America,591,bo
Bonaire (Netherlands),🇧🇶,BQ,Kralendijk,North America,599,bq
Bosnia and Herzegovina,🇧🇦,BA,Sarajevo,Europe,387,ba
Botswana,🇧🇼,BW,Gaborone,Africa,267,bw
Bouvet Island (Norway),,BV,,Antarctica,47,bv
Brazil,🇧🇷,BR,Brasília,South America,55,br
British Indian Ocean Territory (UK),🇮🇴,IO,Diego Garcia,Africa,246,io
British Virgin Islands (UK),🇻🇬,VG,Road Town,North America,1,vg
Brunei,🇧🇳,BN,Bandar Seri Begawan,Asia,673,bn
Bulgaria,🇧🇬,BG,Sofia,Europe,359,bg
Burkina Faso,🇧🇫,BF,Ouagadougou,Africa,226,bf
Burundi,🇧🇮,BI,Gitega,Africa,257,bi
Cambodia,🇰🇭,KH,Phnom Penh,Asia,855,kh
Cameroon,🇨🇲,CM,Yaoundé,Africa,237,cm
Canada,🇨🇦,CA,Ottawa,North America,1,ca
Cape Verde,🇨🇻,CV,Praia,Africa,238,cv
Cayman Islands (UK),🇰🇾,KY,George Town,North America,1,ky
Central African Republic,🇨🇫,CF,Bangui,Africa,236,cf
Chad,🇹🇩,TD,N'Djamena,Africa,235,td
Chile,🇨🇱,CL,Santiago,South America,56,cl
China,🇨🇳,CN,Beijing,Asia,86,cn
Christmas Island (Australia),🇨🇽,CX,Flying Fish Cove,Oceania,61,cx
Clipperton Island (France),🇨🇵,CP,Port Jaouen,North America,262,cp
Cocos (Keeling) Islands (Australia),🇨🇨,CC,West Island,Oceania,61,cc
Colombia,🇨🇴,CO,Bogotá,South America,57,co
Comoros,🇰🇲,KM,Moroni,Africa,269,km
Cook Islands,🇨🇰,CK,Avarua,Oceania,682,ck
Coral Sea Islands (Australia),🇨🇽,,,Oceania,61,cs
Costa Rica,🇨🇷,CR,San José,North America,506,cr
Croatia,🇭🇷,HR,Zagreb,Europe,385,hr
Cuba,🇨🇺,CU,Havana,North America,53,cu
Curaçao (Netherlands),🇨🇼,CW,Willemstad,North America,599,cw
Cyprus,🇨🇾,CY,Nicosia,Europe,357,cy
Czech Republic,🇨🇿,CZ,Prague,Europe,420,cz
Democratic Republic of the Congo,🇨🇩,CD,Kinshasa,Africa,243,cd
Denmark (mainland),🇩🇰,DK,Copenhagen,Europe,45,dk
Djibouti,🇩🇯,DJ,Djibouti,Africa,253,dj
Dominica,🇩🇲,DM,Roseau,North America,1,dm
Dominican Republic,🇩🇴,DO,Santo Domingo,North America,1,do
East Timor,🇹🇱,TL,Dili,Asia,670,tl
Easter Island (Chile),,,Hanga Roa,South America,56,cl
Ecuador,🇪🇨,EC,Quito,South America,593,ec
Egypt,🇪🇬,EG,Cairo,Africa,20,eg
El Salvador,🇸🇻,SV,San Salvador,North America,503,sv
Equatorial Guinea,🇬🇶,GQ,Malabo,Africa,240,gq
Eritrea,🇪🇷,ER,Asmara,Africa,291,er
Estonia,🇪🇪,EE,Tallinn,Europe,372,ee
Eswatini,🇸🇿,SZ,Mbabane,Africa,268,sz
Ethiopia,🇪🇹,ET,Addis Ababa,Africa,251,et
Falkland Islands (UK),🇫🇰,FK,Stanley,South America,500,fk
Faroe Islands (Denmark),🇫🇴,FO,Tórshavn,Europe,298,fo
Fiji,🇫🇯,FJ,Suva,Oceania,679,fj
Finland,🇫🇮,FI,Helsinki,Europe,358,fi
France,🇫🇷,FR,Paris,Europe,33,fr
France (metropolitan),,,,Europe,33,fr
French Polynesia (France),🇵🇫,PF,Papeete,Oceania,689,pf
French Southern Territories (France),🇹🇫,TF,Port-aux-Français,Africa,262,tf
Gabon,🇬🇦,GA,Libreville,Africa,241,ga
Gambia,🇬🇲,GM,Banjul,Africa,220,gm
Georgia,🇬🇪,GE,Tbilisi,Asia,995,ge
Germany,🇩🇪,DE,Berlin,Europe,49,de
Ghana,🇬🇭,GH,Accra,Africa,233,gh
Gibraltar (UK),🇬🇮,GI,Gibraltar,Europe,350,gi
Greece,🇬🇷,GR,Athens,Europe,30,gr
Greenland (Denmark),🇬🇱,GL,Nuuk,North America,299,gl
Grenada,🇬🇩,GD,St George's,North America,1,gd
Guam (US),🇬🇺,GU,Hagåtña,Oceania,1,gu
Guatemala,🇬🇹,GT,Guatemala City,North America,502,gt
Guernsey (UK),🇬🇬,GG,St Peter Port,Europe,44,gg
Guinea,🇬🇳,GN,Conakry,Africa,224,gn
Guinea-Bissau,🇬🇼,GW,Bissau,Africa,245,gw
Guyana,🇬🇾,GY,Georgetown,South America,592,gy
Haiti,🇭🇹,HT,Port-au-Prince,North America,509,ht
Heard Island and McDonald Islands (Australia),,HM,,Antarctica,672,hm
Honduras,🇭🇳,HN,Tegucigalpa,North America,504,hn
Hong Kong (China),🇭🇰,HK,Hong Kong,Asia,852,hk
Hungary,🇭🇺,HU,Budapest,Europe,36,hu
Iceland,🇮🇸,IS,Rey,,,
India,🇮🇳,IN,New Delhi,Asia,91,in
Indonesia,🇮🇩,ID,Jakarta,Asia,62,id
Iran,🇮🇷,IR,Tehran,Asia,98,ir
Iraq,🇮🇶,IQ,Baghdad,Asia,964,iq
Ireland,🇮🇪,IE,Dublin,Europe,353,ie
Isle of Man (UK),🇮🇲,IM,Douglas,Europe,44,im
Israel,🇮🇱,IL,Jerusalem,Asia,972,il
Italy,🇮🇹,IT,Rome,Europe,39,it
Ivory Coast,🇨🇮,CI,Yamoussoukro,Africa,225,ci
Jamaica,🇯🇲,JM,Kingston,North America,1,jm
Jan Mayen (Norway),🇯🇲,,,Europe,47,sj
Japan,🇯🇵,JP,Tokyo,Asia,81,jp
Jersey (UK),🇯🇪,JE,Saint Helier,Europe,44,je
Jordan,🇯🇴,JO,Amman,Asia,962,jo
Kazakhstan,🇰🇿,KZ,Nur-Sultan,Asia,7,kz
Kenya,🇰🇪,KE,Nairobi,Africa,254,ke
Kingdom of Denmark,🇩🇰,DK,Copenhagen,Europe,45,dk
Kiribati,🇰🇮,KI,South Tarawa,Oceania,686,ki
Kosovo,🇽🇰,XK,Pristina,Europe,383,xk
Kuwait,🇰🇼,KW,Kuwait City,Asia,965,kw
Kyrgyzstan,🇰🇬,KG,Bishkek,Asia,996,kg
Laos,🇱🇦,LA,Vientiane,Asia,856,la
Latvia,🇱🇻,LV,Riga,Europe,371,lv
Lebanon,🇱🇧,LB,Beirut,Asia,961,lb
Lesotho,🇱🇸,LS,Maseru,Africa,266,ls
Liberia,🇱🇷,LR,Monrovia,Africa,231,lr
Libya,🇱🇾,LY,Tripoli,Africa,218,ly
Liechtenstein,🇱🇮,LI,Vaduz,Europe,423,li
Lithuania,🇱🇹,LT,Vilnius,Europe,370,lt
Luxembourg,🇱🇺,LU,Luxembourg,Europe,352,lu
Macau (China),🇲🇴,MO,Macau,Asia,853,mo
Madagascar,🇲🇬,MG,Antananarivo,Africa,261,mg
Malawi,🇲🇼,MW,Lilongwe,Africa,265,mw
Malaysia,🇲🇾,MY,Kuala Lumpur,Asia,60,my
Maldives,🇲🇻,MV,Malé,Asia,960,mv
Mali,🇲🇱,ML,Bamako,Africa,223,ml
Malta,🇲🇹,MT,Valletta,Europe,356,mt
Marshall Islands,🇲🇭,MH,Majuro,Oceania,692,mh
Mauritania,🇲🇷,MR,Nouakchott,Africa,222,mr
Mauritius,🇲🇺,MU,Port Louis,Africa,230,mu
Mexico,🇲🇽,MX,Mexico City,North America,52,mx
Micronesia,🇫🇲,FM,Palikir,Oceania,691,fm
Moldova,🇲🇩,MD,Chisinau,Europe,373,md
Monaco,🇲🇨,MC,Monaco,Europe,377,mc
Mongolia,🇲🇳,MN,Ulaanbaatar,Asia,976,mn
Montenegro,🇲🇪,ME,Podgorica,Europe,382,me
Montserrat (UK),🇲🇸,MS,Plymouth,North America,1,ms
Morocco,🇲🇦,MA,Rabat,Africa,212,ma
Mozambique,🇲🇿,MZ,Maputo,Africa,258,mz
Myanmar,🇲🇲,MM,Naypyidaw,Asia,95,mm
Namibia,🇳🇦,NA,Windhoek,Africa,264,na
Nauru,🇳🇷,NR,Yaren,Oceania,674,nr
Nepal,🇳🇵,NP,Kathmandu,Asia,977,np
Netherlands,🇳🇱,NL,Amsterdam,Europe,31,nl
New Caledonia (France),🇳🇨,NC,Nouméa,Oceania,687,nc
New Zealand,🇳🇿,NZ,Wellington,Oceania,64,nz
Nicaragua,🇳🇮,NI,Managua,North America,505,ni
Niger,🇳🇪,NE,Niamey,Africa,227,ne
Nigeria,🇳🇬,NG,Abuja,Africa,234,ng
Niue (New Zealand),🇳🇺,NU,Alofi,Oceania,683,nu
Norfolk Island (Australia),🇳🇫,NF,Kingston,Oceania,672,nf
North Korea,🇰🇵,KP,Pyongyang,Asia,850,kp
North Macedonia,🇲🇰,MK,Skopje,Europe,389,mk
Northern Cyprus,🇨🇾,CY,Nicosia,Europe,357,cy
Northern Mariana Islands (US),🇲🇵,MP,Saipan,Oceania,1,mp
Norway (mainland),🇳🇴,NO,Oslo,Europe,47,no
Oman,🇴🇲,OM,Muscat,Asia,968,om
Pakistan,🇵🇰,PK,Islamabad,Asia,92,pk
Palau,🇵🇼,PW,Ngerulmud,Oceania,680,pw
Palestine,🇵🇸,PS,Ramallah,Asia,970,ps
Panama,🇵🇦,PA,Panama City,North America,507,pa
Papua New Guinea,🇵🇬,PG,Port Moresby,Oceania,675,pg
Paraguay,🇵🇾,PY,Asunción,South America,595,py
Peru,🇵🇪,PE,Lima,South America,51,pe
Philippines,🇵🇭,PH,Manila,Asia,63,ph
Pitcairn Islands (UK),🇵🇳,PN,Adamstown,Oceania,64,pn
Poland,🇵🇱,PL,Warsaw,Europe,48,pl
Portugal,🇵🇹,PT,Lisbon,Europe,351,pt
Puerto Rico (US),🇵🇷,PR,San Juan,North America,1,pr
Qatar,🇶🇦,QA,Doha,Asia,974,qa
Republic of the Congo,🇨🇬,CG,Brazzaville,Africa,242,cg
Romania,🇷🇴,RO,Bucharest,Europe,40,ro
Russia,🇷🇺,RU,Moscow,Europe,7,ru
Rwanda,🇷🇼,RW,Kigali,Africa,250,rw
Saba (Netherlands),🇧🇶,BQ,The Bottom,North America,599,bq
Saint Barthélemy (France),🇧🇱,BL,Gustavia,North America,590,bl
"Saint Helena, Ascension and Tristan da Cunha (UK)",🇸🇭,SH,Jamestown,Africa,290,sh
Saint Kitts and Nevis,🇰🇳,KN,Basseterre,North America,1,kn
Saint Lucia,🇱🇨,LC,Castries,North America,1,lc
Saint Martin (France),,MF,Marigot,North America,590,mf
Saint Pierre and Miquelon (France),🇵🇲,PM,Saint-Pierre,North America,508,pm
Saint Vincent and the Grenadines,🇻🇨,VC,Kingstown,North America,1,vc
Samoa,🇼🇸,WS,Apia,Oceania,685,ws
San Marino,🇸🇲,SM,San Marino,Europe,378,sm
São Tomé and Príncipe,🇸🇹,ST,São Tomé,Africa,239,st
Saudi Arabia,🇸🇦,SA,Riyadh,Asia,966,sa
Senegal,🇸🇳,SN,Dakar,Africa,221,sn
Serbia,🇷🇸,RS,Belgrade,Europe,381,rs
Seychelles,🇸🇨,SC,Victoria,Africa,248,sc
Sierra Leone,🇸🇱,SL,Freetown,Africa,232,sl
Singapore,🇸🇬,SG,Singapore,Asia,65,sg
Sint Eustatius (Netherlands),🇧🇶,BQ,Oranjestad,North America,599,bq
Sint Maarten (Netherlands),🇸🇽,SX,Philipsburg,North America,1,sx
Slovakia,🇸🇰,SK,Bratislava,Europe,421,sk
Slovenia,🇸🇮,SI,Ljubljana,Europe,386,si
Solomon Islands,🇸🇧,SB,Honiara,Oceania,677,sb
Somalia,🇸🇴,SO,Mogadishu,Africa,252,so
Somaliland,🇸🇴,SO,Hargeisa,Africa,252,so
South Africa,🇿🇦,ZA,Pretoria,Africa,27,za
South Georgia and the South Sandwich Islands (UK),🇬🇸,GS,King Edward Point,South America,500,gs
South Korea,🇰🇷,KR,Seoul,Asia,82,kr
South Ossetia,🇬🇪,GE,Tskhinvali,Asia,995,ge
South Sudan,🇸🇸,SS,Juba,Africa,211,ss
Spain,🇪🇸,ES,Madrid,Europe,34,es
Spratly Islands (disputed),,,,Asia,,
Sri Lanka,🇱🇰,LK,Colombo,Asia,94,lk
Sudan,🇸🇩,SD,Khartoum,Africa,249,sd
Suriname,🇸🇷,SR,Paramaribo,South America,597,sr
Svalbard (Norway),,SJ,Longyearbyen,Europe,47,sj
Sweden,🇸🇪,SE,Stockholm,Europe,46,se
Switzerland,🇨🇭,CH,Bern,Europe,41,ch
Syria,🇸🇾,SY,Damascus,Asia,963,sy
Taiwan,🇹🇼,TW,Taipei,Asia,886,tw
Tajikistan,🇹🇯,TJ,Dushanbe,Asia,992,tj
Tanzania,🇹🇿,TZ,Dodoma,Africa,255,tz
Thailand,🇹🇭,TH,Bangkok,Asia,66,th
Togo,🇹🇬,TG,Lomé,Africa,228,tg
Tokelau (New Zealand),🇹🇰,TK,Nukunonu,Oceania,690,tk
Tonga,🇹🇴,TO,Nukuʻalofa,Oceania,676,to
Transnistria,🇹🇩,MD,Tiraspol,Europe,373,md
Trinidad and Tobago,🇹🇹,TT,Port of Spain,North America,1,tt
Tunisia,🇹🇳,TN,Tunis,Africa,216,tn
Turkey,🇹🇷,TR,Ankara,Asia,90,tr
Turkmenistan,🇹🇲,TM,Ashgabat,Asia,993,tm
Turks and Caicos Islands (UK),🇹🇨,TC,Cockburn Town,North America,649,tc
Tuvalu,🇹🇻,TV,Funafuti,Oceania,688,tv
Uganda,🇺🇬,UG,Kampala,Africa,256,ug
Ukraine,🇺🇦,UA,Kiev,Europe,380,ua
United Arab Emirates,🇦🇪,AE,Abu Dhabi,Asia,971,ae
United Kingdom,🇬🇧,GB,London,Europe,44,uk
United States,🇺🇸,US,Washington,North America,1,us
Uruguay,🇺🇾,UY,Montevideo,South America,598,uy
US Minor Outlying Islands (US),,UM,,North America,1,us
US Virgin Islands (US),🇻🇮,VI,Charlotte Amalie,North America,1,vi
Uzbekistan,🇺🇿,UZ,Tashkent,Asia,998,uz
Vanuatu,🇻🇺,VU,Port Vila,Oceania,678,vu
Vatican City,🇻🇦,VA,Vatican City,Europe,379,va
Venezuela,🇻🇪,VE,Caracas,South America,58,ve
Vietnam,🇻🇳,VN,Hanoi,Asia,84,vn
Wallis and Futuna (France),🇼🇫,WF,Mata-Utu,Oceania,681,wf
Western Sahara,🇪🇭,EH,El Aaiún,Africa,212,eh
Yemen,🇾🇪,YE,Sana'a,Asia,967,ye
Zambia,🇿🇲,ZM,Lusaka,Africa,260,zm
Zimbabwe,🇿🇼,ZW,Harare,Africa,263,zw"""

df = pd.read_csv(StringIO(csv_str), dtype=str, keep_default_na=False)

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


def get_regions(
    name=None,
    flag=None,
    country_code=None,
    capital=None,
    state=None,
    telephone_area_code=None,
    internet_domain=None,
):
    output = []
    for i in range(len(df)):
        if (
            (name is None or df.iloc[i]["Name"] == name)
            and (flag is None or df.iloc[i]["Flag"] == flag)
            and (country_code is None or df.iloc[i]["Country Code"] == country_code)
            and (capital is None or df.iloc[i]["Capital"] == capital)
            and (state is None or df.iloc[i]["State"] == state)
            and (
                telephone_area_code is None
                or df.iloc[i]["Telephone Area Code"] == telephone_area_code
            )
            and (
                internet_domain is None
                or df.iloc[i]["Internet Domain"] == internet_domain
            )
        ):
            output.append(Region(df.iloc[i]["Name"]))
    return output