# NovaBank Analytics

![CI](https://github.com/francescbatlle/novabank-analytics/actions/workflows/ci.yml/badge.svg)

NovaBank is a fictional European neobank with 50,000 customers. This project acts as its first data scientist and answers the questions its leadership asks, one business area at a time.

| Area | Question |
|---|---|
| [Customers](customers/) | Do customers stay? Did the Spain launch increase usage? |
| [Payments](payments/) | How many payments fail? Does the new checkout improve success rate? |
| [Fraud](fraud/) | Which payments are fraudulent, and how much does detecting them save? |
| [Finance](finance/) | How much money will move next month? Do our records match the payment processor? |
| [Assistant](assistant/) | Can someone without SQL ask the data questions? |

The data is simulated in [`bank_data/`](bank_data/) with known true effects, so every estimate can be checked against the truth.

_Work in progress._
