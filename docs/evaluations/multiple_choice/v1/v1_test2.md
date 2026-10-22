# StudySync: Multiple Choice V1 — Test 2 Generated Questions

**Topic:** Logistic Regression  
**Questions Generated:** 10  
**Source:** Logistic Regression course notes (same as Test 1)  
**Prompt Version:** V1

---

### Question 1

**What type of response does logistic regression predict?**

A. An unsupervised cluster ID  
B. A continuous numerical response  
C. A sequence of tokens  
D. A categorical response

**Correct Answer:** D. A categorical response

**Explanation:** Logistic regression is a classification method used to predict a categorical response.

---

### Question 2

**What does logistic regression actually model for a binary classification problem?**

A. The frequency of words in a document  
B. The probability that Y belongs to a particular class  
C. The direct class label Y  
D. The squared error of the residuals

**Correct Answer:** B. The probability that Y belongs to a particular class

**Explanation:** Rather than modeling Y directly, logistic regression models the probability that Y belongs to a particular class.

---

### Question 3

**If a credit card company wants to identify more potentially risky customers, how might they adjust the classification threshold?**

A. Set the threshold equal to the weight w  
B. Set the threshold equal to the bias b  
C. Lower the threshold (e.g., to 0.1)  
D. Raise the threshold (e.g., to 0.9)

**Correct Answer:** C. Lower the threshold (e.g., to 0.1)

**Explanation:** A credit card company that wants to identify more potentially risky customers could use a lower threshold like p(X) > 0.1, because lowering the threshold makes the classifier more willing to predict the positive class.

---

### Question 4

**For the standard classification threshold of 0.5, where does the decision boundary occur?**

A. Where p(X) = 0  
B. Where p(X) = 0.5  
C. Where p(X) = 1  
D. Where p(X) = 0.1

**Correct Answer:** B. Where p(X) = 0.5

**Explanation:** For the standard threshold of 0.5, the decision boundary occurs where p(X) = 0.5.

---

### Question 5

**Why is linear regression poorly suited for binary classification compared to logistic regression?**

A. Linear regression requires categorical inputs.  
B. Linear regression cannot handle more than one predictor.  
C. Linear regression can only be used for text classification.  
D. Linear regression can produce predictions outside the valid probability range.

**Correct Answer:** D. Linear regression can produce predictions outside the valid probability range.

**Explanation:** Linear regression is poorly suited for binary classification because it can produce predictions outside the valid probability range, while logistic regression always produces values between 0 and 1.

---

### Question 6

**In the logit form of the logistic function, what does z represent?**

A. The sigmoid activation output  
B. The final probability  
C. The learning rate  
D. The logit (w · x + b)

**Correct Answer:** D. The logit (w · x + b)

**Explanation:** The logit is defined as z = w · x + b.

---

### Question 7

**In logistic regression notation, which parameter corresponds to the intercept β₀?**

A. The sigmoid function σ  
B. The feature vector x  
C. The bias b  
D. The weight vector w

**Correct Answer:** C. The bias b

**Explanation:** In the equivalence between notation styles, b corresponds to the intercept β₀, while w contains the feature coefficients.

---

### Question 8

**What does a positive weight associated with a feature indicate in logistic regression?**

A. That the feature has a zero probability  
B. Evidence toward the positive class  
C. That the feature should be ignored  
D. Evidence toward the negative class

**Correct Answer:** B. Evidence toward the positive class

**Explanation:** A positive weight represents evidence toward the positive class, whereas a negative weight represents evidence toward the negative class.

---

### Question 9

**How is P(y=0 | x) calculated given P(y=1 | x) in a binary logistic regression model?**

A. 1 - P(y=1 | x)  
B. 1 / P(y=1 | x)  
C. exp(P(y=1 | x))  
D. P(y=1 | x) - 1

**Correct Answer:** A. 1 - P(y=1 | x)

**Explanation:** The probability of the alternative binary class is calculated as P(y=0 | x) = 1 - P(y=1 | x).

---

### Question 10

**What is the effect of a larger absolute weight in logistic regression?**

A. It turns off the sigmoid function  
B. It forces the feature value to be positive  
C. It creates a stronger influence on the prediction  
D. It ensures the probability is exactly 0.5

**Correct Answer:** C. It creates a stronger influence on the prediction

**Explanation:** A larger absolute weight represents a stronger influence on the prediction.