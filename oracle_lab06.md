# Oracle (ORCL) — Lab 06

## R — Five sourced rows

| Input | Value | Unit | As-of date | Locator / source |
|---|---:|---|---|---|
| Starting FCFF | **-$19,666.474** | USD millions | FY ended May 31, 2026 | Oracle FY2026 10-K. Operating cash flow = $31,977M; interest expense = $4,599M; effective tax rate = 12.6%; capex = $55,663M. FCFF = 31,977 + 4,599 × (1 − 0.126) − 55,663. Locators: Item 7 liquidity/cash flows; Consolidated Statements of Operations. |
| Years 1–5 | **-$20B, $0B, $25B, $55B, $65B** | FCFF, USD | FY2027–FY2031 | **Forecast estimate, not company guidance.** Oracle has negative current FCFF, so I use an explicit path rather than growing a loss. The path reflects continued near-term AI/data-center capex followed by cash-flow recovery as Oracle works toward its FY2030 revenue target. |
| WACC | **11.4%** | percent | Sep. 10, 2026 | **Estimate.** Cost of equity ≈ 4.95% risk-free + 1.73 beta × 5% ERP = 13.60%. Pre-tax debt cost ≈ FY2026 interest expense / average debt = 4.14%; after tax ≈ 3.62%. Weighted by market-value equity and debt gives about 11.4%. |
| Terminal growth | **3.0%** | percent | Sep. 10, 2026 | **Estimate.** Course instruction: use a long-run economy assumption, not Oracle's near-term growth rate. |
| Cash · debt · diluted shares | **31,289 · 129,541 · 2,914** | USD millions · USD millions · millions shares | May 31, 2026 | Oracle FY2026 10-K. Locators: Consolidated Balance Sheets; borrowings/debt note; EPS note. |

**Share-price target for reverse DCF:** **$156.61 per share**, observed Sep. 10, 2026 at approximately 5:24 PM ET from Public market data.

### Forecast rationale
Oracle's FY2026 free cash flow was sharply negative because capital expenditures rose to $55.7B. Oracle also guided to at least $90B of FY2027 revenue, while management has targeted $225B of total revenue in FY2030. My explicit FCFF path is therefore a simple estimate of a transition from heavy investment to positive cash generation; it is not Oracle guidance.

---

## V — Reasonableness

Base-case DCF value = **$151.01/share**.

Observed price = **$156.61/share**.

The DCF is about **0.96×** the observed price, so it is inside the required **0.5×–2.0×** reasonableness band.

The input I distrust most is the **five-year FCFF path**. Oracle is spending heavily on AI/data-center capacity, so the timing of capex and the conversion of backlog into operating cash flow can move the valuation materially.

---

## E — Sensitivity

| WACC \ terminal growth | 2.0% | 3.0% | 4.0% |
|---|---:|---:|---:|
| **10.4%** | $157.91 | $182.06 | $213.77 |
| **11.4%** | $132.67 | **$151.01** | $174.31 |
| **12.4%** | $112.42 | $126.72 | $144.41 |

Direction check: value **falls when WACC rises** and **rises when terminal growth rises**.

Corner range: **$112.42 to $213.77/share**.

---

## Reverse DCF

### Training proof
The training case reproduces the professor's grid and solves to approximately a **+1.78 percentage-point shift** to every explicit growth rate to reach a $30.00 share price, holding starting FCFF, WACC, terminal growth, cash, debt, and diluted shares fixed.

### Oracle
Oracle's FY2026 FCFF is negative, so applying a growth-rate shift would mechanically grow a loss. I therefore follow the negative-FCFF exception and reverse the **explicit FCFF path** instead.

At a target price of **$156.61**, the reverse DCF requires about **+$1.51B of FCFF in every forecast year** relative to my base path.

Base FCFF path:
**-$20.00B, $0.00B, $25.00B, $55.00B, $65.00B**

Price-implied path:
**-$18.49B, $1.51B, $26.51B, $56.51B, $66.51B**

Held fixed: **11.4% WACC, 3.0% terminal growth, $31.289B cash, $129.541B debt, and 2.914B diluted shares**.

This is one set of assumptions consistent with the price; it is **not proof of mispricing**.

---

## Conditional call

**Watch-defer. Initiate/add if the market price falls below roughly $151 per share, or if new evidence supports an FCFF path above my base case; otherwise hold off. Monitor: operating cash flow relative to capital expenditures.**

The main question is whether Oracle can convert its large cloud backlog and AI infrastructure investment into enough cash flow to reach roughly **$66.5B of Year-5 FCFF** under the price-implied path.
