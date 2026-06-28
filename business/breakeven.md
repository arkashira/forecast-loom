# Breakeven Analysis – forecast‑loom

| Metric | Assumptions | Value |
|--------|-------------|-------|
| **Compute cost per active user** | 1 CPU‑hour per month for model inference + 0.5 CPU‑hour for training updates | **$0.12** |
| **Storage cost per active user** | 10 GB/month of time‑series data + 1 GB of model artefacts | **$0.04** |
| **Bandwidth cost per active user** | 5 GB/month of API traffic (in/out) | **$0.02** |
| **Total variable cost per active user** | Compute + Storage + Bandwidth | **$0.18** |
| **Fixed monthly overhead** | Cloud ops, monitoring, support (incl. 1 engineer) | **$3,000** |
| **Average monthly active users (MAU)** | 1,000 (baseline for break‑even) | – |

---

## Pricing Tiers

| Tier | Monthly Price | Features |
|------|---------------|----------|
| **Starter** | $25 | • 10 k datapoints/month<br>• 1 model per project<br>• Basic API (REST)<br>• Email support |
| **Pro** | $75 | • 100 k datapoints/month<br>• 5 models per project<br>• Web‑UI + API<br>• Priority email support |
| **Enterprise** | $250 | • Unlimited datapoints<br>• Unlimited models<br>• Dedicated account manager<br>• SLA 99.9% uptime<br>• On‑prem & hybrid options |

---

## Customer Acquisition Cost (CAC)

| Channel | CAC (USD) |
|---------|-----------|
| Paid ads (Google, LinkedIn) | $120 |
| Partner referrals | $80 |
| Content marketing | $40 |
| **Average CAC** | **$80** |

---

## Lifetime Value (LTV)

| Tier | Avg. Monthly Revenue | Avg. Churn | LTV |
|------|----------------------|------------|-----|
| Starter | $25 | 10 %/mo | $250 |
| Pro | $75 | 8 %/mo | $937.50 |
| Enterprise | $250 | 5 %/mo | $5,000 |

*LTV = (Monthly Recurring Revenue) ÷ Churn Rate.*

---

## Break‑Even Users

### Variable Cost per User
- **Starter**: $0.18 × 1,000 = $180
- **Pro**: $0.18 × 1,000 = $180
- **Enterprise**: $0.18 × 1,000 = $180

### Monthly Revenue per User
- **Starter**: $25
- **Pro**: $75
- **Enterprise**: $250

### Break‑Even MAU (ignoring fixed costs)

| Tier | Users Needed to Cover Variable Costs |
|------|-------------------------------------|
| Starter | 180 / $25 ≈ **7.2** → **8 users** |
| Pro | 180 / $75 ≈ **2.4** → **3 users** |
| Enterprise | 180 / $250 ≈ **0.72** → **1 user** |

### Including Fixed Costs

Let **F** = $3,000 fixed. Break‑even MAU = (F + Variable Cost) / Monthly Price.

| Tier | MAU to Break‑Even |
|------|-------------------|
| Starter | (3,000 + 180) / 25 ≈ **127** |
| Pro | (3,000 + 180) / 75 ≈ **40** |
| Enterprise | (3,000 + 180) / 250 ≈ **13** |

---

## Path to $10 K MRR

| Tier | Users Needed | Total MRR |
|------|--------------|-----------|
| Starter | 400 users | $10,000 |
| Pro | 133 users | $10,000 |
| Enterprise | 40 users | $10,000 |

**Recommended ramp strategy**

1. **Launch Pro tier first** – higher margin and lower churn.  
   *Target 133 Pro users → $10 K MRR in ~4 months.*

2. **Add Enterprise tier** – once Pro base is stable, upsell 40 Enterprise users for a quick $10 K bump.

3. **Scale Starter** – for volume‑heavy customers; 400 Starter users can be reached via partner channel outreach.

---

### Key Takeaway

- **Break‑even** is reached with as few as **13 Enterprise** users or **40 Pro** users.  
- **$10 K MRR** can be achieved with **133 Pro users** (or 40 Enterprise users).  
- CAC is low enough that a **$80 CAC** yields a **>3× LTV** for Pro and Enterprise tiers, ensuring a healthy acquisition funnel.