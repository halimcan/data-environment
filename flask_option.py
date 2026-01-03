# pylint: disable=missing-docstring

import os
# os modülü işletim sistemiyle konuşmamızı sağlar
# Environment variable'lar da işletim sistemi seviyesinde tutulur

def start():
    """returns the right message"""
    # start() fonksiyonu programın nasıl başlayacağını belirler
    # Ama bu karar kodun içinden değil, DIŞARIDAN verilecek

    env = os.getenv("FLASK_ENV")
    # FLASK_ENV adlı environment variable'ı okumaya çalışıyoruz
    # Eğer FLASK_ENV hiç set edilmemişse:
    # → env = None olur
    # Program burada crash etmez, güvenli şekilde devam eder

    if env == "development":
        # Eğer program "development" ortamında çalıştırılıyorsa
        # (örneğin local geliştirme yaparken)
        return "Starting in development mode..."
        # Debug, log, test data gibi şeyler bu modda olur

    elif env == "production":
        # Eğer program "production" ortamında çalışıyorsa
        # (gerçek kullanıcılar, gerçek veri)
        return "Starting in production mode..."
        # Güvenlik, performans ve stabilite ön plandadır

    else:
        # Eğer:
        # - FLASK_ENV hiç yoksa
        # - ya da beklenmeyen bir değer varsa
        return "Starting in empty mode..."
        # Program varsayılan (safe) bir davranışla başlar
        # Bu "defensive programming" örneğidir

if __name__ == "__main__":
    # Bu dosya doğrudan çalıştırıldığında burası devreye girer
    # (import edildiğinde çalışmaz)

    print(start())
    # start() fonksiyonunun döndürdüğü sonucu ekrana basar
    # Fonksiyonun return kullanmasının sebebi de budur

# Burada environment variable kullanarak uygulamanın çalışma modunu kontrol ediyorum.
# Kod aynı kalıyor, sadece FLASK_ENV değişerek farklı davranış elde ediliyor.
# Bu yaklaşım production, Docker ve cloud ortamlarında standarttır.”

