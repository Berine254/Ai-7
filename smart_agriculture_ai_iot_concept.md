## 2. Smart Agriculture – AI-IoT Concept & Diagram

### 📜 Proposal Summary

- **Sensors:**
    - Soil Moisture Sensor (e.g., YL-69)
    - Temperature Sensor (e.g., DHT11)
    - Humidity Sensor (e.g., DHT22)
    - Sunlight Sensor (e.g., BH1750)
- **AI Model:**
    - Random Forest Regressor trained on soil & weather data to predict crop yield.
- **Edge Device:**
    - Raspberry Pi or ESP32 for local processing.

---

### 📊 Data Flow Diagram

```
+---------------------+        +---------------------+
|   IoT Sensors       | -----> |   Edge Device       | -----> | 
|   Farm Dashboard    |        |   (ESP32 or Pi)     |        |
| - Soil Moisture     |        | - Runs AI Model     |        |
| - Temperature       |        +---------------------+        |
| - Humidity          |                                   |
| - Light Intensity   |                                   |
+---------------------+                                   |
                                                          |
                <-----------------------------------------+
                |          View Predictions & Irrigation  |
                +-----------------------------------------+
```