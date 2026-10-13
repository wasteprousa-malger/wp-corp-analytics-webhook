# Architecture Decisions

This document captures key architectural decisions for the WP Corporate Analytics Webhook platform. The goal is to record not only what decisions were made, but why they were made.

---

# ADR-001 - Preserve Raw Payloads

## Status

Accepted

## Decision

Persist all webhook payloads in raw form before any transformation, validation, or business logic is applied.

## Rationale

- Preserves source-system fidelity
- Supports replay and recovery scenarios
- Simplifies troubleshooting
- Enables future processing requirements without requiring source-system retransmission

## Implications

- Storage requirements will increase over time
- Downstream processes should treat raw data as immutable

---

# ADR-002 - Serverless First

## Status

Accepted

## Decision

Use Azure Functions as the primary compute platform for webhook ingestion and lightweight integration workloads.

## Rationale

- Low operational overhead
- Native Azure integration
- Cost-effective for event-driven workloads
- Scales automatically with demand

## Implications

- Functions should remain lightweight
- Long-running processes should be delegated to downstream services

---

# ADR-003 - Azure Storage as Landing Zone

## Status

Accepted

## Decision

Webhook payloads will be written to Azure Storage before ingestion into Microsoft Fabric.

## Rationale

- Decouples ingestion from analytics processing
- Creates an auditable system of record
- Supports replay and backfill operations
- Simplifies recovery from downstream failures

## Implications

- Storage becomes the authoritative landing zone
- Fabric consumes data from storage rather than directly from webhooks

---

# ADR-004 - Managed Identity Preferred

## Status

Accepted

## Decision

Use Managed Identity whenever Azure resources need to authenticate with other Azure services.

## Rationale

- Eliminates secret management wherever possible
- Reduces security risk
- Aligns with Azure best practices
- Simplifies credential rotation

## Implications

- RBAC assignments must be maintained
- Secret-based authentication remains an exception rather than the default

---

# ADR-005 - Source Control for All Configuration

## Status

Accepted

## Decision

Application code, infrastructure artifacts, documentation, and deployment assets should be stored in Git.

## Rationale

- Provides change history
- Supports collaboration
- Enables reproducible deployments
- Reduces configuration drift

## Implications

- Direct production modifications should be avoided
- Documentation evolves alongside implementation

---

# ADR-006 - Bronze → Silver → Gold Alignment

## Status

Accepted

## Decision

The webhook platform will support the broader Corporate Analytics Bronze → Silver → Gold architecture.

## Rationale

- Consistent analytics patterns across platforms
- Clear separation of concerns
- Supports both operational and analytical workloads
- Aligns with existing Microsoft Fabric standards

## Implications

- Webhook services focus on ingestion
- Transformation logic belongs in downstream processing layers

---

# ADR-007 - Integration Platform, Not a Single Webhook

## Status

Accepted

## Decision

This repository will serve as a reusable integration platform capable of hosting multiple webhook endpoints and integration services.

## Rationale

- Encourages reuse of common components
- Avoids proliferation of small projects
- Creates a centralized operational model
- Supports future enterprise integrations

## Implications

Examples of future capabilities may include:

- Webhooks
- Scheduled jobs
- API integrations
- Automation services
- Data quality services
- Event-driven processing

---

# ADR-008 - Keep the Platform Simple

## Status

Accepted

## Decision

Favor simple, understandable solutions over complex frameworks until a clear need for additional complexity exists.

## Rationale

- The platform is in its early stages
- Simpler solutions are easier to troubleshoot
- Reduces maintenance burden
- Accelerates delivery of business value

## Implications

- Avoid premature optimization
- Introduce new technologies only when justified by requirements
- Prefer standard Azure services and Python libraries

---

# Guiding Principle

Preserve data first. Transform later.

Systems should prioritize reliable ingestion and retention of source data before applying business rules, transformations, or analytical logic.
