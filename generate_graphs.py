import pandas as pd
import matplotlib.pyplot as plt

# Read experimental results
df = pd.read_csv("results/workload_results.csv")

# 1. Concurrent Requests vs Response Time
plt.figure()
plt.plot(df["Concurrent Requests"], df["Response Time (ms)"], marker="o")
plt.xlabel("Concurrent Requests")
plt.ylabel("Average Response Time (ms)")
plt.title("Concurrent Requests vs Average Response Time")
plt.grid(True)
plt.savefig("results/response_time.png", dpi=300, bbox_inches="tight")
plt.close()

# 2. Concurrent Requests vs Throughput
plt.figure()
plt.plot(df["Concurrent Requests"], df["Throughput (req/s)"], marker="o")
plt.xlabel("Concurrent Requests")
plt.ylabel("Throughput (requests/sec)")
plt.title("Concurrent Requests vs Throughput")
plt.grid(True)
plt.savefig("results/throughput.png", dpi=300, bbox_inches="tight")
plt.close()

# 3. Concurrent Requests vs CPU Utilization
plt.figure()
plt.plot(df["Concurrent Requests"], df["Item CPU (%)"], marker="o", label="Item Service")
plt.plot(df["Concurrent Requests"], df["Handover CPU (%)"], marker="o", label="Handover Service")
plt.plot(df["Concurrent Requests"], df["User CPU (%)"], marker="o", label="User Service")
plt.xlabel("Concurrent Requests")
plt.ylabel("CPU Utilization (%)")
plt.title("Concurrent Requests vs CPU Utilization")
plt.legend()
plt.grid(True)
plt.savefig("results/cpu_utilization.png", dpi=300, bbox_inches="tight")
plt.close()

# 4. Concurrent Requests vs Memory Utilization
plt.figure()
plt.plot(df["Concurrent Requests"], df["Item Memory (MiB)"], marker="o", label="Item Service")
plt.plot(df["Concurrent Requests"], df["Handover Memory (MiB)"], marker="o", label="Handover Service")
plt.plot(df["Concurrent Requests"], df["User Memory (MiB)"], marker="o", label="User Service")
plt.xlabel("Concurrent Requests")
plt.ylabel("Memory Usage (MiB)")
plt.title("Concurrent Requests vs Memory Utilization")
plt.legend()
plt.grid(True)
plt.savefig("results/memory_utilization.png", dpi=300, bbox_inches="tight")
plt.close()

print("All 4 graphs generated successfully.")