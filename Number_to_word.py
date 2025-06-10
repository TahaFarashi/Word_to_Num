vahed = ["", "هزار", "میلیون", "میلیارد", "تریلیون", "کوادریلیون"]

def three_digit_to_words(number):
    """تبدیل عدد سه‌رقمی به متن فارسی"""
    units = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    tens = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    teens = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
    hundreds = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]

    words = []
    
    if number >= 100:
        words.append(hundreds[number // 100])
        number %= 100
    
    if 10 <= number < 20:
        words.append(teens[number - 10])
        number = 0  
    
    if number >= 20:
        words.append(tens[number // 10])
        number %= 10
    
    if number > 0:
        words.append(units[number])
    
    return " و ".join(words)  

def number_to_words(number):
    if number == 0:
        return "صفر"

    parts = []
    i = 0

    while number > 0:
        c = number % 1000  
        if c != 0:
            words = three_digit_to_words(c) 
            if i > 0:
                words += " " + vahed[i]  
            parts.append(words)
        number //= 1000  
        i += 1  

    return " و ".join(reversed(parts))  


while True:
    try:
        toman = int(input("لطفاً مقدار تومان را وارد کنید: "))
        break
    except ValueError:
        print("ورودی نامعتبر! لطفاً یک عدد صحیح وارد کنید.")

rial = toman * 10  
print(number_to_words(rial) + " ریال")