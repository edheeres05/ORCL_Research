# Lab 08 — Oracle Peer Comparison

## Define / Discover

**Target:** Oracle Corporation (ORCL)  
**Comparison date:** September 10, 2026

Oracle earns most of its revenue from cloud and software, with additional hardware and services revenue. In FY2026, cloud and software represented 87% of total revenue. Oracle's FY2026 GAAP diluted EPS was positive at **$5.83**, so P/E can be used for this lab.

What I still needed to research:
- which listed companies have similar enterprise cloud/software economics;
- each candidate's latest annual reported GAAP diluted EPS available by September 10, 2026;
- same-date stock prices;
- business-model differences that could make a candidate only a qualified peer or an exclusion.

## Peer policy — written before final selection

I will admit listed operating companies with meaningful enterprise cloud/software revenue, recurring subscription or support economics, positive annual GAAP diluted EPS, and enough scale that their earnings are reasonably comparable with Oracle.

I will **qualify** a candidate when the core enterprise cloud/software economics fit but the company has important additional businesses or a materially different product mix.

I will **exclude** a candidate if it is mainly hardware, semiconductors, consulting/services, a non-operating holding company, has zero/negative annual GAAP diluted EPS, has an incompatible currency/share basis, or cannot be matched to the September 10, 2026 trading date.

## Candidate decisions and sources

| Company | Decision | Sep. 10, 2026 close | Latest annual GAAP diluted EPS public by date | Fiscal period | Publication date | Business reason / difference |
|---|---|---:|---:|---|---|---|
| Oracle (ORCL) | Target | $152.94 | $5.83 | FY ended May 31, 2026 | June 10, 2026 | 87% of FY2026 revenue came from cloud and software; also has hardware and services. |
| Microsoft (MSFT) | QUALIFY | $492.44 | $17.95 | FY ended June 30, 2026 | July 29, 2026 | Strong enterprise cloud/software overlap through Azure, Microsoft 365, Dynamics and server products. Difference: Microsoft is much more diversified into consumer, gaming, search and devices. FY2026 GAAP EPS also included a $0.67 positive impact from OpenAI investments. |
| Salesforce (CRM) | QUALIFY | $243.00 | $7.80 | FY ended Jan. 31, 2026 | Feb. 25, 2026 | 95% of FY2026 revenue came from subscription and support, giving strong recurring enterprise-software economics. Difference: Salesforce is mainly CRM/application software and does not have Oracle's comparable infrastructure/hardware mix. |

### Source locators

**Oracle**
- SEC FY2026 Form 10-K — Item 1 Business; cloud/software, hardware and services business descriptions:  
  https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
- Oracle FY2026 earnings release filed June 10, 2026 — FY2026 GAAP diluted EPS $5.83:  
  https://www.sec.gov/Archives/edgar/data/1341439/000119312526265848/orcl-ex99_1.htm
- Sep. 10, 2026 historical close $152.94:  
  https://stockanalysis.com/stocks/orcl/history/

**Microsoft**
- SEC FY2026 Form 10-K — Item 1 / segment descriptions, including Intelligent Cloud and Productivity and Business Processes:  
  https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- Microsoft FY2026 earnings release dated July 29, 2026 — FY2026 GAAP diluted EPS $17.95:  
  https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- Sep. 10, 2026 historical close $492.44:  
  https://stockanalysis.com/stocks/msft/history/

**Salesforce**
- SEC FY2026 Form 10-K — Overview and Sources of Revenues; 95% subscription and support:  
  https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm
- Salesforce FY2026 results dated Feb. 25, 2026 — FY2026 GAAP diluted EPS $7.80:  
  https://www.sec.gov/Archives/edgar/data/1108524/000110852426000056/crm-q4fy26xexhibit991.htm
- Sep. 10, 2026 historical close $243.00:  
  https://stockanalysis.com/stocks/crm/history/

## Implement — P/E comparison

Formula:

**Peer P/E = peer price / peer annual GAAP diluted EPS**

**Implied ORCL price = peer P/E × ORCL annual GAAP diluted EPS**

