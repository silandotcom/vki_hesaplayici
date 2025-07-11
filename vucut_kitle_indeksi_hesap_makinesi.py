while True: # geçersiz bir değer girilmesi durumunda tekrar veri girişi istemesi için while loop'u
    try: # geçerli değerler olması için try
        kg = int(input("Kilonuzu girin: "))
        boy = float(input("Boyunuzu metre cinsinden girin: "))
        if boy < 1 or boy > 2.5:
            raise ValueError("Boy metre cinsinden 1 ile 2.5 arasında olmalı.")
        bmi = kg/boy**2
        print("Vucut kitle indeksi: " , bmi)
        if bmi > 45:
            print("Vücut kitle indeksiniz cok yüksek. Asiri sismansiniz. ") 
        elif bmi > 35:
            print("Vücut kitle indeksiniz cok yüksek. Saglik acisindan önemli. ") 
        elif bmi > 30:
            print("Vücut kitle indeksiniz yüksek. Şişmansiniz. ") 
        elif bmi > 25:
            print("Vücut kitle indeksiniz yüksek. Hafif şişmansiniz. ")
        elif bmi > 20:
            print("Vücut kitle indeksiniz normal. ")
        else:
            print("Vücut kitle indeksiniz dusuk. Zayifsiniz. ")
        break
    except ValueError as hata: # geçersiz değer olması durumunda hata uyarısı
        print("Ηatalı giriş:" , hata)
        print("Lütfen tekrar deneyin.")