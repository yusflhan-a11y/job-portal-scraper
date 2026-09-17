import requests
from bs4 import BeautifulSoup

url = "https://www.youthall.com/tr/is-ilanlari/"

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
           } # Bu bölümde bilgisayar programımıza insan görünümü kazandırıyoruz. Yani bilgisayar programımızın bir tarayıcı gibi davranmasını sağlıyoruz.

response = requests.get(url, headers=headers) 
# requests kütüphanesi ile url adresine istek gönderiyoruz. Bu istek sonucunda bize bir response dönecek.
response.encoding = "utf-8" 
# response'un encoding türünü utf-8 olarak ayarlıyoruz. Bu sayede Türkçe karakterler doğru bir şekilde görüntülenecek.

if response.status_code == 200: 
    # Eğer response'un status code'u 200 ise yani istek başarılı ise
    print("İstek başarili. Sayfa içeriği alindi.") 
    # Başarılı olduğunu ekrana yazdırıyoruz.
    soup = BeautifulSoup(response.text, "html.parser") 
    # response'un text kısmını Beautiful Soup kütüphanesi ile parse ediyoruz. Yani html kodlarını daha kolay bir şekilde işleyebilmek için BeautifulSoup kütüphanesini kullanıyoruz.

    title = soup.title.string
    print("Sayfa Basligi:" ,title) 
    # Sayfanın başlığını ekrana yazdırıyoruz.
else:
    print("İstek basarisiz. Status code:", response.status_code) 
    # Eğer istek başarısız ise status code'u ekrana yazdırıyoruz.