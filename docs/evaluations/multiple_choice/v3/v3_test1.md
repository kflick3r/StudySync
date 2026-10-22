StudySync: Multiple Choice V3 — Test 1 Generated Questions
Topic: Logistic Regression
Questions Generated: 7
Source: Logistic Regression course notes
Prompt Version: V3
Question 1
What is the primary purpose of logistic regression?

A. To predict a continuous quantitative response variable directly
B. To predict the probability that a categorical response belongs to a particular class
C. To determine the exact numerical difference between multiple classes
D. To classify data without bounding output values between zero and one  

Correct Answer: B. To predict the probability that a categorical response belongs to a particular class

Explanation: Logistic regression is a classification method used to model the probability that a categorical response Y belongs to a particular class, ensuring valid probability bounds.
Question 2
If a credit card company wants to identify more potentially risky customers by capturing a larger group, how might they adjust the standard classification threshold of 0.5?

A. Set the threshold to zero
B. Increase the threshold to a value like 0.9
C. Keep the threshold fixed at exactly 0.5
D. Lower the threshold to a value like 0.1  

Correct Answer: D. Lower the threshold to a value like 0.1

Explanation: Lowering the threshold (for example, to 0.1) makes the classifier more willing to predict the positive class, helping identify more potentially risky customers.
Question 3
For a single predictor in logistic regression, where does the decision boundary occur using the standard threshold of 0.5?

A. Where $x = 0$
B. Where $wx + b = 0$
C. Where $wx + b = 0.5$
D. Where $p(X) = 1$  

Correct Answer: B. Where $wx + b = 0$

Explanation: For the standard threshold of 0.5, the decision boundary occurs where $p(X) = 0.5$, which happens when the logit $z = 0$, or $wx + b = 0$ for a single predictor.
Question 4
How does the logistic function handle predicted probabilities compared to linear regression?

A. It maps inputs to discrete integers without continuous probabilities
B. It can produce values below 0 and above 1
C. It uses a straight line to fit the binary classification targets directly
D. It produces an S-shaped curve bounded strictly between 0 and 1  

Correct Answer: D. It produces an S-shaped curve bounded strictly between 0 and 1

Explanation: Unlike linear regression, which can produce predictions outside the valid probability range, the logistic function produces an S-shaped curve bounded by $0 < p(X) < 1$.
Question 5
In the logit form of the logistic function, what role does the sigmoid function $\sigma(z)$ play?

A. It measures the negative weight evidence for the negative class
B. It transforms the input features into raw regression coefficients
C. It calculates the bias term directly from the training data
D. It converts the logit into a probability  

Correct Answer: D. It converts the logit into a probability

Explanation: The sigmoid function $\sigma(z) = 1/(1 + e^{-z})$ converts the logit $z$ into a probability bounded between 0 and 1.
Question 6
In logistic regression feature weights, what does a positive weight indicate about a feature's contribution?

A. It provides evidence toward the positive class
B. It has no influence on the classification decision
C. It forces the probability output to equal exactly 1
D. It provides evidence toward the negative class  

Correct Answer: A. It provides evidence toward the positive class

Explanation: Each weight represents how a feature contributes; a positive weight acts as evidence toward the positive class, while a negative weight provides evidence toward the negative class.
Question 7
Given a single predictor model where $w = 1$ and $b = 2$, at what value of $x$ does the decision boundary occur for the standard threshold of 0.5?

A. $x = 0.5$
B. $x = 1$
C. $x = 2$
D. $x = -2$  

Correct Answer: D. $x = -2$

Explanation: The decision boundary occurs where $wx + b = 0$. Substituting $w = 1$ and $b = 2$ gives $1x + 2 = 0$, which solves to $x = -2$.