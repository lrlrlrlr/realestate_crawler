import requests

url = "https://www.realestate.com.au/find-agency/graphql"


headers = {
    'host': "www.realestate.com.au",
    'connection': "keep-alive",
    'content-length': "671",
    'accept': "*/*",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    'content-type': "application/json",
    'origin': "https://www.realestate.com.au",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.realestate.com.au/agency/meriton-sydney-MHDSYD?cid=nhbpp|rent",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
    'cookie': "reauid=994648686f290000283f485f6b000000df9e2c00; Country=AU; brz_load_segmentation=false; brz_load_segment=false; OB-USER-TOKEN=23616a9b-5d43-40f4-9cf7-508e38fa08df; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; s_vi=[CS]v1|2FA41F948515EFA6-60000686978B8E23[CE]; s_ecid=MCMID%7C07298258585732704421930926246184416330; s_cc=true; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22b017ba28-2d96-803d-558f-a1900df2deeb%22%2C%22c%22%3A1598570304204%2C%22l%22%3A1598570304204%7D; _stc=Other; qsi_abSrpCarouselAd=false; reauinf=eyJtbGlkIjoiYWMqKippQHFxLmNvbSIsImdlaWQiOiIzNTZiMjkyMDAxNDA1MTUzNTVjNTI0N2E2YmU5NzFmNWFhMjMwNGM2NWRkODhhZjNhYmNiY2Q0MTk3ZWI0N2NhIiwiY2lkIjoiNDAyODdmMGE2NWNiMjk3NDAxNjVlYzM0OTQzYTE5NGUiLCJsaWQiOiI1YTFhZDZmNy02NTEzLTQyMGYtODEwMy1hNGMzYWVkMGUyMjciLCJpc05ld1VzZXIiOmZhbHNlLCJleHBpcnlNaWxsaXMiOjE2MzAxMDc3NTQ5NTd9; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%225a1ad6f7-6513-420f-8103-a4c3aed0e227%22%2C%22c%22%3A1598571822644%2C%22l%22%3A1598571822644%7D; lmdstok=aWQjNDAyODdmMGE3NDhkMDQ3NTAxNzQ5MDAwOTEzMzMzZWU6Mzc0NzYyNzQzNzQxMjo3NzJjYmI5MmJiYjY3ODQ5YzA0Y2Q3N2NlZWNlZjYwZQ; s_nr=1602402149488; AWSELB=E32BC90112C9C0CF56D4194ABA698EBC86B542A11EBB76C2CF6CA3492090D9AFC471C58597179A0AA1CE04D6BA027A44131093611B11D2D530CE5C55125C6A08722A44C4FD; AWSELBCORS=E32BC90112C9C0CF56D4194ABA698EBC86B542A11EBB76C2CF6CA3492090D9AFC471C58597179A0AA1CE04D6BA027A44131093611B11D2D530CE5C55125C6A08722A44C4FD; bm_pack=a921b48b-da39-8dc2-5b29-4e4e652c80c3; _gid=GA1.3.899254574.1602681400; QSI_SI_cBxmNpOQdMkiWVf_intercept=true; JSESSIONID=70AA768AA49D4EE8959D135A642890A9; _sp_ses.2fe7=*; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C18550%7CMCMID%7C07298258585732704421930926246184416330%7CMCAAMLH-1603367161%7C8%7CMCAAMB-1603367161%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1602769561s%7CNONE%7CMCAID%7C2FA41F948515EFA6-60000686978B8E23%7CvVersion%7C3.1.2; pageview_counter.srs=7; kmam_lapoz=ymAJdZWNpwfVn27iWlKRtQ%3D%3D%3A%3AC1tbW%2F6UZgM7o%2Fp9%2FGJJYdnRGRtOZt6jEOyq1gcFg9a3o14lXWPz2TVKFNZ7eu2rjPXSQ18Q1ThjHgTXQOtOwoOpVCQ%2FSghCujtmPQiE0uoSxtCvz%2FYto2V2imf%2BrBPulQ6vJ8eGeihY6cI5TjbXEmO3m3uhjOAPBr2mn7yWHcGpRnnltflFFa0jxJTrDg6fyo%2FGQLMPE0xTv51TXz3Fo7OTvhq1t%2B6Bf9K%2FwuTdmRJP48VxN%2BuAPOdIlaxkKbRVX99uerPaK7pjVq636oVnIryNe2IVZ8CpqK0d31CHsN%2Bb74i%2Foha8MO0ZsgteXmZLdt0cuQC6a18iV3y27vkpwjHo1uKtYow5VYuhpRg7eDJEH0XzjscNFtSL9uJPSeT8dLoDPJPSyiKa8X4IMTzZeqBRFWm8GdiUGVGM9%2Fll3g7TKZi7r8Ag2gBIbvxnejxlFtsJOB1sLi%2FLFcBAMr0Bbi9NA%2BfLbq1srPbwRLvFTNunGRVegumHjbrLuW5Yi%2FOLVeYqTKglrwfpxXVvajt7fmxipVgB2FXtRoqGeKtNKGU%3D; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22935a76b9-c425-919a-596f-2c1c416dbfb8%22%2C%22e%22%3A1602764486202%2C%22c%22%3A1602762372325%2C%22l%22%3A1602762686202%7D; _ga_F962Q8PWJ0=GS1.1.1602762359.7.1.1602763480.0; _ga=GA1.1.694394837.1600143761; _sp_id.2fe7=f3158881-f296-43f2-b1b7-4acfd61a9870.1598570280.10.1602764159.1602739666.bd45aed5-12f5-4465-a5f4-eb785bcc2907; utag_main=v_id:01743236af24001969408c722d7e03073002106b00bd0$_sn:10$_ss:0$_st:1602765958804$vapi_domain:realestate.com.au$dc_visit:8$ses_id:1602762360091%3Bexp-session$_pn:16%3Bexp-session$dc_event:39%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; s_sq=rea-live%3D%2526c.%2526a.%2526activitymap.%2526page%253Drea%25253Afind%252520agent%25253Aagency%252520page%2526link%253DShow%252520more%252520properties%2526region%253Dapp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Drea%25253Afind%252520agent%25253Aagency%252520page%2526pidt%253D1%2526oid%253Dfunctionun%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT",
    'cache-control': "no-cache",
    }

data = '''{"operationName":null,"variables":{"input":{"agencyId":"MHDSYD","page":6,"pageSize":12,"channel":"sold","sort":"sold-date-desc"}},"query":"query ($input: AgencyListingsRequest!) {\n  agencyListings(input: $input) {\n    totalCount\n    listings {\n      id\n      channel\n      address {\n        streetAddress\n        postcode\n        suburb\n        __typename\n      }\n      mainImage {\n        uri\n        server\n        __typename\n      }\n      displayPrice\n      displayDate\n      features {\n        bedrooms\n        bathrooms\n        parkingSpaces\n        __typename\n      }\n      url\n      __typename\n    }\n    next\n    __typename\n  }\n}\n"}'''
response = requests.request("POST", url, headers=headers, data=data)

print(response.text)