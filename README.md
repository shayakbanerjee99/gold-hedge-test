# gold-hedge-test
We’ve all heard the classic advice that gold is a safe haven when there is turbulence in the equity markets. I have been a benificiary of this advice for a long time, but the recent turbulence in the market changed my mind. I set out to do a comparative analysis to see what the data suggests.
I compared SPY (S&P 500 ETF) and GLD (Gold ETF) from June 2024 to June 2026 — a period that had some real turbulence in it.

Here is what I found:
On a USD 100 starting investment, GLD grew to around USD 190 while SPY reached roughly $147. Gold won this round clearly.

- But the rolling correlation between the two swung between +0.9 and -0.9 depending on the period. That is not the behaviour of a reliable hedge.
- I computed a beta-adjusted spread and tracked its z-score. It breached +2 in early 2026, which is could open an opportunity in taking opposing positions in both assets.
- Both assets saw drawdowns above 15% at different points. Gold did not consistently cushion SPY's falls.

My interpretation is that gold is a conditional hedge, not a permanent one. There are specific regimes where it decorrelates from equities and provides real protection. But outside those regimes, the relationship is unstable and the correlation can flip quickly.
For anyone thinking about portfolio construction or pairs strategies, the z-score framework is worth exploring further. The signal does not always appear, but when it does, it is meaningful

# Running the notebook
1. Create an API key on massive - https://massive.com
1. Update your API key in `config.py`
1. Download data using `download_data.py`
1. Run `gld-spy-hedge.ipynb`