import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasından gizli anahtarı al
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print(f"🔑 Test Edilen API Key: {api_key[:5]}... (Gizlilik için kırpıldı)\n")

try:
    # Google'a bağlan
    genai.configure(api_key=api_key)

    print("📦 Bu API Anahtarı ile Erişebildiğin Modeller:")
    print("-" * 40)

    # Sadece metin üretebilen modelleri listele
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ {m.name}")

    print("-" * 40)
    print("🎯 Sistem Testi Tamamlandı!")

except Exception as e:
    print(f"❌ BAĞLANTI HATASI: {e}")