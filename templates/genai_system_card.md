# GenAI System Card — {{MODEL_ID}} / {{SYSTEM_NAME}} (v{{SYSTEM_VERSION}})
- Owners: {{TEAM}} | Email: {{CONTACT}} | Date: {{DATE}}
- Related: [model card](model_card.md) · [data card](data_card.md) · [validation report](validation_report.md) · [change control](mrm/change_control.md) · [third-party due diligence](mrm/third_party_model_due_diligence.md) if the base model is a vendor's
- Use case: {{INTENDED_USE}} | Out of scope: {{OUT_OF_SCOPE}}
- Decision criticality/risk tier: {{TIER}} | Regulatory scope: {{REGULATIONS}}

Companion to `model_card.md` for systems built on LLMs, RAG, or agentic pipelines.
The model card assumes features, a threshold, and a score. A generative system's behaviour
is instead governed by prompts, retrieval sources, templates, and control settings — so
those are the governed components, and T7 is not satisfied until they can be reconstructed
for any past output.

## Components and Versions
| Component | Identifier / version | Owner | Change control |
|---|---|---|---|
| Base model | {{PROVIDER/MODEL/VERSION}} | {{...}} | {{who approves a model version change}} |
| System prompt | {{PROMPT_ID@VERSION, hash}} | {{...}} | {{...}} |
| Task/user prompt templates | {{TEMPLATE_IDS@VERSIONS}} | {{...}} | {{...}} |
| Retrieval index | {{INDEX_ID, build date, doc count}} | {{...}} | {{...}} |
| Guardrail / filter config | {{ID@VERSION}} | {{...}} | {{...}} |
| Tools / functions callable | {{LIST, with permissions}} | {{...}} | {{...}} |
| Decoding settings | temperature={{...}}, top_p={{...}}, max_tokens={{...}}, seed={{...}} | {{...}} | {{...}} |

- Model version updates from the provider: how communicated={{...}}, notice period={{...}},
  who re-validates before the new version reaches production={{...}}
- Prompt changes are material changes: a prompt edit can alter outcomes as much as a
  threshold change. Approval rights={{...}}, evidence retained={{...}}

## Retrieval and Grounding (if applicable)
- Corpus and provenance: {{SOURCES}}, licensing/consent basis={{...}}
- Refresh cadence and staleness bound: {{...}}
- Chunking/embedding: model={{...}}, chunk size={{...}}, overlap={{...}}
- Retrieval params: k={{...}}, filters={{...}}, reranker={{...}}
- Access scoping: does retrieval respect the requesting user's entitlements? {{Yes/No, how}}
- Citation policy: every claim cited={{Yes/No}}, unsupported-claim behaviour={{refuse/hedge/answer}}
- Coverage gaps: what the corpus does NOT contain that users may assume it does={{...}}

## Decision Pathway Reconstruction (T7)
For any past output, the institution must be able to recover:
- [ ] Base model version and decoding settings in force
- [ ] Prompt/template IDs and versions (hashes, not just names)
- [ ] Retrieved chunks and their source document IDs and versions
- [ ] Tool calls made and their arguments and results
- [ ] Guardrail decisions (what was blocked, rewritten, or flagged)
- [ ] The output actually shown to the user (not a regenerated approximation)
- [ ] The human action that followed, and by whom

- Log store and retention: {{SYSTEM, retention period, access controls}}
- Regeneration caveat: outputs are not reliably reproducible by re-running the prompt.
  Reconstruction depends on the stored record, not on replay. Confirm the record is
  sufficient on its own: {{Yes/No}}

## Generated Explanations
Applies when the system explains its own output, or explains another model's decision.
- Are generated explanations used to justify consequential decisions? {{Yes/No}}
- If yes, grounding control: {{how the rationale is constrained to actual decision factors}}
- Faithfulness testing: method={{...}}, sample size={{...}}, disagreement rate={{...}}
- Fluent-but-false risk: a generated rationale can be well-formed and wrong about why the
  decision happened. Where a reason is legally operative (adverse action, clinical
  rationale, SAR narrative), the reason must come from the decision system and the LLM
  may only render it. Confirm which applies here: {{generated / rendered-only}}
- Prohibited: presenting generated rationale as the basis of a decision the generator
  did not make.

## Evaluation
- Task-level eval set: size={{...}}, provenance={{...}}, refresh cadence={{...}}
- Quality metrics: {{groundedness, citation accuracy, task success, refusal correctness}}
- Counter-metrics (E2): {{hallucination rate, over-refusal rate, verification time added,
  edit distance from draft to filed version}}
- Human baseline comparison (E3): {{what the current process achieves on the same set}}
- Non-determinism: runs per eval item={{...}}, variance observed={{...}}
- Adversarial: prompt injection (direct and via retrieved content), jailbreak, data
  exfiltration through output. Last tested={{DATE}}, findings={{LINK}}

## Limitations and Guardrails
- Known failure modes: {{...}}
- Approved uses / prohibited uses: {{...}}
- Where output must not be relied on without independent verification: {{...}}
- Refusal and escalation behaviour: {{...}}

## Approvals
- System owner sign-off: {{NAME/DATE}}
- Independent validation: {{NAME/DATE}}
- Security review (prompt injection, leakage, tool permissions): {{NAME/DATE}}
- Business/Compliance: {{NAME/DATE}}
