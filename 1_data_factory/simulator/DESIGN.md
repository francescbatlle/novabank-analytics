# NovaBank simulator design

NovaBank is a fictional European neobank. The simulator generates one full year of activity (2025) with known true effects, so every analysis in this repo can be checked against the truth.

## Scale

- Period: 2025-01-01 to 2025-12-31
- Customers: 50,000 across FR, ES, IT, DE, NL
- Transactions: ~2 million
- Random seed fixed for reproducibility (42)

## Tables

| Table | What it represents | Main columns |
|---|---|---|
| `customers` | Bank customers | customer_id, signup_date, country, acquisition_channel, plan |
| `transactions` | Every payment | transaction_id, customer_id, created_at, amount_eur, merchant_category, payment_method, status, failure_reason, is_fraud |
| `experiment_assignments` | Checkout experiment exposure | customer_id, experiment_name, variant, assigned_at |
| `product_launches` | Feature launches | feature_name, country, launch_date |
| `psp_settlements` | Payment processor report | transaction_id, settled_at, amount_eur, fee_eur |

## Hidden true effects

Stored in `ground_truth.yaml`. Not to be opened until each effect has been estimated.

| Effect | Analysed in |
|---|---|
| Checkout v2 impact on payment success rate | `payments/` |
| Checkout v2 impact on fraud rate | `payments/` |
| Instant payments launch in Spain (from 2025-09-01) on payments per active customer | `customers/` |
| Fraud drivers (time of day, account age, amount) | `fraud/` |
| Processor report errors (missing, amount mismatch, duplicates) | `finance/` |

## Realism

- New signups grow 5% per month, spread smoothly across days
- Weekly seasonality: more payments on Fridays and Saturdays
- Yearly seasonality: December peak
- Black Friday (2025-11-28): 2.5x normal volume; following weekend 1.5x; Cyber Monday (2025-12-01) 1.8x; higher share of online electronics and fashion
- About a quarter of customers become inactive within their first 3 months
- Payment amounts follow a log-normal distribution

## Checkout experiment

- Name: `checkout_v2`
- Window: 2025-10-01 to 2025-10-28
- Assignment: 50/50 at customer level

## Sources

Customer weights are calibrated on Revolut's public figures, used as a proxy for a European neobank.

| Parameter | Value used | Basis | Source |
|---|---|---|---|
| Country shares | FR 31%, ES 28%, IT 20%, DE 14%, NL 7% | Revolut retail customers per market, late 2025 / early 2026. IT interpolated | See links below |
| Acquisition channels | 63% organic + referral | Revolut 2025: 63% of new retail customers via organic channels and referrals. Split within groups is an assumption | [insights4vc](https://insights4vc.substack.com/p/revolut-6b-revenue-70m-customers) |
| Paid plans | ~8% of customers | Estimated from 2025 subscription revenue (GBP 708M) and 68.3M customers. Split across tiers is an assumption | [FXC Intelligence](https://www.fxcintel.com/research/reports/ct-revolut-2025-earnings) |
| Monthly signup growth | 5% | 16M new customers in 2025 vs "1M every 17 days" at year end | [Revolut Annual Report 2025](https://www.revolut.com/annual-report-2025/) |

Country sources:

- FR: [MoneyVox](https://www.moneyvox.fr/banque-en-ligne/actualites/107050/revolut-annonce-franchir-le-cap-des-7-millions-de-clients)
- ES: [HelpMyCash](https://www.helpmycash.com/noticias/banco/revolut)
- IT: [Finanza Digitale](https://www.finanzadigitale.com/news/revolut-italia-5-milioni-clienti/), [Milano Finanza](https://www.milanofinanza.it/news/revolut-accelera-con-margini-in-espansione-e-punta-a-100-milioni-di-clienti-entro-il-2027-202603251121014261)
- DE: [FAZ summary](https://newsar.codejungle.org/articles/33491)
- NL: [Banken.nl](https://www.banken.nl/nieuws/26926/revolut-groeit-door-naar-15-miljoen-nederlandse-klanten)
