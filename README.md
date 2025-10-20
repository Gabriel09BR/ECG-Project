# ECG Signal Acquisition and Visualization System

This project consists of the development of a simple electrocardiograph (ECG) capable of acquiring, amplifying, filtering, and visualizing bioelectrical cardiac signals in real time using an ESP32 microcontroller.  
The processed data is sent to a computer or web dashboard for visualization and analysis.

## System Overview

The following diagram shows the main processing stages:

```mermaid
graph LR
    A["Signal Acquisition"] --> B["Instrumentation Amplifier"]
    B --> C["High-Pass Filter"]
    C --> D["Low-Pass Filter"]
    D --> E["Notch Filter"]
    E --> F["🌐 Web Dashboard"]

    %% Block styles
    style A fill:#fff8b0,stroke:#333,stroke-width:1px,color:#000
    style B fill:#b5b3ff,stroke:#333,stroke-width:1px,color:#000
    style C fill:#b3f5ff,stroke:#333,stroke-width:1px,color:#000
    style D fill:#b3f5ff,stroke:#333,stroke-width:1px,color:#000
    style E fill:#b3f5ff,stroke:#333,stroke-width:1px,color:#000
    style F fill:#d3ffd3,stroke:#333,stroke-width:1px,color:#000

## How It Works

1. The ECG signal is acquired from the electrodes.
2. The signal is amplified by the instrumentation amplifier.
3. Filters remove noise and unwanted frequencies (e.g., 60 Hz power-line interference).
4. The processed signal is digitized by the ESP32 ADC.
5. Data is transmitted to a computer or visualized in real time through a web dashboard.
