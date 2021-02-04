###  Mortgage example

Shows how much you will have to pay if you take a mortgage,
provided  much money is spent on interest and on the 
principal.

For example, you take 4 000 000, interest rate is 2.85 percent per year, time - 20 years.
The output is 
```text
month: 239	remaining amount: 21833	paid amount: 5230455	balance amount: 21781	interest amount: 104	balance sum: 3978167	interest sum: 1252288
```

which means that you spend **5 230 455**, total interest paid is **1 252 288**, monthly payment is **21885**.

How to calculate monthly payment?
https://moezhile.ru/kreditovanie/ezhemesyachnyj-platezh.html#i-2


### How to run
Virtual environments link

https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

1. If virtual environment is not created, create it
```shell
virtualenv mortgage_example_venv
```

2. Navigate there and activate it
```shell
cd mortgage_example_venv;
cd Scripts
activate
```

3. After you finish working, deactivate it.
```shell
cd mortgage_example_venv;
cd Scripts
deactivate
```

4. Run `./app/mortgage_example.py`