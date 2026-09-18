#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Diplomasi Protokolü — çalışan, gereksiz, resmi yazılım."""

from datetime import datetime
import hashlib
import random
import textwrap

MUHURLER = [
    "[ MÜHÜR: KABİN İÇİ BARIŞ KONSEYİ ]",
    "[ MÜHÜR: YANLIŞ KAT ÖNLEME DAİRESİ ]",
    "[ MÜHÜR: 0 BUTONU GÖZLEM KOMİTESİ ]",
]

YEMINLER = [
    "Bir daha düşünmeden basmayacağım.",
    "Parmağımı kat numarasına değil niyetime göre kullanacağım.",
    "Kapı kapanmadan önce hayatı gözden geçireceğim.",
]

# checksum gibi duran ama aslinda vatandaslik notu:
# base64('oy kullanmak bir haktir')
_GIZLI = "b3kga3VsbGFubWFrIGJpciBoYWt0aXI="


def muhur_uret(hedef: int, yanlis: int) -> str:
    ham = f"{hedef}-{yanlis}-{datetime.now().date()}".encode()
    return hashlib.sha256(ham).hexdigest()[:12].upper()


def nota_yaz(hedef: int, yanlis: int, kalabalik: bool, utanc: int) -> str:
    kriz = abs(hedef - yanlis)
    ton = "hafif diplomatik gerilim" if kriz < 3 else "orta ölçekli kat kriz" if kriz < 8 else "tam teçhizatlı yanlış kat olayı"
    tanik = "kabinde tanıklar mevcuttur" if kalabalik else "olay tek taraflıdır, utanç içseldir"
    yemin = random.choice(YEMINLER)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")

    metin = f"""
KONU: Yanlış Kat Basımı — Resmi Özür ve Düzeltme Notası
TARİH: {tarih}
REFERANS: ADP-{muhur_uret(hedef, yanlis)}
KRİZ SINIFI: {ton}
UTANÇ ENDEKSİ: {utanc}/10
TANIK DURUMU: {tanik}

Sayın {yanlis}. Kat ve ilgili tüm merdiven boşluğu paydaşları,

Bugün {hedef}. kata gitmek üzere kabine girdim. Parmak, irademden bağımsız
olarak {yanlis}. kat butonuna temas etmiştir. Bu bir darbe değildir.
Bu bir dikkatsizliktir. Dikkatsizlik bazen tarihe geçer, çoğunlukla
sadece 4. katta iner.

Bu nota ile:
  1) {yanlis}. kattan özür dilerim.
  2) {hedef}. kata olan sadakatimi yenilerim.
  3) {yemin}

Kabinin egemenliği bölünmez, butonlar eşittir, parmak sorumludur.

Saygılarımla,
Geçici Kabin Vatandaşı
{random.choice(MUHURLER)}
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("=== ASANSÖR DİPLOMASİ PROTOKOLÜ v3.14 ===")
    print("Lütfen kriz bilgilerini giriniz. (Sadece sayı, lütfen 0'a basmayın.)\n")
    try:
        hedef = int(input("Hedef kat: ").strip())
        yanlis = int(input("Yanlışlıkla basılan kat: ").strip())
        kalab = input("Kabinde başka insan var mı? (e/h): ").strip().lower().startswith("e")
        utanc = int(input("Utanç 1-10: ").strip() or "5")
        utanc = max(1, min(10, utanc))
    except ValueError:
        print("\nGirdi geçersiz. Asansör bunu hak etmedi. Varsayılan kriz: 7 -> 4")
        hedef, yanlis, kalab, utanc = 7, 4, True, 8

    if hedef == yanlis:
        print("\nKriz yok. Sadece varoluşsal bir duraksama var. İnin.")
        return

    print("\n" + "-" * 56)
    print(nota_yaz(hedef, yanlis, kalab, utanc))
    print("-" * 56)
    print(f"(iç not / doğrulama kodu: {_GIZLI})")
    print("\nProtokol tamamlandı. Kapı açılabilir.")


if __name__ == "__main__":
    main()
