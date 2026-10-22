StudySync: Multiple Choice V3 — Test 2 Generated Questions
Topic: Logistic Regression
Questions Generated: 6
Source: Logistic Regression course notes
Prompt Version: V3
Question 1
What is the primary purpose of logistic regression according to the notes?

A. To predict the probability that a categorical response belongs to a particular class
B. To predict a continuous numerical response value directly
C. To cluster unlabeled observations into distinct groups based on distance
D. To transform categorical variables into numerical dummy variables  

Correct Answer: A. To predict the probability that a categorical response belongs to a particular class

Explanation: Logistic regression is a classification method used to predict a categorical response by modeling the probability that the response belongs to a particular class, rather than modeling the response directly.
Question 2
If a credit card company wants to identify more potentially risky customers by making the classifier more willing to predict the positive class, what adjustment should they make to the classification threshold?

A. Set the threshold equal to the decision boundary x = -b/w
B. Keep the threshold fixed at exactly 0.5
C. Increase the threshold above 0.5
D. Lower the threshold below 0.5, such as to 0.1  

Correct Answer: D. Lower the threshold below 0.5, such as to 0.1

Explanation: Lowering the threshold (for example, to 0.1) makes the classifier more willing to predict the positive class, allowing the company to identify more potentially risky customers.
Question 3
For a single predictor in logistic regression, where does the standard decision boundary of 0.5 occur in terms of the model parameters $w$ and $b$?

A. $x = -(w+b)$
B. $x = w/-b$
C. $x = b/w$
D. $x = -b/w$  

Correct Answer: D. $x = -b/w$

Explanation: For the standard threshold of 0.5, the decision boundary occurs where $p(X) = 0.5$, which means $z = wx + b = 0$. Solving for $x$ yields $x = -b/w$.
Question 4
Why is linear regression poorly suited for binary classification compared to logistic regression?

A. Linear regression can produce predicted probabilities outside the valid range of 0 and 1.
B. Linear regression cannot incorporate a bias or intercept term.
C. Linear regression requires categorical predictors instead of numerical features.
D. Linear regression always results in an S-shaped curve.  

Correct Answer: A. Linear regression can produce predicted probabilities outside the valid range of 0 and 1.

Explanation: Linear regression can produce predictions below 0 or above 1, whereas logistic regression uses the logistic function to produce values strictly bounded between 0 and 1.
Question 5
In logistic regression, how does the sign and magnitude of a feature weight ($w_i$) affect the classification decision?

A. A positive weight represents evidence toward the positive class, and larger absolute weights have stronger influence.
B. A negative weight has no effect on the prediction unless the bias term is zero.
C. A positive weight represents evidence toward the negative class, and larger absolute weights have weaker influence.
D. A negative weight represents evidence toward the positive class, and larger absolute weights have weaker influence.  

Correct Answer: A. A positive weight represents evidence toward the positive class, and larger absolute weights have stronger influence.

Explanation: A positive weight provides evidence toward the positive class, a negative weight provides evidence toward the negative class, and a larger absolute weight indicates a stronger influence on the prediction.
Question 6
Given the logit formulation $z = w \cdot x + b$, what is the role of the sigmoid function $\sigma(z)$?

A. It subtracts the bias from the feature coefficients.
B. It calculates the exact classification threshold without needing a preset value.
C. It converts the input feature vector directly into the model weights.
D. It converts the logit into a probability between 0 and 1.  

Correct Answer: D. It converts the logit into a probability between 0 and 1.

Explanation: The sigmoid function $\sigma(z) = 1/(1 + e^{-z})$ converts the logit $z$, which can be any real number, into a probability value between 0 and 1.