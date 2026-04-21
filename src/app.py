import streamlit as st
import os
from rag_engine import AIOpsRAGEngine
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Auto-Ticket-Closer | AIOps", layout="wide")

st.title("🤖 Auto-Ticket-Closer: AI-Powered SRE Assistant")
st.markdown("Huawei Cloud CCE operasyonları için otonom ticket çözüm ve doküman analiz platformu.")

# Sol panel: Ayarlar ve Doküman Yükleme
with st.sidebar:
    st.header("📚 Bilgi Bankası Yönetimi")
    uploaded_file = st.file_uploader("Çözüm rehberi veya Runbook yükle (TXT/PDF)", type=["txt", "pdf"])
    if uploaded_file:
        st.success("Doküman başarıyla yüklendi! RAG motoru için hazır.")

# Ana panel: Ticket ve Log Girişi
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎟️ Ticket Detayları")
    ticket_input = st.text_area("Müşteri şikayetini buraya yapıştırın...", height=150,
                                placeholder="Örn: tr-west-1 bölgesinde 502 hatası alıyoruz...")

with col2:
    st.subheader("📋 Sistem Logları")
    log_input = st.text_area("Kubernetes / Uygulama loglarını buraya yapıştırın...", height=150,
                             placeholder="Örn: java.lang.OutOfMemoryError: Java heap space...")

if st.button("🚀 Çözüm Üret ve Ticket'ı Analiz Et"):
    if ticket_input and log_input:
        with st.spinner("AI Mühendisi dokümanları tarıyor ve çözüm üretiyor..."):
            try:
                # RAG Motorunu tetikle
                engine = AIOpsRAGEngine()
                solution = engine.resolve_ticket(ticket_input, log_input)

                st.divider()
                st.subheader("🎯 Otonom Çözüm Raporu")
                st.info(solution)

                st.success("İşlem Tamamlandı: Çözüm önerisi hazırlandı.")
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen hem ticket detaylarını hem de logları girin.")