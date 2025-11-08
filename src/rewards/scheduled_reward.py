class ScheduledCompositeReward:
    """
    R_t = α(t)*R_QA + β(t)*R_CLIP + γ(t)*R_len + δ(t)*R_cov
    Placeholder; integrate with CapRL later.
    """
    def __init__(self):
        pass

    def __call__(self, qa_acc, clip_sim, length_tokens, coverage_score, step, total_steps):
        # TODO: replace with scheduled mixture of sub-rewards
        return float(qa_acc)
