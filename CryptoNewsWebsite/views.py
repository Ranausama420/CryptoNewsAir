from django.shortcuts import render, get_object_or_404
import json
from crypto_news_api import CryptoControlAPI
from datetime import datetime
from .models import newsdata, topnewsdata, bitcoinnewsdata, ripplenewsdata, ethereumnewsdata
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.conf import settings
from isodate import parse_duration
# noimcs api 0f6a657c7f9f4a9f6f3423eb8ed7648f
from urllib.parse import urlparse


# youtube AIzaSyAk3UoGTfZfjkKlFP6XSrPFBzl7mt2l2SY
# Create your views here.

def index(request):
    # Coin details
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cbitcoin-cash%2Cbitcoin-cash-sv%2Ctether%2Cripple%2Ccardano%2Ctezos%2Cchainlink&sparkline=false&price_change_percentage=24h'
    datarequest = requests.get(url)
    data = json.loads(datarequest.content)
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin%2Cbinancecoin%2Ccrypto-com-chain%2Ceos%2Cstellar%2Ctron%2Cmonero%2Cvechain%2Cusd-coin&sparkline=false&price_change_percentage=24h'
    datarequest1 = requests.get(url1)
    data1 = json.loads(datarequest1.content)
    url2 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=huobi-token%2Cethereum-classic%2Cneo%2Ccosmos%2Ciota%2Cdash%2Czcash%2Cdogecoin%2Chedgetrade&sparkline=false&price_change_percentage=24h'
    datarequest2 = requests.get(url2)
    data2 = json.loads(datarequest2.content)

    # For news
    api = CryptoControlAPI("464cd273a240ec567bf16e9cb74e308a")
    news = api.getLatestNews("en")
    news1 = api.getTopNews("en")
    bit = api.getLatestNewsByCoin('bitcoin')
    xrp = api.getLatestNewsByCoin('ripple')
    eth = api.getLatestNewsByCoin('ethereum')
    # for li in news1:
    #     f = open("data.txt", "a")
    #     for keys in li:
    #         # print(keys)
    #         f.write(keys + "\n")

    frmtdate = []
    frmtdate1 = []
    frmtdate2 = []
    frmtdate3 = []
    frmtdate4 = []
    for li in news:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        try:
            databaseobj = newsdata(idbyapi=li["_id"], hotness=li["hotness"], activityHotness=li["activityHotness"],
                                   primaryCategory=li["primaryCategory"], words=li["words"],
                                   similarArticles=li["similarArticles"],
                                   coins=li["coins"], description=li["description"], publishedAt=li["publishedAt"],
                                   title=li["title"], url=li["url"], source=li["source"],
                                   sourceDomain=li["sourceDomain"], originalImageUrl=li["originalImageUrl"])
            if newsdata.objects.filter(idbyapi=li["_id"]).exists():
                dum = "already exist"
            else:
                databaseobj.save()

        except Exception as e:
            print(str(e))
    for li in news1:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate1.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        try:
            databaseobj = topnewsdata(idbyapi=li["_id"], hotness=li["hotness"], activityHotness=li["activityHotness"],
                                      primaryCategory=li["primaryCategory"], words=li["words"],
                                      similarArticles=li["similarArticles"],
                                      coins=li["coins"], description=li["description"], publishedAt=li["publishedAt"],
                                      title=li["title"], url=li["url"], source=li["source"],
                                      sourceDomain=li["sourceDomain"], originalImageUrl=li["originalImageUrl"])
            if topnewsdata.objects.filter(idbyapi=li["_id"]).exists():
                dum = "already exist"
            else:
                databaseobj.save()

        except Exception as e:
            print(str(e))
    for li in bit:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        try:
            databaseobj = bitcoinnewsdata(idbyapi=li["_id"], hotness=li["hotness"],
                                          activityHotness=li["activityHotness"],
                                          primaryCategory=li["primaryCategory"], words=li["words"],
                                          similarArticles=li["similarArticles"],
                                          coins=li["coins"], description=li["description"],
                                          publishedAt=li["publishedAt"],
                                          title=li["title"], url=li["url"], source=li["source"],
                                          sourceDomain=li["sourceDomain"], originalImageUrl=li["originalImageUrl"])
            if bitcoinnewsdata.objects.filter(idbyapi=li["_id"]).exists():
                dum = "already exist"
            else:
                databaseobj.save()

        except Exception as e:
            print(str(e))
    for li in xrp:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate3.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        try:
            databaseobj = ripplenewsdata(idbyapi=li["_id"], hotness=li["hotness"],
                                         activityHotness=li["activityHotness"],
                                         primaryCategory=li["primaryCategory"], words=li["words"],
                                         similarArticles=li["similarArticles"],
                                         coins=li["coins"], description=li["description"],
                                         publishedAt=li["publishedAt"],
                                         title=li["title"], url=li["url"], source=li["source"],
                                         sourceDomain=li["sourceDomain"], originalImageUrl=li["originalImageUrl"])
            if ripplenewsdata.objects.filter(idbyapi=li["_id"]).exists():
                dum = "already exist"
            else:
                databaseobj.save()
        except Exception as e:
            print(str(e))
    for li in eth:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate4.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        try:
            databaseobj = ethereumnewsdata(idbyapi=li["_id"], hotness=li["hotness"],
                                           activityHotness=li["activityHotness"],
                                           primaryCategory=li["primaryCategory"], words=li["words"],
                                           similarArticles=li["similarArticles"],
                                           coins=li["coins"], description=li["description"],
                                           publishedAt=li["publishedAt"],
                                           title=li["title"], url=li["url"], source=li["source"],
                                           sourceDomain=li["sourceDomain"], originalImageUrl=li["originalImageUrl"])
            if ethereumnewsdata.objects.filter(idbyapi=li["_id"]).exists():
                dum = "already exist"
            else:
                databaseobj.save()
        except Exception as e:
            print(str(e))

    context = {
        'data': data,
        'data1': data1,
        'data2': data2,
        'news': news,
        "news1zip": zip(news1, frmtdate1),
        "zipdata": zip(news[3:15], frmtdate[3:15]),
        "frmtdate": frmtdate,
        "tdnews": zip(news[12:25], frmtdate[12:25]),
        "tdnews1": zip(news[25:], frmtdate[25:]),
        'bit': zip(bit[10:18], frmtdate2[10:18]),
        'xrp': zip(xrp[10:18], frmtdate3[10:18]),
        'eth': zip(eth[10:18], frmtdate4[10:18])

    }

    return render(request, 'CryptoNewsWebsite/index.html', context)


