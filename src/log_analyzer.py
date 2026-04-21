import time


def fetch_and_analyze_logs(cluster_name, namespace):
    print(f"📡 Otonom Sistem: '{cluster_name}' kümesindeki '{namespace}' ortamına bağlanılıyor...")
    time.sleep(1)  # Gerçekçilik efekti
    print("🔎 Otonom Sistem: Çöken Pod'ların son 50 satırlık logları taranıyor...\n")


    simulated_k8s_logs = """
    [INFO] 2026-04-17 15:42:01 - FastAPI application started successfully.
    [INFO] 2026-04-17 15:45:12 - Handling incoming traffic spike (1000 req/sec)...
    [WARN] 2026-04-17 15:46:05 - Memory usage exceeded 85% threshold.
    [WARN] 2026-04-17 15:46:10 - Memory usage at 95%, garbage collection failed.
    [FATAL] 2026-04-17 15:46:12 - java.lang.OutOfMemoryError: Java heap space
    [ERROR] 2026-04-17 15:46:13 - Pod Name: ecommerce-frontend-7f8b9c-xyz12
    [ERROR] 2026-04-17 15:46:13 - Reason: OOMKilled (Out Of Memory)
    [INFO] 2026-04-17 15:46:14 - Kubernetes is attempting to restart the container... CrashLoopBackOff.
    """

    print("--- 📋 KUBERNETES CRASH LOGLARI ---")
    print(simulated_k8s_logs)
    print("----------------------------------\n")

    # Otonom Kök Neden Analizi (RCA)
    if "OOMKilled" in simulated_k8s_logs or "OutOfMemoryError" in simulated_k8s_logs:
        root_cause = "OOMKilled (Bellek Yetersizliği)"
        print(f"🚨 TESPİT EDİLEN KÖK NEDEN: {root_cause}")
        return root_cause

    return "Bilinmeyen Hata"


if __name__ == "__main__":
    fetch_and_analyze_logs("tr-west-1-prod-cluster", "production")