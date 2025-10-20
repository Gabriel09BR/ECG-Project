# ESP-Project

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
