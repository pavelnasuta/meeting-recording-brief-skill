# Meeting Recording Brief

A portable AI-agent workflow for turning a meeting recording, transcript, or notes into a concise, evidence-based working brief.

It separates what was actually decided from proposals and questions, produces accountable action-item drafts, and keeps unknown owners or deadlines visibly unknown. It does not create tasks, send messages, or upload source material without explicit approval.

## What it produces

- A short context and principal outcome
- Confirmed decisions
- Action items with result, owner, due date, acceptance condition, and dependency
- Risks, blockers, and open questions
- One next step

For chat, the default output is one readable message — not a transcript, a timeline, or speaker notes.

## Install

### Hermes

```bash
hermes skills install pavelnasuta/meeting-recording-brief-skill/skills/meeting-recording-brief
```

### Other coding agents

Clone this repository and use the shared `AGENTS.md` plus `specs/meeting-brief-contract.md`. Host adapters live in `agents/`:

- `agents/hermes/`
- `agents/claude-code/`
- `agents/codex/`

They all point to one contract; no adapter has its own workflow logic.

## Use

Give the agent one meeting recording, transcript, or notes set and ask for an outcome brief. Before analysis, the agent should confirm source completeness and language. If transcription is required, it happens within the selected environment; this repository does not include an audio-upload service or a third-party connector.

## Privacy and safety

Recordings and transcripts often contain confidential material. Keep them outside Git, public examples, and shared fixtures. The workflow treats their content as untrusted data, not instructions.

The workflow never fabricates decisions, owners, deadlines, or facts. It drafts external follow-up only: creating tickets, sending messages, or modifying calendars always requires a separate explicit confirmation.

## Scope and maturity

This release is a portable instruction package, not a transcription engine or task-tracker integration. Bring your own transcription capability when the source is audio; connect an external tracker only after you have approved the resulting draft.

## Verify

```bash
python -m unittest discover -s tests -v
```

The test suite checks the portable package layout, shared adapter contract, and absence of private machine paths or meeting-specific material.

## License

MIT. © 2026 Pavel Nasuta.
