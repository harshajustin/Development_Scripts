from pathlib import Path

# Use current directory as root
ROOT = Path(".")

structure = {
    "paper": {
        "sections": [
            "abstract.tex",
            "introduction.tex",
            "related_work.tex",
            "system_architecture.tex",
            "implementation.tex",
            "evaluation.tex",
            "limitations.tex",
            "conclusion.tex",
        ],
        "figures": [
            "router_orchestration.png",
            "persona_isolation.png",
            "validation_gate_flow.png",
            "pause_ask_resume.png",
            "conversation_state_model.png",
        ],
        "tables": [
            "hallucination_reduction.tex",
            "clarification_frequency.tex",
            "validation_failures.tex",
            "deterministic_resume.tex",
        ],
        "__files__": ["main.tex", "bibliography.bib"],
    },
    "architecture": [
        "system_overview.md",
        "router_orchestration.md",
        "persona_isolation.md",
        "sqlguardian_enforcement.md",
        "clarification_loop.md",
        "conversation_state.md",
        "observability.md",
        "execution_planning.md",
    ],
    "experiments": {
        "design": [
            "methodology.md",
            "experimental_setup.md",
            "evaluation_protocol.md",
        ],
        "hallucination_analysis": [
            "cases.json",
            "before_after_comparison.md",
            "guardian_blocking_examples.md",
        ],
        "ambiguity_clarification": [
            "ambiguous_queries.md",
            "clarification_traces.md",
            "recovery_analysis.md",
        ],
        "validation_gate": [
            "blocked_queries.md",
            "retry_cycles.md",
            "safety_invariants.md",
        ],
        "multi_turn": [
            "deterministic_resume_cases.md",
            "state_transition_logs.md",
            "conversation_trace_analysis.md",
        ],
    },
    "related_work": [
        "survey_notes.md",
        "model_centric_approaches.md",
        "rag_pipelines.md",
        "self_reflection_systems.md",
        "enterprise_graph_systems.md",
        "persona_architecture_analysis.md",
    ],
    "evolution": [
        "v1_linear_pipeline.md",
        "missing_components_analysis.md",
        "persona_inspiration.md",
        "router_vs_model_brain.md",
        "architectural_enforcement_principle.md",
    ],
    "diagrams": [
        "system_flow.mmd",
        "state_machine.mmd",
        "persona_transition_graph.mmd",
        "validation_retry_cycle.mmd",
        "duplex_pause_resume.mmd",
    ],
    "datasets": [
        "ambiguity_dataset.json",
        "hallucination_cases.json",
        "validation_edge_cases.json",
    ],
    "appendix_material": [
        "persona_io_contracts.md",
        "formal_state_definition.md",
        "extended_examples.md",
    ],
    "notes": [
        "weekly_progress.md",
        "open_questions.md",
        "reviewer_questions.md",
        "future_work.md",
    ],
}

root_files = ["README.md", "LICENSE"]


def create_structure(base_path: Path, tree):
    for name, content in tree.items():
        if isinstance(content, dict):
            folder_path = base_path / name
            folder_path.mkdir(parents=True, exist_ok=True)

            files = content.pop("__files__", [])
            for file in files:
                (folder_path / file).touch()

            create_structure(folder_path, content)

        elif isinstance(content, list):
            folder_path = base_path / name
            folder_path.mkdir(parents=True, exist_ok=True)

            for file in content:
                (folder_path / file).touch()


def main():
    print("Creating research structure in current directory...")
    
    for file in root_files:
        (ROOT / file).touch()

    create_structure(ROOT, structure)

    print("✅ Structure created successfully.")


if __name__ == "__main__":
    main()
