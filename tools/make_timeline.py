"""Timeline figure for the index README (dates from each repository's README)."""
from datetime import date

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

THREADS = [  # name, start, end, colour (blue: research repo, grey: notes only, orange: current)
    ('vlm-experiments: a frozen VLM reads a whole match', date(2025, 10, 1), date(2025, 12, 15), '#2a78d6'),
    ('product-side R&D (notes only)', date(2026, 2, 1), date(2026, 4, 30), '#9a9993'),
    ('MoveHarness: an honest scorer (CAISc 2026)', date(2026, 6, 20), date(2026, 7, 15), '#2a78d6'),
    ('movement-research: measurement under contact', date(2026, 8, 18), date(2026, 8, 26), '#2a78d6'),
    ('limb-entanglement: whose arm is it?', date(2026, 8, 26), date(2026, 10, 22), '#2a78d6'),
    ('fast-slow-vision: Human State v0', date(2026, 9, 21), date(2026, 9, 28), '#2a78d6'),
    ('kakashi-autolabel: VLM agent + SAM 3.1 labelling', date(2026, 9, 30), date(2026, 10, 22), '#2a78d6'),
    ('engage3D: two-person engagement in 3D', date(2026, 10, 22), date(2026, 11, 10), '#eb6834'),
    ('Blindsight: spatial information inside VLMs', date(2026, 10, 28), date(2026, 11, 3), '#eb6834'),
]
fig, ax = plt.subplots(figsize=(9.6, 3.9), facecolor='#fcfcfb')
ax.set_facecolor('#fcfcfb')
for i, (name, a, b, col) in enumerate(THREADS):
    y = len(THREADS) - 1 - i
    ax.barh(y, mdates.date2num(b) - mdates.date2num(a), left=mdates.date2num(a), height=0.55, color=col)
    ax.text(mdates.date2num(a) - 4, y, name, ha='right', va='center', fontsize=8.6, color='#333')
ax.set_yticks([])
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 4, 7, 10)))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.set_xlim(mdates.date2num(date(2025, 4, 15)), mdates.date2num(date(2026, 11, 20)))
for s in ('top', 'right', 'left'):
    ax.spines[s].set_visible(False)
ax.set_title('Research threads, 2025-2026 (orange: current)', fontsize=10.5, loc='left')
fig.tight_layout()
fig.savefig('assets/timeline.png', dpi=130)