def singlepost(request, title):
    newsobj = get_object_or_404(newsdata, title=title)

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cbitcoin-cash%2Cbitcoin-cash-sv%2Cripple&sparkline=false&price_change_percentage=24h'
    datarequest = requests.get(url)
    data = json.loads(datarequest.content)
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin%2Cbinancecoin%2Ccrypto-com-chain%2Ceos%2Cstellar%2Ctron%2Cmonero%2Cvechain%2Cusd-coin%2chuobi-token%2Cethereum-classic%2Cneo%2Ccosmos%2Ciota%2Cdash%2Czcash%2Cdogecoin%2Chedgetrade&sparkline=false&price_change_percentage=24h'
    datarequest1 = requests.get(url1)
    data1 = json.loads(datarequest1.content)

    page = requests.get(newsobj.url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paras = soup.find_all('p')

    paralist = []
    f = open("data.txt", "w")
    f.write(newsobj.url)
    for i in range(len(paras)):
        print(i)
        # f.write(str(i)+"\n")
        # f.write(paras[i].text+"\n")
        print(paras[i].text)
        paralist.append(paras[i].text)

    context = {
        'newsobj': newsobj,
        'data': data,
        'data1': data1,
        'paras': paralist
    }

    return render(request, 'CryptoNewsWebsite/single-post.html', context)


def catagory(request, title):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cbitcoin-cash%2Cbitcoin-cash-sv%2Cripple&sparkline=false&price_change_percentage=24h'
    datarequest = requests.get(url)
    data = json.loads(datarequest.content)
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin%2Cbinancecoin%2Ccrypto-com-chain%2Ceos%2Cstellar%2Ctron%2Cmonero%2Cvechain%2Cusd-coin%2chuobi-token%2Cethereum-classic%2Cneo%2Ccosmos%2Ciota%2Cdash%2Czcash%2Cdogecoin%2Chedgetrade&sparkline=false&price_change_percentage=24h'
    datarequest1 = requests.get(url1)
    data1 = json.loads(datarequest1.content)
    # For news
    api = CryptoControlAPI("464cd273a240ec567bf16e9cb74e308a")
    news = api.getLatestNews("en")
    news1 = api.getTopNews("en")
    frmtdate = []
    frmtdate1 = []
    frmtdate2 = []
    for li in news:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
    for li in news1:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate1.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
    if title == 'latest':
        str = 'latest'
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(news, frmtdate),
        }
    if title == 'Bitcoin News':
        str = 'Bitcoin News'
        bit = bitcoinnewsdata.objects.all().order_by('-publishedAt')
        paginator = Paginator(bit, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        print(type(page_number))
        page_obj = paginator.get_page(page_number)
        for li in bit:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Ripple News':
        str = 'Ripple News'
        xrp = ripplenewsdata.objects.all().order_by('-publishedAt')
        paginator = Paginator(xrp, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in xrp:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Ethereum News':
        str = 'Ethereum News'
        eth = ethereumnewsdata.objects.all().order_by('-publishedAt')
        paginator = Paginator(eth, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in eth:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Blockchain News':
        str = 'Blockchain News'
        newsobj = newsdata.objects.filter(primaryCategory='Blockchain').order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Mining News':
        str = 'Mining News'
        newsobj = newsdata.objects.filter(primaryCategory='Mining').order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Analysis News':
        str = 'Analysis News'
        newsobj = newsdata.objects.filter(primaryCategory='Analysis').order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'Exchanges News':
        str = 'Exchanges News'
        newsobj = newsdata.objects.filter(primaryCategory='Exchanges').order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'General News':
        str = 'General News'
        newsobj = newsdata.objects.filter(primaryCategory='General').order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }
    if title == 'All News':
        str = 'All News'
        newsobj = newsdata.objects.all().order_by('-publishedAt')
        paginator = Paginator(newsobj, 25)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for li in newsobj:
            dateinstring = li.publishedAt
            dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
            frmtdate2.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))
        context = {
            'latest': str,
            'data': data,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            "tdnews": zip(page_obj, frmtdate2),
            'page_obj': page_obj
        }

    return render(request, 'CryptoNewsWebsite/catagory.html', context)


