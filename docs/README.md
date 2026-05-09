# Docs

This folder contains architecture and design notes for FastRecall.

## Files

- `architecture.md` explains the full system at a conceptual level.
- `flowcharts.md` contains Mermaid flowcharts for ingestion, indexing,
  retrieval, and answer generation.
- `data_model.md` shows the planned internal records.
- `developer_journey.md` gives the recommended implementation order.
- `commands.md` lists the CLI commands FastRecall should eventually support.

## Flow

Read `architecture.md` first, then `flowcharts.md`, then implement the project
phase by phase using `developer_journey.md`.

This folder should stay implementation-light. Put code in `fastrecall/`.
