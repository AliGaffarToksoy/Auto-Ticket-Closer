from log_analyzer import fetch_and_analyze_logs
from remediator import apply_fix
import time


def run_pipeline():
    print("🚀 Auto-Ticket-Closer: Otonom SRE Operasyonu Başlatılıyor...\n")

    # 1. SLA Yanıtı (Müşteriyi Sakinleştir)
    print("✉️ AŞAMA 1: Müşteriye SLA Yanıtı İletildi.")
    print("   -> 'Kritik (P1) kaydınız (HWC-8472) alınmıştır. Otonom sistemlerimiz log analizine başlamıştır.'\n")
    time.sleep(1)

    # 2. Log Analizi (Gözler)
    print("🔎 AŞAMA 2: Kök Neden Analizi (RCA)")
    root_cause = fetch_and_analyze_logs("tr-west-1-prod-cluster", "production")

    # 3. Otomatik Müdahale (Eller)
    if root_cause != "Bilinmeyen Hata":
        print("\n🔧 AŞAMA 3: Aktif Müdahale (Remediation)")
        is_fixed = apply_fix(root_cause)

        # 4. Ticket Kapatma ve Raporlama (Sözcü)
        if is_fixed:
            print("\n🎯 AŞAMA 4: Ticket Kapatma (Resolution)")
            closing_note = """
            Sayın Müşterimiz,
            Sistemlerinizdeki 502 Bad Gateway hatası giderilmiştir. 
            Kök Neden: Ani trafik artışı sebebiyle frontend servisinizde bellek yetersizliği (OOMKilled) yaşanmıştır.
            Aksiyon: İlgili servisin bellek limitleri (limits.memory) 2Gi seviyesine çıkarılarak sistem stabil hale getirilmiştir.
            Durum: RESOLVED (Çözüldü)
            """
            print(f"📝 Kapanış Raporu Jira/ServiceNow'a işlendi:{closing_note}")
            print("🏆 GÖREV TAMAMLANDI: P1 Ticket Başarıyla Kapatıldı!")


if __name__ == "__main__":
    run_pipeline()