def videos(request, title):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cbitcoin-cash%2Cbitcoin-cash-sv%2Cripple&sparkline=false&price_change_percentage=24h'
    datarequest = requests.get(url)
    data = json.loads(datarequest.content)
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin%2Cbinancecoin%2Ccrypto-com-chain%2Ceos%2Cstellar%2Ctron%2Cmonero%2Cvechain%2Cusd-coin%2chuobi-token%2Cethereum-classic%2Cneo%2Ccosmos%2Ciota%2Cdash%2Czcash%2Cdogecoin%2Chedgetrade&sparkline=false&price_change_percentage=24h'
    datarequest1 = requests.get(url1)
    data1 = json.loads(datarequest1.content)
    api = CryptoControlAPI("464cd273a240ec567bf16e9cb74e308a")
    news1 = api.getTopNews("en")
    frmtdate1 = []
    for li in news1:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate1.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))

    url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    videos = []
    params = {
        'part': 'snippet',
        'q': title,
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9,
        'type': 'video'
    }
    r = requests.get(url, params=params)

    results = r.json()['items']
    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])
    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet,contentDetails',
        'id': ','.join(video_ids),
        'maxResults': 9
    }
    r = requests.get(video_url, params=video_params)
    results = r.json()['items']

    for result in results:
        dateinstring = result['snippet']['publishedAt']
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%SZ')
        p = dateobj.strftime('%d/%m/%Y'),

        video_data = {
            'title': result['snippet']['title'],
            'date': dateobj.strftime('%d/%m/%Y'),
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={result["id"]}',
            'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail': result['snippet']['thumbnails']['high']['url']
        }

        videos.append(video_data)

    context = {
        'videos': videos,
        'latest': title,
        'data': data,
        'data1': data1,
        "news1zip": zip(news1, frmtdate1),

    }

    return render(request, 'CryptoNewsWebsite/videos.html', context)

