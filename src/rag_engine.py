import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings



load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("🚨 Kiritik Hata: GOOGLE_API_KEY bulunamadı! Lütfen .env dosyanızı kontrol edin.")


class AIOpsRAGEngine:
    def __init__(self):
        print("🧠 AIOps RAG Motoru Başlatılıyor...")
        # Dosya yollarını Docker veya Lokal fark etmeksizin dinamik olarak bul
        current_dir = os.path.dirname(os.path.abspath(__file__))  # src klasörü
        base_dir = os.path.dirname(current_dir)  # Ana proje klasörü

        self.vector_db_path = os.path.join(base_dir, "knowledge_base", "chroma_db")
        self.doc_path = os.path.join(base_dir, "knowledge_base", "huawei_runbook.txt")


        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.1)

        self.vectorstore = self._initialize_knowledge_base()

    def _initialize_knowledge_base(self):
        print("📚 Huawei Runbook Dokümanları Vektör Uzayına Yükleniyor...")


        loader = TextLoader(self.doc_path)
        docs = loader.load()


        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)


        vectorstore = Chroma.from_documents(documents=splits, embedding=self.embeddings,
                                            persist_directory=self.vector_db_path)
        print("✅ Bilgi Bankası (Knowledge Base) Hazır ve Vektörleştirildi!\n")
        return vectorstore

    def resolve_ticket(self, ticket_text, k8s_logs):
        print("🔍 RAG Sistemi: Bilet ve Loglar Analiz Ediliyor...")

        # 1. Aşama: Retriever ile Vektör Veritabanında Arama Yap
        # Retriever bir 'string' bekler, o yüzden aramayı loglardaki hata mesajıyla yapıyoruz.
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": 2})
        relevant_docs = retriever.invoke(k8s_logs)

        # Gelen dokümanları tek bir metne dönüştür
        context_text = "\n\n".join(doc.page_content for doc in relevant_docs)

        # 2. Aşama: AI'a SRE Rolü ve Bağlamı (Context) Ver
        system_prompt = (
            "Sen Huawei Cloud CCE (Kubernetes) ekibinde çalışan Kıdemli bir SRE mühendisisin. "
            "Aşağıdaki resmi dokümantasyon bağlamını (SOP) HARFİYEN uygulamak zorundasın.\n\n"
            f"BAĞLAM (RESMİ DOKÜMAN): \n{context_text}\n\n"
            "KURALLAR:\n"
            "1. KÖK NEDEN: Bağlamdan yola çıkarak loglardaki spesifik isimlerle tespit yap.\n"
            "2. OTONOM ÇÖZÜM KOMUTU: Asla 'get' veya 'describe' gibi pasif komutlar önerme! Doğrudan SOP'deki AKSİYON komutunu (örn: kubectl apply -f secret.yaml) loglardaki isme göre uyarla.\n"
            "3. MÜŞTERİ NOTU: Müşteriye 'şunu yapın' deme. Çözümü BİZİM uyguladığımızı ve kesintinin giderildiğini profesyonel bir SLA diliyle anlat.\n\n"
            "Çıktını KÖK NEDEN, OTONOM ÇÖZÜM KOMUTU ve MÜŞTERİ NOTU başlıklarıyla ver."
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", f"Müşteri Şikayeti: {ticket_text}\n\nKubernetes Logları: {k8s_logs}")
        ])

        # 3. Aşama: Basit ve Temiz Zincir (Prompt -> LLM -> String Output)
        rag_chain = prompt | self.llm | StrOutputParser()

        print("⚙️ Gemini LLM, dokümanları kullanarak otonom çözüm üretiyor...\n")

        # LLM'i tetikle (Artık retriever burada çalışmıyor, veriyi önceden aldık)
        solution = rag_chain.invoke({})
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