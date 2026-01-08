#!/usr/bin/env python3
"""
UNICORN Framework Score Calculator

Calculates aggregate scores, pass rates, and statistics from evaluation CSVs.

Usage:
    python score-calculator.py --input results.csv --output report.json
    python score-calculator.py --input results.csv --format markdown
"""

import argparse
import csv
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class DimensionStats:
    """Statistics for a single dimension."""
    dimension: str
    l1_scores: list
    l2_scores: list
    l3_scores: list
    
    @property
    def l1_pass_rate(self) -> float:
        return self._pass_rate(self.l1_scores)
    
    @property
    def l2_pass_rate(self) -> float:
        return self._pass_rate(self.l2_scores)
    
    @property
    def l3_pass_rate(self) -> float:
        return self._pass_rate(self.l3_scores)
    
    @property
    def degradation(self) -> float:
        """Calculate L1 to L3 degradation in percentage points."""
        return self.l1_pass_rate - self.l3_pass_rate
    
    @property
    def average_score(self) -> float:
        all_scores = self.l1_scores + self.l2_scores + self.l3_scores
        return sum(all_scores) / len(all_scores) if all_scores else 0
    
    def _pass_rate(self, scores: list) -> float:
        """Calculate pass rate (scores >= 2) as percentage."""
        if not scores:
            return 0.0
        passing = sum(1 for s in scores if s >= 2)
        return (passing / len(scores)) * 100


def parse_csv(filepath: Path) -> list[dict]:
    """Parse evaluation CSV file."""
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip rows without scores
            if not row.get('Score') or row['Score'].strip() == '':
                continue
            try:
                results.append({
                    'test_case_id': row.get('Test_Case_ID', ''),
                    'system': row.get('System', ''),
                    'dimension': row.get('Dimension', ''),
                    'level': int(row.get('Level', 0)),
                    'score': int(row.get('Score', 0)),
                    'evaluator': row.get('Evaluator', ''),
                    'notes': row.get('Notes', '')
                })
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping malformed row: {e}", file=sys.stderr)
    return results


def calculate_statistics(results: list[dict]) -> dict:
    """Calculate comprehensive statistics from results."""
    
    # Group by dimension
    dimension_data = defaultdict(lambda: {'l1': [], 'l2': [], 'l3': []})
    
    for r in results:
        dim = r['dimension']
        level = r['level']
        score = r['score']
        
        if level == 1:
            dimension_data[dim]['l1'].append(score)
        elif level == 2:
            dimension_data[dim]['l2'].append(score)
        elif level == 3:
            dimension_data[dim]['l3'].append(score)
    
    # Calculate per-dimension statistics
    dimension_stats = {}
    for dim, data in dimension_data.items():
        stats = DimensionStats(
            dimension=dim,
            l1_scores=data['l1'],
            l2_scores=data['l2'],
            l3_scores=data['l3']
        )
        dimension_stats[dim] = {
            'l1_pass_rate': round(stats.l1_pass_rate, 1),
            'l2_pass_rate': round(stats.l2_pass_rate, 1),
            'l3_pass_rate': round(stats.l3_pass_rate, 1),
            'degradation': round(stats.degradation, 1),
            'average_score': round(stats.average_score, 2),
            'total_tests': len(data['l1']) + len(data['l2']) + len(data['l3'])
        }
    
    # Calculate overall statistics
    all_l1 = [r['score'] for r in results if r['level'] == 1]
    all_l2 = [r['score'] for r in results if r['level'] == 2]
    all_l3 = [r['score'] for r in results if r['level'] == 3]
    
    overall_stats = DimensionStats(
        dimension='Overall',
        l1_scores=all_l1,
        l2_scores=all_l2,
        l3_scores=all_l3
    )
    
    # Group by system
    system_data = defaultdict(list)
    for r in results:
        system_data[r['system']].append(r['score'])
    
    system_stats = {}
    for system, scores in system_data.items():
        passing = sum(1 for s in scores if s >= 2)
        system_stats[system] = {
            'total_tests': len(scores),
            'pass_rate': round((passing / len(scores)) * 100, 1) if scores else 0,
            'average_score': round(sum(scores) / len(scores), 2) if scores else 0
        }
    
    return {
        'summary': {
            'total_tests': len(results),
            'l1_pass_rate': round(overall_stats.l1_pass_rate, 1),
            'l2_pass_rate': round(overall_stats.l2_pass_rate, 1),
            'l3_pass_rate': round(overall_stats.l3_pass_rate, 1),
            'overall_degradation': round(overall_stats.degradation, 1),
            'average_score': round(overall_stats.average_score, 2)
        },
        'by_dimension': dimension_stats,
        'by_system': system_stats
    }