def marketcap(request, page):
    url = 'https://api.coingecko.com/api/v3/global'
    datarequest = requests.get(url)
    gdata = json.loads(datarequest.content)

    if page == 1:
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=150&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d'
        datarequest = requests.get(url)
        data = json.loads(datarequest.content)
        # for d in data:
        #     print(d['market_cap_rank'])

        context = {
            'data': data,
            'gdata': gdata
        }
    if page > 1:
        print(page)
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=150&page=" + str(
            page) + "&sparkline=false&price_change_percentage=1h%2C24h%2C7d"
        print(url)
        datarequest = requests.get(url)
        data = json.loads(datarequest.content)
        for d in data:
            print(d['market_cap_rank'])

        context = {
            'data': data,
            'gdata': gdata
        }



    return render(request, 'CryptoNewsWebsite/marketcap.html', context)

def exchange(request,page):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cbitcoin-cash%2Cbitcoin-cash-sv%2Cripple&sparkline=false&price_change_percentage=24h'
    datarequest = requests.get(url)
    coindata = json.loads(datarequest.content)
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin%2Cbinancecoin%2Ccrypto-com-chain%2Ceos%2Cstellar%2Ctron%2Cmonero%2Cvechain%2Cusd-coin%2chuobi-token%2Cethereum-classic%2Cneo%2Ccosmos%2Ciota%2Cdash%2Czcash%2Cdogecoin%2Chedgetrade%2cmaker&sparkline=false&price_change_percentage=24h'
    datarequest1 = requests.get(url1)
    data1 = json.loads(datarequest1.content)
    api = CryptoControlAPI("464cd273a240ec567bf16e9cb74e308a")
    news1 = api.getTopNews("en")
    frmtdate1 = []
    for li in news1:
        dateinstring = li["publishedAt"]
        dateobj = datetime.strptime(dateinstring, '%Y-%m-%dT%H:%M:%S.%fZ')
        frmtdate1.append(dateobj.strftime('%d-%m-%Y %I:%M %p'))


    if page == 1:
        url = 'https://api.coingecko.com/api/v3/exchanges?per_page=50&page=1'
        datarequest = requests.get(url)
        data = json.loads(datarequest.content)
        scores= []
        for score in data:
            scores.append(score['trust_score'])



        context = {
            'data': data,
            'scores': scores,
            'coindata': coindata,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            'page':page

        }
    if page > 1:
        print(page)
        url = "https://api.coingecko.com/api/v3/exchanges?per_page=50&page="+str(page)
        print(url)
        datarequest = requests.get(url)
        data = json.loads(datarequest.content)
        context = {
            'data': data,
            'coindata': coindata,
            'data1': data1,
            "news1zip": zip(news1, frmtdate1),
            'page': page

        }

    return render(request, 'CryptoNewsWebsite/exchange.html', context)