Inputs:
- ORCL EPS = **$5.83**
- MSFT: **$492.44 / $17.95 = 27.433983x**
- CRM: **$243.00 / $7.80 = 31.153846x**

Results:
- MSFT-implied ORCL price = **$159.94**
- CRM-implied ORCL price = **$181.63**
- Median peer P/E = **29.293915x**
- Median-implied ORCL price = **$170.78**
- Peer-implied range = **$159.94–$181.63**

ORCL's actual September 10 close was **$152.94**.

## Validate

### Hand check

Microsoft:

**$492.44 / $17.95 = 27.433983x**

Applying that multiple to Oracle:

**27.433983 × $5.83 = $159.94**

### Peer removal

Salesforce has the higher P/E, so I predicted that removing Salesforce would lower the implied Oracle price.

Calculator result:
- Two-peer median-implied value = **$170.78**
- Remove Salesforce → Microsoft-only reference = **$159.94**
- Change = **-$10.84**

This behaves as expected. The tradeoff is that removing Salesforce leaves only one peer, so the result becomes a single reference rather than a range and provides less information about market dispersion.

## Evolve — DCF versus peer P/E

| Method | Oracle result and date | Main assumption / limitation |
|---|---|---|
| Week 3 DCF | Base value **$151.01/share**; sensitivity range **$112.42–$213.77**; Sept. 10, 2026 comparison | Depends heavily on the five-year FCFF path, WACC and terminal-growth assumptions. |
| Peer P/E | **$159.94–$181.63**, median **$170.78**; Sept. 10, 2026 | Depends on whether Microsoft and Salesforce deserve similar earnings multiples despite differences in business mix and growth/capital intensity. |

I would **not average the two methods**. The DCF base case is approximately equal to Oracle's September 10 market price, while the peer P/E comparison produces a higher reference range.

## Skeptical AI criticism

**Weakest supported assumption:** the main weakness is peer comparability. Microsoft and Salesforce both share enterprise cloud/software economics with Oracle, but Oracle is in a much heavier infrastructure buildout and has a different mix of IaaS, software support, applications, hardware and services.

**Mismatch check:**
- Company: correct target and named peers.
- Date: all stock prices use September 10, 2026.
- Valuation object: both methods are expressed as equity value per common share.
- Earnings definition: all peer calculations use annual reported **GAAP diluted EPS**, not quarterly or adjusted EPS.
- Important qualification: Microsoft's FY2026 GAAP EPS included a $0.67 positive impact from OpenAI investments, so its reported P/E contains a non-operating earnings effect.

**Decision on criticism: ACCEPT.**  
The criticism is supported by the primary sources. It does not make the peer comparison unusable, but it means I should treat the peer result as a market reference rather than a precise intrinsic value.

**Question that could change my decision:**  
Would I still initiate if Salesforce were judged too application-focused and removed, leaving only Microsoft's $159.94 reference?

**Answer:**  
My confidence would drop substantially. A Microsoft-only reference of $159.94 is only modestly above Oracle's $152.94 market price, while my DCF base value is $151.01. In that case I would be much closer to **watch-defer** than a confident initiate.

## Reflect — conclusion

**Decision: INITIATE, but only as a small position.**

Microsoft and Salesforce belong as qualified peers because both have large recurring enterprise cloud/software businesses, but neither perfectly matches Oracle. Microsoft is more diversified, while Salesforce is more application/CRM focused.

The peer comparison adds a market-based check to my DCF. It indicates that the market applies higher earnings multiples to comparable cloud/software businesses, producing an Oracle reference range of **$159.94–$181.63**. My DCF base value of **$151.01** is much more conservative and roughly matches the September 10 market price of **$152.94**.

I am not averaging the two methods. I would initiate only a small position because the peer evidence supports upside, but the DCF does not show a large margin of safety at its base case.

Evidence that would change my decision includes:
- Oracle's cloud growth slowing materially versus my forecast;
- infrastructure spending staying high longer than assumed and delaying free-cash-flow recovery;
- evidence that Microsoft or Salesforce are not economically comparable enough to support the peer range;
- or, on the positive side, stronger evidence that Oracle's cloud growth converts into sustained operating cash flow and free cash flow faster than my Week 3 assumptions.