def format_markdown(stats: dict) -> str:
    """Format statistics as markdown report."""
    lines = [
        "# UNICORN Framework Evaluation Report",
        "",
        "## Summary",
        "",
        f"- **Total Tests:** {stats['summary']['total_tests']}",
        f"- **L1 Pass Rate:** {stats['summary']['l1_pass_rate']}%",
        f"- **L2 Pass Rate:** {stats['summary']['l2_pass_rate']}%",
        f"- **L3 Pass Rate:** {stats['summary']['l3_pass_rate']}%",
        f"- **Overall Degradation:** {stats['summary']['overall_degradation']} percentage points",
        f"- **Average Score:** {stats['summary']['average_score']}/3.0",
        "",
        "## Results by Dimension",
        "",
        "| Dimension | L1 | L2 | L3 | Δ L1→L3 |",
        "|-----------|-----|-----|-----|---------|"
    ]
    
    for dim, data in sorted(stats['by_dimension'].items()):
        lines.append(
            f"| {dim} | {data['l1_pass_rate']}% | {data['l2_pass_rate']}% | "
            f"{data['l3_pass_rate']}% | -{data['degradation']}pp |"
        )
    
    lines.extend([
        "",
        "## Results by System",
        "",
        "| System | Tests | Pass Rate | Avg Score |",
        "|--------|-------|-----------|-----------|"
    ])
    
    for system, data in sorted(stats['by_system'].items()):
        lines.append(
            f"| {system} | {data['total_tests']} | {data['pass_rate']}% | "
            f"{data['average_score']}/3.0 |"
        )
    
    lines.extend([
        "",
        "## Key Findings",
        "",
        "### Most Vulnerable Dimensions (Lowest L3 Pass Rate)",
        ""
    ])
    
    # Sort dimensions by L3 pass rate
    sorted_dims = sorted(
        stats['by_dimension'].items(),
        key=lambda x: x[1]['l3_pass_rate']
    )
    
    for dim, data in sorted_dims[:3]:
        lines.append(f"- **{dim}**: {data['l3_pass_rate']}% L3 pass rate")
    
    lines.extend([
        "",
        "### Most Resilient Dimensions (Highest L3 Pass Rate)",
        ""
    ])
    
    for dim, data in sorted_dims[-3:]:
        lines.append(f"- **{dim}**: {data['l3_pass_rate']}% L3 pass rate")
    
    lines.extend([
        "",
        "---",
        "*Generated by UNICORN Framework Score Calculator*"
    ])
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Calculate UNICORN Framework evaluation statistics'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Input CSV file with evaluation results'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output file (default: stdout)'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['json', 'markdown'],
        default='json',
        help='Output format (default: json)'
    )
    
    args = parser.parse_args()
    
    # Parse input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    results = parse_csv(input_path)
    
    if not results:
        print("Error: No valid results found in CSV", file=sys.stderr)
        sys.exit(1)
    
    # Calculate statistics
    stats = calculate_statistics(results)
    
    # Format output
    if args.format == 'json':
        output = json.dumps(stats, indent=2)
    else:
        output = format_markdown(stats)
    
    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report written to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
