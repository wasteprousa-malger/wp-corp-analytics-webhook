# WP Corporate Analytics Webhook

Azure Function-based webhook endpoints for enterprise systems and operational platforms. Lands raw data in Azure storage and serves as an ingestion layer for Microsoft Fabric analytics pipelines.

---

## Purpose

This repository contains serverless integration services developed by the Corporate Analytics team. The primary goal is to provide a lightweight, scalable platform for receiving events, integrating with external systems, and landing raw data into Azure for downstream analytics processing.

Current use cases include:

- Webhook ingestion
- API integrations
- Event-driven automation
- Data landing and archival
- Analytics platform support

---

## Architecture

```text
External Systems
    │
    ▼
┌─────────────────────┐
│ Azure Functions     │
│ Webhook Endpoints   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Azure Storage       │
│ Raw Data Landing    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Microsoft Fabric    │
│ Bronze Layer        │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Silver Layer        │
│ Standardized Data   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Gold Layer          │
│ Reporting & BI      │
└─────────────────────┘
```

---

## Design Principles

- Serverless-first architecture
- Raw data preserved before transformation
- Managed Identity preferred over stored credentials
- Infrastructure and code managed through source control
- Support both webhook-driven and scheduled integrations
- Align with the Corporate Analytics Bronze → Silver → Gold data architecture

---

## Project Structure

```text
wp-corp-analytics-webhook/
│
├── functions/
│   └── webhook/
│
├── tests/
│
├── host.json
├── requirements.txt
├── local.settings.json
└── README.md
```

---

## Technology Stack

- Azure Functions
- Azure Storage / ADLS Gen2
- Managed Identity
- Application Insights
- GitHub
- Microsoft Fabric

---

## Data Flow

```text
Source System
      │
      ▼
Webhook Endpoint
      │
      ▼
Raw JSON Archive (ADLS Gen2)
      │
      ▼
Fabric Bronze
      │
      ▼
Fabric Silver
      │
      ▼
Fabric Gold
      │
      ▼
Reporting & Analytics
```

---

## Future Enhancements

Potential additions as the platform matures:

- Additional webhook endpoints
- Enterprise API integrations
- Automated data validation
- Metadata-driven ingestion
- Fabric orchestration integration
- Event Grid integration
- Service Bus integration
- Integration monitoring dashboards
- Centralized secrets management through Key Vault

---

## Operational Goals

- Standardize webhook ingestion patterns
- Establish a reusable integration framework
- Minimize infrastructure management through serverless services
- Maintain full-fidelity raw data archives
- Support both real-time and batch analytics workloads
- Provide a secure foundation for future integrations

---

## Status

🚧 Initial platform setup and webhook development in progress.

Current environment includes:

- Azure Function App
- Storage Account
- Application Insights
- Managed Identity
- GitHub Source Control

The first milestone is to establish a working webhook endpoint, validate end-to-end receipt of events, and persist payloads to Azure Storage for downstream ingestion into Microsoft Fabric.
