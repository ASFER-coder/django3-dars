from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


songgi_yangiliklar = [
    {
        "title": "Python Backend Dasturlashga Kirish",
        "date": "15 Mart, 2024",
        "content": "2025-yilda backend sohasi Python tilisiz tasavvur qilib bo‘lmaydi. Flask va FastAPI kabi framework’lar yordamida siz bir necha soat ichida to‘liq ishlaydigan REST API yarata olasiz. Dastlab HTTP so‘rovlar, JSON format va server mantig‘ini o‘rganing. So‘ngra autentifikatsiya va ma’lumotlar bazasi integratsiyasiga o‘ting. Muhimi — nazariya emas, har kuni kichik amaliy mashq."
    },
    {
        "title": "Nega API Muhim?",
        "date": "10 Mart, 2024",
        "content": "API — zamonaviy dasturlar orasidagi “til”. U orqali web, mobil va hatto IoT qurilmalar bir-biri bilan muloqot qiladi. Yaxshi API qurish — bu tezlik, xavfsizlik va qulaylikni birlashtirish demak. Dasturingiz uchun OpenAPI hujjatini yozing, Postman bilan test qiling va foydalanuvchilar uchun soddalikka e’tibor bering. Ishonchli API — muvaffaqiyatli xizmatning yuragi."
    },
    {
        "title": "Birinchi Backend Loyihangiz",
        "date": "5 Mart, 2024",
        "content": "Biror narsani haqiqatan o‘rganishning yagona yo‘li — amalda qo‘llash. Oddiy blog yoki task menejer API yozing. CRUD amallarni bajaring, JWT orqali login tizimi qo‘shing, so‘ngra bu loyihani GitHub’ga joylashtiring. Portfoliongizda haqiqiy loyiha bo‘lishi sizni boshqa dasturchilardan ajratib turadi."
    }
]


sport_postlari = [
    {
        "title": "Sportning Sog‘liq Uchun Foydasi",
        "date": "20 Mart, 2024",
        "content": "2025-yilda sog‘lom turmush tarzi eng muhim trendlardan biri. Har kuni 30–40 daqiqa harakat — yurak, miya va immunitet uchun eng yaxshi dori. Yugurish, suzish, yoga yoki fitnes — farqi yo‘q, asosiysi muntazamlik. Sport nafaqat tanani, balki fikrni ham tiniqlashtiradi."
    },
    {
        "title": "Jismoniy Mashqlarni Boshlash Uchun Maslahatlar",
        "date": "18 Mart, 2024",
        "content": "Agar sportni endi boshlayotgan bo‘lsangiz, mukammallikka emas, odatga e’tibor bering. Kichik mashqlar bilan boshlang: ertalab 15 daqiqa yurish yoki kechqurun engil cho‘zilish mashqlari. O‘zingizni qiynamang — eng muhim narsa, har kuni oz bo‘lsa ham davom etishdir. Bir oyda natija sekin, ammo barqaror tarzda ko‘rinadi."
    },
    {
        "title": "Jamoaviy Sportning Afzalliklari",
        "date": "12 Mart, 2024",
        "content": "Jamoaviy sport turlari — sog‘lom tananing va kuchli ijtimoiy ko‘nikmalarning manbai. Basketbol, futbol, voleybol yoki tennis — bu nafaqat harakat, balki jamoada ishlash, muloqot qilish va strategik fikrlashni rivojlantiradi. Birgalikda mashq qilish motivatsiyani ikki baravar oshiradi."
    }
]


dasturlash_postlari = [
    {
        "title": "Dasturlashni Qayerdan Boshlash Kerak?",
        "date": "28 Mart, 2024",
        "content": "2025-yilda dasturlashni o‘rganish uchun resurslar ko‘p, ammo eng muhimi — yo‘l xaritasi. Python bilan boshlang: sintaksis, o‘zgaruvchilar, funksiya va modul tushunchalarini o‘zlashtiring. So‘ngra kichik loyihalar yozing — kalkulyator, chat-bot, yoki oddiy veb-xizmat. Amaliy mashqlar nazariyadan ming karra samaraliroq."
    },
    {
        "title": "Nega GitHub Muhim?",
        "date": "24 Mart, 2024",
        "content": "GitHub — bu faqat kod saqlanadigan joy emas, balki sizning professional profilingiz. Loyihalaringizni joylashtiring, `README` yozing, open-source loyihalarda qatnashing. Ish beruvchilar GitHub sahifangiz orqali sizning real tajribangizni ko‘radi. Har bir push — bu o‘sish bosqichi."
    },
    {
        "title": "API Bilan Ishlashni O‘rganing",
        "date": "21 Mart, 2024",
        "content": "Bugungi kunda API’ni bilmagan dasturchi deyarli mavjud emas. Telegram botlaridan tortib ob-havo dasturlarigacha — hammasi API orqali ishlaydi. Python’da `requests` yoki `httpx` bilan so‘rov yuboring, ma’lumotni JSON formatda qayta ishlang. Shu orqali siz real dunyo ilovalari bilan muloqot qiladigan kod yozishni o‘rganasiz."
    }
]


def index(request):
    data = {
        "posts" : songgi_yangiliklar

    }
    return render(request, "blog/index.html", data)

def sport(request):
    data = {
        "posts" : sport_postlari
    }
    return render(request, "blog/sport.html", data)

def dasturlash(request):
    data = {
        "posts" : dasturlash_postlari
    }
    return render(request, "blog/dasturlash.html", data)