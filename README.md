Python code which uses mlxtend libary to perform data analysis.

Apriori algorithm allows to get frequent item sets from provided data, based on which further we can create associated rules.

Association rules can be in short described as situation where for example occurance of one even leads to occurence of another even within the dataset.

More upon this here: https://en.wikipedia.org/wiki/Association_rule_learning#:~:text=Support%20is%20the%20evidence%20of,Confidence%20and%20the%20actual%20Confidence.

As an example that could be when a customer buys one product in a store, he is likely to buy another product in tandem.

In this example, data regarding US Police officer passings has been used.

Based on low support of 2.5%, following features have been noticed to be frequent:

![image](https://github.com/Lonceg/Apriori-Association-rules/assets/92753179/ffa5273c-f483-4837-bdf0-8d75bf8a6adb)

52% of passings is caused by gunfire, 10% are caused by automobile accidets. Most likely states are also listed.

With confidence of at least 10% following association rules have been created:

![image](https://github.com/Lonceg/Apriori-Association-rules/assets/92753179/f58e6700-9178-4ded-ab8b-f5188b2a457e)

In case of association rules, confidence is what is important. It means % chance of consequent based on the fact that precedent is present.

From this we can read that:
In the state of NY there is 47% chance officer who passed was from NYPD.
At the same time every NYPD officer was from state of NY and this rule is pretty much redundant with 100% confidence.
States of CA had following % chance of passing resulting from a gunfire:
CA 44%
IL 59%
KY 74%
TX 58%
US 50%

As a result of the analyis these states could be concluded the focus of additional police funding, protective equipment or stricter gun laws.
Especially states of KY, IL and TX as confidence is even above the national support.
