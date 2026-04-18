import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import HuggingFaceEmbeddings


# 1. Güvenlik: .env dosyasından API anahtarını gizlice yükle
load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("🚨 Kiritik Hata: GOOGLE_API_KEY bulunamadı! Lütfen .env dosyanızı kontrol edin.")


class AIOpsRAGEngine:
    def __init__(self):
        print("🧠 AIOps RAG Motoru Başlatılıyor...")
        self.vector_db_path = "../knowledge_base/chroma_db"
        self.doc_path = "../knowledge_base/huawei_runbook.txt"

        # Google Gemini Modelleri (Hem gömme hem de metin üretimi için)
        # Veri güvenliği ve sıfır maliyet için yerel açık kaynaklı Embedding kullanıyoruz
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                          temperature=0.1)  # Düşük sıcaklık = Sıfır halüsinasyon

        self.vectorstore = self._initialize_knowledge_base()

    def _initialize_knowledge_base(self):
        print("📚 Huawei Runbook Dokümanları Vektör Uzayına Yükleniyor...")

        # Resmi dokümantasyonu oku
        loader = TextLoader(self.doc_path)
        docs = loader.load()

        # Metni LLM'in rahat sindirebileceği küçük parçalara (chunk) böl
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)

        # ChromaDB (Vektör Veritabanı) oluştur ve belleğe al
        vectorstore = Chroma.from_documents(documents=splits, embedding=self.embeddings,
                                            persist_directory=self.vector_db_path)
        print("✅ Bilgi Bankası (Knowledge Base) Hazır ve Vektörleştirildi!\n")
        return vectorstore

    def resolve_ticket(self, ticket_text, k8s_logs):
        print("🔍 RAG Sistemi: Bilet ve Loglar Analiz Ediliyor...")

        # Veritabanında en alakalı dokümanları bulacak olan Retriever
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 2})

        # AI'a verdiğimiz SRE (Site Reliability Engineer) Rolü
        system_prompt = (
            "Sen Huawei Cloud CCE (Kubernetes) ekibinde çalışan Kıdemli bir SRE mühendisisin. "
            "Aşağıdaki bağlamı (Context - resmi Huawei dokümanları) kullanarak müşterinin yaşadığı sorunu analiz et. "
            "Bağlamda olmayan HİÇBİR ŞEYİ uydurma (Halüsinasyon yapma). "
            "Çıktını şu formatta ver:\n"
            "KÖK NEDEN: [Tek cümlelik tespit]\n"
            "OTONOM ÇÖZÜM KOMUTU: [Çalıştırılacak kubectl komutu]\n"
            "MÜŞTERİ NOTU: [Müşteriye yazılacak profesyonel SLA yanıtı]\n\n"
            "Bağlam (Context): {context}"
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "Müşteri Şikayeti: {ticket}\n\nKubernetes Logları: {logs}")
        ])

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Zinciri (Chain) Kur: Soruyu al -> Doküman bul -> Prompt'a ekle -> Gemini'ye yolla -> Metin Çıktısı Al
        rag_chain = (
                {"context": retriever | format_docs, "ticket": RunnablePassthrough(), "logs": RunnablePassthrough()}
                | prompt
                | self.llm
                | StrOutputParser()
        )

        print("⚙️ Gemini LLM, dokümanları kullanarak otonom çözüm üretiyor...\n")

        # LLM'i tetikle
        solution = rag_chain.invoke({"ticket": ticket_text, "logs": k8s_logs})
        return solution


if __name__ == "__main__":
    # Test Senaryosu
    sample_ticket = "Tr-west-1 bölgesindeki web sitemiz 502 veriyor, acil destek."
    sample_logs = "java.lang.OutOfMemoryError: Java heap space... Reason: OOMKilled"

    engine = AIOpsRAGEngine()
    result = engine.resolve_ticket(sample_ticket, sample_logs)

    print("🎯 OTONOM RAG ÇÖZÜMÜ:")
    print("-" * 40)
    print(result)
    print("-" * 40)