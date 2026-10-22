StudySync: Multiple Choice V2 — Test 2 Generated Questions
Topic: Logistic Regression
Questions Generated: 8
Source: Logistic Regression course notes
Prompt Version: V2
Question 1
What type of response does logistic regression predict?

A. A continuous numerical response
B. A linear time-series response
C. An unbounded quantitative response
D. A categorical response  

Correct Answer: D. A categorical response

Explanation: Logistic regression is a classification method used specifically to predict a categorical response, rather than a continuous or quantitative one.
Question 2
What is the range of output values produced by the logistic function $p(X)$?

A. Strictly between 0 and 1, such that $0 < p(X) < 1$
B. Only exact integers such as 0 or 1
C. Any real number from $-\infty$ to $+\infty$
D. Between -1 and 1  

Correct Answer: A. Strictly between 0 and 1, such that $0 < p(X) < 1$

Explanation: Unlike linear regression, the logistic function produces an S-shaped curve bounded strictly between 0 and 1, representing a valid probability range.
Question 3
In a logistic regression model, what does a classification threshold of 0.1 do compared to a threshold of 0.5?

A. It makes the classifier more willing to predict the positive class.
B. It restricts the model to only predict continuous values.
C. It makes the classifier more willing to predict the negative class.
D. It forces the decision boundary to always equal zero regardless of weights.  

Correct Answer: A. It makes the classifier more willing to predict the positive class.

Explanation: Lowering the classification threshold (for example, from 0.5 to 0.1) means a lower probability is required to trigger a positive prediction, making the classifier more willing to identify potential positive instances.
Question 4
For a single predictor with a standard threshold where $p(X) = 0.5$, at what value of $z$ does the sigmoid equal 0.5?

A. z = 0.5
B. z = 0
C. z = 1
D. z = -1  

Correct Answer: B. z = 0

Explanation: The sigmoid equals 0.5 when the logit $z = 0$. For a single predictor where $wx + b = 0$, this leads to the decision boundary at $x = -b/w$.
Question 5
What does a positive feature weight indicate in logistic regression?

A. Evidence toward the negative class
B. Evidence toward the positive class
C. An invalid feature that should be removed
D. A prediction probability of exactly 1.0  

Correct Answer: B. Evidence toward the positive class

Explanation: Each weight represents how a feature contributes to the decision: a positive weight provides evidence toward the positive class, while a negative weight provides evidence toward the negative class.
Question 6
How are the coefficients $\beta_0$ and $\beta_1$ in the logistic model determined?

A. They are set manually by the user based on the classification threshold.
B. They must be learned from the training data.
C. They are calculated directly by taking the square root of the input features.
D. They are always equal to 0 and 1 respectively.  

Correct Answer: B. They must be learned from the training data.

Explanation: The coefficients $\beta_0$ and $\beta_1$ (or weights and biases) must be learned from the training data.
Question 7
What is the primary reason linear regression is poorly suited for binary classification?

A. It cannot include a bias or intercept term.
B. It can only produce integer values.
C. It can produce predictions outside the valid probability range of 0 to 1.
D. It requires the classification threshold to always be set to 0.1.  

Correct Answer: C. It can produce predictions outside the valid probability range of 0 to 1.

Explanation: Linear regression can produce predicted values below 0 or above 1, making it poorly suited for modeling probabilities, whereas logistic regression always outputs values bounded between 0 and 1.
Question 8
In the logit form of the logistic function, what does the variable $z$ represent?

A. The error rate of the training data
B. The logit, calculated as $w \cdot x + b$
C. The final predicted probability
D. The classification threshold  

Correct Answer: B. The logit, calculated as $w \cdot x + b$

Explanation: The notes explicitly define $z = w \cdot x + b$ as the logit, which is then converted into a probability by the sigmoid function $\sigma(z)$.