# ESP-Project

```mermaid
graph LR
    A["🟨 Aquisição de Sinal"] --> B["🟦 Amplificador de Instrumentação"]
    B --> C["🟦 Filtro Passa Altas"]
    C --> D["🟦 Filtro Passa Baixas"]
    D --> E["🟦 Filtro Notch"]
    E --> F["🖥️ Osciloscópio"]

    style A fill:#fff8b0,stroke:#333,stroke-width:1px
    style B fill:#b5b3ff,stroke:#333,stroke-width:1px
    style C fill:#b3f5ff,stroke:#333,stroke-width:1px
    style D fill:#b3f5ff,stroke:#333,stroke-width:1px
    style E fill:#b3f5ff,stroke:#333,stroke-width:1px
