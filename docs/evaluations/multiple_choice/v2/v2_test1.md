StudySync: Multiple Choice V2 — Test 1 Generated Questions
Topic: Logistic Regression
Questions Generated: 9
Source: Logistic Regression course notes
Prompt Version: V2
Question 1
What type of response variable does logistic regression predict?

A. A continuous numerical response
B. An unbounded response
C. A time-series response
D. A categorical response  

Correct Answer: D. A categorical response

Explanation: Logistic regression is a classification method specifically used to predict a categorical response, unlike linear regression which models continuous values.
Question 2
What does logistic regression actually model for a binary classification problem?

A. The squared error of the classes
B. The exact numerical value of the response Y
C. The probability that Y belongs to a particular class
D. The direct difference between two classes  

Correct Answer: C. The probability that Y belongs to a particular class

Explanation: Rather than modeling Y directly, logistic regression models the probability that Y belongs to a particular class, such as $p(X) = P(Y = Yes \mid X)$.
Question 3
If a credit card company wants to identify more potentially risky customers by lowering the classification threshold from 0.5 to 0.1, how does the behavior of the classifier change?

A. It only predicts values equal to 0.1
B. It converts all probabilities to negative values
C. It becomes more willing to predict the positive class
D. It becomes less willing to predict the positive class  

Correct Answer: C. It becomes more willing to predict the positive class

Explanation: Lowering the threshold (for example, to $p(X) > 0.1$) makes the classifier more willing to predict the positive class because fewer requirements are needed to trigger a 'Yes' prediction.
Question 4
For a single predictor with a standard threshold of 0.5, where does the decision boundary occur in terms of the logit $z$?

A. $z = -1$
B. $z = 1$
C. $z = 0.5$
D. $z = 0$  

Correct Answer: D. $z = 0$

Explanation: The decision boundary for the standard threshold of 0.5 occurs where $p(X) = 0.5$, which corresponds to a sigmoid value equal to 0.5, happening when $z = 0$.
Question 5
Why is standard linear regression poorly suited for binary classification compared to logistic regression?

A. Linear regression requires too many classes
B. Linear regression can only handle negative weights
C. Linear regression cannot calculate an intercept
D. Linear regression can produce predicted probabilities below 0 or above 1  

Correct Answer: D. Linear regression can produce predicted probabilities below 0 or above 1

Explanation: Linear regression can produce predictions outside the valid probability range (below 0 or above 1), whereas logistic regression always produces values bounded strictly between 0 and 1.
Question 6
In the logit form of the logistic function, what does the variable $z$ represent?

A. The training error rate
B. The final predicted probability
C. The logit ($z = w \cdot x + b$)
D. The logistic curve boundary  

Correct Answer: C. The logit ($z = w \cdot x + b$)

Explanation: The variable $z$ represents the logit, which is calculated as $z = w \cdot x + b$ before being converted into a probability by the sigmoid function.
Question 7
What does a positive weight ($w_i$) assigned to a feature indicate about its contribution to the classification decision?

A. It provides evidence toward the negative class
B. It provides evidence toward the positive class
C. It forces the probability to exactly 1
D. It has no influence on the prediction  

Correct Answer: B. It provides evidence toward the positive class

Explanation: Each weight represents how a feature contributes: a positive weight serves as evidence toward the positive class, while a negative weight provides evidence toward the negative class.
Question 8
Given a feature vector $x$ and a weight vector $w$ with a bias $b$, how are features combined to compute the logit $z$ for multiple features?

A. $z = \prod_{i=1}^{n}(w_i + x_i) - b$
B. $z = w_0 + x_0 \cdot b$
C. $z = \frac{w \cdot x}{b}$
D. $z = \sum_{i=1}^{n} w_i x_i + b$  

Correct Answer: D. $z = \sum_{i=1}^{n} w_i x_i + b$

Explanation: The notes define the combination of features as $z = w \cdot x + b$, which is equivalently written as the summation $z = \sum_{i=1}^{n} w_i x_i + b$.
Question 9
If $P(y = 1 \mid x) = \sigma(w \cdot x + b)$, how is the probability of the opposite class, $P(y = 0 \mid x)$, calculated?

A. $-P(y = 1 \mid x)$
B. $1 - P(y = 1 \mid x)$
C. $1 + P(y = 1 \mid x)$
D. $\frac{1}{P(y=1\mid x)}$  

Correct Answer: B. $1 - P(y = 1 \mid x)$

Explanation: Based on the notes, the binary probabilities complement each other, so $P(y = 0 \mid x) = 1 - P(y = 1 \mid x)$.