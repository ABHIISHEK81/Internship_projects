def evaluate(results):
    total = len(results)
    citation_count = sum(1 for r in results if r["has_citations"])
    return {
        "citation_coverage": citation_count / total
    }
