"""Lab 05 - Yeniden kullanılabilir kargo teklifi (shipping quote).

Kurallar (istersen ödevdeki değerlere göre değiştir):
- Ara toplam >= 100 TL ise %10 indirim, değilse indirim yok.
- İndirimli tutar >= 150 TL ise kargo ücretsiz, değilse 29.90 TL.
"""

DISCOUNT_THRESHOLD = 100.0   # indirim için alt sınır
DISCOUNT_RATE = 0.10         # indirim oranı
FREE_SHIPPING_THRESHOLD = 150.0
SHIPPING_FEE = 29.90


def calculate_subtotal(items):
    """items: (birim_fiyat, adet) çiftlerinden oluşan liste. Ara toplamı döndürür."""
    total = 0.0
    for price, quantity in items:
        total += price * quantity
    return round(total, 2)


def calculate_discount_rate(subtotal):
    """Ara toplama göre indirim oranını (0.0 - 1.0) döndürür."""
    if subtotal >= DISCOUNT_THRESHOLD:
        return DISCOUNT_RATE
    return 0.0


def calculate_shipping_fee(discounted_amount):
    """İndirimli tutara göre kargo ücretini döndürür."""
    if discounted_amount >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return SHIPPING_FEE


def calculate_final_total(items):
    """Diğer üç fonksiyonu kullanarak nihai toplamı döndürür."""
    subtotal = calculate_subtotal(items)
    rate = calculate_discount_rate(subtotal)
    discounted = subtotal * (1 - rate)
    fee = calculate_shipping_fee(discounted)
    return round(discounted + fee, 2)


def print_quote(name, items):
    """Teklifi ekrana YAZAR (print). Hiçbir şey döndürmez (None)."""
    subtotal = calculate_subtotal(items)
    rate = calculate_discount_rate(subtotal)
    fee = calculate_shipping_fee(subtotal * (1 - rate))
    total = calculate_final_total(items)
    print(f"--- {name} ---")
    print(f"Ara toplam : {subtotal:.2f} TL")
    print(f"İndirim    : %{rate * 100:.0f}")
    print(f"Kargo      : {fee:.2f} TL")
    print(f"Toplam     : {total:.2f} TL")


# print ve return farkı:
# - return: değeri fonksiyonu çağıran koda GERİ VERİR; değişkene atanır,
#   başka hesapta kullanılır, assert ile test edilir.
# - print: değeri sadece EKRANA yazar; fonksiyonun sonucu None olur,
#   yani başka kod bu değeri kullanamaz.


if __name__ == "__main__":
    # Aynı kod iki sipariş için döngüyle tekrar kullanılıyor (kopyalama yok).
    orders = {
        "Sipariş 1 (küçük)": [(20.0, 2), (15.5, 1)],
        "Sipariş 2 (büyük)": [(60.0, 2), (45.0, 2)],
    }
    for order_name, order_items in orders.items():
        print_quote(order_name, order_items)

    # Testler
    assert calculate_subtotal([(20.0, 2), (15.5, 1)]) == 55.5
    assert calculate_discount_rate(99.99) == 0.0    # eşiğin hemen altı
    assert calculate_discount_rate(100.0) == 0.10   # tam eşik (sınır)
    assert calculate_shipping_fee(149.99) == 29.90  # ücretsiz kargo sınırının altı
    assert calculate_shipping_fee(150.0) == 0.0     # tam sınır
    assert calculate_final_total([(20.0, 2), (15.5, 1)]) == 85.4
    assert calculate_final_total([(60.0, 2), (45.0, 2)]) == 189.0
    print("Tüm testler geçti.")