import platform, os
import psutil
from fastapi import FastAPI
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI(title="RPi Monitor")

CPU_USAGE = Gauge("rpi_cpu_usage_percent", "CPU usage %")
RAM_USAGE = Gauge("rpi_ram_usage_percent", "RAM usage %")
CPU_TEMP  = Gauge("rpi_cpu_temp_celsius",  "CPU temperature")
CPU_CORES = Gauge("rpi_cpu_cores",         "CPU core count")

def read_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read()) / 1000.0
    except:
        return 0.0

@app.get("/")
def info():
    return {
        "system": platform.system(),
        "arch":   platform.machine(),
        "cores":  os.cpu_count(),
        "ram_%":  psutil.virtual_memory().percent,
        "cpu_%":  psutil.cpu_percent(interval=1),
        "temp_c": read_temp(),
    }

@app.get("/metrics")
def metrics():
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    RAM_USAGE.set(psutil.virtual_memory().percent)
    CPU_TEMP.set(read_temp())
    CPU_CORES.set(os.cpu_count())
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
