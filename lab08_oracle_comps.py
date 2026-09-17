# Lab 08 — Oracle peer P/E comparison
# Run: python lab08_oracle_comps.py

from statistics import median

# -----------------------------
# Editable inputs
# -----------------------------
target = {
    "ticker": "ORCL",
    "price": 152.94,      # Sep. 10, 2026 close
    "eps": 5.83,          # FY2026 GAAP diluted EPS
}

peers = [
    {
        "ticker": "MSFT",
        "price": 492.44,  # Sep. 10, 2026 close
        "eps": 17.95,     # FY2026 GAAP diluted EPS
    },
    {
        "ticker": "CRM",
        "price": 243.00,  # Sep. 10, 2026 close
        "eps": 7.80,      # FY2026 GAAP diluted EPS
    },
]

# -----------------------------
# Calculations
# -----------------------------
peer_results = []
for peer in peers:
    pe = peer["price"] / peer["eps"]
    implied_price = pe * target["eps"]
    peer_results.append({
        "ticker": peer["ticker"],
        "pe": pe,
        "implied_price": implied_price,
    })

peer_pes = [x["pe"] for x in peer_results]
implied_prices = [x["implied_price"] for x in peer_results]

median_pe = median(peer_pes)
median_implied = median_pe * target["eps"]

print(f"Target: {target['ticker']}")
print(f"Target price: ${target['price']:.2f}")
print(f"Target diluted EPS: ${target['eps']:.2f}")
print()

for x in peer_results:
    print(
        f"{x['ticker']}: "
        f"P/E = {x['pe']:.6f}x, "
        f"ORCL implied price = ${x['implied_price']:.2f}"
    )

print()
print(f"Peer median P/E: {median_pe:.6f}x")
print(f"Implied range: ${min(implied_prices):.2f} - ${max(implied_prices):.2f}")
print(f"Median-implied ORCL price: ${median_implied:.2f}")
print()

print("Leave-one-out check:")
for removed in peers:
    remaining = [p for p in peers if p["ticker"] != removed["ticker"]]
    if not remaining:
        print(f"Remove {removed['ticker']}: no estimate")
        continue

    remaining_pes = [p["price"] / p["eps"] for p in remaining]
    new_median_pe = median(remaining_pes)
    new_implied = new_median_pe * target["eps"]
    change = new_implied - median_implied

    print(
        f"Remove {removed['ticker']}: "
        f"${new_implied:.2f} "
        f"({change:+.2f} vs. two-peer median)"
    )
