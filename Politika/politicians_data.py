def create_politician(
    name, title, biography, image_name, highlights, country, born_year, position
):
    biography = " ".join(biography.split())
    return {
        "name": name,
        "title": title,
        "biography": biography,
        "image_name": image_name,
        "highlights": highlights,
        "country": country,
        "born_year": born_year,
        "position": position,
    }


politicians = [
    create_politician(
        name="Cevdet Yılmaz",
        title="Vice President of Turkey",
        biography="""
        Cevdet Yılmaz (born 1 April 1967, Bingöl) is a Turkish politician who has served in various governmental roles. 
        He has been a Member of Parliament since 2007 and has held positions such as Minister of Development and Minister of State. 
        Yılmaz is known for his work in economic policy and development planning. He became Vice President of Turkey in 2023.
        """,
        image_name="https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2056000/cevdet-yilmaz-aa-2056105.jpg",
        highlights=[
            {"icon": "calendar", "text": "1967"},
            {
                "icon": "graduationcap",
                "text": "Middle East Technical University / Public Administration / 1988",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2001"},
        ],
        country="Turkey",
        born_year=1967,
        position="turVicePres",
    ),
    create_politician(
        name="Recep Tayyip Erdoğan",
        title="President of Turkey",
        biography="""
        Recep Tayyip Erdoğan (born 26 February 1954) is a Turkish politician serving as the current President of Turkey.
        He previously served as Prime Minister from 2003 to 2014 and as Mayor of Istanbul from 1994 to 1998.
        Erdoğan has been the leader of the Justice and Development Party (AKP) since 2001.
        He is known for his conservative policies and has been a significant figure in Turkish politics for over two decades.
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Turkish_President_Recep_Tayyip_Erdo%C4%9Fan_in_January_2024_%28cropped%29.jpg/1200px-Turkish_President_Recep_Tayyip_Erdo%C4%9Fan_in_January_2024_%28cropped%29.jpg",
        highlights=[
            {"icon": "calendar", "text": "1954"},
            {
                "icon": "graduationcap",
                "text": "Marmara University / Business Administration / 1981",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2001"},
        ],
        country="Turkey",
        born_year=1954,
        position="turPresident",
    ),
    create_politician(
        name="Mehmet Nuri Ersoy",
        title="Minister of Culture and Tourism",
        biography="""
        Mehmet Nuri Ersoy (born 1968) is a Turkish businessman and politician who has been serving as the Minister of Culture and Tourism since 2018.
        He is the founder of the tourism company ETS and has a background in the tourism industry.
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Mehmet_Nuri_Ersoy_in_November_2023.jpg/1200px-Mehmet_Nuri_Ersoy_in_November_2023.jpg",
        highlights=[
            {"icon": "calendar", "text": "1968"},
            {"icon": "briefcase", "text": "Founder of ETS / 1991"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1968,
        position="turTourism",
    ),
    create_politician(
        name="Fatih Dönmez",
        title="Minister of Energy and Natural Resources",
        biography="""
        Fatih Dönmez (born 1965) is a Turkish engineer and politician who has been the Minister of Energy and Natural Resources since 2018.
        He has a background in electrical engineering and has held various positions in the energy sector.
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/b/b3/Fatih_Donmez%2C_Ministry_of_Energy_and_Natural_Resources_of_Turkey.jpg",
        highlights=[
            {"icon": "calendar", "text": "1965"},
            {
                "icon": "graduationcap",
                "text": "Istanbul Technical University / Electrical Engineering / 1987",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1965,
        position="turEnergy",
    ),
    create_politician(
        name="Murat Kurum",
        title="Minister of Environment and Urbanization",
        biography="""
        Murat Kurum (born 1976) is a Turkish politician serving as the Minister of Environment and Urbanization since 2018.
        He has a background in civil engineering and has worked in various roles related to urban planning and development.
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/AK_Parti_%C4%B0stanbul_Milletvekili_Murat_Kurum_%28cropped%29.jpg/1200px-AK_Parti_%C4%B0stanbul_Milletvekili_Murat_Kurum_%28cropped%29.jpg",
        highlights=[
            {"icon": "calendar", "text": "1976"},
            {
                "icon": "graduationcap",
                "text": "Selcuk University / Civil Engineering / 1999",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1976,
        position="turEnv",
    ),
    create_politician(
        name="Derya Yanık",
        title="Minister of Family and Social Services",
        biography="""
        Derya Yanık (born 1972) is a Turkish lawyer and politician who has been serving as the Minister of Family and Social Services since 2021.
        She has a background in law and has worked in various roles related to social policy and women's rights.
        """,
        image_name="https://cdnuploads.aa.com.tr/uploads/Contents/2022/06/16/thumbs_b_c_b0e07352a581dc35d06ede5860c3a668.jpg?v=114414",
        highlights=[
            {"icon": "calendar", "text": "1972"},
            {"icon": "graduationcap", "text": "Istanbul University / Law / 1996"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2021"},
        ],
        country="Turkey",
        born_year=1972,
        position="turFamSocial",
    ),
    create_politician(
        name="Hakan Fidan",
        title="Minister of Foreign Affairs",
        biography="""
        Hakan Fidan (born 1968) is a Turkish diplomat and politician who has been serving as the Minister of Foreign Affairs since 2023.
        He has previously served as the head of the National Intelligence Organization (MIT).
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/4/49/Foreign_Minister_of_Turkey_Hakan_Fidan_at_the_Department_of_State_in_Washington%2C_D.C._on_March_8%2C_2024_%28cropped%29.jpg",
        highlights=[
            {"icon": "calendar", "text": "1968"},
            {
                "icon": "graduationcap",
                "text": "Bilkent University / International Relations / 1999",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2023"},
        ],
        country="Turkey",
        born_year=1968,
        position="turForeign",
    ),
    create_politician(
        name="Fahrettin Koca",
        title="Minister of Health",
        biography="""
        Fahrettin Koca (born 1965) is a Turkish physician and politician who has been serving as the Minister of Health since 2018.
        He has a background in medicine and has worked in various roles related to healthcare management.
        """,
        image_name="https://static.euronews.com/articles/stories/04/63/74/72/1200x675_cmsv2_d1fab692-61c9-549d-b741-5e810e9f909c-4637472.jpg",
        highlights=[
            {"icon": "calendar", "text": "1965"},
            {"icon": "graduationcap", "text": "Istanbul University / Medicine / 1988"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1965,
        position="turHealth",
    ),
    create_politician(
        name="Mehmet Muş",
        title="Minister of Industry and Technology",
        biography="""
        Mehmet Muş (born 1982) is a Turkish economist and politician who has been serving as the Minister of Industry and Technology since 2021.
        He has a background in economics and has worked in various roles related to industrial policy and economic development.
        """,
        image_name="https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1564000/mehmet-mus-1564852.jpg",
        highlights=[
            {"icon": "calendar", "text": "1982"},
            {"icon": "graduationcap", "text": "Marmara University / Economics / 2005"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2021"},
        ],
        country="Turkey",
        born_year=1982,
        position="turIndTech",
    ),
    create_politician(
        name="Süleyman Soylu",
        title="Minister of Interior",
        biography="""
        Süleyman Soylu (born 1969) is a Turkish politician who has been serving as the Minister of Interior since 2016.
        He has a background in business and has worked in various roles related to security and governance.
        """,
        image_name="https://media-cdn.t24.com.tr/media/library/2023/05/1683985458623-suleymansoylu.jpg",
        highlights=[
            {"icon": "calendar", "text": "1969"},
            {
                "icon": "graduationcap",
                "text": "Istanbul University / Business Administration / 1992",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2016"},
        ],
        country="Turkey",
        born_year=1969,
        position="turInt",
    ),
    create_politician(
        name="Abdulhamit Gül",
        title="Minister of Justice",
        biography="""
        Abdulhamit Gül (born 1977) is a Turkish lawyer and politician who has been serving as the Minister of Justice since 2017.
        He has a background in law and has worked in various roles related to justice and legal reform.
        """,
        image_name="https://cdnuploads.aa.com.tr/uploads/Contents/2018/07/09/thumbs_b_c_af26da90fd8956d7ba9b82ca8faf1efe.jpg",
        highlights=[
            {
                "icon": "calendarhttps://cdnuploads.aa.com.tr/uploads/Contents/2018/07/09/thumbs_b_c_af26da90fd8956d7ba9b82ca8faf1efe.jpg",
                "text": "1977",
            },
            {"icon": "graduationcap", "text": "Ankara University / Law / 1999"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2017"},
        ],
        country="Turkey",
        born_year=1977,
        position="turJustice",
    ),
    create_politician(
        name="Vedat Bilgin",
        title="Minister of Labor and Social Security",
        biography="""
        Vedat Bilgin (born 1954) is a Turkish sociologist and politician who has been serving as the Minister of Labor and Social Security since 2021.
        He has a background in sociology and has worked in various roles related to labor policy and social security.
        """,
        image_name="https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1740000/vedat-bilgin-aa-1740872.jpg",
        highlights=[
            {"icon": "calendar", "text": "1954"},
            {"icon": "graduationcap", "text": "Ankara University / Sociology / 1977"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2021"},
        ],
        country="Turkey",
        born_year=1954,
        position="turLaborSocialSec",
    ),
    create_politician(
        name="Hulusi Akar",
        title="Minister of National Defense",
        biography="""
        Hulusi Akar (born 1952) is a Turkish retired general and politician who has been serving as the Minister of National Defense since 2018.
        He has a background in the military and has served in various roles related to national defense and security.
        """,
        image_name="https://upload.wikimedia.org/wikipedia/commons/7/77/Hulusi_Akar_%28cropped%2C_2019%29.jpg",
        highlights=[
            {"icon": "calendar", "text": "1952"},
            {"icon": "briefcase", "text": "Chief of the General Staff / 2015"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1952,
        position="turDefense",
    ),
    create_politician(
        name="Ziya Selçuk",
        title="Minister of National Education",
        biography="""
        Ziya Selçuk (born 1961) is a Turkish educator and politician who has been serving as the Minister of National Education since 2018.
        He has a background in education and has worked in various roles related to educational policy and reform.
        """,
        image_name="https://cdnuploads.aa.com.tr/uploads/Contents/2020/08/04/thumbs_b_c_ac8a1b9a29953f247732d46247001b96.jpg",
        highlights=[
            {"icon": "calendar", "text": "1961"},
            {
                "icon": "graduationcap",
                "text": "Hacettepe University / Educational Psychology / 1983",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1961,
        position="turEdu",
    ),
    create_politician(
        name="Ruhsar Pekcan",
        title="Minister of Trade",
        biography="""
        Ruhsar Pekcan (born 1958) is a Turkish businesswoman and politician who has been serving as the Minister of Trade since 2018.
        She has a background in engineering and business and has worked in various roles related to trade and commerce.
        """,
        image_name="https://www.cumhuriyet.com.tr/Archive/2021/5/3/1833013/kapak_100730.png",
        highlights=[
            {"icon": "calendar", "text": "1958"},
            {
                "icon": "graduationcap",
                "text": "Istanbul Technical University / Electrical Engineering / 1980",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1958,
        position="turTrade",
    ),
    create_politician(
        name="Adil Karaismailoğlu",
        title="Minister of Transport and Infrastructure",
        biography="""
        Adil Karaismailoğlu (born 1969) is a Turkish engineer and politician who has been serving as the Minister of Transport and Infrastructure since 2020.
        He has a background in engineering and has worked in various roles related to transport and infrastructure development.
        """,
        image_name="https://image.hurimg.com/i/hurriyet/75/750x422/5e7f83297af5071abcbc9f89.jpg",
        highlights=[
            {"icon": "calendar", "text": "1969"},
            {
                "icon": "graduationcap",
                "text": "Karadeniz Technical University / Civil Engineering / 1992",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2020"},
        ],
        country="Turkey",
        born_year=1969,
        position="turTraInf",
    ),
    create_politician(
        name="Lütfi Elvan",
        title="Minister of Treasury and Finance",
        biography="""
        Lütfi Elvan (born 1962) is a Turkish economist and politician who has been serving as the Minister of Treasury and Finance since 2020.
        He has a background in economics and has worked in various roles related to financial policy and economic development.
        """,
        image_name="https://i.dunya.com/storage/files/images/2021/02/23/lutfi-elvan-sZrc_cover.jpg",
        highlights=[
            {"icon": "calendar", "text": "1962"},
            {"icon": "graduationcap", "text": "Ankara University / Economics / 1985"},
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2020"},
        ],
        country="Turkey",
        born_year=1962,
        position="turTreaFin",
    ),
    create_politician(
        name="Mehmet Kasapoğlu",
        title="Minister of Youth and Sports",
        biography="""
        Mehmet Kasapoğlu (born 1976) is a Turkish politician who has been serving as the Minister of Youth and Sports since 2018.
        He has a background in public administration and has worked in various roles related to youth policy and sports management.
        """,
        image_name="https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1578000/mehmet-muharrem-kasapoglu-1579977.jpg",
        highlights=[
            {"icon": "calendar", "text": "1976"},
            {
                "icon": "graduationcap",
                "text": "Marmara University / Public Administration / 1999",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2018"},
        ],
        country="Turkey",
        born_year=1976,
        position="turSport",
    ),
    create_politician(
        name="Şahap Kavcıoğlu",
        title="Governor of the Central Bank of the Republic of Turkey",
        biography="""
        Şahap Kavcıoğlu (born 1967) is a Turkish banker and economist who has been serving as the Governor of the Central Bank of the Republic of Turkey since 2021.
        He has a background in banking and finance and has worked in various roles related to monetary policy and banking regulation.
        """,
        image_name="https://cdn1.ntv.com.tr/gorsel/g8420pZjsUqKM9G451DPHA.jpg?width=952&height=540&mode=both&scale=both",
        highlights=[
            {"icon": "calendar", "text": "1967"},
            {
                "icon": "graduationcap",
                "text": "Anadolu University / Banking and Finance / 1989",
            },
            {"icon": "person.3.fill", "text": "Justice and Development Party / 2021"},
        ],
        country="Turkey",
        born_year=1967,
        position="turBank",
    ),
]
