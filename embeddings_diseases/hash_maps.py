

# Hash map to connect sponsor to ticker symbol

sponsor_to_ticker = {
    'Janssen, LP' : 'JNJ', # Owned by JNJ
    'Novartis' : 'NVS',
    'Wave Life Sciences Ltd.' : 'WVE',
    'Restorbio Inc.' : 'TORC', # delisted
    'GEIGY Pharmaceuticals' : 'NVS', # Owned by Novartis
    'Vical' : 'VICL', 
    'Vertex Pharmaceuticals Incorporated': 'VRTX',
    'Biogen': 'BIIB',
    'PharmaMar' : 'PHM',
    'Eisai Inc.':'4523.T',
    'Eli Lilly and Company': 'LLY',
    'Merck Sharp & Dohme LLC' : 'MRK',
    'NeurogesX': 'NGSX', # delisted
    'Johnson & Johnson Pharmaceutical Research & Development, L.L.C.' : 'JNJ',
    'Pfizer': 'PFE',
    'Bristol-Myers Squibb': 'BMY',
    'Gilead Sciences': 'GILD',
    'Amgen':'AMGN',
    'Abbott' : 'ABT',
    'Wyeth is now a wholly owned subsidiary of Pfizer' : 'PFE',
    'Cephalon': 'CEPH', # delisted 2005
    'Mallinckrodt':'MNKKQ',
    'Procter and Gamble' : 'PG',
    'QLT Inc.': 'QLTI-Q',
    'Tularik': 'AMGN', # Acquired by Amgen in 2004, check dates of trials though
    'GlaxoSmithKline': 'GSK',
    'Sumitomo Pharma America, Inc.': '4506.T', 
    'Introgen Therapeutics': 'INGN', # delisted 2008-2009
    'Otsuka Pharmaceutical Development & Commercialization, Inc.': '4578',
    'Sanofi': 'SNY',
    'Ono Pharma USA Inc': '4528.T',
    'InterMune': 'ITMN', # delisted 
    'Genentech, Inc.': 'ROG', # acquired in 2009, check dates
    'Nitromed': 'NTMD', # delisted 2009
    'Hoffmann-La Roche': 'ROG',
    'Millennium Pharmaceuticals, Inc.': 'MLNM', # bought by Takeda, check date
    'McNeil Consumer & Specialty Pharmaceuticals, a Division of McNeil-PPC, Inc.': 'JNJ', # JNJ subsidiary
    'AstraZeneca': 'AZN',
    'Novacea':'NOVC',
    'Celgene Corporation': 'CELG', # Acquired by BMS in 2019, check dates
    'Celgene': 'CELG', # Acquired by BMS in 2019, check dates
    'CTI BioPharma' : 'CTIC', # possibly delisted 
    'United Therapeutics': 'UTHR',
    'Teva Branded Pharmaceutical Products R&D, Inc.': 'TEVA',
    'Kos Pharmaceuticals' : 'KOSP', # Acquired by Abbott in 2005, check dates
    'Jazz Pharmaceuticals': 'JAZZ',
    'Agennix': 'AGX.DE',
    'Organon and Co': 'OGN',
    'Genzyme, a Sanofi Company': 'SNY',
    'Actelion': 'ATLN', # acquired by JNJ 2017, check dates
    'Human Genome Sciences Inc.': 'HGSI', # Acquired by GSK in 2012, check dates
    'Warner Chilcott': 'WCRX',
    'Titan Pharmaceuticals': 'TTNP',
    'Novartis Pharmaceuticals': 'NVS',
    'Voyager Pharmaceutical Corporation': 'VYGR',
    'INSYS Therapeutics Inc': 'INSYQ',
    'Shionogi': '4507.T', # On the Japanese exchange
    'Bayer': 'BAYN',
    'Shire': 'SHPG', # acquired by Takeda in 2019
    'AbbVie (prior sponsor, Abbott)': 'ABBV',
    'Spectrum Pharmaceuticals, Inc': 'SPPI',
    'Conatus Pharmaceuticals Inc.': 'CNAT',
    'Telik': 'TELK', # delisted 2014
    'Synvista Therapeutics, Inc': 'SYNI',
    'La Jolla Pharmaceutical Company': 'LJPC',
    'Scios, Inc.': 'SCIO', # Acquired by JNJ 2003
    'EMD Serono': 'MRK.DE',
    'The Medicines Company': 'MDCO', # possibly acquired
    'Threshold Pharmaceuticals': 'THLD',
    'Forest Laboratories': 'FRX-OLD', # defunct since 2020
    'BioCryst Pharmaceuticals': 'BCRX',
    'Advancis Pharmaceutical Corporation': 'MBRK',
    'Chiron Corporation': 'CHIR-OLD', # defunct since 2005
    'Sumitomo Pharma Co., Ltd.': '4506.T', # On the japanese exchange
    'Swedish Orphan Biovitrum': 'SOBI.ST', # Swedish exchange
    'Cubist Pharmaceuticals LLC, a subsidiary of Merck & Co., Inc. (Rahway, New Jersey USA)': 'MRK', 
    'Janssen Research & Development, LLC': 'JNJ',
    'UCB Pharma': 'UCB.BR',
    'Myrexis Inc.': 'MYRX',
    'Astellas Pharma Inc': '4503.T', # On Japanese exchange
    'Novo Nordisk A/S': 'NVO',
    'Affymax': 'AFFY',
    'Galectin Therapeutics Inc.': 'GALT',
    'Vion Pharmaceuticals': 'VION', # delisted 2008
    'Astex Pharmaceuticals, Inc.': 'ASTX', # delisted
    'Syntara': 'SNT.AX', # Australian exchange
    'Cytogen Corporation': '217330.KQ',
    'Pharmacyclics LLC.': 'PCYC', # delisted, purchased by AbbVie in 2017, check date
    'Orion Corporation, Orion Pharma': 'ORNBV.HE',
    'Emmaus Medical, Inc.': 'EMMA',
    'Acorda Therapeutics': 'ACOR',
    'Corcept Therapeutics': 'CORT',
    'GTx': 'ONCT', 
    'SGX Pharmaceuticals, Inc.': 'SGXP',
    'Keryx Biopharmaceuticals': 'KERX',
    "Pfizer's Upjohn has merged with Mylan to form Viatris Inc.": 'VTRS',
    'Synta Pharmaceuticals Corp.': 'SNTA',
    'Neurobiological Technologies': 'NTII',
    'Ligand Pharmaceuticals' : 'LGND',
    'Daiichi Sankyo Co., Ltd.': '4568.T',
    'Solvay Pharmaceuticals': 'SOLB.BR',
    'Daiichi Sankyo': '4568.T',
    'Teva takeda': 'TEVA', # TEVA owns 51%, takeda the rest
    'Chugai Pharmaceutical': '4519.T',
    'Merck KGaA, Darmstadt, Germany': 'MRK.DE',
    'UCB Pharma SA': 'UCB.BR',
    'Sankyo Pharma Gmbh': '4568.T',
    'Taiho Pharmaceutical Co., Ltd.': '4578.T', # Subsidiary of otsuka holdings
    'Miravant Pharmaceuticals': 'MRVT',
    'UCB Japan Co. Ltd.': 'UCB.BR',
    'Bausch Health Americas, Inc.': 'BHC',
    'Eisai Limited': '4523.T',
    'Eisai Co., Ltd.': '4523.T',
    'Eisai Korea Inc.': '4523.T',
    'Allergan': 'AGN', # later acquired by AbbVie
    'Kyowa Kirin, Inc.': '4151.T',
    'Kyowa Kirin Co., Ltd.': '4151.T',
    'Mitsubishi Tanabe Pharma Corporation': '4188.T',
    'Teva Neuroscience, Inc.': 'TEVA',
    'Brooklyn ImmunoTherapeutics, LLC': 'ERNA', # changed name to eterna, NASDAQ:ERNA. Used to be BTX, so need to check
    'Janssen-Ortho LLC': 'JNJ',
    'Ortho-McNeil Pharmaceutical': 'JNJ', # owned by JNJ
    'Exelixis': 'EXEL',
    'Janssen-Cilag International NV': 'JNJ',
    'Janssen-Cilag S.p.A.': 'JNJ',
    'Janssen Korea, Ltd., Korea': 'JNJ',
    'Janssen Pharmaceutica N.V., Belgium': 'JNJ',
    'Grifols Therapeutics LLC': 'GRFS',
    'TTY Biopharm': 'TTY.TWO',
    'Endo Pharmaceuticals': 'ENDP',
    'Cadence Pharmaceuticals': 'CADX',
    'Clavis Pharma': 'CLAVIS.OL', # I think, could also be CPHAF
    'Otsuka Pharmaceutical Co., Ltd.': '4578.T',
    'Ipsen': 'IPN.PA',
    'Mast Therapeutics, Inc.': 'MSTX', # merged with Savara NASDAQ:SVRA, check dates
    'PTC Therapeutics': 'PTCT',
    'Symbollon Pharmaceuticals': 'SYMBA',
    'Point Therapeutics': 'TPNT', # need to double check
    'Janssen-Ortho Inc., Canada': 'JNJ',
    'Sunesis Pharmaceuticals': 'SNSS',
    'Achieve Life Sciences': 'ACHV',
    'Vanda Pharmaceuticals': 'VNDA',
    'Innovive Pharmaceuticals': 'INVA',
    'Puma Biotechnology, Inc.': 'PBYI',
    # 'Progen Pharmaceuticals': '296160.KRX', # Hard to find info however
    'Aurinia Pharmaceuticals Inc.': 'AUPH',
    'Korea Otsuka Pharmaceutical Co., Ltd.': '4578.T',
    'Indivior Inc.': 'INDV',
    'Teva GTC': 'TEVA',
    'BioDelivery Sciences International': 'BDSI',
    # 'Icagen': 'ICGN', # acquired by Pfizer, check dates
    'OSI Pharmaceuticals': 'OSIP', # bought by Astellas (4503.T) in 2010, check dates
    'Janssen-Cilag Pty Ltd': 'JNJ',
    "Y's Therapeutics, Inc.": 'YMAB',
    'Zeria Pharmaceutical': '4559.T',
    'XenoPort, Inc.': 'LMW.DE',
    'Alcon Research': 'ALC',
    'GlobeImmune': 'GBIM',
    'ArQule, Inc., a subsidiary of Merck Sharp & Dohme LLC, a subsidiary of Merck & Co., Inc. (Rahway, NJ USA)': 'MRK',
    'Immtech Pharmaceuticals, Inc': 'IMM',
    'Amicus Therapeutics': 'FOLD',
    'CASI Pharmaceuticals, Inc.': 'CASI',
    'Endocyte': 'ECYT',
    'Mannkind Corporation': 'MNKD',
    'Janssen Cilag S.A.S.': 'JNJ',
    'Optimer Pharmaceuticals LLC, a subsidiary of Merck & Co., Inc. (Rahway, New Jersey USA)': 'MRK',
    'Halozyme Therapeutics': 'HALO',
    'Taro Pharmaceuticals USA': 'TARO',
    'Ocera Therapeutics': 'OCRX', # delisted 2017
    'Repligen Corporation': 'RGEN', 
    'CTI-1, LLC': 'CTIC',
    'Mirati Therapeutics Inc.': 'MRTX', # not on yf
    'Delcath Systems Inc.': 'DCTH',
    'Boryung Pharmaceutical Co., Ltd': '003850.KS',
    'Nycomed': '4502.T', # Acquired in 2011, check dates
    'Rigel Pharmaceuticals': 'RIGL',
    'Teva Pharmaceutical Industries, Ltd.': 'TEVA',
    'NovaCardia, Inc., a subsidiary of Merck & Co., Inc. (Rahway, New Jersey USA)': 'MRK',
    'BioWest Therapeutics Inc': 'CHQ.TSX', # delisted
    'Genaera Corporation': 'GENR', # delisted in 2009
    'NewLink Genetics Corporation': 'NLNK', # not on yf
    'New River Pharmaceuticals': 'NRPH', # not on yf
    'Heron Therapeutics': 'HRTX',
    'Alimera Sciences': 'ALIM',
    'Cellectar Biosciences, Inc.': 'CLRB',
    'Can-Fite BioPharma': 'CANF',
    'Xian-Janssen Pharmaceutical Ltd.': 'JNJ',
    'Validus Pharmaceuticals': 'VR', # delisted 2018, try to get data
    'Bukwang Pharmaceutical': '003000.KS',
    'Prescient Therapeutics, Ltd.': 'PTX',
    'Ono Pharmaceutical Co. Ltd': '4528.T',
    'POZEN': 'POZN',
    'Baxter Healthcare Corporation': 'BAX',
    'Alexza Pharmaceuticals, Inc.': 'ALXA',
    'Bausch & Lomb Incorporated': 'BLCO',
    'Cyclacel Pharmaceuticals, Inc.': 'CYCC',
    'QuatRx Pharmaceuticals Company': 'QTRX', # delisted
    'MediGene': 'MDG1',
    'Janssen Cilag N.V./S.A.': 'JNJ',
    'Tibotec, Inc': 'JNJ',
    'Bankole Johnson': 'ADIL', # double check
    'MEI Pharma, Inc.': 'MEIP',
    'SymBio Pharmaceuticals': '4582.T',
    'ZymoGenetics': 'ZGEN', # acquired by BMS around 2010 I think
    'ARYx Therapeutics': 'ARYX',
    'SkyePharma AG': 'SKP', # delisted, acquired by Vectura VEC.L
    'Otsuka Pharmaceutical, Inc., Philippines': '4578.T',
    'NeuroSearch A/S': 'NRSA.SG',
    'Schering-Plough': 'SGP', # merged with MRK 2009
    'Janssen Pharmaceutical K.K.': 'JNJ',
    'AEterna Zentaris': 'AEZS',
    'Taiho Oncology, Inc.': '4578.T', # owned by Otsuka
    'Galderma R&D': 'GALD.SW',
    'Genmab': 'GMAB',
    'Ironwood Pharmaceuticals, Inc.': 'IRWD',
    'BioMarin Pharmaceutical': 'BMRN',
    # 'Genta Incorporated': 'GNTA', # delisted, now GNTA is Genenta
    'Valerio Therapeutics': 'ALVIO',
    'Transgene': 'TNG',
    'Cascadian Therapeutics Inc.': 'CASC', # probs delisted
    'Faes Farma, S.A.': 'FAE.MC',
    'Adherex Technologies, Inc.': 'FENC',
    'Alaunos Therapeutics': 'TCRT',
    'Handok Inc.':'002390.KS',
    'Infinity Pharmaceuticals, Inc.': 'INFIQ',
    'AbbVie': 'ABBV',
    'Eleison Pharmaceuticals LLC.': 'ELSN', # probs delisted, not on yf
    'Theravance Biopharma': 'TBPH',
    'Poniard Pharmaceuticals': 'PARD',
    'Anthera Pharmaceuticals': 'ANTH',
    'Horizon Pharma Ireland, Ltd., Dublin Ireland': 'HZNP', # probably delisted
    'Kadmon Corporation, LLC': 'KDMN', # acquired by Snaofi 2021, try to get data
    'Orexigen Therapeutics, Inc': 'OREX',
    'Chimerix': 'CMRX',
    'Idorsia Pharmaceuticals Ltd.': 'IDIA.SW',
    'Celldex Therapeutics': 'CLDX',
    'Ceragenix Pharmaceuticals': 'CGXP',
    'Kissei Pharmaceutical Co., Ltd.': '4547.T',
    'Array Biopharma, now a wholly owned subsidiary of Pfizer': 'PFE',
    'Marinus Pharmaceuticals': 'MRNS',
    'Transcept Pharmaceuticals': 'TSPT', # delisted not sure when
    'Enzon Pharmaceuticals, Inc.': 'ENZN',
    'Aegerion Pharmaceuticals, Inc.': 'AEGR', # delisted not sure when
    'DARA Therapeutics': 'DARA', # probably delisted
    'Advanz Pharma': 'ADVZ.TO', # delisted
    'Durect': 'DRRX',
    'Incyte Corporation': 'INCY',
    'AGC Biologics S.p.A.': '5201.T',
    'Egalet Ltd': 'EGLTQ',
    'Korea Otsuka International Asia Arab': '4578.T',
    'Impax Laboratories, LLC': 'IPXL',
    'Medivation, Inc.': 'MDVN', # acquired by PFE in 2016
    'Heidelberg Pharma AG': 'HPHA.DE',
    'OPKO Health, Inc.': 'OPK',
    'Intercept Pharmaceuticals': 'ICPT', # acquired 2023, try to find data
    'AVEO Pharmaceuticals, Inc.': 'AVEO',
    'PriCara, Unit of Ortho-McNeil, Inc.': 'JNJ', # JNJ owns Ortho-McNeil
    'Peregrine Pharmaceuticals': 'CDMO', # changed names, USED to be PPHM
    'NicOx': 'NICXF', # or ALCOX on EPA Exchange
    'Mateon Therapeutics': 'OXG.DE',
    'Alkermes, Inc.': 'ALKS',
    'XOMA (US) LLC': 'XOMA',
    'Genexine, Inc.': '095700.KQ',
    'Targanta Therapeutics Corporation': 'TARG', # delisted long ago 
    'Lundbeck LLC': 'HLUN-A.CO',
    'Basilea Pharmaceutica': 'BSLN.SW',
    'CytRx': 'CYTR', # delisted 2019, find data
    'Taiwan Otsuka Pharm. Co., Ltd': '4578.T',
    'UCB BIOSCIENCES, Inc.': 'UCB.BR',
    'Vifor Pharma': 'VIFN.SW', # delisted 2022, find data
    'Corthera, Inc.(formerly BAS Medical, Inc.), a member of the Novartis group of companies': 'NVS',
    'AtheroGenics': 'AGIX', # delisted 2009
    'Seagen Inc.': 'SGEN',
    'Tibotec BVBA': 'JNJ',
    'CrystalGenomics, Inc.': '083790.KQ',
    'Ortho-McNeil Janssen Scientific Affairs, LLC': 'JNJ',
    'Dynavax Technologies Corporation': 'DVAX',
    'Nastech Pharmaceutical Company, Inc.': 'NSTK',
    'Santhera Pharmaceuticals': 'SANN.SW',
    'Radius Health, Inc.': 'RDUS',
    'Biodel': 'BDQ.DE',
    'Nippon Kayaku Co., Ltd.': '4272.T',
    'Momenta Pharmaceuticals, Inc.': 'MNTA', # acquired 2020 by JNJ, find data
    'SciClone Pharmaceuticals': '6600.HK',
    'ALK-Abelló A/S': 'ALK-B.CO',
    'Becton, Dickinson and Company': 'BDX',
    'XTL Biopharmaceuticals': 'XTLB',
    'Repros Therapeutics Inc.': 'RPRX', # delisted 2018
    'Insmed Incorporated': 'INSM',
    'Active Biotech AB': 'ACTI.ST',
    'BioLineRx, Ltd.': 'BLRX',
    'Avanir Pharmaceuticals': 'AVNR', # delisted 2015
    'JANSSEN Alzheimer Immunotherapy Research & Development, LLC': 'JNJ',
    'Candel Therapeutics, Inc.': 'CADL',
    'Cumberland Pharmaceuticals': 'CPIX',
    'Targacept Inc.': 'TRGT', # delisted 2016
    'UCB BIOSCIENCES GmbH': 'UCB.BR',
    'H. Lundbeck A/S': 'HLUN-A.CO',
    'Syndax Pharmaceuticals': 'SNDX',
    'Biotie Therapies Inc.': 'BTH1V.HE',
    'Newron Pharmaceuticals SPA': 'NWRN',
    'Theratechnologies': 'TH.TO',
    'CytoDyn, Inc.': 'CYDY',
    'SK Life Science, Inc.':'326030.KS',
    'Ardea Biosciences, Inc.': 'RDEA', # acquired by AZN 2012
    'Imunon': 'IMNN', 
    'Evotec Neurosciences GmbH': 'EVT.DE',
    'Cytokinetics': 'CYTK',
    'Chelsea Therapeutics': 'CHTP',
    'JW Pharmaceutical': '001065.KS',
    'EMD Serono Research & Development Institute, Inc.': 'MRK.DE',
    'Melinta Therapeutics, Inc.': 'MLNT', # delisted 2020, find data
    'Mylan Pharmaceuticals Inc': 'VTRS', # MYL delisted 2020 to form Viatris VTRS, or MYL.VI
    'Meda Pharmaceuticals': 'MEDA-A.ST',
    'Acura Pharmaceuticals Inc.': 'ACUR',
    'Hutchison Medipharma Limited': 'HCM',
    'Alnylam Pharmaceuticals': 'ALNY',
    'Athenex, Inc.': 'ATNX',
    'Sumitomo Pharma (Suzhou) Co., Ltd.': '4506.T',
    'FUJIFILM Toyama Chemical Co., Ltd.': 'FUJIY',
    'Reata, a wholly owned subsidiary of Biogen': 'BIIB',
    'Generex Biotechnology Corp.': 'GB8A.SG',
    'Bellus Health Inc. - a GSK company': 'GSK',
    'Daiichi Sankyo Europe, GmbH, a Daiichi Sankyo Company': '4568.T',
    'Horizon Pharma USA, Inc.': 'HZNP', 
    'MediciNova': 'MNOV',
    'Mesoblast, Inc.': 'MESO',
    'TaiGen Biotechnology Co., Ltd.': '4157.TWO',
    'Palatin Technologies, Inc': 'PTN',
    'Stiefel, a GSK Company': 'GSK',
    'Ainos, Inc. (f/k/a Amarillo Biosciences Inc.': 'AIMD',
    'CanBas Co. Ltd.': '4575.T',
    'CymaBay Therapeutics, Inc.': 'CBAY', # acquired 2024, get data, check finnhub
    'Cephalon, Inc.': 'CEPH', # delisted
    'Regado Biosciences, Inc.': '9RB.SG',
    'Talphera, Inc': 'TLPH',
    'ERYtech Pharma': 'ERYP', # possibly delisted
    'Diamyd Therapeutics AB': 'DMYD-B.ST',
    'Sirtex Medical': 'SQX.DE',
    'NuPathe Inc.': 'PATH', # acquired by TEVA in 2014
    'Diffusion Pharmaceuticals Inc':'DFFN', # merger 2023, get data
    'Alexion Pharmaceuticals, Inc.': 'ALXN', # acquired 2021 by AZN
    'Curis, Inc.': 'CRIS',
    'Idera Pharmaceuticals, Inc.': 'ACGN', # changed from IDRA, then delisted 2023 
    'Thallion Pharmaceuticals': 'TLN.TO', # delisted
    'NephroGenex, Inc.': 'NRXGQ', # delisted 2016
    'Janssen Biotech, Inc.': 'JNJ',
    'Yuhan Corporation': '000100.KS',
    'Albireo': 'ALBO', # went bust 2023
    '4SC AG': 'VSC.F',
    'Janssen-Cilag Farmaceutica Ltda.': 'JNJ',
    'Zogenix, Inc.': 'ZGNX', # UCB acquired in 2022
    'Astellas Pharma Europe B.V.': 'ALPMY',
    'Almirall, S.A.': 'ALM.MC',
    'Samyang Biopharmaceuticals Corporation': '000070.KS',
    'LG Life Sciences': '051910.KS',
    'ChemoCentryx': 'CCXY', # acquired Amgen 2022, get data
    'Rexahn Pharmaceuticals, Inc.': 'US67577R1023.SG',
    'Sirtris, a GSK Company': 'GSK',
    'Betta Pharmaceuticals Co., Ltd.': '300558.SZ',
    'Reckitt Benckiser Inc.': 'RBGLY',
    'Teva Pharmaceuticals USA': 'TEVA',
    'Reckitt Benckiser LLC': 'RBGLY',
    'Traws Pharma, Inc.': 'TRAW',
    'Johnson & Johnson Pte Ltd': 'JNJ',
    'AMAG Pharmaceuticals, Inc.': 'AMU.DE',
    'Janssen Infectious Diseases BVBA': 'JNJ',
    'Lundbeck Italia S.p.A.': 'HLUN-A.CO',
    'Resverlogix Corp': 'RVX.TO',
    'Aerie Pharmaceuticals': 'AERI', # acquired 2022, get data
    'Biotest': 'BIO.DE',
    'Celltrion': '068270.KS',
    'Mesoblast, Ltd.': 'MESO',
    'Toray Industries, Inc': 'TRYIY',
    'Xenon Pharmaceuticals Inc.': 'XENE',
    'Tobira Therapeutics, Inc.': 'TBRA',
    'Hanmi Pharmaceutical Company Limited': '128940.KS',
    'RECORDATI GROUP': 'REC.MI',
    'Chong Kun Dang Pharmaceutical': '185750.KS',
    'Livzon Pharmaceutical Group Inc.': '1513.HK',
    'Nabriva Therapeutics AG': 'NBRVF',
    'GlycoMimetics Incorporated': 'GLYC',
    'Inotek Pharmaceuticals Corporation': 'ITEK', # delisted sometime late 2010s
    'Arno Therapeutics': 'ARNI',
    'Clovis Oncology, Inc.': 'CLVS',
    'Synairgen Research Ltd.': 'SRG',
    'Eyegate Pharmaceuticals, Inc.': 'EYEG', # possibly delisted
    'Furiex Pharmaceuticals, Inc': 'FURX',
    'Galapagos NV': 'GLPG',
    'Philogen S.p.A.': 'PHIL.MI',
    'Jiangsu Simcere Pharmaceutical Co., Ltd.': '2096.HK',
    'Geron Corporation': 'GERN',
    'FibroGen': 'FGEN',
    'Merrimack Pharmaceuticals': 'MACK', # delisted 2024
    'Mochida Pharmaceutical Company, Ltd.': '4534.T',
    'Celularity Incorporated': 'CELU',
    'Janssen Scientific Affairs, LLC': 'JNJ',
    'Bio-Path Holdings, Inc.': 'BPTH',
    'Vyne Therapeutics Inc.': 'VYNE',
    'Sandoz': 'SDZ', # or NVS, spinned-off in 2023
    'Janssen-Cilag, S.A.': 'JNJ',
    'Trevena Inc.': 'TRVN', 
    'Aptevo Therapeutics': 'APVO',
    'Santen Pharmaceutical Co., Ltd.': 'SNPHY',
    'OncoMed Pharmaceuticals, Inc.': 'OMED',
    'Mereo BioPharma': 'MREO',
    'Jiangsu HengRui Medicine Co., Ltd.': '600276.SS',
    'Oxford BioMedica': 'OXB.L',
    'Cerenis Therapeutics, SA': 'ABNX.PA',
    'Pacira Pharmaceuticals, Inc': 'PCRX',
    'Ariad Pharmaceuticals': 'ARIA', # delisted/acquired 2017
    'Vitae Pharmaceuticals, Inc.':'VTAE', # delisted/acquired 2016
    'Innocoll': 'INNL', # delisted 2017
    'Lytix Biopharma AS': 'LYTIX.OL',
    'NeuroDerm Ltd.': 'NDRM',
    'UCB Korea Co., Ltd.': 'UCB.BR',
    'Naurex, Inc, an affiliate of Allergan plc': 'AGN', # now part of AbbVie
    'Akebia Therapeutics': 'AKBA',
    'PhaseBio Pharmaceuticals Inc.': 'PHASQ',
    'ImmunoGen, Inc.': 'IMGN', # delisted 2024, get data
    'Provectus Pharmaceuticals': 'PVCT',
    "Teva Women's Health": 'TEVA',
    'Capnia, Inc.': 'SLNO', # changed name in 2017
    'Santen SAS': 'SNPHY',
    'Human Genome Sciences Inc., a GSK Company': 'GSK',
    'Vascular Biogenics Ltd. operating as VBL Therapeutics': 'VBLT',
    'Genfit': 'GNFT',
    'Scynexis, Inc.': 'SCYX',
    'Tetraphase Pharmaceuticals, Inc.': 'TTPH', # delisted
    'Immatics Biotechnologies GmbH': 'IMTX',
    'Amarantus BioScience Holdings, Inc.': 'AMBS',
    'Regeneron Pharmaceuticals': 'REGN',
    'Neurocrine Biosciences': 'NBIX',
    'Abbott Medical Devices': 'ABT',
    'TWi Biotechnology, Inc.': '6610.TWO',
    'Intec Pharma Ltd.':'5NU.SG',
    'Quince Therapeutics S.p.A.': 'QNCX',
    'AB Science': 'AB.PA',
    'Janssen R&D Ireland': 'JNJ',
    'Asahi Kasei Pharma Corporation': 'AHKSY',
    'Rockwell Medical Technologies, Inc.': 'RMTI',
    'Polaris Group': '6550.TW',
    'SK Chemicals Co., Ltd.': '285130.KS',
    'Astellas Pharma Europe Ltd.': 'ALPMY',
    'Prism Pharma Co., Ltd.': '206A.T',
    'Evofem Inc.': 'EVFM',
    '3M' : 'MMM',
    'Orexo AB': 'ORX.ST',
    'Astellas Pharma Korea, Inc.': 'ALPMY',
    'Nivalis Therapeutics, Inc.': 'NVLS', # delisted
    'Unigene Laboratories Inc.': 'UGNE', # delisted
    'Bavarian Nordic':'BVNRY',
    'Addex Pharma S.A.': 'ADXN',
    'Durata Therapeutics Inc., an affiliate of Allergan plc': 'AGN', # delisted
    'Ardelyx': 'ARDX',
    'Eisai China Inc.': '4523.T',
    'NovaBay Pharmaceuticals, Inc.': 'NBY',
    'HK inno.N Corporation': '195940.KQ',
    'Relypsa, Inc.': 'RLYP', #acquired in 2016
    "CSL Behring": 'CSL.AX',
    'Lexicon Pharmaceuticals': 'LXRX',
    'Janssen-Cilag Ltd.,Thailand': 'JNJ',
    'Tsumura USA': '4540.T',
    'UCB Biopharma S.P.R.L.': 'UCB.BR',
    'Adamas Pharmaceuticals, Inc.': 'ADMS', # delisted
    'Ultragenyx Pharmaceutical Inc': 'RARE',
    'Kubota Vision Inc.': '4596.T',
    'Chiasma, Inc.': 'CHMA', # acquired 2021
    'Ionis Pharmaceuticals, Inc.': 'IONS',
    'Lpath, Inc.': 'LPTN',
    'Aduro Biotech, Inc.': 'ADRO', # probably delisted
    'Sierra Oncology LLC - a GSK company': 'GSK',
    'Glenmark Pharmaceuticals Ltd. India': 'GLENMARK.NS',
    'Afferent Pharmaceuticals, Inc., a subsidiary of Merck & Co., Inc. (Rahway, New Jersey USA)': 'MRK',
    'TetraLogic Pharmaceuticals': 'TLOG',
    'Glaukos Corporation': 'GKOS',
    'Bellerophon Pulse Technologies': 'BLPH',
    'Kwang Dong Pharmaceutical co., ltd.': '009290.KS',
    'GPCR Therapeutics, Inc.': 'GPCR',
    'Capricor Inc.': 'CAPR',
    'Dermavant Sciences GmbH': 'DRMT',
    'Optinose US Inc.': 'OPTN',
    'Targeted Medical Pharma': 'TRGM',
    'Tocagen Inc.': 'TOCA', # delisted
    'Vectura Limited': 'VEC', # delisted
    'Zydus Lifesciences Limited': 'ZYDUSLIFE.NS',
    'Nuwellis, Inc.': 'NUWE',
    'Janssen Inc.': 'JNJ',
    'Concert Pharmaceuticals': 'CNCE',
    'RedHill Biopharma Limited': 'RDHL',
    'Reviva Pharmaceuticals': 'RVPH',
    'Nektar Therapeutics': 'NKTR',
    'Amarin Pharma Inc.': 'AMRN',
    'Intra-Cellular Therapies, Inc.': 'ITCI',
    'Tesaro, Inc.': 'TSRO',
    'Lundbeck Canada Inc.': 'HLUN-A.CO',
    'Panion & BF Biotech Inc.': '1760.TW',
    'Beijing Kawin Technology Share-Holding Co., Ltd.': '688687.SS',
    'Il-Yang Pharm. Co., Ltd.': '007570.KS',
    "Lee's Pharmaceutical Limited": '0950.HK',
    'Circadian Technologies Ltd.': 'OPT', # renamed to Ophtea LTD in 2015
    'Depomed': 'DEPO', # could also be ASRT
    'OBI Pharma, Inc':'4174.TWO',
    'Janssen-Cilag G.m.b.H': 'JNJ',
    'Trius Therapeutics LLC, a subsidiary of Merck & Co., Inc. (Rahway, New Jersey USA)': 'MRK',
    'Neuralstem Inc.': 'CUR', # could also be PALI
    'Shanghai Zhangjiang Biotechnology Limited Company': '1349.HK',
    'Pain Therapeutics': 'PTIE', # Delisted
    'Valneva Austria GmbH': 'VALN',
    'Tracon Pharmaceuticals Inc.': 'TCON',
    'Astellas Pharma Global Development, Inc.': 'ALPMY',
    'Changchun Huayang High-tech Co., Ltd': '000661.SZ',
    'Johnson & Johnson Taiwan Ltd': 'JNJ',
    'Argos Therapeutics': 'ARGS',
    'Portola Pharmaceuticals': 'PTLA', # delisted
    'Nuvo Research GmbH': 'MRV', # delisted
    'Aridis Pharmaceuticals, Inc.': 'ARDS',
    'Prana Biotechnology Limited': 'PRNAF',
    'AIM ImmunoTech Inc.': 'AIM',
    'Asahi Kasei Pharma America Corporation': 'AHKSY',
    'HemaQuest Pharmaceuticals Inc.': 'VIRX', # changed to Viracta in 2015
    'Janssen Pharmaceutica': 'JNJ',
    'Esperion Therapeutics, Inc.': 'ESPR',
    'Travere Therapeutics, Inc.': 'TVTX',
    'TSH Biopharm Corporation Limited': '8432.TWO',
    'ASLAN Pharmaceuticals': 'ASLN',
    'Sun Pharma Advanced Research Company Limited': 'SPARC.NS',
    'Antares Pharma Inc.': 'ATRS',
    'Egetis Therapeutics': 'EGTX',
    'Agile Therapeutics': 'AGRX',
    'OPKO IP Holdings II, Inc.': 'OPK',
    'Tasly Pharmaceuticals, Inc.': '600535.SS',
    'Piramal Enterprises Limited': 'PEL.NS',
    'Hanlim Pharm. Co., Ltd.': '128940.KS',
    'Astellas Pharma Canada, Inc.': 'ALPMY',
    'Clinigen, Inc.': '78C.F',
    'Innate Pharma': 'IPH.PA',
    'Humanigen, Inc.': 'HGENQ',
    'Neuren Pharmaceuticals Limited': 'NEU.AX',
    'Sun Pharmaceutical Industries Limited': 'SUNPHARMA.NS', 
    'Janssen-Cilag Ltd.': 'JNJ',
    'Acceleron Pharma, Inc., a wholly-owned subsidiary of Merck & Co., Inc., Rahway, NJ USA': 'MRK',
    'Intersect ENT': 'XENT',
    'Astellas Pharma Taiwan, Inc.': 'ALPMY',
    'ZS Pharma, Inc.': 'ZSPH', # acquired in 2015 by AZN
    'RVL Pharmaceuticals, Inc.': 'RVLPQ',
    'Savara Inc.': 'SVRA',
    'Eleven Biotherapeutics': 'EBIO', # changed name, might be carisma therapeutics
    'Protalex, Inc.': 'PRTX',
    'Beyond Air Inc.': 'XAIR',
    'MDD US Operations, LLC a subsidiary of Supernus Pharmaceuticals': 'SUPN',
    'Alder Biopharmaceuticals, Inc.': 'ALDR', # acquired in 2019
    'Daewon Pharmaceutical Co., Ltd.': '003220.KS',
    'Cara Therapeutics, Inc.': 'CARA',
    'Hansa Biopharma AB': 'HNSA.ST',
    'Syneos Health': 'SYNH', # delisted
    'Silence Therapeutics GmbH': 'SLN',
    'Ampio Pharmaceuticals. Inc.': 'AMPE',
    'NeuroBo Pharmaceuticals Inc.': 'NRBO',
    'Invion, Inc.': 'IVX.AX',
    'Sellas Life Sciences Group': 'SLS',
    'Integra LifeSciences Corporation': 'IART',
    'Chia Tai Tianqing Pharmaceutical Group Co., Ltd.': '1177.HK',
    'Neos Therapeutics, Inc': 'NEOS', # delisted 2021
    'Lixte Biotechnology Holdings, Inc.': 'LIXT',
    'Daiichi Sankyo Korea Co., Ltd., a Daiichi Sankyo Company': '4568.T',
    'Daehwa Pharmaceutical Co., Ltd.': '067080.KQ',
    'Ocular Therapeutix, Inc.': 'OCUL',
    'Processa Pharmaceuticals': 'PCSA',
    'Enanta Pharmaceuticals, Inc': 'ENTA',
    'Reckitt Benckiser Healthcare (UK) Limited': 'RBGLY',
    'Urovant Sciences GmbH': 'UROV', # delisted
    'Achaogen, Inc.': 'AKAO', # delisted 2019, bankrupt
    'Verastem, Inc.': 'VSTM',
    'Aquinox Pharmaceuticals (Canada) Inc.': 'AQXP', # possibly delisted, not on yf
    'Oramed, Ltd.': 'ORMP',
    'Samsung Bioepis Co., Ltd.': '207940.KS',
    'Karyopharm Therapeutics Inc': 'KPTI',
    'Quantum Genomics SA': 'ALQGC.PA',
    'Pulmatrix Inc.': 'PULM',
    'IlDong Pharmaceutical Co Ltd': '249420.KS',
    'Ophthotech Corporation': 'OPHT', # delisted
    'Avalo Therapeutics, Inc.': 'AVTX',
    'TherapeuticsMD': 'TXMD',
    'Otonomy, Inc.': 'OTIC',
    'Poxel SA': 'POXEL.PA',
    'Omeros Corporation': 'OMER',
    'ResMed': 'RMD',
    'NovoCure Ltd.': 'NVCR',
    'Shineway Pharmaceutical Co.,Ltd': '2877.HK',
    'Astellas Pharma China, Inc.': 'APLMY',
    'Serodus AS': 'SER', # delisted
    'Kamada, Ltd.': 'KMDA',
    'PLx Pharma': 'PLXP', # delisted
    'Soligenix': 'SNGX',
    'Cttq': '1177.HK',
    'TG Therapeutics, Inc.': 'TGTX',
    'e-Therapeutics PLC': 'ETXPF',
    'Carbylan Therapeutics, Inc.': 'CBYL',
    'Tenax Therapeutics, Inc.': 'TENX',
    'Evoke Pharma': 'EVOK',
    'ACADIA Pharmaceuticals Inc.': 'ACAD',
    'CSPC ZhongQi Pharmaceutical Technology Co., Ltd.': '1093.HK',
    'Arena Pharmaceuticals': 'ARNA',
    'Golden Biotechnology Corporation': '4132.TWO',
    'Calithera Biosciences, Inc': 'CALA',
    'Sage Therapeutics': 'SAGE',
    'Alcobra Ltd.': 'ADHD',
    'Sorrento Therapeutics, Inc.': 'SRNE',
    'Mologen AG': 'MGN.DE',
    'Stemline Therapeutics, Inc.': 'STML', # delisted
    'Concordia Laboratories Inc.': 'CXRX', # delisted
    'Rovi Pharmaceuticals Laboratories': 'ROVI.MC',
    'Atrium Innovations': 'ATBIF', # delisted
    'Summit Therapeutics': 'SMMT',
    'Coherus Biosciences, Inc.': 'CHRS',
    'Pherecydes Pharma': 'ALPHE', # delisted 2023
    'Chipscreen Biosciences, Ltd.': '688321.SS',
    'Epizyme, Inc.': 'EPZM', # delisted
    'UCB Pharma SA, Belgium': 'UCB.BR',
    'Kala Pharmaceuticals, Inc.': 'KALA',
    'Kitov Pharmaceuticals, Ltd.': 'KTOV', # delisted
    'Auspex Pharmaceuticals, Inc.': 'ASPX', # delisted
    'Ranbaxy Laboratories Limited': 'RBXY', # delisted
    'Perosphere Pharmaceuticals Inc, a wholly owned subsidiary of AMAG Pharmaceuticals, Inc.': 'AMU.DE',
    'Center Laboratories, Inc.': '4123.TWO',
    'Camurus AB': 'CAMX',
    'Kiromic BioPharma Inc.': 'KRBP',
    'Mylan Inc.': 'VTRS', # changed name
    'Innate Immunotherapeutics': 'INNMF',
    'Foresee Pharmaceuticals Co., Ltd.': '6576.TWO',
    'Anavex Life Sciences Corp.': 'AVXL',
    'Mylan Pharma UK Ltd.': 'VTRS',
    'Novavax': 'NVAX',
    'Abivax S.A.': 'ABVX',
    'Beijing Biostar Pharmaceuticals Co., Ltd.': '810563.SS',
    'Galecto Biotech AB': 'GLTO',
    'Bellerophon': 'BLPH',
    'MicuRx': '688373.SS',
    'Yungjin Pharm. Co., Ltd.': '003520.KS',
    'Ultimovacs ASA': 'ULTI.OL',
    'Galmed Research and Development, Ltd.': 'GLMD',
    'Provectus Biopharmaceuticals, Inc.': 'PVCT',
    'Heptares Therapeutics Limited': 'SOLTF', # changed name 2024 to Nxera Pharma Co Ltd
    'Milestone Pharmaceuticals Inc.': 'MIST',
    'Clearside Biomedical, Inc.': 'CLSD',
    'Ablynx, a Sanofi company': 'SNY',
    'ObsEva SA': 'OBSNZ.XC', # delisted 2024
    'Rhythm Pharmaceuticals, Inc.': 'RYTM',
    'Stealth BioTherapeutics Inc.': 'MITO', # delisted
    'Janssen Vaccines & Prevention B.V.': 'JNJ',
    'Innovation Pharmaceuticals, Inc.': 'IPIX',
    'Alcon, a Novartis Company': 'NVS',
    'Herantis Pharma Plc.': 'HRTIS.HE',
    'scPharmaceuticals, Inc.': 'SCPH',
    'Revive Therapeutics, Ltd.': 'RVVTF',
    'Helix BioPharma Corporation': 'HBP.TO',
    'MyoKardia, Inc.': 'MYOK', # delisted
    'Shanghai Shyndec Pharmaceutical Co., Ltd.': '600420.SS',
    'Pharnext S.C.A.': 'ALPHA.PA',
    'Biota Pharmaceuticals, Inc.': 'BOTA', # delisted
    'Pharco Pharmaceuticals': 'PHPC', # delisted
    'Catabasis Pharmaceuticals': 'CATB', # delisted
    'Paratek Pharmaceuticals Inc': 'PRTK', # delisted
    'DexTech Medical AB': 'DEX.ST',
    'Elevation Oncology': 'ELEV',
    'Janssen Sciences Ireland UC': 'JNJ',
    'MorphoSys AG': 'MOR',
    'Yakult Honsha Co., LTD': 'YKLTY',
    'OptiNose AS': 'OPTN',
    'Verona Pharma plc': 'VRNA',
    'Dong-A ST Co., Ltd.': '170900.KS',
    'Kineta Inc.': 'KA',
    'Tonix Pharmaceuticals, Inc.': 'TNXP',
    'Seres Therapeutics, Inc.': 'MCRB',
    # 'Baxalta now part of Shire': 'SHPG',
    'Orient Pharma Co., Ltd.': '4166.TWO',
    'Zosano Pharma Corporation': 'ZSANQ', # delisted
    'Corbus Pharmaceuticals Inc.': 'CRBP',
    'Visterra, Inc.': 'VIST',
    'Mabion SA':'MAB.WA',
    'SIGA Technologies': 'SIBA',
    'TaiMed Biologics Inc.': '4147.TWO',
    'Jiangsu Hansoh Pharmaceutical Co., Ltd.': '3692.HK',
    'Shanghai Fudan-Zhangjiang Bio-Pharmaceutical Co., Ltd.': '1349.HK',
    'Bellicum Pharmaceuticals': 'BLCM', # possibly delisted
    'Huons Co., Ltd.': '243070.KQ',
    'Holy Stone Healthcare Co., Ltd': '4194.TWO',
    'Cellceutix Corporation': 'CTIX', # delisted
    'Theriva Biologics, Inc.': 'TOVX',
    'PepTonic Medical AB': '28L.F',
    'G1 Therapeutics, Inc.': 'GTHX',
    'Inventiva Pharma': 'IVA',
    'Axsome Therapeutics, Inc.': 'AXSM',
    'ImmuPharma': 'IMM.L',
    'Akcea Therapeutics': 'AKCA', # delisted 2020, get data
    'Adocia': 'ADOC.PA',
    'ProQR Therapeutics': 'PRQR',
    'Tamir Biotechnology, Inc.': 'ACEL', # delisted, now another company
    'iX Biopharma Ltd.': '42C.SI',
    'Vitae Pharmaceuticals Inc., an Allergan affiliate': 'AGN', # allergan acquired
    'Axovant Sciences Ltd.': 'AXGT',
    'Hua Medicine Limited': '2552.HK',
    'UCB Celltech': 'UCB.BR',
    'Ohr Pharmaceutical Inc.': 'OHRP', # possibly delisted
    'Oncolytics Biotech': 'ONCY',
    'Agios Pharmaceuticals, Inc.': 'AGIO',
    'Glenmark Specialty S.A.': 'GLENMARK.NS',
    'Prothena Biosciences Ltd.': 'PRTA',
    'CorMedix': 'CRMD',
    'Braeburn Pharmaceuticals': 'BBRX', # delisted
    'WntResearch AB': 'WNT.ST',
    'Eiger BioPharmaceuticals': 'EIGR',
    'Shield Therapeutics': 'STX.L',
    'ThromboGenics': 'OXUR.BR', # changed to Oxurion in 2018
    'Zogenix International Limited, Inc., a subsidiary of Zogenix, Inc.': 'ZGNX', # acquired by UCB 2022
    'Medivir': 'MVIR.ST',
    'Proteostasis Therapeutics, Inc.': 'PTI', # delisted
    'Actinogen Medical': 'ACW.AX',
    'Cidara Therapeutics Inc.': 'CDTX',
    'Saniona': 'SANION.ST',
    'F-star Therapeutics, Inc.': 'FSTX', # delisted 2023
    'Amorepacific Corporation': '090430.KS',
    'Cocrystal Pharma, Inc.': 'COCP',
    'Aevi Genomic Medicine, LLC, a Cerecor company': 'CERC', # delisted
    'Kura Oncology, Inc.': 'KURA',
    'GeNeuro SA': 'GNRO.PA',
    'Shin Poong Pharmaceutical Co. Ltd.': '019170.KS',
    'Prometheus Laboratories': 'RXDX', # delisted
    'OSE Immunotherapeutics': 'OSE.PA',
    'Hybrigenics Corporation': '3HB.F', # rebranded, not sure what is the correct ticker nowadays
    'Enteris BioPharma Inc.': 'SWKH', # owned by SWKH
    'NLS Pharmaceutics': 'NLSP',
    'Tricida, Inc.': 'TCDA', # delisted
    'VBI Vaccines Inc.': 'VBIV',
    'Global Blood Therapeutics': 'GBT', # delisted
    'Mirna Therapeutics, Inc.': 'MIRN', # delisted
    'Protagonist Therapeutics, Inc.': 'PTGX',
    'Cyclerion Therapeutics': 'CYCN',
    'Cognition Therapeutics': 'CGTX',
    'Madrigal Pharmaceuticals, Inc.': 'MDGL',
    'Viking Therapeutics, Inc.': 'VKTX',
    'Bionomics Limited': 'BNOX',
    'Noxopharm Limited': 'NOX.AX',
    'Liminal BioSciences Ltd.': 'LMNL', # delisted 2023
    'Histogen': 'HSTO',
    'argenx': 'ARGX',
    'Lyra Therapeutics': 'LYRA',
    'Evgen Pharma': 'TCF.L', # changed name 2024
    'Zealand Pharma': 'ZEAL.CO',
    'NeuroRx, Inc.': 'NRXP', 
    'Kitov Pharma Ltd': 'KTOV', # delisted
    'Taiwan Liposome Company': 'TLC', # delisted 2021
    'Ascletis Pharmaceuticals Co., Ltd.': '1672.HK',
    'Myovant Sciences GmbH': 'MYOV', # delisted
    'Relmada Therapeutics, Inc.': 'RMLD',
    'Stayble Therapeutics': 'STABL.ST',
    'BRIM Biotechnology Inc.': '6885.TWO',
    'BriaCell Therapeutics Corporation': 'BCTX',
    'Xeris Pharmaceuticals': 'XERS',
    'BeyondSpring Pharmaceuticals Inc.': 'BYSI',
    'BioVie Inc.': 'BIVI',
    'Jiangsu Wuzhong Pharmaceutical Group Co., Ltd.': '600200.SS',
    'Zai Lab Pty. Ltd.': 'ZLAB',
    'Takara Bio Inc.': '4974.T',
    'Aquestive Therapeutics': 'AQST',
    'Daewoong Pharmaceutical Co. LTD.': '069620.KS',
    'Flex Pharma, Inc.': 'FLKS', # delisted
    'EyePoint Pharmaceuticals, Inc.': 'EYPT',
    'Biosearch S.A.': 'BIOS', # delisted
    'LG Chem': '051910.KS',
    'Aptinyx': 'APTX',
    'Korea United Pharm. Inc.': '033270.KS',
    'Calliditas Therapeutics AB': 'CALT',
    'Graybug Vision': 'GRAY', # changed name 2023 to CalciMedica, CALC
    'Avenue Therapeutics, Inc.': 'ATXI',
    'Barinthus Biotherapeutics': 'BRNS',
    'Sienna Biopharmaceuticals': 'SNNAQ',
    'Johnson & Johnson Consumer Inc. (J&JCI)': 'JNJ',
    'Deciphera Pharmaceuticals LLC': 'DCPH', # delisted
    'IntegraGen SA': 'ALINT.PA',
    'Aprea Therapeutics': 'APRE',
    'Aldeyra Therapeutics, Inc.': 'ALDX',
    'Ocugen': 'OCGN',
    'Novan, Inc.': 'NOVN', # delisted
    'Teijin America, Inc.': 'TINLY',
    'AnaptysBio, Inc.': 'ANAB',
    'Oxurion': 'OXUR.BR',
    'Oyster Point Pharma, Inc.': 'OYST', # delisted
    'Arcutis Biotherapeutics, Inc.': 'ARQT',
    'Nicox Ophthalmics, Inc.': 'NICXF',
    'miRagen Therapeutics, Inc.': 'VRDN',
}